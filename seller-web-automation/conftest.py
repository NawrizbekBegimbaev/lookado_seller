"""
Pytest configuration and fixtures for test automation framework.

PHASE 1 REFACTORING - CRITICAL FIXES:
1. Changed page and context fixtures from SESSION to FUNCTION scope for test isolation
2. Integrated new utils and config modules
3. Removed code duplication (test data loading, env var reads)
4. Made auto-use fixtures configurable
5. Added proper type hints and docstrings

This enables parallel test execution and prevents state pollution between tests.
"""

import json
import pytest
from pathlib import Path
from typing import Dict, Any, Generator
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from dotenv import load_dotenv
from filelock import FileLock

# Import our new centralized modules
from config import settings
from utils import TestDataLoader, setup_logger, BrowserHelpers

# Path for cached auth state (shared across parallel workers)
AUTH_STATE_PATH = Path("test_data/.auth_state.json")
AUTH_STATE_LOCK = Path("test_data/.auth_state.lock")

# Load environment variables
load_dotenv()

# Setup logger
logger = setup_logger(__name__, "conftest.log")


# ================================================================================
# Command Line Options
# ================================================================================

def pytest_addoption(parser):
    """Add custom command line options for pytest."""
    parser.addoption(
        "--browser_name",
        action="store",
        default=settings.BROWSER,
        help="Browser selection: chromium, firefox, webkit"
    )
    parser.addoption(
        "--url_name",
        action="store",
        default=settings.BASE_URL,
        help="Base URL for tests"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=settings.HEADLESS,
        help="Run browser in headless mode"
    )


# ================================================================================
# Browser Fixtures (Session Scope - Shared for Performance)
# ================================================================================

@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    """
    Session-level Playwright instance.

    Initialized once per test session for performance.
    """
    from playwright.sync_api import sync_playwright

    logger.info("Starting Playwright session")
    pw = sync_playwright().start()
    yield pw
    logger.info("Stopping Playwright session")
    pw.stop()


@pytest.fixture(scope="session")
def browser(playwright: Playwright, request) -> Generator[Browser, None, None]:
    """
    Session-level browser instance.

    Browser is launched once per session to improve performance.
    Individual tests get isolated contexts and pages.

    Args:
        playwright: Playwright instance
        request: Pytest request object for accessing CLI options

    Yields:
        Browser instance
    """
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")

    logger.info(f"Launching {browser_name} browser (headless={headless})")

    launch_options = settings.get_browser_launch_options()
    launch_options["headless"] = headless

    # Select browser based on name
    if browser_name in ("chrome", "chromium"):
        browser_instance = playwright.chromium.launch(**launch_options)
    elif browser_name == "firefox":
        browser_instance = playwright.firefox.launch(**launch_options)
    elif browser_name == "webkit":
        browser_instance = playwright.webkit.launch(**launch_options)
    else:
        logger.warning(f"Unknown browser '{browser_name}', defaulting to chromium")
        browser_instance = playwright.chromium.launch(**launch_options)

    yield browser_instance

    logger.info("Closing browser")
    browser_instance.close()


# ================================================================================
# E2E Session Fixtures (Session Scope - SHARED STATE for User Flow Tests)
# ================================================================================
# These fixtures are for E2E tests that need to share browser session
# Use these when testing real user journeys: Login → Registration → Become Seller → etc.

@pytest.fixture(scope="session")
def session_context(browser: Browser, request) -> Generator[BrowserContext, None, None]:
    """
    Session-level browser context for E2E user flow tests.

    Shares state across all tests in the session:
    - Cookies persist
    - localStorage persists
    - Login state maintained

    Use this for sequential user journey tests.
    """
    logger.info("Creating SESSION-SCOPED browser context for E2E tests")

    headless = request.config.getoption("headless")

    # Use viewport for headless mode, no_viewport for headed mode (maximized)
    if headless:
        context_options = settings.get_browser_context_options_with_viewport()
    else:
        context_options = settings.get_browser_context_options()

    context_instance = browser.new_context(**context_options)

    yield context_instance

    logger.info("Closing SESSION-SCOPED browser context")
    context_instance.close()


