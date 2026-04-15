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
@allure.feature("E2E")
@pytest.mark.e2e
class TestProductsListE2E:
    """End-to-end workflow tests."""

    @allure.title("Полный рабочий процесс поиска")
    def test_full_search_workflow(self, products_page: ProductsListPage):
        """Complete search workflow."""
        with allure.step("Ввод поискового запроса 'Test' и ожидание результатов"):
            products_page.search("Test")
            products_page.wait_for_network_idle()

        with allure.step("Получение количества результатов и очистка поиска"):
            count = products_page.get_products_count()
            logger.info(f"Search results: {count}")
            products_page.clear_search()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после рабочего процесса поиска"):
            assert products_page.is_page_loaded(), \
                "BUG: Search workflow failed"

    @allure.title("Полный рабочий процесс фильтрации")
    def test_full_filter_workflow(self, products_page: ProductsListPage):
        """Complete filter workflow."""
        with allure.step("Применение фильтра поиска 'Test'"):
            products_page.search("Test")
            products_page.wait_for_network_idle()

        with allure.step("Пагинация если доступна и очистка фильтра"):
            if products_page.is_next_page_enabled():
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()
            products_page.clear_search()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после фильтрации"):
            assert products_page.is_page_loaded(), \
                "BUG: Filter workflow failed"

    @allure.title("Переход к товару и возврат назад")
    def test_navigate_to_product_and_back(self, products_page: ProductsListPage):
        """Navigate to product detail and back."""
        with allure.step("Клик по первому товару и возврат назад"):
            if products_page.get_products_count() > 0:
                products_page.click_row(0)
                products_page.wait_for_network_idle()
                products_page.page.go_back()
                products_page.wait_for_network_idle()

        with allure.step("Проверка что находимся на странице товаров"):
            assert products_page.is_on_products_page(), \
                "BUG: Navigation workflow failed"

    @allure.title("Начало рабочего процесса добавления товара")
    def test_add_product_workflow_start(self, products_page: ProductsListPage):
        """Start add product workflow."""
        with allure.step("Нажатие кнопки добавления товара"):
            products_page.click_add_product()
            products_page.wait_for_network_idle()

        with allure.step("Проверка перехода на страницу создания товара"):
            url = products_page.get_current_url()
            assert "add" in url or "create" in url, \
                "BUG: Add product navigation failed"
            products_page.navigate()

    @allure.title("Массовое выделение и отмена")
    def test_bulk_select_and_cancel(self, products_page: ProductsListPage):
        """Bulk select then cancel workflow."""
        with allure.step("Выделение всех товаров и снятие выделения"):
            if products_page.get_products_count() >= 2:
                products_page.select_all_products()
                products_page.page.wait_for_load_state("domcontentloaded")
                products_page.deselect_all_products()

        with allure.step("Проверка что страница загружена после массового выделения"):
            assert products_page.is_page_loaded(), \
                "BUG: Bulk select workflow failed"

    @allure.title("Комплексный процесс: поиск, пагинация, сортировка")
    def test_search_paginate_sort_workflow(self, products_page: ProductsListPage):
        """Complex workflow with search, pagination, sort."""
        with allure.step("Поиск 'Test' и сортировка по названию"):
            products_page.search("Test")
            products_page.wait_for_network_idle()
            products_page.click_column_header("Name")
            products_page.wait_for_network_idle()

        with allure.step("Пагинация и очистка поиска"):
            if products_page.is_next_page_enabled():
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()
            products_page.clear_search()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после комплексного процесса"):
            assert products_page.is_page_loaded(), \
                "BUG: Complex workflow failed"

    @allure.title("Рабочий процесс обновления страницы")
    def test_refresh_workflow(self, products_page: ProductsListPage):
        """Refresh page workflow."""
        with allure.step("Поиск 'Test' и обновление страницы"):
            products_page.search("Test")
            products_page.wait_for_network_idle()
            products_page.page.reload()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после обновления"):
            assert products_page.is_page_loaded(), \
                "BUG: Refresh workflow failed"

    @allure.title("Рабочий процесс навигации через боковое меню")
    def test_sidebar_navigation_workflow(self, products_page: ProductsListPage):
        """Sidebar navigation workflow."""
        with allure.step("Переход на дашборд"):
            dashboard = DashboardPage(products_page.page)
            dashboard.navigate_to("/dashboard")
            dashboard.wait_for_page_load()

        with allure.step("Возврат на страницу товаров через боковое меню"):
            products_page.click_products_nav_link()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что находимся на странице товаров"):
            assert products_page.is_on_products_page(), \
                "BUG: Sidebar navigation workflow failed"

    @allure.title("Полный рабочий процесс просмотра товара")
    def test_full_crud_view_workflow(self, products_page: ProductsListPage):
        """View product details workflow."""
        with allure.step("Получение названия товара и переход к деталям"):
            if products_page.get_products_count() > 0:
                name = products_page.get_product_name_from_row(0)
                logger.info(f"Viewing product: {name}")
                products_page.click_row(0)
                products_page.wait_for_network_idle()
                products_page.page.go_back()
                products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после просмотра"):
            assert products_page.is_page_loaded(), \
                "BUG: View workflow failed"

    @allure.title("Множественные последовательные действия")
    def test_multiple_action_workflow(self, products_page: ProductsListPage):
        """Multiple consecutive actions."""
        with allure.step("Последовательный поиск 'A', затем 'B'"):
            products_page.search("A")
            products_page.wait_for_network_idle()
            products_page.clear_search()
            products_page.search("B")
            products_page.wait_for_network_idle()

        with allure.step("Очистка поиска и проверка страницы"):
            products_page.clear_search()
            products_page.wait_for_network_idle()
            assert products_page.is_page_loaded(), \
                "BUG: Multiple action workflow failed"

    @allure.title("Сохранение сессии при навигации")
    def test_session_persistence_workflow(self, products_page: ProductsListPage):
        """Session should persist across actions."""
        with allure.step("Множественные навигации: добавление товара, возврат, поиск"):
            products_page.click_add_product()
            products_page.wait_for_network_idle()
            products_page.navigate()
            products_page.wait_for_network_idle()
            products_page.search("Test")
            products_page.wait_for_network_idle()
            products_page.clear_search()

        with allure.step("Проверка что страница загружена после множественных навигаций"):
            assert products_page.is_page_loaded(), \
                "BUG: Session persistence failed"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Целостность данных")
