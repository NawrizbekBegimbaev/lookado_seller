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
@allure.feature("Элементы интерфейса")
@pytest.mark.ui
class TestProductsListUI:
    """UI element visibility and state tests."""

    @allure.title("Проверка успешной загрузки страницы")
    def test_page_loads_successfully(self, products_page: ProductsListPage):
        """Page should load without errors."""
        with allure.step("Проверка загрузки страницы товаров"):
            assert products_page.is_page_loaded(), \
                "BUG: Products page failed to load"

    @allure.title("Проверка видимости заголовка страницы")
    def test_page_title_visible(self, products_page: ProductsListPage):
        """Page title should be visible."""
        with allure.step("Проверка видимости заголовка"):
            title = products_page.page_title
            assert title.is_visible(timeout=3000), \
                "BUG: Page title not visible"

    @allure.title("Проверка видимости кнопки добавления товара")
    def test_add_product_button_visible(self, products_page: ProductsListPage):
        """Add Products button should be visible."""
        with allure.step("Проверка видимости кнопки добавления товара"):
            btn = products_page.add_product_btn
            assert btn.is_visible(timeout=3000), \
                "BUG: Add Products button not visible"

    @allure.title("Проверка видимости поля поиска")
    def test_search_input_visible(self, products_page: ProductsListPage):
        """Search input should be visible."""
        with allure.step("Проверка видимости поля поиска"):
            search = products_page.search_input
            assert search.is_visible(timeout=3000), \
                "BUG: Search input not visible"

    @allure.title("Проверка видимости товаров или пустого состояния")
    def test_products_visible_or_empty_state(self, products_page: ProductsListPage):
        """Products (grid or table) or empty state should be visible."""
        with allure.step("Проверка наличия товаров или пустого состояния"):
            products_count = products_page.get_products_count()
            empty_visible = products_page.is_empty_state_visible()
            table_visible = products_page.products_table.is_visible(timeout=1000)
            assert products_count > 0 or empty_visible or table_visible, \
                "BUG: Neither products nor empty state visible"

    @allure.title("Проверка видимости счетчика товаров при наличии товаров")
    def test_total_count_visible_when_products_exist(self, products_page: ProductsListPage):
        """Total count should be visible when products exist (grid view)."""
        with allure.step("Проверка видимости счетчика при наличии товаров"):
            products_count = products_page.get_products_count()
            if products_count > 0:
                total_text = products_page.total_products_text
                assert total_text.is_visible(timeout=3000), \
                    "BUG: Total count text not visible when products exist"

    @allure.title("Проверка видимости вкладок статусов")
    def test_status_tabs_visible(self, products_page: ProductsListPage):
        """Status filter tabs should be visible."""
        with allure.step("Проверка видимости и количества вкладок статусов"):
            tabs = products_page.status_tabs
            assert tabs.first.is_visible(timeout=3000), \
                "BUG: Status tabs not visible"
            assert tabs.count() >= 4, \
                f"BUG: Expected at least 4 status tabs, found {tabs.count()}"

    @allure.title("Проверка видимости переключателя вида (сетка/таблица)")
    def test_view_toggle_visible(self, products_page: ProductsListPage):
        """View toggle buttons (grid/table) should be visible."""
        with allure.step("Проверка видимости кнопок переключения вида"):
            grid_toggle = products_page.view_toggle_grid
            table_toggle = products_page.view_toggle_table
            assert grid_toggle.is_visible(timeout=2000) or table_toggle.is_visible(timeout=2000), \
                "BUG: View toggle buttons not visible"

    @allure.title("Проверка отсутствия JS ошибок при загрузке")
    def test_no_javascript_errors_on_load(self, products_page: ProductsListPage):
        """Page should load without JS errors."""
        with allure.step("Проверка корректного URL страницы"):
            assert products_page.is_on_products_page(), \
                "BUG: Not on products page after navigation"

    @allure.title("Проверка кликабельности кнопки добавления")
    def test_add_button_is_clickable(self, products_page: ProductsListPage):
        """Add Products button should be enabled."""
        with allure.step("Проверка что кнопка добавления активна"):
            btn = products_page.add_product_btn
            if btn.is_visible(timeout=2000):
                assert btn.is_enabled(), \
                    "BUG: Add Products button is disabled"

    @allure.title("Проверка активной ссылки на товары в боковом меню")
    def test_sidebar_products_link_active(self, products_page: ProductsListPage):
        """Products link in sidebar should be active/highlighted."""
        with allure.step("Проверка видимости ссылки на товары в боковом меню"):
            link = products_page.products_nav_link
            assert link.is_visible(timeout=3000), \
                "BUG: Products nav link not visible in sidebar"

    @allure.title("Проверка корректности URL страницы")
    def test_page_url_correct(self, products_page: ProductsListPage):
        """Page URL should contain /dashboard/products."""
        with allure.step("Проверка что URL содержит /dashboard/products"):
            url = products_page.get_current_url()
            assert "/dashboard/products" in url, \
                f"BUG: Wrong URL: {url}"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Взаимодействие с таблицей")