@pytest.fixture(scope="session")
def session_page(session_context: BrowserContext, request) -> Generator[Page, None, None]:
    """
    Session-level page for E2E user flow tests.

    Single page instance shared across all tests:
    - Login once, stay logged in
    - Navigate between pages without losing state
    - Real user experience simulation

    Usage:
        def test_login(session_page): ...
        def test_registration(session_page): ...  # Same page, still logged in
    """
    logger.info("Creating SESSION-SCOPED page for E2E tests")

    page_instance = session_context.new_page()

    # Navigate to base URL
    base_url = request.config.getoption("url_name")
    page_instance.goto(base_url)

    yield page_instance

    logger.info("Closing SESSION-SCOPED page")
    page_instance.close()


@pytest.fixture(scope="session")
def authenticated_session(session_page: Page) -> Generator[Page, None, None]:
    """
    Session-level authenticated page.

    Logs in ONCE at session start, maintains auth across all tests.

    Flow:
    1. First test requests this fixture → Login performed
    2. Subsequent tests → Already logged in, continues from current state

    Usage:
        class TestBecomeSeller:
            def test_step1(self, authenticated_session): ...
            def test_step2(self, authenticated_session): ...  # Still logged in
    """
    from pages.login_page import LoginPage

    # Load credentials from becomeseller test data (qa.shavkatov@gmail.com / 11111111)
    # This fixture is primarily used by becomeseller tests which need these credentials
    becomeseller_data = TestDataLoader.load("becomeseller")
    credentials = becomeseller_data.get("login_credentials", {})

    if not credentials:
        logger.error("No login credentials found in becomeseller test data")
        pytest.fail("Login credentials not available in becomeseller_test_data.json")

    logger.info(f"Performing SESSION login for: {credentials['email']}")

    # Perform login
    login_page = LoginPage(session_page)
    login_page.open_login_page()
    login_page.perform_login(
        email=credentials["email"],
        password=credentials["password"]
    )

    # Wait for dashboard with increased timeout and better handling
    try:
        # First wait for any navigation to complete
        session_page.wait_for_load_state("load", timeout=30000)

        # Check if we're on dashboard or if URL contains dashboard
        current_url = session_page.url
        if "dashboard" in current_url:
            logger.info("SESSION authentication successful - will persist across tests")
        else:
            # Try waiting for dashboard URL with longer timeout
            session_page.wait_for_url("**/dashboard**", timeout=30000)
            logger.info("SESSION authentication successful - will persist across tests")
    except Exception as e:
        # Check if we're actually logged in despite the timeout
        current_url = session_page.url
        if "dashboard" in current_url or "login" not in current_url:
            logger.info(f"SESSION authentication successful (URL: {current_url})")
        else:
            logger.error(f"Session login failed: {e}")
            pytest.fail("Session authentication failed")

    yield session_page


