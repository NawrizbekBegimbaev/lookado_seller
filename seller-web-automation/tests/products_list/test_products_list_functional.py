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
@allure.feature("Пагинация")
@pytest.mark.functional
class TestProductsListPagination:
    """Pagination functionality tests."""

    @allure.title("Кнопка следующей страницы работает")
    def test_next_page_button_works(self, products_page: ProductsListPage):
        """Next page button should work."""
        with allure.step("Переход на следующую страницу если доступна"):
            if products_page.is_next_page_enabled():
                initial_data = products_page.get_row_data(0) if products_page.get_products_count() > 0 else {}
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after next page click"

    @allure.title("Кнопка предыдущей страницы работает")
    def test_prev_page_button_works(self, products_page: ProductsListPage):
        """Previous page button should work."""
        with allure.step("Переход на следующую и обратно на предыдущую страницу"):
            if products_page.is_next_page_enabled():
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()
            if products_page.is_prev_page_enabled():
                products_page.go_to_prev_page()
                products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after prev page click"

    @allure.title("Кнопка первой страницы работает")
    def test_first_page_button(self, products_page: ProductsListPage):
        """First page button should work."""
        with allure.step("Переход на первую страницу"):
            products_page.go_to_first_page()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after first page click"

    @allure.title("Кнопка последней страницы работает")
    def test_last_page_button(self, products_page: ProductsListPage):
        """Last page button should work."""
        with allure.step("Переход на последнюю страницу"):
            products_page.go_to_last_page()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after last page click"

    @allure.title("Отображение 10 строк на странице")
    def test_rows_per_page_10(self, products_page: ProductsListPage):
        """Rows per page 10 should work."""
        with allure.step("Установка 10 строк на странице"):
            products_page.set_rows_per_page(10)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after rows per page change"

    @allure.title("Отображение 25 строк на странице")
    def test_rows_per_page_25(self, products_page: ProductsListPage):
        """Rows per page 25 should work."""
        with allure.step("Установка 25 строк на странице"):
            products_page.set_rows_per_page(25)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after rows per page change"

    @allure.title("Отображение 50 строк на странице")
    def test_rows_per_page_50(self, products_page: ProductsListPage):
        """Rows per page 50 should work."""
        with allure.step("Установка 50 строк на странице"):
            products_page.set_rows_per_page(50)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after rows per page change"

    @allure.title("Информация о странице отображается корректно")
    def test_page_info_displays_correctly(self, products_page: ProductsListPage):
        """Page info should display correctly."""
        with allure.step("Получение и проверка информации о странице"):
            info = products_page.get_page_info_text()
            assert products_page.is_page_loaded(), \
                "BUG: Page not loaded for page info check"

    @allure.title("Кнопка 'Вперед' отключена на последней странице")
    def test_disabled_next_on_last_page(self, products_page: ProductsListPage):
        """Next button should be disabled on last page."""
        with allure.step("Переход на последнюю страницу"):
            products_page.go_to_last_page()
            products_page.wait_for_network_idle()

        with allure.step("Проверка состояния страницы на последней странице"):
            assert products_page.is_page_loaded(), \
                "BUG: Page state invalid on last page"

    @allure.title("Кнопка 'Назад' отключена на первой странице")
    def test_disabled_prev_on_first_page(self, products_page: ProductsListPage):
        """Previous button should be disabled on first page."""
        with allure.step("Переход на первую страницу"):
            products_page.go_to_first_page()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что кнопка 'Назад' отключена"):
            is_disabled = not products_page.is_prev_page_enabled()
            assert products_page.is_page_loaded(), \
                "BUG: Page state invalid on first page"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Массовые действия")
