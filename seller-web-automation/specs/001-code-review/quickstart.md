
# Quickstart Guide: Test Automation Framework

**Goal**: Get a new developer writing their first test in 15 minutes.

**Target Audience**: Developers/QA engineers new to this project.

---

## Step 1: Setup (5 minutes)

### 1.1 Prerequisites

Check that you have:
- Python 3.13+ installed
- Git installed
- IDE with Python support (VS Code, PyCharm, etc.)

```bash
# Verify Python version
python --version  # Should show 3.13+

# Verify Git
git --version
```

### 1.2 Clone and Install

```bash
# Clone repository
git clone <repository-url>
cd seller_web1

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### 1.3 Configure Environment

Create `.env` file in project root:

```bash
# Copy example or create new
cat > .env << 'EOF'
# Base URL
BASE_URL=https://dev-seller.greatmall.uz

# Browser settings
BROWSER=chromium
HEADLESS=false

# Allure TestOps (optional)
ALLURE_ENDPOINT=https://allure.example.com
ALLURE_TOKEN=your_token_here
ALLURE_PROJECT_ID=your_project_id

# Test credentials (DO NOT commit real credentials!)
TEST_EMAIL=test@example.com
TEST_PASSWORD=SecurePassword123
EOF
```

**✅ Setup Complete!** You're ready to run tests.

---

## Step 2: Run Your First Test (2 minutes)

### 2.1 Run All Login Tests

```bash
# Run login tests (7 tests)
pytest tests/test_login.py -v

# Expected output:
# tests/test_login.py::TestLogin::test_verify_login_ui_elements PASSED
# tests/test_login.py::TestLogin::test_verify_email_validation PASSED
# ...
# ========== 7 passed in 15.23s ==========
```

### 2.2 Run Single Test

```bash
# Run specific test
pytest tests/test_login.py::TestLogin::test_verify_email_validation -v

# Run with visible browser (not headless)
pytest tests/test_login.py::TestLogin::test_verify_email_validation -v --headless=false
```

### 2.3 Run Tests in Parallel

```bash
# Run tests in parallel (4 workers)
pytest tests/ -n 4 -v