@pytest.fixture(scope="session")
def seller_auth_state(browser: Browser, request) -> dict:
    """
    Login ONCE, save storage_state for reuse by all session fixtures.

    Returns cached auth state dict. Saves to disk for parallel workers.
    Validates cached state before returning — re-logins if stale.

    With pytest-xdist: FileLock ensures only ONE worker performs login.
    Other workers wait for the lock, then read the cached state.
    """
    from pages.login_page import LoginPage

    # FileLock prevents race condition when 4 workers start simultaneously.
    # First worker acquires lock, logs in, writes file.
    # Other workers wait, then read cached state without logging in.
    with FileLock(str(AUTH_STATE_LOCK), timeout=120):
        # Inside lock: check cache first (another worker may have just written it)
        if AUTH_STATE_PATH.exists():
            try:
                state = json.loads(AUTH_STATE_PATH.read_text())
                logger.info("Found cached auth state, validating...")

                headless = request.config.getoption("headless")
                if headless:
                    ctx_opts = settings.get_browser_context_options_with_viewport()
                else:
                    ctx_opts = settings.get_browser_context_options()
                ctx_opts["storage_state"] = state
                val_ctx = browser.new_context(**ctx_opts)
                val_page = val_ctx.new_page()
                val_page.goto(f"{settings.BASE_URL}/dashboard", wait_until="load", timeout=30000)
                val_page.wait_for_load_state("networkidle", timeout=15000)
                val_url = val_page.url
                val_page.close()
                val_ctx.close()

                if "auth/login" not in val_url:
                    logger.info(f"Cached auth state is valid (URL: {val_url})")
                    return state
                else:
                    logger.warning("Cached auth state expired, performing fresh login")
            except Exception as e:
                logger.warning(f"Cached auth state check failed: {e}, performing fresh login")

        logger.info("Performing login to generate auth state")

        headless = request.config.getoption("headless")
        if headless:
            context_options = settings.get_browser_context_options_with_viewport()
        else:
            context_options = settings.get_browser_context_options()

        context = browser.new_context(**context_options)
        page = context.new_page()

        seller_data = TestDataLoader.load("shopcreate")
        credentials = seller_data.get("valid_credentials", {})
        if not credentials:
            pytest.fail("Seller credentials not available in shopcreate_test_data.json")

        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.perform_login(
            email=credentials["email"],
            password=credentials["password"]
        )

        # Wait for login to complete — staging can take 10-15s to redirect
        page.wait_for_load_state("load", timeout=30000)
        if "auth/login" in page.url:
            try:
                page.wait_for_url("**/dashboard**", timeout=30000)
            except Exception:
                pass
        if "auth/login" in page.url:
            pytest.fail("Auth state generation failed - stuck on login page")

        logger.info(f"Auth state generated. URL: {page.url}")

        # Выбрать активный магазин вместо "На рассмотрении"
        try:
            # Перейти на dashboard/products чтобы загрузился полный layout с header
            page.goto(f"{settings.BASE_URL}/dashboard/products", wait_until="networkidle", timeout=15000)
            shop_btn = page.locator(".MuiAvatar-root").first
            logger.info(f"Shop button visible: {shop_btn.is_visible(timeout=10000)}")
            if shop_btn.is_visible():
                shop_btn.click()
                popover = page.locator(".MuiPopover-paper")
                popover.wait_for(state="visible", timeout=5000)
                # Ищем menuitem со статусом "Faol" или "Активный" (активный магазин)
                active_shop = popover.locator(
                    "[role='menuitem']:has-text('Faol'), "
                    "[role='menuitem']:has-text('Активный'), "
                    "[role='menuitem']:has-text('Active')"
                ).first
                if active_shop.is_visible(timeout=3000):
                    active_shop.click()
                    page.wait_for_load_state("networkidle", timeout=10000)
                    logger.info("Switched to active shop")
                else:
                    page.keyboard.press("Escape")
                    logger.info("No active shop found, keeping current shop")
            else:
                logger.warning("Shop button not visible on dashboard")
        except Exception as e:
            logger.warning(f"Failed to switch shop: {e}")

        # Переключить язык на русский
        try:
            lang_btn = page.get_by_role("button", name="Languages button")
            if lang_btn.is_visible(timeout=5000):
                lang_btn.click()
                ru_option = page.get_by_role("menuitem", name="Русский")
                if ru_option.is_visible(timeout=3000):
                    ru_option.click()
                    page.wait_for_load_state("networkidle", timeout=10000)
                    # Ждём пока sidebar обновится на русский
                    page.locator("nav a[aria-label='Товары'], nav a[aria-label='Главная страница']").first.wait_for(
                        state="visible", timeout=10000
                    )
                    logger.info("Switched language to Russian")
                else:
                    page.keyboard.press("Escape")
                    logger.info("Russian language option not found")
        except Exception as e:
            logger.warning(f"Failed to switch language: {e}")

        state = context.storage_state()
        AUTH_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
        AUTH_STATE_PATH.write_text(json.dumps(state))
        logger.info(f"Auth state cached to {AUTH_STATE_PATH}")

        page.close()
        context.close()
        return state


@pytest.fixture
def fresh_authenticated_page(browser: Browser, request, seller_auth_state) -> Generator[Page, None, None]:
    """
    Function-scoped: each test gets its own isolated context+page with auth.

    Uses cached seller_auth_state dict (serializable, parallel-safe).
    Creates a new browser context per test — no state pollution.
    """
    headless = request.config.getoption("headless")
    if headless:
        ctx_opts = settings.get_browser_context_options_with_viewport()
    else:
        ctx_opts = settings.get_browser_context_options()

    ctx_opts["storage_state"] = seller_auth_state
    context = browser.new_context(**ctx_opts)
    page = context.new_page()

    yield page

    page.close()
    context.close()


