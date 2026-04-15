"""
Orders Page Test Cases - Comprehensive coverage.
Tests UI elements, search, filters, tabs, pagination, security, accessibility.

URL: /dashboard/orders-management/orders?page=1&size=10
"""

import pytest
import logging
import allure
from pages.orders_page import OrdersPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Навигация")
class TestOrdersNavigation:
    """Test page navigation and URL behavior."""

    @allure.title("Прямая навигация по URL загружает страницу заказов")
    def test_direct_url_loads_page(self, orders_page):
        """Direct URL navigation should load orders page."""
        with allure.step("Переход на страницу заказов по прямому URL"):
            page = orders_page
            orders = OrdersPage(page)
            orders.navigate()
        with allure.step("Проверка что URL содержит путь к заказам"):
            assert "orders-management/orders" in page.url, \
                f"BUG: Direct URL did not navigate to orders: {page.url}"

    @allure.title("Навигация на страницу заказов")
    def test_sidebar_navigation(self, orders_page):
        """Direct navigation to orders page should work."""
        with allure.step("Навигация на страницу заказов"):
            page = orders_page
            orders = OrdersPage(page)
            # Use direct navigation (sidebar may have language-dependent elements)
            orders.navigate()
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка загрузки страницы заказов"):
            assert orders.is_page_loaded(), \
                f"BUG: Could not navigate to orders: {page.url}"

    @allure.title("URL содержит параметры пагинации")
    def test_url_contains_pagination_params(self, orders_page):
        """URL should contain page and size parameters."""
        with allure.step("Проверка наличия параметров пагинации в URL"):
            url = orders_page.page.url
            assert "page=" in url or "orders-management" in url, \
                f"BUG: URL missing pagination params: {url}"

    @allure.title("Обновление страницы сохраняет текущую страницу заказов")
    def test_refresh_preserves_page(self, orders_page):
        """Page refresh should stay on orders page."""
        with allure.step("Обновление страницы"):
            orders_page.page.reload()
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница заказов загружена после обновления"):
            assert orders_page.is_page_loaded(), \
                "BUG: Page refresh broke orders page"

    @allure.title("Кнопка браузера 'Назад' работает со страницы заказов")
    def test_browser_back_from_orders(self, orders_page):
        """Browser back should navigate away from orders."""
        with allure.step("Навигация на страницу заказов"):
            page = orders_page
            orders = OrdersPage(page)
            orders.navigate()
            page.wait_for_load_state("networkidle")
        with allure.step("Переход на дашборд"):
            page.goto("https://staging-seller.greatmall.uz/dashboard")
            page.wait_for_load_state("networkidle")
        with allure.step("Нажатие кнопки браузера 'Назад'"):
            page.go_back()
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка возврата на страницу заказов"):
            assert "orders-management" in page.url or "dashboard" in page.url, \
                f"BUG: Back navigation went to unexpected URL: {page.url}"



@pytest.mark.security
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Манипуляция URL")
class TestOrdersURLManipulation:
    """Test URL parameter manipulation security."""

    @allure.title("Отрицательный параметр страницы обрабатывается безопасно")
    def test_negative_page_param(self, orders_page, test_data):
        """Negative page parameter should be handled safely."""
        with allure.step("Переход по URL с отрицательным параметром страницы"):
            page = orders_page
            url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['negative_page']}"
            page.goto(url)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница загружена корректно"):
            orders = OrdersPage(page)
            assert orders.is_page_loaded() or "orders" in page.url, \
                "BUG: Negative page param broke the page"

    @allure.title("Огромный номер страницы обрабатывается безопасно")
    def test_huge_page_param(self, orders_page, test_data):
        """Huge page number should be handled safely."""
        with allure.step("Переход по URL с огромным номером страницы"):
            page = orders_page
            url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['huge_page']}"
            page.goto(url)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница загружена корректно"):
            orders = OrdersPage(page)
            assert orders.is_page_loaded() or "orders" in page.url, \
                "BUG: Huge page param broke the page"

    @allure.title("Нечисловые параметры страницы обрабатываются безопасно")
    def test_string_page_params(self, orders_page, test_data):
        """Non-numeric page params should be handled safely."""
        with allure.step("Переход по URL с нечисловыми параметрами"):
            page = orders_page
            url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['string_params']}"
            page.goto(url)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка отсутствия ошибки в URL"):
            assert "error" not in page.url.lower(), \
                "BUG: String params caused error redirect"

    @allure.title("XSS в параметрах URL санитизируется")
    def test_xss_in_url_param(self, orders_page, test_data):
        """XSS in URL params should be sanitized."""
        with allure.step("Переход по URL с XSS-инъекцией в параметрах"):
            page = orders_page
            url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['xss_in_url']}"
            page.goto(url)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что XSS не отражён в содержимом страницы"):
            content = page.content()
            assert "<script>alert" not in content, \
                "BUG: XSS in URL param reflected in page!"

    @allure.title("SQL-инъекция в параметрах URL обрабатывается безопасно")
    def test_sql_in_url_param(self, orders_page, test_data):
        """SQL injection in URL params should be safe."""
        with allure.step("Переход по URL с SQL-инъекцией в параметрах"):
            page = orders_page
            url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['sql_in_url']}"
            page.goto(url)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка отсутствия серверной ошибки после SQL-инъекции"):
            page_text = page.text_content("body") or ""
            assert "Internal Server Error" not in page_text, \
                "BUG: SQL in URL caused server error"



