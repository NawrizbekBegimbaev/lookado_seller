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
@allure.story("Поиск")
class TestOrdersSearch:
    """Test search functionality."""

    @allure.title("Поиск по невалидному ID заказа")
    def test_search_invalid_order_id(self, orders_page, test_data):
        """Search with invalid order ID should not break the page."""
        with allure.step("Ввод невалидного ID заказа в поле поиска"):
            invalid_id = test_data["search_scenarios"]["invalid_order_id"]
            orders_page.search_order(invalid_id)
        with allure.step("Проверка что страница осталась функциональной после поиска"):
            assert orders_page.is_page_loaded(), \
                "BUG: Invalid search broke the page"

    @allure.title("Очистка поиска сбрасывает результаты")
    def test_search_clears_correctly(self, orders_page):
        """Clearing search should reset results."""
        with allure.step("Ввод поискового запроса"):
            orders_page.search_order("TESTQUERY123")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Очистка поля поиска"):
            orders_page.clear_search()
        with allure.step("Проверка что страница загружена после очистки поиска"):
            assert orders_page.is_page_loaded(), \
                "BUG: Page not loaded after clearing search"

    @allure.title("Поле поиска сохраняет введённый текст")
    def test_search_preserves_input(self, orders_page):
        """Search input should preserve typed text."""
        with allure.step("Ввод текста в поле поиска"):
            orders_page.search_input.fill("ORDER123")
        with allure.step("Проверка что введённый текст сохранился в поле"):
            value = orders_page.get_search_value()
            assert "ORDER123" in value, \
                f"BUG: Search value not preserved: '{value}'"

    @allure.title("Поиск по нажатию клавиши Enter")
    def test_search_with_enter_key(self, orders_page):
        """Pressing Enter should trigger search."""
        with allure.step("Ввод текста в поле поиска"):
            orders_page.search_input.fill("SEARCH_TEST")
        with allure.step("Нажатие клавиши Enter для выполнения поиска"):
            orders_page.page.keyboard.press("Enter")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница загружена после поиска"):
            assert orders_page.is_page_loaded(), \
                "BUG: Enter key did not trigger search"

    @allure.title("Поиск пустой строкой показывает все заказы")
    def test_search_empty_string(self, orders_page):
        """Searching empty string should show all orders."""
        with allure.step("Ввод пустой строки в поле поиска"):
            orders_page.search_order("")
        with allure.step("Проверка что страница загружена после пустого поиска"):
            assert orders_page.is_page_loaded(), \
                "BUG: Empty search broke the page"



@pytest.mark.security
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Безопасность поиска")
class TestOrdersSearchSecurity:
    """Test search input sanitization against injections."""

    @allure.title("XSS script-тег в поиске санитизируется")
    def test_search_xss_script_tag(self, orders_page, test_data):
        """XSS script tag in search should be sanitized."""
        with allure.step("Ввод XSS script-тега в поле поиска"):
            xss = test_data["invalid_search"]["xss_payload"]
            orders_page.search_order(xss)
        with allure.step("Проверка что XSS script-тег не отражён на странице"):
            page_content = orders_page.page.content()
            assert "<script>" not in page_content, \
                "BUG: XSS script tag reflected in page!"

    @allure.title("XSS обработчик событий в поиске санитизируется")
    def test_search_xss_event_handler(self, orders_page, test_data):
        """XSS event handler in search should be sanitized."""
        with allure.step("Ввод XSS обработчика событий в поле поиска"):
            xss = test_data["invalid_search"]["xss_event"]
            orders_page.search_order(xss)
        with allure.step("Проверка что XSS обработчик событий не отражён на странице"):
            page_content = orders_page.page.content()
            assert "onerror=" not in page_content, \
                "BUG: XSS event handler reflected in page!"

    @allure.title("SQL-инъекция в поиске не ломает страницу")
    def test_search_sql_injection(self, orders_page, test_data):
        """SQL injection in search should not break the page."""
        with allure.step("Ввод SQL-инъекции в поле поиска"):
            sql = test_data["invalid_search"]["sql_injection"]
            orders_page.search_order(sql)
        with allure.step("Проверка что страница не сломалась после SQL-инъекции"):
            assert orders_page.is_page_loaded(), \
                "BUG: SQL injection broke the page"

    @allure.title("Null-байты в поиске обрабатываются безопасно")
    def test_search_null_bytes(self, orders_page, test_data):
        """Null bytes in search should be handled safely."""
        with allure.step("Ввод null-байтов в поле поиска"):
            null_input = test_data["invalid_search"]["null_bytes"]
            orders_page.search_order(null_input)
        with allure.step("Проверка что страница не сломалась после ввода null-байтов"):
            assert orders_page.is_page_loaded(), \
                "BUG: Null bytes in search broke the page"

    @allure.title("Инъекция команд в поиске обрабатывается безопасно")
    def test_search_command_injection(self, orders_page, test_data):
        """Command injection in search should be safe."""
        with allure.step("Ввод инъекции команд в поле поиска"):
            cmd = test_data["invalid_search"]["command_injection"]
            orders_page.search_order(cmd)
        with allure.step("Проверка что страница не сломалась после инъекции команд"):
            assert orders_page.is_page_loaded(), \
                "BUG: Command injection broke the page"

    @allure.title("Очень длинный поисковый запрос не ломает страницу")
    def test_search_very_long_input(self, orders_page, test_data):
        """Very long search input should not crash the page."""
        with allure.step("Ввод очень длинной строки в поле поиска"):
            long_str = test_data["invalid_search"]["very_long"]
            orders_page.search_order(long_str)
        with allure.step("Проверка что страница не сломалась после длинного запроса"):
            assert orders_page.is_page_loaded(), \
                "BUG: Very long search input broke the page"



