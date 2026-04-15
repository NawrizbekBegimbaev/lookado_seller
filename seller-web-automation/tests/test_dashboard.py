"""
Dashboard Test Suite — Post-Login Functionality.

Senior QA approach: minimal tests, maximum coverage.
All tests (except auth guard) require fresh_authenticated_page.
Currently blocked by OTP authentication change on staging.
"""

import pytest
import allure
from playwright.sync_api import expect
from config.settings import settings


# =============================================================================
# AUTH GUARD — Works without authentication
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Дашборд")
@allure.feature("Защита авторизации")
class TestDashboardAuthGuard:
    """Authentication guard — unauthenticated users must be redirected."""

    @allure.title("Неавторизованный пользователь перенаправляется на страницу входа")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_unauthenticated_redirects_to_login(self, browser, request):
        """Unauthenticated access to /dashboard redirects to login."""
        with allure.step("Создание неавторизованного контекста браузера"):
            headless = request.config.getoption("headless", default=True)
            context_options = (
                settings.get_browser_context_options_with_viewport()
                if headless else settings.get_browser_context_options()
            )
            context = browser.new_context(**context_options)
            page = context.new_page()
        try:
            with allure.step("Переход на дашборд без авторизации"):
                page.goto(f"{settings.BASE_URL}/dashboard")
                page.wait_for_load_state("load")
                page.wait_for_load_state("networkidle")
            with allure.step("Проверка перенаправления на страницу входа"):
                assert "login" in page.url.lower() or "auth" in page.url.lower(), \
                    f"BUG: Unauthenticated user should be redirected to login, got: {page.url}"
        finally:
            context.close()


# =============================================================================
# SMOKE — Core dashboard after login
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Дашборд")
@allure.feature("Интерфейс дашборда")
class TestDashboardSmoke:
    """Core dashboard functionality — requires authentication."""

    @allure.title("Дашборд загружается с основными элементами")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_dashboard_loads_with_core_elements(self, fresh_authenticated_page):
        """Dashboard has sidebar, shop button, and content area."""
        page = fresh_authenticated_page
        with allure.step("Навигация на дашборд"):
            page.goto(f"{settings.BASE_URL}/dashboard", wait_until="domcontentloaded")
            page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка URL дашборда"):
            assert "dashboard" in page.url.lower(), f"Expected dashboard URL, got: {page.url}"
        with allure.step("Проверка видимости кнопки выбора магазина"):
            shop_btn = page.locator("button:has(.MuiAvatar-root)").first
            expect(shop_btn).to_be_visible(timeout=10000)
        with allure.step("Проверка видимости бокового меню"):
            sidebar = page.locator("nav").or_(page.locator("[role='navigation']")).first
            expect(sidebar).to_be_visible(timeout=5000)

    @allure.title("Проверка HTTPS соединения дашборда")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_https_connection(self, fresh_authenticated_page):
        """Dashboard is served over HTTPS."""
        page = fresh_authenticated_page
        with allure.step("Навигация на дашборд"):
            page.goto(f"{settings.BASE_URL}/dashboard", wait_until="domcontentloaded")
        with allure.step("Проверка что дашборд загружен по HTTPS"):
            assert page.url.startswith("https://"), \
                f"BUG: Dashboard must use HTTPS, got: {page.url}"

    @allure.title("Отсутствие чувствительных данных в URL")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_no_sensitive_data_in_url(self, fresh_authenticated_page):
        """No passwords or tokens exposed in URL."""
        page = fresh_authenticated_page
        with allure.step("Навигация на дашборд"):
            page.goto(f"{settings.BASE_URL}/dashboard", wait_until="domcontentloaded")
        with allure.step("Проверка отсутствия чувствительных данных в URL"):
            url_lower = page.url.lower()
            for pattern in ["password", "token", "secret", "api_key"]:
                assert pattern not in url_lower, \
                    f"BUG: URL contains sensitive data: '{pattern}'"