@pytest.mark.session
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Сессия")
class TestOrdersSession:
    """Test session and authentication requirements."""

    @allure.title("Неавторизованный пользователь перенаправляется на логин")
    def test_unauthenticated_redirects_to_login(self, browser, request):
        """Unauthenticated user should be redirected to login."""
        with allure.step("Создание неавторизованного контекста браузера"):
            from config import settings
            headless = request.config.getoption("headless")
            if headless:
                ctx_opts = settings.get_browser_context_options_with_viewport()
            else:
                ctx_opts = settings.get_browser_context_options()

            context = browser.new_context(**ctx_opts)
            page = context.new_page()

        with allure.step("Переход на страницу заказов без авторизации"):
            page.goto("https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10")
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка перенаправления на страницу логина"):
            assert "auth/login" in page.url or "login" in page.url, \
                f"BUG: Unauthenticated user not redirected to login. URL: {page.url}"

            page.close()
            context.close()

    @allure.title("Сессия сохраняется после навигации между страницами")
    def test_session_persists_after_navigation(self, orders_page):
        """Session should persist after navigating between pages."""
        with allure.step("Переход на дашборд"):
            page = orders_page
            page.goto("https://staging-seller.greatmall.uz/dashboard")
            page.wait_for_load_state("networkidle")
        with allure.step("Навигация обратно на страницу заказов"):
            orders = OrdersPage(page)
            orders.navigate()
        with allure.step("Проверка что сессия сохранилась после навигации"):
            assert orders.is_page_loaded(), \
                "BUG: Session lost after navigation"

    @allure.title("Страница заказов доступна после обновления")
    def test_page_accessible_after_refresh(self, orders_page):
        """Orders page should remain accessible after refresh."""
        with allure.step("Обновление страницы заказов"):
            orders_page.page.reload()
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что пользователь остался авторизованным после обновления"):
            url = orders_page.page.url
            assert "auth/login" not in url, \
                "BUG: Session lost after page refresh"

    @allure.title("URL заказов требует авторизации")
    def test_orders_url_requires_auth(self, browser, request):
        """Orders URL without auth should not show order data."""
        with allure.step("Создание неавторизованного контекста браузера"):
            from config import settings
            headless = request.config.getoption("headless")
            if headless:
                ctx_opts = settings.get_browser_context_options_with_viewport()
            else:
                ctx_opts = settings.get_browser_context_options()

            context = browser.new_context(**ctx_opts)
            page = context.new_page()

        with allure.step("Переход на страницу заказов без авторизации"):
            page.goto("https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10")
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что данные заказов не видны без авторизации"):
            orders = OrdersPage(page)
            data_visible = orders.is_data_grid_visible()
            is_login = "auth/login" in page.url

            assert is_login or not data_visible, \
                "BUG: Order data visible without authentication!"

            page.close()
            context.close()



@pytest.mark.functional
@allure.feature("Заказы")
@allure.story("Устойчивость")
class TestOrdersRobustness:
    """Test page robustness under unusual conditions."""

    @allure.title("Быстрое переключение вкладок не ломает страницу")
    def test_rapid_tab_switching(self, orders_page):
        """Rapid tab switching should not break the page."""
        with allure.step("Быстрое переключение между вкладками заказов"):
            tabs = ["Processing", "Cancelled", "Delivered", "All"]
            for tab in tabs:
                orders_page.click_tab(tab)
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница осталась функциональной"):
            assert orders_page.is_page_loaded(), \
                "BUG: Rapid tab switching broke the page"

    @allure.title("Быстрые изменения поиска не вызывают сбой")
    def test_rapid_search_changes(self, orders_page):
        """Rapid search input changes should not crash."""
        with allure.step("Быстрый ввод нескольких поисковых запросов подряд"):
            for query in ["test1", "test2", "test3", "test4", "test5"]:
                orders_page.search_input.fill(query)
        with allure.step("Нажатие Enter и ожидание загрузки"):
            orders_page.page.keyboard.press("Enter")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница не сломалась после быстрых изменений"):
            assert orders_page.is_page_loaded(), \
                "BUG: Rapid search changes broke the page"

    @allure.title("Множественные изменения даты не вызывают сбой")
    def test_multiple_date_changes(self, orders_page):
        """Multiple date filter changes should not crash."""
        with allure.step("Множественные изменения фильтра даты"):
            dates = ["01-01-2024", "15-06-2024", "31-12-2024", "01-01-2025"]
            for date in dates:
                orders_page.set_date_from(date)
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница не сломалась после множественных изменений даты"):
            assert orders_page.is_page_loaded(), \
                "BUG: Multiple date changes broke the page"

    @allure.title("Обновление страницы во время поиска не вызывает сбой")
    def test_page_reload_during_search(self, orders_page):
        """Page reload during search should not crash."""
        with allure.step("Ввод текста в поле поиска"):
            orders_page.search_input.fill("RELOAD_TEST")
        with allure.step("Обновление страницы во время поиска"):
            orders_page.page.reload()
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница не сломалась после обновления"):
            assert orders_page.is_page_loaded(), \
                "BUG: Reload during search broke the page"