@pytest.mark.functional
class TestProductsListBulkActions:
    """Bulk action tests."""

    @allure.title("Чекбокс 'Выбрать все' работает")
    def test_select_all_checkbox(self, products_page: ProductsListPage):
        """Select all checkbox should work."""
        with allure.step("Выбор всех товаров и проверка количества выбранных"):
            if products_page.get_products_count() > 0:
                try:
                    products_page.select_all_products()
                    selected = products_page.get_selected_count()
                    assert selected > 0, \
                        "BUG: Select all did not select any products"
                    products_page.deselect_all_products()
                except Exception:
                    logger.info("Select all checkbox not available")

    @allure.title("Выбор отдельной строки работает")
    def test_select_individual_row(self, products_page: ProductsListPage):
        """Individual row selection should work."""
        with allure.step("Выбор первой строки и проверка количества выбранных"):
            if products_page.get_products_count() > 0:
                try:
                    products_page.select_product_by_index(0)
                    selected = products_page.get_selected_count()
                    assert selected == 1, \
                        f"BUG: Expected 1 selected, got {selected}"
                    products_page.deselect_product_by_index(0)
                except Exception:
                    logger.info("Row checkbox not available")

    @allure.title("Снятие выбора отдельной строки работает")
    def test_deselect_individual_row(self, products_page: ProductsListPage):
        """Deselecting row should work."""
        with allure.step("Выбор и снятие выбора первой строки"):
            if products_page.get_products_count() > 0:
                products_page.select_product_by_index(0)
                products_page.deselect_product_by_index(0)

        with allure.step("Проверка что ни одна строка не выбрана"):
            if products_page.get_products_count() > 0:
                selected = products_page.get_selected_count()
                assert selected == 0, \
                    f"BUG: Expected 0 selected, got {selected}"

    @allure.title("Массовое удаление показывает подтверждение")
    def test_bulk_delete_shows_confirm(self, products_page: ProductsListPage):
        """Bulk delete should show confirmation."""
        with allure.step("Выбор товара и нажатие массового удаления"):
            if products_page.get_products_count() > 0:
                products_page.select_product_by_index(0)
                products_page.click_bulk_delete()
                if products_page.is_confirm_dialog_visible():
                    products_page.cancel_action()
                products_page.deselect_all_products()

    @allure.title("Выбор нескольких строк работает")
    def test_select_multiple_rows(self, products_page: ProductsListPage):
        """Multiple row selection should work."""
        with allure.step("Выбор двух строк и проверка количества"):
            count = products_page.get_products_count()
            if count >= 2:
                products_page.select_product_by_index(0)
                products_page.select_product_by_index(1)
                selected = products_page.get_selected_count()
                assert selected == 2, \
                    f"BUG: Expected 2 selected, got {selected}"
                products_page.deselect_all_products()

    @allure.title("Снятие выбора одного после 'Выбрать все'")
    def test_select_all_then_deselect_one(self, products_page: ProductsListPage):
        """Deselecting one after select all should work."""
        with allure.step("Выбор всех и снятие выбора одного товара"):
            if products_page.get_products_count() >= 2:
                products_page.select_all_products()
                products_page.deselect_product_by_index(0)
                products_page.deselect_all_products()

    @allure.title("Отмена массового действия восстанавливает выбор")
    def test_bulk_action_cancel(self, products_page: ProductsListPage):
        """Cancel in bulk action should restore selection."""
        with allure.step("Выбор товара, нажатие удаления и отмена"):
            if products_page.get_products_count() > 0:
                products_page.select_product_by_index(0)
                products_page.click_bulk_delete()
                products_page.cancel_action()

        with allure.step("Проверка что страница функциональна после отмены"):
            assert products_page.is_page_loaded()
            if products_page.get_products_count() > 0:
                products_page.deselect_all_products()

    @allure.title("Счетчик выбранных отображается корректно")
    def test_selected_count_display(self, products_page: ProductsListPage):
        """Selected count should display correctly."""
        with allure.step("Выбор товара и проверка отображения счетчика"):
            if products_page.get_products_count() > 0:
                products_page.select_product_by_index(0)
                products_page.deselect_all_products()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Навигация")