@pytest.fixture(scope="session")
def seller_authenticated_session(browser: Browser, request, seller_auth_state) -> Generator[Page, None, None]:
    """
    Session-level authenticated page for SELLER account.

    Uses cached storage_state to skip login. Fast context creation.

    Usage:
        class TestShopCreate:
            def test_step1(self, seller_authenticated_session): ...
            def test_step2(self, seller_authenticated_session): ...
    """
    logger.info("Creating SELLER session from cached auth state")

    headless = request.config.getoption("headless")
    if headless:
        context_options = settings.get_browser_context_options_with_viewport()
    else:
        context_options = settings.get_browser_context_options()

    # Use cached auth state — no login needed!
    context_options["storage_state"] = seller_auth_state
    context = browser.new_context(**context_options)
    page = context.new_page()

    # Navigate to dashboard to verify auth works
    page.goto(f"{settings.STAGING_URL}/dashboard", wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=15000)

    if "auth/login" in page.url:
        logger.warning("Cached auth state expired, re-authenticating")
        AUTH_STATE_PATH.unlink(missing_ok=True)
        from pages.login_page import LoginPage
        seller_data = TestDataLoader.load("shopcreate")
        credentials = seller_data.get("valid_credentials", {})
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.perform_login(email=credentials["email"], password=credentials["password"])
        try:
            page.wait_for_url("**/dashboard**", timeout=30000)
        except Exception:
            page.wait_for_load_state("networkidle", timeout=15000)
        if "auth/login" in page.url:
            # Last resort: direct navigation after login
            page.goto(f"{settings.STAGING_URL}/dashboard", wait_until="domcontentloaded")
            page.wait_for_load_state("networkidle", timeout=15000)
        if "auth/login" in page.url:
            pytest.fail("Seller session authentication failed")

    logger.info(f"SELLER SESSION ready (URL: {page.url})")

    yield page

    logger.info("Closing SELLER SESSION")
    page.close()
    context.close()


# ================================================================================
# Context and Page Fixtures (Session Scope - SHARED BROWSER!)
# ================================================================================
# These fixtures share the same browser session across all tests
# This is what users typically expect - browser stays open

@pytest.fixture(scope="session")
def context(browser: Browser, request) -> Generator[BrowserContext, None, None]:
    """
    Session-level browser context - shared across all tests.

    Single context for entire test session:
    - Browser stays open
    - Faster test execution
    - State persists between tests

    Args:
        browser: Browser instance (session-scoped)
        request: Pytest request object

    Yields:
        BrowserContext instance
    """
    logger.info("Creating SESSION-SCOPED browser context")

    headless = request.config.getoption("headless")

    # Use viewport for headless mode, no_viewport for headed mode (maximized)
    if headless:
        context_options = settings.get_browser_context_options_with_viewport()
    else:
        context_options = settings.get_browser_context_options()

    context_instance = browser.new_context(**context_options)

    yield context_instance

    logger.info("Closing SESSION-SCOPED browser context")
    context_instance.close()


@pytest.fixture(scope="session")
def page(context: BrowserContext, request) -> Generator[Page, None, None]:
    """
    Session-level page - shared across all tests.

    Single page instance for entire test session:
    - Browser stays open between tests
    - Login state persists
    - Much faster execution

    Args:
        context: BrowserContext instance (session-scoped)
        request: Pytest request object

    Yields:
        Page instance
    """
    logger.info("Creating SESSION-SCOPED page")

    page_instance = context.new_page()

    # Navigate to base URL
    base_url = request.config.getoption("url_name")
    page_instance.goto(base_url)

    yield page_instance

    logger.info("Closing SESSION-SCOPED page")
    page_instance.close()


@pytest.fixture(scope="session")
def page_with_base_url(page: Page, request) -> Generator[Page, None, None]:
    """
    Session-level fixture that ensures page is at base URL.

    Useful for tests that need to start at home page.

    Args:
        page: Page instance
        request: Pytest request object

    Yields:
        Page instance at base URL
    """
    base_url = request.config.getoption("url_name")
    page.goto(base_url)
    yield page


# Backward compatibility alias
@pytest.fixture
def browserInstance(page_with_base_url: Page) -> Page:
    """
    Backward compatibility fixture.

    DEPRECATED: Use 'page' or 'page_with_base_url' instead.
    """
    logger.warning("'browserInstance' fixture is deprecated. Use 'page' instead.")
    return page_with_base_url