# Expected: 50%+ faster execution
```

**✅ First Test Complete!** You've successfully run existing tests.

---

## Step 3: Write a New Page Object (3 minutes)

### 3.1 Create Page Object File

Create `pages/dashboard_page.py`:

```python
"""Dashboard page object"""
from typing import Optional
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Dashboard page - main user landing page after login"""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "https://dev-seller.greatmall.uz/dashboard"

    # =========================================================================
    # Locators (as @property methods)
    # =========================================================================

    @property
    def user_menu_button(self) -> Locator:
        """User menu button in top-right corner"""
        return self.page.get_by_role("button", name="User Menu")

    @property
    def logout_button(self) -> Locator:
        """Logout button in user menu"""
        return self.page.get_by_role("menuitem", name="Logout")

    @property
    def dashboard_title(self) -> Locator:
        """Dashboard page title"""
        return self.page.get_by_role("heading", name="Dashboard")

    # =========================================================================
    # Actions
    # =========================================================================

    def open_user_menu(self) -> None:
        """Open user menu dropdown"""
        self.user_menu_button.click()

    def click_logout(self) -> None:
        """Click logout button"""
        self.logout_button.click()

    # =========================================================================
    # Verifications
    # =========================================================================

    def is_dashboard_visible(self) -> bool:
        """Check if dashboard page is displayed"""
        return self.dashboard_title.is_visible()

    def is_user_menu_open(self) -> bool:
        """Check if user menu is expanded"""
        return self.logout_button.is_visible()
```

**Key Points**:
- ✅ Locators use ARIA roles (`get_by_role`)
- ✅ Locators are `@property` methods
- ✅ Actions are descriptive methods
- ✅ Verifications return `bool`, no assertions
- ✅ All methods have type hints and docstrings

---

## Step 4: Write a New Test (3 minutes)

### 4.1 Create Test File

Create `tests/test_dashboard.py`:

```python
"""Dashboard page tests"""
import pytest
import allure
from pages.dashboard_page import DashboardPage


@allure.epic("Seller Web Platform")
@allure.feature("Dashboard")
class TestDashboard:
    """Dashboard page test suite"""

    @allure.title("Verify dashboard page loads after login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_dashboard_loads(self, authenticated_page):
        """Test that dashboard page loads correctly after login"""

        with allure.step("Initialize dashboard page object"):
            dashboard_page = DashboardPage(authenticated_page)

        with allure.step("Verify dashboard is visible"):
            assert dashboard_page.is_dashboard_visible(), \
                "Dashboard page should be visible after login"

        with allure.step("Verify correct URL"):
            assert "dashboard" in authenticated_page.url, \
                "URL should contain 'dashboard'"

    @allure.title("Verify user can logout from dashboard")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_verify_logout(self, authenticated_page):
        """Test that user can logout from dashboard"""

        with allure.step("Initialize dashboard page object"):
            dashboard_page = DashboardPage(authenticated_page)

        with allure.step("Open user menu"):
            dashboard_page.open_user_menu()
            assert dashboard_page.is_user_menu_open(), \
                "User menu should open when clicked"

        with allure.step("Click logout"):
            dashboard_page.click_logout()

        with allure.step("Verify redirected to login page"):
            authenticated_page.wait_for_url("**/login**", timeout=5000)
            assert "login" in authenticated_page.url, \
                "Should redirect to login page after logout"
```

**Key Points**:
- ✅ Tests use `authenticated_page` fixture (pre-logged-in)
- ✅ Each test has Allure decorators
- ✅ Test steps wrapped in `with allure.step()`
- ✅ Assertions have descriptive messages
- ✅ Tests use page object methods, not direct locators

### 4.2 Run Your New Test

```bash
# Run your new test
pytest tests/test_dashboard.py -v

# Expected output:
# tests/test_dashboard.py::TestDashboard::test_verify_dashboard_loads PASSED
# tests/test_dashboard.py::TestDashboard::test_verify_logout PASSED
# ========== 2 passed in 8.45s ==========
```

**✅ First Test Written!** You've created a page object and test from scratch.

---

## Step 5: Run Tests in Parallel (1 minute)

### 5.1 Parallel Execution

```bash
# Run all tests in parallel
pytest tests/ -n 4 --dist loadscope -v

# With Allure report generation
pytest tests/ -n 4 --dist loadscope --alluredir=allure-results -v
```

**Why It Works**:
- Function-scoped fixtures provide test isolation
- Each test gets fresh browser context and page
- No state pollution between tests

### 5.2 Verify Test Isolation

```bash
# Run tests in random order to verify independence
pytest tests/ --random-order -v

# All tests should pass regardless of order
```

---

## Step 6: Debug Failing Tests (1 minute)

### 6.1 Run Single Test with Debugging

```bash
# Run test with visible browser and slower execution
pytest tests/test_dashboard.py::TestDashboard::test_verify_logout -v \
  --headless=false \
  --slowmo=1000

# --slowmo=1000 adds 1 second delay between actions (easier to see)
```

### 6.2 Capture Screenshots on Failure

Screenshots are automatically captured on test failure:

```python
# In conftest.py (already configured):
@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    """Auto-capture screenshot on test failure"""
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/failure_{request.node.name}.png")
```

Failures save screenshots to `screenshots/` directory.

### 6.3 View Console Logs

```python
# Console logs are automatically captured (conftest.py):
@pytest.fixture(autouse=True)
def capture_console_logs(page):
    """Auto-capture console logs during test"""
    console_logs = []
    page.on("console", lambda msg: console_logs.append(msg.text))
    page._console_logs = console_logs
    yield

# Access in test:
def test_example(page):
    # ... test steps ...
    print(page._console_logs)  # View console messages
```

---

## Step 7: View Allure Reports (1 minute)

### 7.1 Generate Allure Report

```bash
# Run tests with Allure result generation
pytest tests/ --alluredir=allure-results -v

# Generate HTML report
allure generate allure-results -o allure-report --clean

# Open report in browser
allure open allure-report
```

### 7.2 View Report

Allure report shows:
- ✅ Test results (passed/failed)
- ✅ Test steps with timing
- ✅ Screenshots (on failure)
- ✅ Console logs
- ✅ Network requests
- ✅ Test history and trends

---

## Common Tasks

### Add Test Data

**Create JSON file** (`test_data/dashboard_test_data.json`):
```json
{
  "user_settings": {
    "language": "en",
    "timezone": "UTC"
  }
}
```

**Use in test**:
```python
def test_user_settings(authenticated_page, test_data):
    """Test user settings"""
    language = test_data["user_settings"]["language"]
    # Use test data in test
```

### Add New Locator Strategy

**Priority**:
1. ARIA roles: `page.get_by_role("button", name="Submit")`
2. Labels: `page.get_by_label("Email")`
3. Placeholder: `page.get_by_placeholder("Enter email")`
4. Test ID: `page.get_by_test_id("submit-btn")` (ask devs to add)
5. CSS/XPath: Last resort only

**Example**:
```python
# ✅ GOOD - ARIA role
self.page.get_by_role("button", name="Create Account")

# ❌ BAD - CSS class
self.page.locator(".MuiButton-root-123abc")  # Brittle!
```

### Run Specific Test Types

```bash
# Smoke tests only
pytest -m smoke -v

# Negative tests only
pytest -m negative -v

# Functional tests only
pytest -m functional -v

# Multiple markers
pytest -m "smoke or critical" -v
```

### Type Checking with mypy

```bash
# Install mypy
pip install mypy

# Run type checking
mypy pages/ tests/

# Configure in mypy.ini (already created)
```

### Code Formatting with black

```bash
# Install black
pip install black

# Format all files
black pages/ tests/ utils/ config/

# Check formatting without changes
black pages/ tests/ --check
```

---

## Project Structure Reference

```
seller_web1/
├── pages/              # Page objects (ARIA roles, no tests)
├── tests/             # Test files (use page objects)
├── utils/            # Utilities (SmartWaits, TestDataLoader)
├── config/           # Configuration (settings.py)
├── test_data/       # Test data (JSON files)
│   └── schemas/     # JSON schemas for validation
├── fixtures/        # Fixture modules (planned)
├── reports/         # Test reports
├── logs/           # Log files
├── screenshots/    # Failure screenshots
├── allure-results/ # Allure test results
├── conftest.py    # pytest fixtures
├── pytest.ini     # pytest configuration
├── requirements.txt # Python dependencies
├── .env          # Environment variables
└── README.md    # Project documentation
```

---

## Best Practices Checklist

### Page Objects
- [ ] Locators use ARIA roles first
- [ ] Locators are `@property` methods
- [ ] No test methods (no `test_*`)
- [ ] No assertions in page objects
- [ ] All methods have type hints
- [ ] All methods have docstrings

### Tests
- [ ] Tests use page object methods
- [ ] Tests have Allure decorators
- [ ] Test steps use `with allure.step()`
- [ ] Assertions have descriptive messages
- [ ] Tests are independent (pass in any order)

### General
- [ ] Tests pass with `pytest -n 4` (parallel)
- [ ] Tests pass with `pytest --random-order`
- [ ] No hardcoded credentials in code
- [ ] Type hints on all functions
- [ ] Docstrings on all public methods

---

## Next Steps

Now that you've completed the quickstart, explore:

1. **Read CLAUDE.md**: Development guidelines and rules
2. **Read README.md**: Full project documentation
3. **Review existing tests**: Learn patterns from `test_login.py`, `test_registration.py`
4. **Review page objects**: Study `pages/base_page.py`, `pages/login_page.py`
5. **Explore utilities**: Check `utils/waits.py`, `utils/test_data_loader.py`

---

## Troubleshooting

### Issue: Tests fail with "context" errors
**Solution**: Ensure `context` and `page` fixtures are function-scoped (not session/class).

### Issue: Tests fail when run in parallel
**Solution**: Check for shared mutable state. Each test should be independent.

### Issue: Locators not found
**Solution**:
1. Check ARIA roles with Playwright Inspector: `playwright codegen <url>`
2. Request test IDs from dev team if ARIA roles unavailable
3. Avoid CSS classes (especially Material-UI classes)

### Issue: Type checking errors with mypy
**Solution**: Add type hints to function signatures. Playwright has built-in stubs.

### Issue: Screenshots not captured on failure
**Solution**: Ensure `screenshot_on_failure` fixture is enabled in conftest.py.

---

## Resources

- **Playwright Documentation**: https://playwright.dev/python
- **pytest Documentation**: https://docs.pytest.org/
- **Allure Framework**: https://docs.qameta.io/allure/
- **Project README**: `README.md`
- **Development Guidelines**: `CLAUDE.md`

---

**Congratulations!** You're now ready to contribute to the test automation framework.

**Time Elapsed**: ~15 minutes
**Next Goal**: Write 3 more tests and open a pull request!