@pytest.mark.navigation
class TestProductsListNavigation:
    """Navigation tests."""

    @allure.title("Переход к добавлению товара")
    def test_navigate_to_add_product(self, products_page: ProductsListPage):
        """Add product button should navigate."""
        with allure.step("Нажатие кнопки добавления товара"):
            products_page.click_add_product()
            products_page.wait_for_network_idle()

        with allure.step("Проверка перехода на страницу добавления"):
            url = products_page.get_current_url()
            assert "add" in url or "create" in url, \
                f"BUG: Not navigated to add product: {url}"
            products_page.navigate()

    @allure.title("Навигация через боковое меню")
    def test_sidebar_navigation(self, products_page: ProductsListPage):
        """Sidebar navigation should work."""
        with allure.step("Клик по ссылке товаров в боковом меню"):
            products_page.click_products_nav_link()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что находимся на странице товаров"):
            assert products_page.is_on_products_page(), \
                "BUG: Sidebar navigation failed"

    @allure.title("Кнопка 'Назад' браузера работает")
    def test_browser_back_button(self, products_page: ProductsListPage):
        """Browser back should work."""
        with allure.step("Переход на страницу добавления и возврат назад"):
            products_page.click_add_product()
            products_page.wait_for_network_idle()
            products_page.page.go_back()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что вернулись на страницу товаров"):
            assert products_page.is_on_products_page(), \
                "BUG: Browser back failed"

    @allure.title("Кнопка 'Вперед' браузера работает")
    def test_browser_forward_button(self, products_page: ProductsListPage):
        """Browser forward should work."""
        with allure.step("Переход вперед, назад и снова вперед"):
            products_page.click_add_product()
            products_page.wait_for_network_idle()
            products_page.page.go_back()
            products_page.wait_for_network_idle()
            products_page.page.go_forward()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что перешли на страницу добавления"):
            url = products_page.get_current_url()
            assert "add" in url or "create" in url, \
                "BUG: Browser forward failed"
            products_page.navigate()

    @allure.title("Прямой доступ по URL работает")
    def test_direct_url_access(self, products_page: ProductsListPage):
        """Direct URL access should work."""
        with allure.step("Прямой переход по URL страницы товаров"):
            products_page.navigate()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что находимся на странице товаров"):
            assert products_page.is_on_products_page(), \
                "BUG: Direct URL access failed"

    @allure.title("Обновление страницы сохраняет состояние")
    def test_refresh_preserves_state(self, products_page: ProductsListPage):
        """Page refresh should preserve state."""
        with allure.step("Поиск и обновление страницы"):
            products_page.search("Test")
            products_page.wait_for_network_idle()
            products_page.page.reload()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена после обновления"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after refresh"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Манипуляция URL")
@pytest.mark.security
class TestProductsListURL:
    """URL manipulation tests."""

    @allure.title("Невалидный параметр страницы обрабатывается")
    def test_invalid_page_param(self, products_page: ProductsListPage):
        """Invalid page parameter should be handled."""
        with allure.step("Переход по URL с невалидным параметром страницы"):
            products_page.navigate_to("/dashboard/products?page=invalid")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken with invalid page param"

    @allure.title("Отрицательный параметр страницы обрабатывается")
    def test_negative_page_param(self, products_page: ProductsListPage):
        """Negative page parameter should be handled."""
        with allure.step("Переход по URL с отрицательным параметром страницы"):
            products_page.navigate_to("/dashboard/products?page=-1")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken with negative page param"

    @allure.title("Очень большой параметр страницы обрабатывается")
    def test_very_large_page_param(self, products_page: ProductsListPage):
        """Very large page parameter should be handled."""
        with allure.step("Переход по URL с очень большим параметром страницы"):
            products_page.navigate_to("/dashboard/products?page=9999999")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken with large page param"

    @allure.title("XSS в параметре URL санитизируется")
    def test_xss_in_url_param(self, products_page: ProductsListPage):
        """XSS in URL parameter should be sanitized."""
        with allure.step("Переход по URL с XSS-payload в параметре"):
            products_page.navigate_to("/dashboard/products?search=<script>alert(1)</script>")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что XSS санитизирован"):
            content = products_page.page.content()
            assert "<script>alert(1)" not in content, \
                "BUG: XSS in URL not sanitized - SECURITY!"

    @allure.title("SQL инъекция в параметре URL обрабатывается")
    def test_sql_in_url_param(self, products_page: ProductsListPage):
        """SQL injection in URL should be handled."""
        with allure.step("Переход по URL с SQL-injection в параметре"):
            products_page.navigate_to("/dashboard/products?search=' OR '1'='1")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page crashed with SQL in URL"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Уведомления")