# ================================================================================
# Test Data Fixture (Using New TestDataLoader)
# ================================================================================

@pytest.fixture
def test_data(request) -> Dict[str, Any]:
    """
    Load test data based on test module name.

    Uses centralized TestDataLoader with caching for performance.

    Args:
        request: Pytest request object

    Returns:
        Dictionary of test data or empty dict if not found

    Example:
        def test_login(page, test_data):
            email = test_data['valid_credentials']['email']
    """
    test_module = request.module.__name__

    # Extract module name from test file name
    # e.g., "tests.test_login" -> "login"
    if "test_" in test_module:
        module_name = test_module.split("test_")[-1]

        try:
            data = TestDataLoader.load(module_name)
            logger.debug(f"Loaded test data for module: {module_name}")
            return data
        except FileNotFoundError:
            logger.warning(f"No test data found for module: {module_name}")
            return {}

    return {}


# ================================================================================
# Authentication Fixtures
# ================================================================================

@pytest.fixture(scope="session")
def authenticated_page(page: Page) -> Page:
    """
    Session-level fixture providing pre-authenticated page.

    Performs login ONCE at session start and maintains auth across all tests.
    Browser stays open, login state persists.

    Args:
        page: Page instance (session-scoped)

    Returns:
        Authenticated Page instance

    Example:
        def test_dashboard_features(authenticated_page):
            # Page is already logged in
            assert "dashboard" in authenticated_page.url
    """
    from pages.login_page import LoginPage

    # Load default credentials from login test data
    login_data = TestDataLoader.load("login")
    credentials = login_data.get("login_credentials") or login_data.get("valid_credentials")

    if not credentials:
        # Try shopcreate credentials as fallback
        shopcreate_data = TestDataLoader.load("shopcreate")
        credentials = shopcreate_data.get("valid_credentials")

    if not credentials:
        logger.error("No login credentials found in test data")
        pytest.skip("Login credentials not available in test data")

    logger.info(f"Performing SESSION authentication for: {credentials.get('email')}")

    # Navigate to login and perform authentication
    login_page = LoginPage(page)
    login_page.open_login_page()

    login_page.perform_login(
        email=credentials["email"],
        password=credentials["password"]
    )

    # Wait for successful login (dashboard redirect)
    try:
        page.wait_for_load_state("load", timeout=15000)
        if "dashboard" in page.url:
            logger.info("SESSION authentication successful - will persist across all tests")
        else:
            page.wait_for_url("**/dashboard/**", timeout=15000)
            logger.info("SESSION authentication successful")
    except Exception as e:
        if "dashboard" in page.url or "login" not in page.url:
            logger.info(f"SESSION authentication successful (URL: {page.url})")
        else:
            logger.error(f"Authentication failed: {e}")
            pytest.fail("Authentication failed")

    return page


# Backward compatibility for test_becomeseller.py
@pytest.fixture(scope="class")
def authenticated_seller_session(page: Page, test_data: Dict[str, Any]) -> Page:
    """
    Class-level authentication fixture for backward compatibility.

    DEPRECATED: Use 'authenticated_page' instead.
    This fixture is kept for compatibility with existing test_becomeseller.py.

    Note: Class-scoped fixtures still share state within a test class,
    so be cautious about state pollution.
    """
    logger.warning(
        "'authenticated_seller_session' is deprecated. "
        "Consider refactoring to use function-scoped 'authenticated_page'."
    )

    from pages.login_page import LoginPage

    # Load become seller test data
    becomeseller_data = TestDataLoader.load("becomeseller")
    credentials = becomeseller_data.get("login_credentials", {})

    if not credentials:
        pytest.skip("Login credentials not found in becomeseller test data")

    # Perform login
    login_page = LoginPage(page)
    login_page.navigate_to(login_page.url)
    login_page.perform_login(
        email=credentials["email"],
        password=credentials["password"]
    )
    page.wait_for_url("**/dashboard/**", timeout=15000)

    return page


# ================================================================================
# Auto-Use Fixtures (Configurable via pytest.ini markers)
# ================================================================================

# Console and network capture disabled for session-scoped fixtures
# These fixtures conflict with session-scope page fixture
# If needed, enable per-test with custom fixtures