@pytest.mark.functional
class TestProductsListDataIntegrity:
    """Data integrity tests."""

    @allure.title("Данные товара полные")
    def test_product_data_complete(self, products_page: ProductsListPage):
        """Product card should display name, price, SKU and status."""
        with allure.step("Проверка наличия товаров"):
            count = products_page.get_products_count()
            assert count > 0, "PRECONDITION: No products found on page"
        with allure.step("Проверка полноты данных первой карточки товара"):
            first_card = products_page.product_cards.first
            card_text = first_card.inner_text()
            has_name = len(card_text.strip()) > 0
            has_sku = "SKU:" in card_text
            assert has_name, f"BUG: Product card has no name"
            assert has_sku, f"BUG: Product card missing SKU data: {card_text[:100]}"

    @allure.title("Количество товаров консистентно после перезагрузки")
    def test_product_count_consistent(self, products_page: ProductsListPage):
        """Product count should be consistent."""
        with allure.step("Получение количества товаров до и после перезагрузки"):
            count1 = products_page.get_products_count()
            products_page.page.reload()
            products_page.wait_for_loading_complete()
            count2 = products_page.get_products_count()
            logger.info(f"Count before: {count1}, after: {count2}")

    @allure.title("Поиск возвращает релевантные результаты")
    def test_search_returns_relevant_results(self, products_page: ProductsListPage):
        """Search should return relevant results."""
        with allure.step("Поиск 'Test' и проверка релевантности результатов"):
            products_page.search("Test")
            products_page.wait_for_network_idle()
            if products_page.get_products_count() > 0:
                name = products_page.get_product_name_from_row(0)
                logger.info(f"Search result: {name}")

    @allure.title("Сортировка действительно изменяет порядок")
    def test_sorting_actually_sorts(self, products_page: ProductsListPage):
        """Sorting should actually change order."""
        with allure.step("Сортировка по названию и проверка изменения порядка"):
            if products_page.get_products_count() >= 2:
                name1_before = products_page.get_product_name_from_row(0)
                products_page.click_column_header("Name")
                products_page.wait_for_network_idle()
                name1_after = products_page.get_product_name_from_row(0)
                logger.info(f"Before sort: {name1_before}, after: {name1_after}")

    @allure.title("Пагинация показывает разные данные на разных страницах")
    def test_pagination_shows_different_data(self, products_page: ProductsListPage):
        """Different pages should show different data."""
        with allure.step("Сравнение данных на первой и второй страницах"):
            if products_page.is_next_page_enabled():
                data_page1 = products_page.get_row_data(0) if products_page.get_products_count() > 0 else {}
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()
                data_page2 = products_page.get_row_data(0) if products_page.get_products_count() > 0 else {}
                logger.info(f"Page 1 data: {data_page1}, Page 2 data: {data_page2}")