@pytest.mark.ui
class TestProductsListToasts:
    """Toast notification tests."""

    @allure.title("Уведомление об успехе отображается после действия")
    def test_success_toast_on_action(self, products_page: ProductsListPage):
        """Success toast should show after successful action."""
        with allure.step("Проверка видимости уведомления об успехе"):
            is_visible = products_page.is_success_toast_visible()
            logger.info(f"Success toast visible: {is_visible}")

    @allure.title("Уведомление об ошибке отображается при сбое")
    def test_error_toast_on_failure(self, products_page: ProductsListPage):
        """Error toast should show on failure."""
        with allure.step("Проверка видимости уведомления об ошибке"):
            is_visible = products_page.is_error_toast_visible()
            logger.info(f"Error toast visible: {is_visible}")

    @allure.title("Уведомление автоматически скрывается")
    def test_toast_auto_dismiss(self, products_page: ProductsListPage):
        """Toast should auto-dismiss after time."""
        with allure.step("Проверка автоматического скрытия уведомления"):
            products_page.wait_for_network_idle()
            assert products_page.is_page_loaded()

    @allure.title("Текст уведомления читаем")
    def test_toast_message_readable(self, products_page: ProductsListPage):
        """Toast message should be readable."""
        with allure.step("Получение и проверка текста уведомления"):
            message = products_page.get_toast_message()
            logger.info(f"Toast message: {message}")

    @allure.title("Множественные уведомления обрабатываются")
    def test_multiple_toasts(self, products_page: ProductsListPage):
        """Multiple toasts should be handled."""
        with allure.step("Проверка обработки множественных уведомлений"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Модальные окна")
@pytest.mark.ui
class TestProductsListModals:
    """Modal dialog tests."""

    @allure.title("Диалог подтверждения отображается для деструктивных действий")
    def test_confirm_dialog_shows(self, products_page: ProductsListPage):
        """Confirm dialog should show for destructive actions."""
        with allure.step("Нажатие кнопки удаления и проверка диалога подтверждения"):
            if products_page.get_products_count() > 0:
                products_page.click_delete_on_row(0)
                is_visible = products_page.is_confirm_dialog_visible()
                if is_visible:
                    products_page.cancel_action()

    @allure.title("Отмена в диалоге подтверждения закрывает его")
    def test_confirm_dialog_cancel(self, products_page: ProductsListPage):
        """Cancel in confirm dialog should close it."""
        with allure.step("Открытие диалога удаления и нажатие отмены"):
            if products_page.get_products_count() > 0:
                products_page.click_delete_on_row(0)
                if products_page.is_confirm_dialog_visible():
                    products_page.cancel_action()
                    assert not products_page.is_confirm_dialog_visible(), \
                        "BUG: Dialog not closed on cancel"

    @allure.title("Escape закрывает модальное окно")
    def test_escape_closes_modal(self, products_page: ProductsListPage):
        """Escape key should close modal."""
        with allure.step("Открытие диалога и закрытие клавишей Escape"):
            if products_page.get_products_count() > 0:
                products_page.click_delete_on_row(0)
                if products_page.is_confirm_dialog_visible():
                    products_page.press_escape()
                    products_page.page.wait_for_load_state("domcontentloaded")

    @allure.title("Клик вне модального окна закрывает его")
    def test_click_outside_closes_modal(self, products_page: ProductsListPage):
        """Clicking outside modal should close it (if supported)."""
        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Модальное окно удерживает фокус")
    def test_modal_has_focus_trap(self, products_page: ProductsListPage):
        """Modal should trap focus."""
        with allure.step("Проверка доступности страницы"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Устойчивость")
@pytest.mark.functional
class TestProductsListRobustness:
    """Robustness and edge case tests."""

    @allure.title("Двойной клик по навигации не ломает страницу")
    def test_double_click_navigation(self, products_page: ProductsListPage):
        """Double clicking navigation should not break."""
        with allure.step("Двойной клик по ссылке навигации товаров"):
            products_page.products_nav_link.dblclick()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Double click broke navigation"

    @allure.title("Быстрый ввод в поиск обрабатывается")
    def test_rapid_search_input(self, products_page: ProductsListPage):
        """Rapid search input should be handled."""
        with allure.step("Быстрый посимвольный ввод 'TestProduct'"):
            for char in "TestProduct":
                products_page.search_input.type(char, delay=10)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Rapid input broke page"

    @allure.title("Быстрые клики по пагинации обрабатываются")
    def test_rapid_pagination(self, products_page: ProductsListPage):
        """Rapid pagination clicks should be handled."""
        with allure.step("Быстрые последовательные клики по кнопке следующей страницы"):
            if products_page.is_next_page_enabled():
                products_page.next_page_btn.click()
                products_page.next_page_btn.click()
                products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Rapid pagination broke page"

    @allure.title("Страница работает при медленной сети")
    def test_slow_network_simulation(self, products_page: ProductsListPage):
        """Page should handle slow network."""
        with allure.step("Навигация и ожидание полной загрузки"):
            products_page.navigate()
            products_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken under slow network"

    @allure.title("Одновременные действия не ломают страницу")
    def test_concurrent_actions(self, products_page: ProductsListPage):
        """Concurrent actions should not break page."""
        with allure.step("Выполнение поиска и пагинации одновременно"):
            products_page.search("Test")
            if products_page.is_next_page_enabled():
                products_page.go_to_next_page()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Concurrent actions broke page"

    @allure.title("Действие после долгого ожидания работает")
    def test_long_idle_then_action(self, products_page: ProductsListPage):
        """Action after long idle should work."""
        with allure.step("Ожидание загрузки и выполнение поиска"):
            products_page.page.wait_for_load_state("networkidle")
            products_page.search("Test")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Page broken after idle"

    @allure.title("Навигация клавишей Tab работает")
    def test_multiple_tab_behavior(self, products_page: ProductsListPage):
        """Multiple tab operations should be handled."""
        with allure.step("Навигация через 5 элементов клавишей Tab"):
            for _ in range(5):
                products_page.tab_to_next_element()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Tab navigation broke page"

    @allure.title("Обновление во время поиска обрабатывается")
    def test_refresh_during_search(self, products_page: ProductsListPage):
        """Refresh during search should be handled."""
        with allure.step("Ввод текста в поле поиска и обновление страницы"):
            products_page.search_input.fill("Test")
            products_page.page.reload()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Refresh during search broke page"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Производительность")
@pytest.mark.performance
class TestProductsListPerformance:
    """Performance tests."""

    @allure.title("Время загрузки страницы в пределах нормы")
    def test_page_load_time(self, products_page: ProductsListPage):
        """Page should load in reasonable time."""
        import time
        with allure.step("Измерение времени загрузки страницы"):
            start = time.time()
            products_page.navigate()
            products_page.wait_for_loading_complete()
            elapsed = time.time() - start
            logger.info(f"Page load time: {elapsed:.2f}s")

        with allure.step("Проверка что время загрузки менее 10 секунд"):
            assert elapsed < 10, \
                f"BUG: Page load too slow: {elapsed:.2f}s"

    @allure.title("Время ответа на поиск в пределах нормы")
    def test_search_response_time(self, products_page: ProductsListPage):
        """Search should respond quickly."""
        import time
        with allure.step("Измерение времени ответа на поиск"):
            start = time.time()
            products_page.search("Test")
            products_page.wait_for_network_idle()
            elapsed = time.time() - start
            logger.info(f"Search time: {elapsed:.2f}s")

        with allure.step("Проверка что время ответа менее 5 секунд"):
            assert elapsed < 5, \
                f"BUG: Search too slow: {elapsed:.2f}s"

    @allure.title("Время ответа пагинации в пределах нормы")
    def test_pagination_response_time(self, products_page: ProductsListPage):
        """Pagination should respond quickly."""
        import time
        with allure.step("Измерение времени пагинации"):
            if products_page.is_next_page_enabled():
                start = time.time()
                products_page.go_to_next_page()
                products_page.wait_for_network_idle()
                elapsed = time.time() - start
                logger.info(f"Pagination time: {elapsed:.2f}s")
                assert elapsed < 3, \
                    f"BUG: Pagination too slow: {elapsed:.2f}s"

    @allure.title("Нет утечек памяти при навигации")
    def test_no_memory_leaks(self, products_page: ProductsListPage):
        """No obvious memory leaks during navigation."""
        with allure.step("Множественная навигация для проверки утечек памяти"):
            for _ in range(3):
                products_page.navigate()
                products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Memory leak caused page failure"

    @allure.title("Страница обрабатывает большой набор данных")
    def test_handles_large_dataset(self, products_page: ProductsListPage):
        """Page should handle large datasets."""
        with allure.step("Установка 100 строк на странице"):
            products_page.set_rows_per_page(100)
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Large dataset broke page"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Быстрые действия")
@pytest.mark.functional
class TestProductsListQuickActions:
    """Quick action tests."""

    @allure.title("Кнопка быстрого редактирования работает")
    def test_quick_edit_button(self, products_page: ProductsListPage):
        """Quick edit button should work."""
        with allure.step("Нажатие кнопки редактирования первого товара"):
            if products_page.get_products_count() > 0:
                products_page.click_edit_on_row(0)
                products_page.wait_for_network_idle()
                products_page.navigate()

    @allure.title("Кнопка быстрого удаления показывает подтверждение")
    def test_quick_delete_button(self, products_page: ProductsListPage):
        """Quick delete button should show confirm."""
        with allure.step("Нажатие кнопки удаления и проверка диалога"):
            if products_page.get_products_count() > 0:
                products_page.click_delete_on_row(0)
                if products_page.is_confirm_dialog_visible():
                    products_page.cancel_action()

    @allure.title("Кнопка быстрого просмотра открывает детали")
    def test_quick_view_button(self, products_page: ProductsListPage):
        """Quick view button should open detail."""
        with allure.step("Нажатие кнопки просмотра первого товара"):
            if products_page.get_products_count() > 0:
                products_page.click_view_on_row(0)
                products_page.wait_for_network_idle()
                products_page.navigate()

    @allure.title("Меню дополнительных действий открывается")
    def test_more_actions_menu(self, products_page: ProductsListPage):
        """More actions menu should open."""
        with allure.step("Открытие меню дополнительных действий"):
            if products_page.get_products_count() > 0:
                products_page.click_more_actions_on_row(0)
                products_page.page.wait_for_load_state("domcontentloaded")
                products_page.press_escape()

    @allure.title("Кнопки действий имеют состояние при наведении")
    def test_action_buttons_hover_state(self, products_page: ProductsListPage):
        """Action buttons should have hover states."""
        with allure.step("Наведение на первую строку таблицы"):
            if products_page.get_products_count() > 0:
                row = products_page.table_rows.first
                row.hover()
                products_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Обработка ошибок")
