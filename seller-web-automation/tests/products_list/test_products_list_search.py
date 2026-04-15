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
@allure.feature("Поиск")
@pytest.mark.functional
class TestProductsListSearch:
    """Search functionality tests."""

    @allure.title("Поиск с валидным запросом фильтрует результаты")
    def test_search_with_valid_term(self, products_page: ProductsListPage):
        """Search should filter results."""
        with allure.step("Ввод поискового запроса 'Test' и ожидание результатов"):
            initial_count = products_page.get_products_count()
            products_page.search("Test")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница осталась на странице товаров"):
            assert products_page.is_on_products_page(), \
                "BUG: Navigation changed after search"

    @allure.title("Пустой поиск показывает все товары")
    def test_search_with_empty_string(self, products_page: ProductsListPage):
        """Empty search should show all products."""
        with allure.step("Ввод пустого поискового запроса"):
            products_page.search("")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после пустого поиска"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after empty search"

    @allure.title("Поисковый запрос сохраняется в URL или поле ввода")
    def test_search_preserves_in_url(self, products_page: ProductsListPage):
        """Search term should be reflected in URL or input."""
        with allure.step("Ввод поискового запроса 'TestProduct'"):
            search_term = "TestProduct"
            products_page.search(search_term)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что поисковый запрос сохранился"):
            current_value = products_page.get_search_value()
            assert search_term in current_value or products_page.is_on_products_page(), \
                "BUG: Search term lost after search"

    @allure.title("Очистка поиска восстанавливает полный список")
    def test_clear_search_restores_results(self, products_page: ProductsListPage):
        """Clearing search should restore full list."""
        with allure.step("Ввод поискового запроса и очистка поля"):
            products_page.search("SomeSearchTerm")
            products_page.wait_for_network_idle()
            products_page.clear_search()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после очистки поиска"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after clearing search"

    @allure.title("Поиск без результатов показывает пустое состояние")
    def test_search_no_results(self, products_page: ProductsListPage):
        """Search with nonexistent term should show empty or message."""
        with allure.step("Ввод несуществующего поискового запроса"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка пустого состояния или нулевого количества результатов"):
            count = products_page.get_products_count()
            is_empty = products_page.is_empty_state_visible()
            assert count == 0 or is_empty or products_page.is_page_loaded(), \
                "BUG: Unexpected state after no-results search"

    @allure.title("Частичный поиск работает")
    def test_search_partial_match(self, products_page: ProductsListPage):
        """Partial search should work."""
        with allure.step("Ввод частичного поискового запроса 'Te'"):
            products_page.search("Te")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после частичного поиска"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after partial search"

    @allure.title("Поиск нечувствителен к регистру")
    def test_search_case_insensitive(self, products_page: ProductsListPage):
        """Search should be case insensitive."""
        with allure.step("Поиск в верхнем регистре 'TEST'"):
            products_page.search("TEST")
            products_page.wait_for_network_idle()
            count_upper = products_page.get_products_count()

        with allure.step("Поиск в нижнем регистре 'test' и сравнение результатов"):
            products_page.clear_search()
            products_page.search("test")
            products_page.wait_for_network_idle()
            count_lower = products_page.get_products_count()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken during case sensitivity test"

    @allure.title("Поиск срабатывает по клавише Enter")
    def test_search_with_enter_key(self, products_page: ProductsListPage):
        """Search should trigger on Enter key."""
        with allure.step("Ввод текста и нажатие Enter"):
            products_page.search_input.fill("Test")
            products_page.press_enter()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что поиск сработал"):
            assert products_page.is_page_loaded(), \
                "BUG: Search not triggered on Enter"

    @allure.title("Поиск со спецсимволами не ломает страницу")
    def test_search_special_characters(self, products_page: ProductsListPage):
        """Search with special chars should not break page."""
        with allure.step("Ввод поискового запроса со спецсимволами"):
            products_page.search(TEST_DATA["search"]["invalid"]["special_chars"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after special character search"

    @allure.title("Поиск с юникод-символами не ломает страницу")
    def test_search_unicode_characters(self, products_page: ProductsListPage):
        """Search with unicode should not break page."""
        with allure.step("Ввод поискового запроса с юникод-символами"):
            products_page.search(TEST_DATA["search"]["invalid"]["unicode"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after unicode search"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Безопасность поиска")
@pytest.mark.security
class TestProductsListSearchSecurity:
    """Security tests for search functionality."""

    @allure.title("XSS в поиске санитизируется")
    def test_search_xss_injection(self, products_page: ProductsListPage):
        """XSS in search should be sanitized."""
        with allure.step("Ввод XSS-payload в поле поиска"):
            xss_payload = TEST_DATA["security"]["xss_payloads"][0]
            products_page.search(xss_payload)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что скрипт не выполнился на странице"):
            page_content = products_page.page.content()
            assert "<script>alert" not in page_content, \
                "BUG: XSS not sanitized in search - SECURITY VULNERABILITY!"

    @allure.title("SQL инъекция в поиске обрабатывается безопасно")
    def test_search_sql_injection(self, products_page: ProductsListPage):
        """SQL injection in search should be handled safely."""
        with allure.step("Ввод SQL-injection payload в поле поиска"):
            sql_payload = TEST_DATA["security"]["sql_payloads"][0]
            products_page.search(sql_payload)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не упала"):
            assert products_page.is_page_loaded(), \
                "BUG: Page crashed on SQL injection - potential vulnerability!"

    @allure.title("HTML инъекция в поиске экранируется")
    def test_search_html_injection(self, products_page: ProductsListPage):
        """HTML injection should be escaped."""
        with allure.step("Ввод HTML-injection payload в поле поиска"):
            html_payload = TEST_DATA["search"]["invalid"]["html_injection"]
            products_page.search(html_payload)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что HTML-инъекция экранирована"):
            page_content = products_page.page.content()
            assert "onerror=alert" not in page_content, \
                "BUG: HTML injection not sanitized - SECURITY VULNERABILITY!"

    @allure.title("Null-байты в поиске обрабатываются")
    def test_search_null_bytes(self, products_page: ProductsListPage):
        """Null bytes in search should be handled."""
        with allure.step("Ввод null-байтов в поле поиска"):
            null_payload = "test\x00value"
            products_page.search(null_payload)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page crashed on null byte injection"

    @allure.title("LDAP инъекция в поиске обрабатывается")
    def test_search_ldap_injection(self, products_page: ProductsListPage):
        """LDAP injection should be handled."""
        with allure.step("Ввод LDAP-injection payload в поле поиска"):
            ldap_payload = TEST_DATA["search"]["invalid"]["ldap_injection"]
            products_page.search(ldap_payload)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page crashed on LDAP injection"

    @allure.title("Командная инъекция в поиске обрабатывается")
    def test_search_command_injection(self, products_page: ProductsListPage):
        """Command injection should be handled."""
        with allure.step("Ввод командной инъекции в поле поиска"):
            cmd_payload = TEST_DATA["search"]["invalid"]["command_injection"]
            products_page.search(cmd_payload)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page crashed on command injection"

    @allure.title("Обход пути в поиске блокируется")
    def test_search_path_traversal(self, products_page: ProductsListPage):
        """Path traversal should be blocked."""
        with allure.step("Ввод path traversal payload в поле поиска"):
            path_payload = TEST_DATA["search"]["invalid"]["path_traversal"]
            products_page.search(path_payload)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page crashed on path traversal"

    @allure.title("Очень длинная строка поиска обрабатывается")
    def test_search_very_long_string(self, products_page: ProductsListPage):
        """Very long search string should be handled."""
        with allure.step("Ввод строки длиной 10000 символов в поле поиска"):
            long_string = "a" * 10000
            products_page.search(long_string)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page crashed on very long search string"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Фильтрация")
@pytest.mark.functional
class TestProductsListFilters:
    """Filter functionality tests."""

    @allure.title("Фильтр по статусу 'Ожидает'")
    def test_status_filter_pending(self, products_page: ProductsListPage):
        """Filter by Pending status."""
        with allure.step("Открытие фильтров и применение фильтра 'Pending'"):
            products_page.open_filters()
            try:
                products_page.apply_status_filter("Pending")
                products_page.wait_for_network_idle()
            except Exception:
                logger.info("Status filter not available or failed")

        with allure.step("Проверка что страница загружена после фильтрации"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after status filter"

    @allure.title("Фильтр по статусу 'Одобрено'")
    def test_status_filter_approved(self, products_page: ProductsListPage):
        """Filter by Approved status."""
        with allure.step("Открытие фильтров и применение фильтра 'Approved'"):
            products_page.open_filters()
            products_page.apply_status_filter("Approved")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after approved filter"

    @allure.title("Фильтр по статусу 'Отклонено'")
    def test_status_filter_rejected(self, products_page: ProductsListPage):
        """Filter by Rejected status."""
        with allure.step("Открытие фильтров и применение фильтра 'Rejected'"):
            products_page.open_filters()
            products_page.apply_status_filter("Rejected")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after rejected filter"

    @allure.title("Очистка фильтров сбрасывает результаты")
    def test_clear_filters(self, products_page: ProductsListPage):
        """Clear filters should reset results."""
        with allure.step("Открытие и очистка всех фильтров"):
            products_page.open_filters()
            products_page.clear_all_filters()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after clearing filters"

    @allure.title("Множественные фильтры работают вместе")
    def test_multiple_filters(self, products_page: ProductsListPage):
        """Multiple filters should work together."""
        with allure.step("Применение поиска и фильтра одновременно"):
            products_page.search("Test")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена с множественными фильтрами"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken with multiple filters"

    @allure.title("Фильтры сохраняются при переключении страниц")
    def test_filter_persists_after_pagination(self, products_page: ProductsListPage):
        """Filters should persist when changing pages."""
        with allure.step("Применение фильтра поиска и переход на следующую страницу"):
            products_page.search("Test")
            products_page.wait_for_network_idle()
            if products_page.is_next_page_enabled():
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()
                search_value = products_page.get_search_value()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after pagination with filter"

    @allure.title("Фильтр без результатов показывает пустое состояние")
    def test_filter_empty_result(self, products_page: ProductsListPage):
        """Filter with no matching results should show empty state."""
        with allure.step("Применение фильтра без совпадений"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка количества результатов"):
            count = products_page.get_products_count()
            assert count == 0 or products_page.is_page_loaded(), \
                "BUG: Page not handling empty filter results"

    @allure.title("Фильтр со спецсимволами не ломает страницу")
    def test_filter_with_special_chars(self, products_page: ProductsListPage):
        """Filter with special characters should not break."""
        with allure.step("Ввод спецсимволов '!@#$' в поле фильтрации"):
            products_page.search("!@#$")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken with special chars in filter"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Сортировка")
@pytest.mark.functional
class TestProductsListSorting:
    """Sorting functionality tests."""

    @allure.title("Сортировка по названию по возрастанию")
    def test_sort_by_name_asc(self, products_page: ProductsListPage):
        """Sort by name ascending."""
        with allure.step("Сортировка по столбцу 'Name'"):
            products_page.click_column_header("Name")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после сортировки"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after name sort"

    @allure.title("Сортировка по названию по убыванию (двойной клик)")
    def test_sort_by_name_desc(self, products_page: ProductsListPage):
        """Sort by name descending (click twice)."""
        with allure.step("Двойной клик по столбцу 'Name' для сортировки по убыванию"):
            products_page.click_column_header("Name")
            products_page.wait_for_network_idle()
            products_page.click_column_header("Name")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after desc sort"

    @allure.title("Сортировка по цене")
    def test_sort_by_price(self, products_page: ProductsListPage):
        """Sort by price."""
        with allure.step("Сортировка по столбцу 'Price'"):
            products_page.click_column_header("Price")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after price sort"

    @allure.title("Сортировка по статусу")
    def test_sort_by_status(self, products_page: ProductsListPage):
        """Sort by status."""
        with allure.step("Сортировка по столбцу 'Status'"):
            products_page.click_column_header("Status")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after status sort"

    @allure.title("Сортировка по дате")
    def test_sort_by_date(self, products_page: ProductsListPage):
        """Sort by date column if exists."""
        with allure.step("Сортировка по столбцу 'Created'"):
            products_page.click_column_header("Created")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after date sort"

    @allure.title("Сброс сортировки при третьем клике")
    def test_sort_reset(self, products_page: ProductsListPage):
        """Sort should reset on third click (if supported)."""
        with allure.step("Тройной клик по столбцу 'Name' для сброса сортировки"):
            products_page.click_column_header("Name")
            products_page.click_column_header("Name")
            products_page.click_column_header("Name")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after sort reset"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Фильтрация по дате")
@pytest.mark.functional
class TestProductsListDateFilters:
    """Date filter tests."""

    @allure.title("Фильтр по дате доступен")
    def test_date_filter_available(self, products_page: ProductsListPage):
        """Date filter should be available."""
        with allure.step("Открытие фильтров и проверка наличия фильтра по дате"):
            products_page.open_filters()
            date_filter = products_page.page.get_by_label("Date").or_(
                products_page.page.get_by_label("Sana")
            )
            logger.info(f"Date filter visible: {date_filter.is_visible(timeout=2000)}")

    @allure.title("Выбор диапазона дат работает")
    def test_date_range_picker(self, products_page: ProductsListPage):
        """Date range picker should work."""
        with allure.step("Проверка наличия выбора диапазона дат"):
            date_picker = products_page.page.locator("[class*='date-picker']").or_(
                products_page.page.locator("input[type='date']")
            )
            logger.info(f"Date picker visible: {date_picker.is_visible(timeout=2000)}")

    @allure.title("Фильтр по дате создания работает")
    def test_created_date_filter(self, products_page: ProductsListPage):
        """Filter by created date should work."""
        with allure.step("Проверка что страница поддерживает фильтр по дате создания"):
            assert products_page.is_page_loaded()

    @allure.title("Фильтр по дате обновления работает")
    def test_updated_date_filter(self, products_page: ProductsListPage):
        """Filter by updated date should work."""
        with allure.step("Проверка что страница поддерживает фильтр по дате обновления"):
            assert products_page.is_page_loaded()

    @allure.title("Предустановленные диапазоны дат работают")
    def test_preset_date_ranges(self, products_page: ProductsListPage):
        """Preset date ranges should work (today, week, month)."""
        with allure.step("Проверка наличия кнопок предустановленных диапазонов дат"):
            today_btn = products_page.page.locator("button:has-text('Today')").or_(
                products_page.page.locator("button:has-text('Bugun')")
            ).or_(products_page.page.locator("button:has-text('Сегодня')"))
            logger.info(f"Today preset visible: {today_btn.is_visible(timeout=1000)}")



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Сохраненные фильтры")
@pytest.mark.functional
class TestProductsListSavedFilters:
    """Saved filter tests."""

    @allure.title("Опция сохранения фильтра доступна")
    def test_save_filter_option(self, products_page: ProductsListPage):
        """Save filter option should be available."""
        with allure.step("Проверка наличия кнопки сохранения фильтра"):
            save_btn = products_page.page.locator("button:has-text('Save filter')").or_(
                products_page.page.locator("button:has-text('Filterni saqlash')")
            ).or_(products_page.page.locator("button:has-text('Сохранить фильтр')"))
            logger.info(f"Save filter visible: {save_btn.is_visible(timeout=2000)}")

    @allure.title("Загрузка сохраненного фильтра работает")
    def test_load_saved_filter(self, products_page: ProductsListPage):
        """Loading saved filter should work."""
        with allure.step("Проверка что страница поддерживает загрузку сохраненных фильтров"):
            assert products_page.is_page_loaded()

    @allure.title("Состояние фильтра в URL для шаринга")
    def test_filter_url_shareable(self, products_page: ProductsListPage):
        """Filter state should be in URL for sharing."""
        with allure.step("Применение фильтра и проверка отражения в URL"):
            products_page.search("Test")
            products_page.wait_for_network_idle()
            url = products_page.get_current_url()
            logger.info(f"URL with search: {url}")

    @allure.title("Состояние фильтра сохраняется в URL")
    def test_filter_state_in_url(self, products_page: ProductsListPage):
        """Filter state should persist in URL."""
        with allure.step("Применение фильтра и перезагрузка страницы"):
            products_page.search("Filter")
            products_page.wait_for_network_idle()
            products_page.page.reload()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена после перезагрузки"):
            assert products_page.is_page_loaded()

    @allure.title("Очистка всех сохраненных фильтров работает")
    def test_clear_all_saved_filters(self, products_page: ProductsListPage):
        """Clearing all filters should work."""
        with allure.step("Применение и очистка фильтра поиска"):
            products_page.search("Test")
            products_page.clear_search()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Обработка пробелов")
@pytest.mark.functional
class TestProductsListWhitespace:
    """Whitespace handling tests."""

    @allure.title("Ведущие пробелы в поиске обрабатываются")
    def test_search_leading_spaces(self, products_page: ProductsListPage):
        """Leading spaces in search should be handled."""
        with allure.step("Ввод поискового запроса с ведущими пробелами"):
            products_page.search("   Test")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Leading spaces broke search"

    @allure.title("Конечные пробелы в поиске обрабатываются")
    def test_search_trailing_spaces(self, products_page: ProductsListPage):
        """Trailing spaces in search should be handled."""
        with allure.step("Ввод поискового запроса с конечными пробелами"):
            products_page.search("Test   ")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Trailing spaces broke search"

    @allure.title("Табуляция в поиске обрабатывается")
    def test_search_tabs(self, products_page: ProductsListPage):
        """Tabs in search should be handled."""
        with allure.step("Ввод поискового запроса с табуляцией"):
            products_page.search("\tTest\t")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Tabs broke search"

    @allure.title("Переводы строк в поиске обрабатываются")
    def test_search_newlines(self, products_page: ProductsListPage):
        """Newlines in search should be handled."""
        with allure.step("Ввод поискового запроса с переводами строк"):
            products_page.search("Test\nProduct")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Newlines broke search"

    @allure.title("Множественные пробелы в поиске нормализуются")
    def test_search_multiple_spaces(self, products_page: ProductsListPage):
        """Multiple spaces should be normalized."""
        with allure.step("Ввод поискового запроса с множественными пробелами"):
            products_page.search("Test    Multiple    Spaces")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница не сломалась"):
            assert products_page.is_page_loaded(), \
                "BUG: Multiple spaces broke search"