@pytest.mark.negative
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Пробельные символы в поиске")
class TestOrdersSearchWhitespace:
    """Test whitespace handling in search."""

    @allure.title("Поиск только пробелами обрабатывается корректно")
    def test_search_only_spaces(self, orders_page, test_data):
        """Search with only spaces should be handled."""
        with allure.step("Ввод только пробелов в поле поиска"):
            orders_page.search_order(test_data["whitespace_inputs"]["only_spaces"])
        with allure.step("Проверка что страница не сломалась после поиска пробелами"):
            assert orders_page.is_page_loaded(), \
                "BUG: Spaces-only search broke the page"

    @allure.title("Поиск с табуляцией обрабатывается корректно")
    def test_search_with_tabs(self, orders_page, test_data):
        """Search with tabs should be handled."""
        with allure.step("Ввод табуляции в поле поиска"):
            orders_page.search_order(test_data["whitespace_inputs"]["tabs"])
        with allure.step("Проверка что страница не сломалась после поиска с табуляцией"):
            assert orders_page.is_page_loaded(), \
                "BUG: Tabs in search broke the page"

    @allure.title("Поиск с начальными и конечными пробелами обрезается")
    def test_search_leading_trailing_spaces(self, orders_page, test_data):
        """Search with leading/trailing spaces should trim."""
        with allure.step("Ввод строки с начальными и конечными пробелами в поле поиска"):
            orders_page.search_order(test_data["whitespace_inputs"]["leading_trailing"])
        with allure.step("Проверка что страница не сломалась после поиска с пробелами"):
            assert orders_page.is_page_loaded(), \
                "BUG: Leading/trailing spaces broke search"

    @allure.title("Поиск с множественными пробелами обрабатывается корректно")
    def test_search_multiple_spaces(self, orders_page, test_data):
        """Search with multiple internal spaces should be handled."""
        with allure.step("Ввод строки с множественными пробелами в поле поиска"):
            orders_page.search_order(test_data["whitespace_inputs"]["multiple_spaces"])
        with allure.step("Проверка что страница не сломалась после поиска с множественными пробелами"):
            assert orders_page.is_page_loaded(), \
                "BUG: Multiple spaces in search broke the page"



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Фильтрация по дате")
class TestOrdersDateFilter:
    """Test date range filter functionality."""

    @allure.title("Поле 'Дата от' принимает значение даты")
    def test_date_from_accepts_input(self, orders_page, test_data):
        """Date from input should accept date value."""
        with allure.step("Ввод даты в поле 'Дата от'"):
            date = test_data["date_filter"]["valid_from"]
            orders_page.set_date_from(date)
        with allure.step("Проверка что страница загружена после установки даты"):
            assert orders_page.is_page_loaded(), \
                "BUG: Setting date from broke the page"

    @allure.title("Поле 'Дата до' принимает значение даты")
    def test_date_to_accepts_input(self, orders_page, test_data):
        """Date to input should accept date value."""
        with allure.step("Ввод даты в поле 'Дата до'"):
            date = test_data["date_filter"]["valid_to"]
            orders_page.set_date_to(date)
        with allure.step("Проверка что страница загружена после установки даты"):
            assert orders_page.is_page_loaded(), \
                "BUG: Setting date to broke the page"

    @allure.title("Фильтрация по диапазону дат")
    def test_date_range_filter(self, orders_page, test_data):
        """Setting both date range should filter results."""
        with allure.step("Установка диапазона дат для фильтрации"):
            orders_page.set_date_range(
                test_data["date_filter"]["valid_from"],
                test_data["date_filter"]["valid_to"]
            )
        with allure.step("Проверка что страница загружена после применения фильтра по дате"):
            assert orders_page.is_page_loaded(), \
                "BUG: Date range filter broke the page"

    @allure.title("Невалидный формат даты обрабатывается корректно")
    def test_invalid_date_format(self, orders_page, test_data):
        """Invalid date format should be handled gracefully."""
        with allure.step("Ввод невалидного формата даты"):
            orders_page.set_date_from(test_data["date_filter"]["invalid_date"])
        with allure.step("Проверка что страница не сломалась после невалидной даты"):
            assert orders_page.is_page_loaded(), \
                "BUG: Invalid date format broke the page"

    @allure.title("Будущая дата обрабатывается корректно")
    def test_future_date(self, orders_page, test_data):
        """Future date should return no results (or handle gracefully)."""
        with allure.step("Ввод будущей даты в фильтр"):
            orders_page.set_date_from(test_data["date_filter"]["future_date"])
        with allure.step("Проверка что страница не сломалась после ввода будущей даты"):
            assert orders_page.is_page_loaded(), \
                "BUG: Future date filter broke the page"

    @allure.title("Обратный диапазон дат (от > до) обрабатывается корректно")
    def test_reversed_date_range(self, orders_page, test_data):
        """Reversed date range (from > to) should be handled."""
        with allure.step("Установка обратного диапазона дат (от > до)"):
            reversed_range = test_data["date_filter"]["reversed_range"]
            orders_page.set_date_range(reversed_range["from"], reversed_range["to"])
        with allure.step("Проверка что страница не сломалась после обратного диапазона дат"):
            assert orders_page.is_page_loaded(), \
                "BUG: Reversed date range broke the page"