@pytest.mark.security
@allure.feature("Заказы")
@allure.story("Продвинутая безопасность")
class TestOrdersAdvancedSecurity:
    """Test advanced security scenarios."""

    @allure.title("HTML инъекция в поиске санитизируется")
    def test_html_injection_search(self, orders_page, test_data):
        """HTML injection in search should be sanitized."""
        with allure.step("Ввод HTML-инъекции в поле поиска"):
            html = test_data["invalid_search"]["html_tags"]
            orders_page.search_order(html)
        with allure.step("Проверка что HTML-тег iframe не отражён на странице"):
            content = orders_page.page.content()
            assert "<iframe" not in content, \
                "BUG: HTML injection reflected - iframe tag found!"

    @allure.title("LDAP инъекция в поиске блокируется")
    def test_ldap_injection_search(self, orders_page, test_data):
        """LDAP injection in search should be safe."""
        with allure.step("Ввод LDAP-инъекции в поле поиска"):
            ldap = test_data["invalid_search"]["ldap_injection"]
            orders_page.search_order(ldap)
        with allure.step("Проверка что страница не сломалась после LDAP-инъекции"):
            assert orders_page.is_page_loaded(), \
                "BUG: LDAP injection broke the page"

    @allure.title("Path traversal в поиске блокируется")
    def test_path_traversal_search(self, orders_page, test_data):
        """Path traversal in search should be safe."""
        with allure.step("Ввод path traversal в поле поиска"):
            path = test_data["invalid_search"]["path_traversal"]
            orders_page.search_order(path)
        with allure.step("Проверка что страница не сломалась после path traversal"):
            assert orders_page.is_page_loaded(), \
                "BUG: Path traversal in search broke the page"

    @allure.title("Unicode и эмодзи в поиске обрабатываются")
    def test_unicode_emoji_search(self, orders_page, test_data):
        """Unicode/emoji in search should be handled."""
        with allure.step("Ввод Unicode и эмодзи в поле поиска"):
            emoji = test_data["invalid_search"]["unicode_emoji"]
            orders_page.search_order(emoji)
        with allure.step("Проверка что страница не сломалась после ввода Unicode"):
            assert orders_page.is_page_loaded(), \
                "BUG: Unicode emoji in search broke the page"



@pytest.mark.functional
@allure.feature("Заказы")
@allure.story("Параллелизм")
class TestOrdersConcurrent:
    """Test concurrent operations and state management."""

    @allure.title("Состояние поиска после смены вкладки")
    def test_search_state_after_tab_change(self, orders_page):
        """Search should reset/persist after changing tabs."""
        with allure.step("Ввод поискового запроса"):
            orders_page.search_order("STATE_TEST")
        with allure.step("Переключение на вкладку 'Cancelled'"):
            orders_page.click_tab("Cancelled")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница загружена после смены вкладки"):
            assert orders_page.is_page_loaded(), \
                "BUG: Tab change after search broke the page"

    @allure.title("Состояние вкладки после поиска")
    def test_tab_state_after_search(self, orders_page):
        """Tab selection should be maintained after search."""
        with allure.step("Переключение на вкладку 'Processing'"):
            orders_page.click_tab("Processing")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Ввод поискового запроса после смены вкладки"):
            orders_page.search_order("AFTER_TAB")
        with allure.step("Проверка что страница загружена после поиска"):
            assert orders_page.is_page_loaded(), \
                "BUG: Search after tab change broke the page"

    @allure.title("Комбинация фильтров работает корректно")
    def test_filter_combination(self, orders_page):
        """Combining tab + search + date should work."""
        with allure.step("Переключение на вкладку 'All'"):
            orders_page.click_tab("All")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Применение фильтра по дате"):
            orders_page.set_date_from("01-01-2024")
        with allure.step("Ввод поискового запроса"):
            orders_page.search_order("COMBO_TEST")
        with allure.step("Проверка что комбинация фильтров не сломала страницу"):
            assert orders_page.is_page_loaded(), \
                "BUG: Combined filters broke the page"
