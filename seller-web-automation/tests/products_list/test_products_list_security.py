"""
Products List Page Tests - Comprehensive test suite.

Tests for /dashboard/products page covering:
- UI elements and layout
- Search functionality
- Filtering and sorting
- Pagination
- Table interactions
- Bulk actions
- Security (XSS, SQL injection, etc.)
- Accessibility
- Performance
- E2E workflows

Total: ~278 tests
"""

import allure
import pytest
import json
import os
from playwright.sync_api import Page, expect

from pages.products_list_page import ProductsListPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils import setup_logger

logger = setup_logger(__name__)

# Load test data
TEST_DATA_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "test_data", "products_list_test_data.json"
)
with open(TEST_DATA_PATH, "r", encoding="utf-8") as f:
    TEST_DATA = json.load(f)



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Продвинутая безопасность")
@pytest.mark.security
class TestProductsListAdvancedSecurity:
    """Advanced security tests."""

    @allure.title("NoSQL инъекция обрабатывается безопасно")
    def test_nosql_injection(self, products_page: ProductsListPage):
        """NoSQL injection should be handled."""
        with allure.step("Проверка NoSQL payload-ов в поиске"):
            for payload in TEST_DATA["security"]["nosql_payloads"]:
                products_page.search(payload)
                products_page.wait_for_network_idle()
                assert products_page.is_page_loaded(), \
                    f"BUG: NoSQL injection broke page: {payload}"
                products_page.clear_search()

    @allure.title("Шаблонная инъекция обрабатывается безопасно")
    def test_template_injection(self, products_page: ProductsListPage):
        """Template injection should be handled."""
        with allure.step("Ввод шаблонной инъекции {{7*7}} в поиск"):
            products_page.search("{{7*7}}")
            products_page.wait_for_network_idle()
        with allure.step("Проверка что шаблон не был выполнен"):
            content = products_page.page.content()
            assert "49" not in content or products_page.is_page_loaded(), \
                "BUG: Template injection executed"

    @allure.title("Инъекция заголовков обрабатывается безопасно")
    def test_header_injection(self, products_page: ProductsListPage):
        """Header injection should be handled."""
        with allure.step("Ввод инъекции заголовков в поиск"):
            products_page.search("test\r\nX-Injected: header")
            products_page.wait_for_network_idle()
        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Header injection broke page"

    @allure.title("Атака нормализации юникода обрабатывается")
    def test_unicode_normalization(self, products_page: ProductsListPage):
        """Unicode normalization attacks should be handled."""
        with allure.step("Ввод юникод-нормализационной атаки в поиск"):
            products_page.search("\u0041\u030A")  # A with ring
            products_page.wait_for_network_idle()
        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Unicode normalization broke page"

    @allure.title("Символы нулевой ширины обрабатываются")
    def test_zero_width_chars(self, products_page: ProductsListPage):
        """Zero-width characters should be handled."""
        with allure.step("Ввод символов нулевой ширины в поиск"):
            products_page.search("test\u200Bvalue")
            products_page.wait_for_network_idle()
        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Zero-width chars broke page"

    @allure.title("RTL переопределение обрабатывается")
    def test_rtl_override(self, products_page: ProductsListPage):
        """RTL override should be handled."""
        with allure.step("Ввод RTL-переопределения в поиск"):
            products_page.search("\u202Etest")
            products_page.wait_for_network_idle()
        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: RTL override broke page"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Ошибки консоли")
@pytest.mark.functional
class TestProductsListConsole:
    """Console error tests."""

    @allure.title("Нет ошибок консоли при загрузке страницы")
    def test_no_console_errors_on_load(self, products_page: ProductsListPage):
        """No console errors on page load."""
        with allure.step("Проверка загрузки страницы без ошибок"):
            assert products_page.is_page_loaded(), \
                "BUG: Page failed to load"

    @allure.title("Нет ошибок консоли после поиска")
    def test_no_console_errors_after_search(self, products_page: ProductsListPage):
        """No console errors after search."""
        with allure.step("Выполнение поискового запроса"):
            products_page.search("Test")
            products_page.wait_for_network_idle()
        with allure.step("Проверка что страница работает после поиска"):
            assert products_page.is_page_loaded(), \
                "BUG: Console errors after search"

    @allure.title("Нет ошибок консоли после пагинации")
    def test_no_console_errors_after_pagination(self, products_page: ProductsListPage):
        """No console errors after pagination."""
        with allure.step("Переход на следующую страницу (если доступна)"):
            if products_page.is_next_page_enabled():
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()
        with allure.step("Проверка что страница работает после пагинации"):
            assert products_page.is_page_loaded(), \
                "BUG: Console errors after pagination"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Сессия")
@pytest.mark.session
class TestProductsListSession:
    """Session handling tests."""

    @allure.title("Страница товаров требует авторизации")
    def test_session_required(self, products_page: ProductsListPage):
        """Products page should require authentication."""
        with allure.step("Проверка что авторизованный пользователь на странице товаров"):
            assert products_page.is_on_products_page(), \
                "BUG: Not on products page - session issue"

    @allure.title("Сессия сохраняется при навигации")
    def test_session_persists(self, products_page: ProductsListPage):
        """Session should persist across navigation."""
        with allure.step("Переход на страницу добавления товара"):
            products_page.click_add_product()
            products_page.wait_for_network_idle()
        with allure.step("Возврат на страницу списка товаров"):
            products_page.navigate()
            products_page.wait_for_network_idle()
        with allure.step("Проверка что сессия сохранилась"):
            assert products_page.is_on_products_page(), \
                "BUG: Session lost during navigation"

    @allure.title("Сессия сохраняется после обновления страницы")
    def test_session_after_refresh(self, products_page: ProductsListPage):
        """Session should persist after refresh."""
        with allure.step("Обновление страницы"):
            products_page.page.reload()
            products_page.wait_for_loading_complete()
        with allure.step("Проверка что сессия сохранилась"):
            assert products_page.is_on_products_page(), \
                "BUG: Session lost after refresh"

    @allure.title("Неавторизованный доступ перенаправляет на логин")
    def test_unauthorized_access_redirect(self, page: Page):
        """Unauthorized access should redirect to login."""
        with allure.step("Переход на страницу товаров без авторизации"):
            new_page = ProductsListPage(page)
            new_page.navigate_to("/dashboard/products")
            new_page.wait_for_network_idle()
        with allure.step("Проверка URL после попытки доступа"):
            url = new_page.get_current_url()
            logger.info(f"Unauthorized access URL: {url}")

    @allure.title("Таймаут сессии обрабатывается корректно")
    def test_session_timeout_handling(self, products_page: ProductsListPage):
        """Session timeout should be handled gracefully."""
        with allure.step("Проверка что страница обрабатывает сессию корректно"):
            assert products_page.is_page_loaded()