# =============================================================================
# NAVIGATION — Sidebar navigation to pages
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Дашборд")
@allure.feature("Навигация")
class TestDashboardNavigation:
    """Sidebar navigation — each link reaches correct page."""

    @allure.title("Навигация по боковому меню")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("aria_label,parent_label", [
        ("Товары", None),
        ("Накладные", None),
        ("Акции", None),
        ("Продвижение", None),
        ("Отзывы", None),
        ("Настройки", None),
    ], ids=["products", "invoices", "promotions", "advertising", "reviews", "settings"])
    def test_sidebar_navigation(self, fresh_authenticated_page, aria_label, parent_label):
        """Clicking sidebar item is visible and clickable."""
        page = fresh_authenticated_page
        sidebar = page.locator("nav.minimal__nav__section__vertical")

        with allure.step("Переход на дашборд"):
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="networkidle", timeout=15000)
            sidebar.wait_for(state="visible", timeout=10000)

        with allure.step(f"Клик по пункту меню: {aria_label}"):
            if parent_label:
                parent = sidebar.get_by_role("button", name=parent_label)
                parent.click()
                page.wait_for_load_state("domcontentloaded")

            nav_item = sidebar.locator(f"a[aria-label='{aria_label}']")
            nav_item.wait_for(state="visible", timeout=5000)
            nav_item.click()
            page.wait_for_load_state("networkidle")

        with allure.step(f"Проверка навигации: {aria_label}"):
            assert "dashboard" in page.url.lower(), \
                f"BUG: Clicking '{aria_label}' should stay on dashboard, got: {page.url}"

    @allure.title("Сохранение сессии после обновления страницы")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_session_persists_after_refresh(self, fresh_authenticated_page):
        """Session survives page refresh on dashboard."""
        page = fresh_authenticated_page
        with allure.step("Навигация на дашборд"):
            page.goto(f"{settings.BASE_URL}/dashboard", wait_until="domcontentloaded")
        with allure.step("Проверка что мы на дашборде"):
            assert "dashboard" in page.url.lower()
        with allure.step("Обновление страницы и проверка сохранения сессии"):
            page.reload()
            page.wait_for_load_state("load")
            page.wait_for_load_state("networkidle")
            assert "login" not in page.url.lower(), \
                "BUG: Session lost after page refresh"


# =============================================================================
# SHOP DROPDOWN — Shop selector functionality
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Дашборд")
@allure.feature("Выпадающий список магазинов")
class TestDashboardShopDropdown:
    """Shop dropdown — switching between seller shops."""

    @allure.title("Открытие выпадающего списка магазинов")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.functional
    def test_shop_dropdown_opens(self, fresh_authenticated_page):
        """Shop dropdown button opens menu with shop list."""
        page = fresh_authenticated_page
        with allure.step("Переход на дашборд и поиск кнопки магазина"):
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="networkidle", timeout=15000)
            shop_btn = page.locator("button:has(.MuiAvatar-root)").first
            expect(shop_btn).to_be_visible(timeout=5000)
        with allure.step("Открытие выпадающего списка магазинов"):
            shop_btn.click()
            page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка видимости выпадающего меню"):
            menu = page.locator("[role='menu']").or_(
                page.locator("[role='listbox']")
            ).or_(page.locator(".MuiMenu-paper")).or_(
                page.locator(".MuiPopover-paper")
            )
            assert menu.first.is_visible(timeout=5000), \
                "BUG: Shop dropdown menu not visible after click"
            page.keyboard.press("Escape")

    @allure.title("Наличие кнопки добавления магазина в выпадающем списке")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_dropdown_has_add_shop_button(self, fresh_authenticated_page):
        """Shop dropdown contains 'Add Shop' option."""
        page = fresh_authenticated_page
        with allure.step("Открытие выпадающего списка магазинов"):
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="networkidle", timeout=15000)
            shop_btn = page.locator("button:has(.MuiAvatar-root)").first
            shop_btn.click()
            popover = page.locator(".MuiPopover-paper")
            popover.wait_for(state="visible", timeout=5000)
        with allure.step("Проверка наличия кнопки 'Добавить магазин'"):
            add_shop = popover.locator(
                "button:has-text('Добавить магазин'), "
                "button:has-text('Do\\'kon qo\\'shish'), "
                "button:has-text('Add Shop')"
            ).first
            assert add_shop.is_visible(timeout=3000), \
                "BUG: 'Add Shop' button missing in dropdown"

    @allure.title("Закрытие выпадающего списка клавишей Escape")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_dropdown_closes_on_escape(self, fresh_authenticated_page):
        """Pressing Escape closes shop dropdown."""
        page = fresh_authenticated_page
        with allure.step("Открытие выпадающего списка магазинов"):
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="networkidle", timeout=15000)
            shop_btn = page.locator("button:has(.MuiAvatar-root)").first
            shop_btn.click()
            popover = page.locator(".MuiPopover-paper")
            popover.wait_for(state="visible", timeout=5000)
        with allure.step("Нажатие Escape и проверка закрытия меню"):
            page.keyboard.press("Escape")
            expect(popover).not_to_be_visible(timeout=5000)


# =============================================================================
# SESSION — Logout and session management
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Дашборд")
@allure.feature("Сессия")
class TestDashboardSession:
    """Session management — logout must be accessible."""

    @allure.title("Доступность кнопки выхода из системы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_logout_accessible(self, fresh_authenticated_page):
        """Logout button or link must be findable from dashboard."""
        page = fresh_authenticated_page
        with allure.step("Переход на дашборд"):
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="networkidle", timeout=15000)

        with allure.step("Открытие меню профиля"):
            account_btn = page.get_by_role("button", name="Account button")
            account_btn.wait_for(state="visible", timeout=10000)
            account_btn.click()

        with allure.step("Проверка наличия кнопки выхода"):
            logout_btn = page.locator(
                "button:has-text('Chiqish'), "
                "button:has-text('Выйти'), "
                "button:has-text('Sign Out')"
            ).first
            assert logout_btn.is_visible(timeout=5000), \
                "BUG: Logout button not accessible from dashboard"


# =============================================================================