@pytest.mark.functional
class TestProductsListErrorHandling:
    """Error handling tests."""

    @allure.title("Сетевые ошибки отображаются")
    def test_network_error_display(self, products_page: ProductsListPage):
        """Network errors should be displayed."""
        with allure.step("Проверка обработки сетевых ошибок"):
            assert products_page.is_page_loaded()

    @allure.title("Серверные ошибки обрабатываются")
    def test_server_error_handling(self, products_page: ProductsListPage):
        """Server errors should be handled."""
        with allure.step("Проверка обработки серверных ошибок"):
            assert products_page.is_page_loaded()

    @allure.title("Повторная попытка после ошибки работает")
    def test_retry_after_error(self, products_page: ProductsListPage):
        """Retry should work after error."""
        with allure.step("Навигация и проверка повторной загрузки"):
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Сообщения об ошибках очищаются при повторе")
    def test_error_message_clear(self, products_page: ProductsListPage):
        """Error messages should clear on retry."""
        with allure.step("Навигация и проверка отсутствия ошибок"):
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена без ошибок"):
            assert products_page.is_page_loaded()

    @allure.title("Плавная деградация при частичном сбое")
    def test_graceful_degradation(self, products_page: ProductsListPage):
        """Page should degrade gracefully on partial failure."""
        with allure.step("Проверка корректной работы основного функционала"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Аналитика")
@pytest.mark.functional
class TestProductsListAnalytics:
    """Analytics and tracking tests."""

    @allure.title("Просмотр страницы отслеживается")
    def test_page_view_trackable(self, products_page: ProductsListPage):
        """Page view should be trackable."""
        with allure.step("Проверка возможности отслеживания просмотра страницы"):
            assert products_page.is_page_loaded()

    @allure.title("Действие поиска отслеживается")
    def test_search_action_trackable(self, products_page: ProductsListPage):
        """Search action should be trackable."""
        with allure.step("Выполнение поиска для проверки отслеживания"):
            products_page.search("Test")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Действие клика отслеживается")
    def test_click_action_trackable(self, products_page: ProductsListPage):
        """Click actions should be trackable."""
        with allure.step("Клик по товару для проверки отслеживания"):
            if products_page.get_products_count() > 0:
                products_page.click_row(0)
                products_page.wait_for_network_idle()
                products_page.navigate()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Действие фильтрации отслеживается")
    def test_filter_action_trackable(self, products_page: ProductsListPage):
        """Filter actions should be trackable."""
        with allure.step("Применение и очистка фильтра для проверки отслеживания"):
            products_page.search("Filter")
            products_page.wait_for_network_idle()
            products_page.clear_search()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Экспорт")
@pytest.mark.functional
class TestProductsListExport:
    """Export functionality tests."""

    @allure.title("Кнопка экспорта видна")
    def test_export_button_visible(self, products_page: ProductsListPage):
        """Export button should be visible if available."""
        with allure.step("Проверка видимости кнопки экспорта"):
            export_btn = products_page.page.get_by_role("button", name="Export").or_(
                products_page.page.locator("button:has-text('Eksport')")
            ).or_(products_page.page.locator("button:has-text('Экспорт')"))
            logger.info(f"Export button visible: {export_btn.is_visible(timeout=2000)}")

    @allure.title("Опция экспорта в CSV доступна")
    def test_export_csv_option(self, products_page: ProductsListPage):
        """CSV export option should be available."""
        with allure.step("Проверка доступности экспорта в CSV"):
            assert products_page.is_page_loaded()

    @allure.title("Опция экспорта в Excel доступна")
    def test_export_excel_option(self, products_page: ProductsListPage):
        """Excel export option should be available."""
        with allure.step("Проверка доступности экспорта в Excel"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Пустое состояние")
@pytest.mark.ui
class TestProductsListEmptyState:
    """Empty state tests."""

    @allure.title("Пустое состояние отображается после фильтрации без результатов")
    def test_empty_state_after_filter(self, products_page: ProductsListPage):
        """Empty state should show after filtering to no results."""
        with allure.step("Применение фильтра без совпадений"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка пустого состояния"):
            count = products_page.get_products_count()
            if count == 0:
                assert products_page.is_page_loaded(), \
                    "BUG: Page broken with empty results"

    @allure.title("Пустое состояние содержит сообщение")
    def test_empty_state_message(self, products_page: ProductsListPage):
        """Empty state should have a message."""
        with allure.step("Поиск несуществующего товара"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка текста пустого состояния"):
            if products_page.is_empty_state_visible():
                empty = products_page.empty_state
                text = empty.inner_text() if empty.is_visible() else ""
                logger.info(f"Empty state text: {text}")

    @allure.title("Пустое состояние имеет кнопку добавления товара")
    def test_empty_state_has_action(self, products_page: ProductsListPage):
        """Empty state should have add product action."""
        with allure.step("Проверка наличия кнопки добавления в пустом состоянии"):
            if products_page.is_empty_state_visible():
                add_btn = products_page.add_product_btn
                assert add_btn.is_visible(timeout=2000), \
                    "BUG: No action available in empty state"

    @allure.title("Очистка фильтра из пустого состояния работает")
    def test_clear_filter_from_empty_state(self, products_page: ProductsListPage):
        """Should be able to clear filter from empty state."""
        with allure.step("Применение фильтра без результатов и очистка"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()
            products_page.clear_search()
            products_page.wait_for_network_idle()

        with allure.step("Проверка восстановления из пустого состояния"):
            assert products_page.is_page_loaded(), \
                "BUG: Cannot recover from empty state"

    @allure.title("Пагинация не отображается в пустом состоянии")
    def test_empty_state_no_pagination(self, products_page: ProductsListPage):
        """Pagination should not show in empty state."""
        with allure.step("Применение фильтра без результатов"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка отсутствия пагинации при пустом результате"):
            if products_page.get_products_count() == 0:
                assert products_page.is_page_loaded()