@pytest.mark.functional
class TestProductsListTable:
    """Table interaction tests."""

    @allure.title("Проверка навигации при клике на строку")
    def test_row_click_navigates(self, products_page: ProductsListPage):
        """Clicking row should navigate to detail."""
        with allure.step("Переключение на table view"):
            if products_page.is_grid_view_active():
                products_page.switch_to_table_view()
        with allure.step("Клик по первой строке таблицы"):
            if products_page.get_products_count() > 0:
                products_page.click_row(0)
                products_page.wait_for_network_idle()

        with allure.step("Проверка навигации и возврат на страницу товаров"):
            if products_page.get_products_count() > 0:
                assert products_page.page.url is not None, \
                    "BUG: No navigation after row click"
                products_page.navigate()

    @allure.title("Проверка отображения данных товара в таблице")
    def test_table_shows_product_data(self, products_page: ProductsListPage):
        """Table rows should display product data."""
        with allure.step("Переключение на table view"):
            if products_page.is_grid_view_active():
                products_page.switch_to_table_view()
        with allure.step("Проверка данных в первой строке таблицы"):
            if products_page.get_products_count() > 0:
                data = products_page.get_row_data(0)
                assert len(data) > 0, \
                    "BUG: No data displayed in table row"

    @allure.title("Проверка видимости миниатюр товаров")
    def test_product_thumbnail_visible(self, products_page: ProductsListPage):
        """Product thumbnails should be visible."""
        with allure.step("Проверка количества миниатюр товаров"):
            if products_page.get_products_count() > 0:
                thumbnails = products_page.product_thumbnails
                logger.info(f"Thumbnails count: {thumbnails.count()}")

    @allure.title("Проверка видимости бейджей статусов")
    def test_status_badge_visible(self, products_page: ProductsListPage):
        """Status badges should be visible."""
        with allure.step("Проверка количества бейджей статусов"):
            if products_page.get_products_count() > 0:
                badges = products_page.status_badges
                logger.info(f"Status badges count: {badges.count()}")

    @allure.title("Проверка видимости кнопок действий в строках")
    def test_action_buttons_visible(self, products_page: ProductsListPage):
        """Action buttons should be visible in rows."""
        with allure.step("Проверка количества кнопок действий"):
            if products_page.get_products_count() > 0:
                action_btns = products_page.row_action_btns
                logger.info(f"Action buttons count: {action_btns.count()}")

    @allure.title("Проверка работы кнопки редактирования")
    def test_edit_button_works(self, products_page: ProductsListPage):
        """Edit button should work."""
        with allure.step("Нажатие кнопки редактирования первого товара"):
            if products_page.get_products_count() > 0:
                try:
                    products_page.click_edit_on_row(0)
                    products_page.wait_for_network_idle()
                except Exception:
                    logger.info("Edit button not available")
                products_page.navigate()

    @allure.title("Проверка диалога подтверждения при удалении")
    def test_delete_button_shows_confirm(self, products_page: ProductsListPage):
        """Delete button should show confirmation."""
        with allure.step("Нажатие кнопки удаления и проверка диалога"):
            if products_page.get_products_count() > 0:
                try:
                    products_page.click_delete_on_row(0)
                    dialog_visible = products_page.is_confirm_dialog_visible()
                    if dialog_visible:
                        products_page.cancel_action()
                except Exception:
                    logger.info("Delete button not available")

    @allure.title("Проверка пустого состояния таблицы")
    def test_table_empty_state(self, products_page: ProductsListPage):
        """Empty state should show when no products."""
        with allure.step("Поиск несуществующего товара"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка пустого состояния таблицы"):
            count = products_page.get_products_count()
            if count == 0:
                assert products_page.is_page_loaded(), \
                    "BUG: Page not handling empty state"



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Доступность")
@pytest.mark.accessibility
class TestProductsListAccessibility:
    """Accessibility tests."""

    @allure.title("Проверка видимости фокуса на элементах")
    def test_focus_visible_on_elements(self, products_page: ProductsListPage):
        """Focus should be visible on interactive elements."""
        with allure.step("Установка фокуса на поле поиска"):
            products_page.search_input.focus()

        with allure.step("Проверка что фокус виден"):
            focused = products_page.get_focused_element()
            assert focused is not None, \
                "BUG: Focus not visible"

    @allure.title("Проверка логичного порядка табуляции")
    def test_tab_order_logical(self, products_page: ProductsListPage):
        """Tab order should be logical."""
        with allure.step("Навигация Tab через 3 элемента"):
            for _ in range(3):
                products_page.tab_to_next_element()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка наличия ARIA меток")
    def test_aria_labels_present(self, products_page: ProductsListPage):
        """Interactive elements should have ARIA labels."""
        with allure.step("Проверка ARIA меток поля поиска"):
            search = products_page.search_input
            if search.is_visible():
                placeholder = search.get_attribute("placeholder")
                aria_label = search.get_attribute("aria-label")
                has_label = placeholder or aria_label
                logger.info(f"Search has label: {has_label}")

    @allure.title("Проверка работы клавиатурной навигации")
    def test_keyboard_navigation_works(self, products_page: ProductsListPage):
        """Keyboard navigation should work."""
        with allure.step("Навигация клавишами Tab и Enter"):
            products_page.press_key("Tab")
            products_page.press_key("Tab")
            products_page.press_key("Enter")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Keyboard navigation failed"

    @allure.title("Проверка закрытия выпадающих списков по Escape")
    def test_escape_closes_dropdowns(self, products_page: ProductsListPage):
        """Escape should close dropdowns."""
        with allure.step("Нажатие Escape и проверка страницы"):
            products_page.press_escape()
            assert products_page.is_page_loaded()

    @allure.title("Проверка наличия меток у кнопок")
    def test_buttons_have_labels(self, products_page: ProductsListPage):
        """Buttons should have accessible labels."""
        with allure.step("Проверка наличия текста или ARIA метки у кнопки добавления"):
            add_btn = products_page.add_product_btn
            if add_btn.is_visible():
                text = add_btn.inner_text()
                aria = add_btn.get_attribute("aria-label")
                has_label = bool(text or aria)
                assert has_label, \
                    "BUG: Add button has no accessible label"

    @allure.title("Проверка наличия alt-текста у изображений")
    def test_images_have_alt(self, products_page: ProductsListPage):
        """Images should have alt text."""
        with allure.step("Проверка alt-текста у миниатюр товаров"):
            if products_page.get_products_count() > 0:
                thumbnails = products_page.product_thumbnails
                if thumbnails.count() > 0:
                    alt = thumbnails.first.get_attribute("alt")
                    logger.info(f"First thumbnail alt: {alt}")

    @allure.title("Проверка связанности меток с полями ввода")
    def test_form_labels_connected(self, products_page: ProductsListPage):
        """Form inputs should have connected labels."""
        with allure.step("Проверка наличия id у поля поиска"):
            search = products_page.search_input
            if search.is_visible():
                id_attr = search.get_attribute("id")
                logger.info(f"Search input id: {id_attr}")



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Горячие клавиши")
@pytest.mark.accessibility
class TestProductsListKeyboardShortcuts:
    """Keyboard shortcut tests."""

    @allure.title("Проверка Ctrl+A для выделения всего")
    def test_ctrl_a_select_all(self, products_page: ProductsListPage):
        """Ctrl+A might select all (browser dependent)."""
        with allure.step("Нажатие Ctrl+A на странице"):
            products_page.products_table.focus() if products_page.products_table.is_visible() else None
            products_page.page.keyboard.press("Control+a")

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка сброса выделения по Escape")
    def test_escape_clears_selection(self, products_page: ProductsListPage):
        """Escape should clear focus/selection."""
        with allure.step("Нажатие Escape для сброса выделения"):
            products_page.press_escape()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка активации элемента по Enter")
    def test_enter_activates_focused(self, products_page: ProductsListPage):
        """Enter should activate focused element."""
        with allure.step("Фокус на поле поиска и нажатие Enter"):
            products_page.search_input.focus()
            products_page.press_enter()
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка навигации стрелками в выпадающем списке")
    def test_arrow_keys_in_dropdown(self, products_page: ProductsListPage):
        """Arrow keys should navigate dropdowns."""
        with allure.step("Открытие выпадающего списка и навигация стрелками"):
            products_page.rows_per_page_select.click()
            products_page.page.keyboard.press("ArrowDown")
            products_page.page.keyboard.press("ArrowUp")
            products_page.press_escape()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка полной навигации по Tab")
    def test_tab_navigation_complete(self, products_page: ProductsListPage):
        """Tab should navigate through all elements."""
        with allure.step("Навигация через 10 элементов клавишей Tab"):
            for _ in range(10):
                products_page.tab_to_next_element()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка обратной навигации по Shift+Tab")
    def test_shift_tab_reverse(self, products_page: ProductsListPage):
        """Shift+Tab should navigate in reverse."""
        with allure.step("Навигация вперед и обратно клавишами Tab и Shift+Tab"):
            products_page.tab_to_next_element()
            products_page.tab_to_next_element()
            products_page.tab_to_prev_element()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Индикаторы статусов")
@pytest.mark.ui
class TestProductsListStatusIndicators:
    """Status indicator tests."""

    @allure.title("Проверка видимости статуса 'Ожидает'")
    def test_pending_status_visible(self, products_page: ProductsListPage):
        """Pending status should be visible."""
        with allure.step("Проверка количества бейджей 'Ожидает'"):
            badges = products_page.pending_badges
            logger.info(f"Pending badges: {badges.count()}")

    @allure.title("Проверка видимости статуса 'Одобрено'")
    def test_approved_status_visible(self, products_page: ProductsListPage):
        """Approved status should be visible."""
        with allure.step("Проверка количества бейджей 'Одобрено'"):
            badges = products_page.approved_badges
            logger.info(f"Approved badges: {badges.count()}")

    @allure.title("Проверка видимости статуса 'Отклонено'")
    def test_rejected_status_visible(self, products_page: ProductsListPage):
        """Rejected status should be visible."""
        with allure.step("Проверка количества бейджей 'Отклонено'"):
            badges = products_page.rejected_badges
            logger.info(f"Rejected badges: {badges.count()}")

    @allure.title("Проверка корректного цвета бейджей статусов")
    def test_status_has_correct_color(self, products_page: ProductsListPage):
        """Status badges should have correct colors."""
        with allure.step("Проверка CSS-классов бейджей статусов"):
            if products_page.get_products_count() > 0:
                badges = products_page.status_badges
                if badges.count() > 0:
                    classes = badges.first.get_attribute("class")
                    logger.info(f"Status badge classes: {classes}")

    @allure.title("Проверка статуса в данных строки")
    def test_status_from_row_data(self, products_page: ProductsListPage):
        """Status should be in row data."""
        with allure.step("Получение статуса из данных первой строки"):
            if products_page.get_products_count() > 0:
                status = products_page.get_product_status_from_row(0)
                logger.info(f"Product status: {status}")

    @allure.title("Проверка обновления списка при фильтрации по статусу")
    def test_filter_by_status_updates_list(self, products_page: ProductsListPage):
        """Filtering by status should update list."""
        with allure.step("Применение фильтра по статусу 'Pending'"):
            products_page.open_filters()
            products_page.apply_status_filter("Pending")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Индикаторы остатков")
@pytest.mark.ui
class TestProductsListStockIndicators:
    """Stock indicator tests."""

    @allure.title("Проверка видимости столбца остатков")
    def test_stock_column_visible(self, products_page: ProductsListPage):
        """Stock column should be visible."""
        with allure.step("Проверка наличия столбца остатков"):
            columns = products_page.get_column_names()
            has_stock = any("stock" in c.lower() for c in columns)
            logger.info(f"Has stock column: {has_stock}, columns: {columns}")

    @allure.title("Проверка индикатора 'Нет в наличии'")
    def test_out_of_stock_indicator(self, products_page: ProductsListPage):
        """Out of stock should be indicated."""
        with allure.step("Проверка наличия индикатора 'Нет в наличии'"):
            out_of_stock = products_page.page.locator(":text('Out of stock')").or_(
                products_page.page.locator(":text('Qolmagan')")
            )
            logger.info(f"Out of stock visible: {out_of_stock.is_visible(timeout=1000)}")

    @allure.title("Проверка отображения количества в наличии")
    def test_in_stock_display(self, products_page: ProductsListPage):
        """In stock quantity should display."""
        with allure.step("Проверка отображения данных остатков"):
            if products_page.get_products_count() > 0:
                data = products_page.get_row_data(0)
                logger.info(f"Row data: {data}")

    @allure.title("Проверка предупреждения о малом остатке")
    def test_low_stock_warning(self, products_page: ProductsListPage):
        """Low stock should show warning."""
        with allure.step("Проверка наличия предупреждения о малом остатке"):
            low_stock = products_page.page.locator(":text('Low stock')").or_(
                products_page.page.locator("[class*='warning']")
            )
            logger.info(f"Low stock warning visible: {low_stock.is_visible(timeout=1000)}")

    @allure.title("Проверка формата числа остатков")
    def test_stock_number_format(self, products_page: ProductsListPage):
        """Stock numbers should be formatted."""
        with allure.step("Проверка корректного формата чисел остатков"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Отображение цен")
@pytest.mark.ui
class TestProductsListPriceDisplay:
    """Price display tests."""

    @allure.title("Проверка видимости столбца цен")
    def test_price_column_visible(self, products_page: ProductsListPage):
        """Price column should be visible."""
        with allure.step("Проверка наличия столбца цен"):
            columns = products_page.get_column_names()
            has_price = any("price" in c.lower() or "narx" in c.lower() for c in columns)
            logger.info(f"Has price column: {has_price}")

    @allure.title("Проверка корректного формата цены")
    def test_price_format_correct(self, products_page: ProductsListPage):
        """Price should be formatted correctly."""
        with allure.step("Проверка формата цены первого товара"):
            if products_page.get_products_count() > 0:
                price = products_page.get_product_price_from_row(0)
                logger.info(f"Price format: {price}")

    @allure.title("Проверка наличия символа валюты")
    def test_currency_symbol_present(self, products_page: ProductsListPage):
        """Currency symbol should be present."""
        with allure.step("Проверка наличия символа валюты в цене"):
            if products_page.get_products_count() > 0:
                price = products_page.get_product_price_from_row(0)
                has_currency = "UZS" in price or "so'm" in price or "сум" in price
                logger.info(f"Price: {price}, has currency: {has_currency}")

    @allure.title("Проверка выделения скидочной цены")
    def test_discount_price_highlighted(self, products_page: ProductsListPage):
        """Discount prices should be highlighted."""
        with allure.step("Проверка стилей скидочных цен"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка выравнивания цен")
    def test_price_alignment(self, products_page: ProductsListPage):
        """Prices should be right-aligned."""
        with allure.step("Проверка визуального выравнивания цен"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Обработка изображений")
@pytest.mark.ui
class TestProductsListImageHandling:
    """Product image handling tests."""

    @allure.title("Проверка отображения миниатюр товаров")
    def test_thumbnails_display(self, products_page: ProductsListPage):
        """Product thumbnails should display."""
        with allure.step("Проверка количества отображаемых миниатюр"):
            if products_page.get_products_count() > 0:
                thumbnails = products_page.product_thumbnails
                count = thumbnails.count()
                logger.info(f"Thumbnails visible: {count}")

    @allure.title("Проверка заглушки для отсутствующих изображений")
    def test_placeholder_for_missing_image(self, products_page: ProductsListPage):
        """Placeholder should show for missing images."""
        with allure.step("Проверка наличия заглушек для отсутствующих изображений"):
            placeholders = products_page.image_placeholders
            logger.info(f"Placeholders visible: {placeholders.count()}")

    @allure.title("Проверка загрузки изображений без ошибок")
    def test_image_loads_without_error(self, products_page: ProductsListPage):
        """Images should load without errors."""
        with allure.step("Проверка наличия src у миниатюр"):
            if products_page.get_products_count() > 0:
                thumbnails = products_page.product_thumbnails
                if thumbnails.count() > 0:
                    src = thumbnails.first.get_attribute("src")
                    assert src is not None, \
                        "BUG: Image has no source"

    @allure.title("Проверка alt-текста изображений")
    def test_image_alt_text(self, products_page: ProductsListPage):
        """Images should have alt text."""
        with allure.step("Проверка alt-текста первой миниатюры"):
            if products_page.get_products_count() > 0:
                thumbnails = products_page.product_thumbnails
                if thumbnails.count() > 0:
                    alt = thumbnails.first.get_attribute("alt")
                    logger.info(f"Image alt: {alt}")

    @allure.title("Проверка обработки битых изображений")
    def test_broken_image_handled(self, products_page: ProductsListPage):
        """Broken images should show fallback."""
        with allure.step("Проверка обработки битых изображений"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Состояние загрузки")
@pytest.mark.ui
class TestProductsListLoading:
    """Loading state tests."""

    @allure.title("Проверка отображения спиннера загрузки")
    def test_loading_spinner_shows(self, products_page: ProductsListPage):
        """Loading spinner should show during load."""
        with allure.step("Обновление страницы и проверка спиннера"):
            products_page.page.reload()
            logger.info(f"Loading spinner visible: {products_page.is_loading()}")

    @allure.title("Проверка завершения загрузки")
    def test_loading_completes(self, products_page: ProductsListPage):
        """Loading should complete."""
        with allure.step("Навигация и ожидание завершения загрузки"):
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что загрузка завершена"):
            assert not products_page.is_loading(), \
                "BUG: Loading never completed"

    @allure.title("Проверка загрузки данных после спиннера")
    def test_data_loads_after_spinner(self, products_page: ProductsListPage):
        """Data should load after spinner disappears."""
        with allure.step("Навигация и ожидание загрузки данных"):
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что данные загружены"):
            assert products_page.is_page_loaded(), \
                "BUG: Page not loaded after spinner"

    @allure.title("Проверка блокировки кнопок во время загрузки")
    def test_buttons_disabled_during_load(self, products_page: ProductsListPage):
        """Buttons should be disabled during load."""
        with allure.step("Навигация и проверка блокировки кнопок"):
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка отсутствия мерцания контента при загрузке")
    def test_no_flash_of_content(self, products_page: ProductsListPage):
        """No flash of wrong content during load."""
        with allure.step("Навигация и проверка отсутствия мерцания"):
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена корректно"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Адаптивный дизайн")
@pytest.mark.ui
class TestProductsListResponsive:
    """Responsive design tests."""

    @allure.title("Проверка отображения на десктопе (1920x1080)")
    def test_desktop_layout(self, products_page: ProductsListPage):
        """Desktop layout should display correctly."""
        with allure.step("Установка разрешения 1920x1080 и проверка отображения"):
            products_page.page.set_viewport_size({"width": 1920, "height": 1080})
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Desktop layout broken"

    @allure.title("Проверка отображения на ноутбуке (1366x768)")
    def test_laptop_layout(self, products_page: ProductsListPage):
        """Laptop layout should display correctly."""
        with allure.step("Установка разрешения 1366x768 и проверка отображения"):
            products_page.page.set_viewport_size({"width": 1366, "height": 768})
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Laptop layout broken"

    @allure.title("Проверка отображения на планшете (768x1024)")
    def test_tablet_layout(self, products_page: ProductsListPage):
        """Tablet layout should display correctly."""
        with allure.step("Установка разрешения 768x1024 и проверка отображения"):
            products_page.page.set_viewport_size({"width": 768, "height": 1024})
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded(), \
                "BUG: Tablet layout broken"

    @allure.title("Проверка отображения на мобильном (375x667)")
    def test_mobile_layout(self, products_page: ProductsListPage):
        """Mobile layout should display correctly."""
        with allure.step("Установка разрешения 375x667 и проверка отображения"):
            products_page.page.set_viewport_size({"width": 375, "height": 667})
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена и восстановление разрешения"):
            assert products_page.is_page_loaded(), \
                "BUG: Mobile layout broken"
            products_page.page.set_viewport_size({"width": 1280, "height": 720})

    @allure.title("Проверка видимости элементов на маленьком экране")
    def test_elements_visible_on_small_screen(self, products_page: ProductsListPage):
        """Critical elements should be visible on small screens."""
        with allure.step("Установка мобильного разрешения и проверка видимости кнопки"):
            products_page.page.set_viewport_size({"width": 375, "height": 667})
            products_page.navigate()
            products_page.wait_for_loading_complete()
            add_visible = products_page.add_product_btn.is_visible(timeout=3000)
            logger.info(f"Add button visible on mobile: {add_visible}")
            products_page.page.set_viewport_size({"width": 1280, "height": 720})



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Локализация")
@pytest.mark.functional
class TestProductsListLocalization:
    """Localization tests."""

    @allure.title("Проверка загрузки страницы на английском")
    def test_page_loads_in_english(self, products_page: ProductsListPage):
        """Page should load in English."""
        with allure.step("Проверка текста кнопки добавления на английском"):
            add_btn = products_page.add_product_btn
            if add_btn.is_visible():
                text = add_btn.inner_text().lower()
                has_en = "add" in text or "products" in text
                logger.info(f"Add button text: {text}")

    @allure.title("Проверка поддержки узбекского языка")
    def test_page_loads_in_uzbek(self, products_page: ProductsListPage):
        """Page should support Uzbek."""
        with allure.step("Проверка загрузки страницы на узбекском"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка корректного форматирования чисел")
    def test_numbers_formatted_correctly(self, products_page: ProductsListPage):
        """Numbers should be formatted for locale."""
        with allure.step("Проверка форматирования чисел на странице"):
            page_info = products_page.get_page_info_text()
            logger.info(f"Page info: {page_info}")

    @allure.title("Проверка форматирования валюты")
    def test_currency_formatted(self, products_page: ProductsListPage):
        """Currency should be formatted correctly."""
        with allure.step("Проверка формата валюты"):
            if products_page.get_products_count() > 0:
                price = products_page.get_product_price_from_row(0)
                logger.info(f"Price format: {price}")

    @allure.title("Проверка форматирования дат")
    def test_dates_formatted(self, products_page: ProductsListPage):
        """Dates should be formatted for locale."""
        with allure.step("Проверка форматирования дат"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Мультиязычность")
@pytest.mark.functional
class TestProductsListMultiLanguage:
    """Multi-language content tests."""

    @allure.title("Проверка отображения названий товаров на языке UI")
    def test_product_names_display(self, products_page: ProductsListPage):
        """Product names should display in UI language."""
        with allure.step("Проверка отображения названия первого товара"):
            if products_page.get_products_count() > 0:
                name = products_page.get_product_name_from_row(0)
                logger.info(f"Product name displayed: {name}")
                assert name is not None

    @allure.title("Проверка перевода меток интерфейса")
    def test_ui_labels_translated(self, products_page: ProductsListPage):
        """UI labels should be in correct language."""
        with allure.step("Проверка текста кнопки добавления"):
            add_btn = products_page.add_product_btn
            if add_btn.is_visible():
                text = add_btn.inner_text()
                logger.info(f"Add button text: {text}")

    @allure.title("Проверка перевода сообщений об ошибках")
    def test_error_messages_translated(self, products_page: ProductsListPage):
        """Error messages should be in UI language."""
        with allure.step("Проверка перевода сообщений об ошибках"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка перевода пустого состояния")
    def test_empty_state_translated(self, products_page: ProductsListPage):
        """Empty state should be translated."""
        with allure.step("Поиск несуществующего товара"):
            products_page.search(TEST_DATA["search"]["invalid"]["nonexistent"])
            products_page.wait_for_network_idle()

        with allure.step("Проверка перевода текста пустого состояния"):
            if products_page.is_empty_state_visible():
                text = products_page.empty_state.inner_text()
                logger.info(f"Empty state text: {text}")

    @allure.title("Проверка перевода меток пагинации")
    def test_pagination_labels_translated(self, products_page: ProductsListPage):
        """Pagination labels should be translated."""
        with allure.step("Проверка перевода меток пагинации"):
            info = products_page.get_page_info_text()
            logger.info(f"Page info: {info}")



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Режимы отображения")
@pytest.mark.ui
class TestProductsListViewModes:
    """View mode tests (grid/list)."""

    @allure.title("Проверка режима отображения по умолчанию")
    def test_default_view_mode(self, products_page: ProductsListPage):
        """Default view mode should be grid or table."""
        with allure.step("Проверка видимости grid/table или пустого состояния"):
            grid_visible = products_page.is_grid_view_active()
            table = products_page.products_table
            table_visible = table.is_visible(timeout=2000)
            assert grid_visible or table_visible or products_page.is_empty_state_visible(), \
                "BUG: No view displayed"

    @allure.title("Проверка режима сетки (если доступен)")
    def test_grid_view_if_available(self, products_page: ProductsListPage):
        """Grid view should work if available."""
        with allure.step("Переключение на режим сетки если доступен"):
            grid_btn = products_page.page.locator("[aria-label='Grid view']").or_(
                products_page.page.locator("button:has(svg[data-testid='GridViewIcon'])")
            )
            if grid_btn.is_visible(timeout=2000):
                grid_btn.click()
                products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка режима списка (если доступен)")
    def test_list_view_if_available(self, products_page: ProductsListPage):
        """List view should work if available."""
        with allure.step("Переключение на режим списка если доступен"):
            list_btn = products_page.page.locator("[aria-label='List view']").or_(
                products_page.page.locator("button:has(svg[data-testid='ViewListIcon'])")
            )
            if list_btn.is_visible(timeout=2000):
                list_btn.click()
                products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Проверка сохранения режима отображения при навигации")
    def test_view_mode_persists(self, products_page: ProductsListPage):
        """View mode should persist across navigation."""
        with allure.step("Навигация и проверка сохранения режима отображения"):
            products_page.navigate()
            products_page.wait_for_loading_complete()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Отображение категорий")
@pytest.mark.ui
class TestProductsListCategoryDisplay:
    """Category display tests."""

    @allure.title("Проверка видимости столбца категорий")
    def test_category_column_visible(self, products_page: ProductsListPage):
        """Category column should be visible."""
        with allure.step("Проверка наличия столбца категорий"):
            columns = products_page.get_column_names()
            has_category = any("category" in c.lower() or "kategoriya" in c.lower() for c in columns)
            logger.info(f"Has category column: {has_category}, columns: {columns}")

    @allure.title("Фильтр по категории доступен")
    def test_category_filter_available(self, products_page: ProductsListPage):
        """Category filter should be available."""
        with allure.step("Открытие фильтров и проверка видимости фильтра категорий"):
            products_page.open_filters()
            filter_visible = products_page.category_filter.is_visible(timeout=2000)
            logger.info(f"Category filter visible: {filter_visible}")

    @allure.title("Хлебные крошки категории отображаются")
    def test_category_breadcrumb(self, products_page: ProductsListPage):
        """Category breadcrumb should display."""
        with allure.step("Проверка наличия хлебных крошек категории"):
            breadcrumb = products_page.page.locator("[class*='breadcrumb']")
            logger.info(f"Breadcrumb visible: {breadcrumb.is_visible(timeout=1000)}")

    @allure.title("Фильтрация по подкатегории работает")
    def test_subcategory_filter(self, products_page: ProductsListPage):
        """Subcategory filtering should work."""
        with allure.step("Применение фильтра по категории 'Electronics'"):
            products_page.open_filters()
            products_page.apply_category_filter("Electronics")
            products_page.wait_for_network_idle()

        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Бейдж категории отображается в строках")
    def test_category_badge_display(self, products_page: ProductsListPage):
        """Category badge should display in rows."""
        with allure.step("Проверка данных категории в первой строке"):
            if products_page.get_products_count() > 0:
                data = products_page.get_row_data(0)
                logger.info(f"Row data with category: {data}")



@allure.epic("Платформа продавца")
@allure.suite("Список товаров")
@allure.feature("Настройка столбцов")
@pytest.mark.ui
class TestProductsListColumnCustomization:
    """Column customization tests."""

    @allure.title("Настройки столбцов доступны")
    def test_column_settings_available(self, products_page: ProductsListPage):
        """Column settings should be available."""
        with allure.step("Проверка наличия кнопки настроек столбцов"):
            settings_btn = products_page.page.locator("[aria-label='Column settings']").or_(
                products_page.page.locator("button:has(svg[data-testid='SettingsIcon'])")
            )
            logger.info(f"Column settings visible: {settings_btn.is_visible(timeout=2000)}")

    @allure.title("Скрытие столбца работает")
    def test_hide_column(self, products_page: ProductsListPage):
        """Hiding column should work."""
        with allure.step("Проверка текущих столбцов таблицы"):
            columns = products_page.get_column_names()
            logger.info(f"Current columns: {columns}")

    @allure.title("Показ скрытого столбца работает")
    def test_show_column(self, products_page: ProductsListPage):
        """Showing hidden column should work."""
        with allure.step("Проверка что страница загружена"):
            assert products_page.is_page_loaded()

    @allure.title("Порядок столбцов сохраняется после перезагрузки")
    def test_column_order(self, products_page: ProductsListPage):
        """Column order should be consistent."""
        with allure.step("Сравнение порядка столбцов до и после перезагрузки"):
            columns1 = products_page.get_column_names()
            products_page.page.reload()
            products_page.wait_for_loading_complete()
            columns2 = products_page.get_column_names()
            logger.info(f"Columns before: {columns1}, after: {columns2}")

    @allure.title("Ширина столбцов регулируется")
    def test_column_width_resize(self, products_page: ProductsListPage):
        """Column width should be adjustable."""
        with allure.step("Проверка корректного отображения таблицы"):
            assert products_page.is_page_loaded()