@pytest.fixture(autouse=True)
def screenshot_on_failure(request) -> None:
    """
    Auto-use fixture to capture screenshot on test failure.

    Screenshots are saved to settings.SCREENSHOTS_DIR.
    Skipped for tests with @pytest.mark.no_failure_screenshot
    """
    if not settings.ENABLE_SCREENSHOTS_ON_FAILURE:
        yield
        return

    # Skip if marker present
    if request.node.get_closest_marker('no_failure_screenshot'):
        yield
        return

    # Check if page fixture is being used
    if 'page' not in request.fixturenames:
        yield
        return

    yield

    # Check if test failed
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        test_name = request.node.name
        logger.info(f"Test failed: {test_name}, capturing screenshot")

        try:
            page = request.getfixturevalue('page')
            BrowserHelpers.capture_screenshot(page, f"failure_{test_name}")
        except Exception as e:
            logger.error(f"Failed to capture failure screenshot: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to make test result available to fixtures.

    This allows the screenshot_on_failure fixture to check if test failed.
    """
    outcome = yield
    rep = outcome.get_result()

    # Store test result in different phases
    setattr(item, f"rep_{rep.when}", rep)


# ================================================================================
# Allure Reporting Configuration
# ================================================================================

# ================================================================================
# Test Ordering — sequential by page, parallel by loadscope
# ================================================================================

# Priority order: Login first, then Dashboard, then pages in logical flow
PAGE_ORDER = [
    "test_login",           # 1. Login
    "test_dashboard",       # 2. Dashboard
    "shop_create",          # 3. Shop Create
    "shop_settings",        # 4. Shop Settings
    "products_list",        # 5. Products List
    "product_create",       # 6. Product Create
    "product_detail",       # 7. Product Detail
    "orders",               # 8. Orders
    "order_detail",         # 9. Order Detail
    "returns",              # 10. Returns
    "employee",             # 11. Employee
    "profile_settings",     # 12. Profile Settings
    "test_promotions",      # 13. Promotions
    "test_reviews",         # 14. Reviews
]


def _get_sort_key(item) -> tuple:
    """Get (page_priority, order_marker, original_index) for sorting.

    1. Page priority — groups tests by page in logical flow
    2. order marker — preserves @pytest.mark.order(N) within a page
    3. original index — preserves file order for tests without order marker
    """
    module_path = str(item.fspath)
    page_priority = len(PAGE_ORDER)
    for idx, page_key in enumerate(PAGE_ORDER):
        if page_key in module_path:
            page_priority = idx
            break

    order_marker = item.get_closest_marker("order")
    order_value = order_marker.args[0] if order_marker and order_marker.args else 999999

    return (page_priority, order_value)


def pytest_collection_modifyitems(config, items):
    """Sort tests by page priority, then by order marker within each page."""
    items.sort(key=_get_sort_key)
    logger.info(
        f"Tests ordered by page priority: {len(items)} items, "
        f"{len(set(item.fspath for item in items))} files"
    )


def pytest_configure(config):
    """
    Configure pytest with Allure and metadata.

    Sets up:
    - Allure TestOps integration
    - HTML report metadata
    - Custom markers
    """
    # Create necessary directories
    settings.SCREENSHOTS_DIR.mkdir(exist_ok=True, parents=True)
    settings.REPORTS_DIR.mkdir(exist_ok=True, parents=True)
    settings.LOGS_DIR.mkdir(exist_ok=True, parents=True)

    # Allure TestOps Configuration
    if settings.ALLURE_ENDPOINT and settings.ALLURE_TOKEN:
        logger.info("Allure TestOps integration configured")
        logger.info(f"Allure Endpoint: {settings.ALLURE_ENDPOINT}")
        logger.info(f"Allure Project ID: {settings.ALLURE_PROJECT_ID}")
    else:
        logger.info("Allure TestOps not configured (missing credentials)")

    # HTML Report Metadata
    config._metadata = {
        "Project": "Seller Web Automation",
        "Environment": config.getoption("--url_name") if hasattr(config, 'getoption') else settings.BASE_URL,
        "Browser": config.getoption("--browser_name") if hasattr(config, 'getoption') else settings.BROWSER,
        "Python": "3.13",
        "Framework": "Playwright + pytest + Allure",
        "Test Data Dir": str(settings.TEST_DATA_DIR),
    }


def pytest_html_report_title(report):
    """Customize HTML report title."""
    report.title = "Seller Web - Test Automation Report"

