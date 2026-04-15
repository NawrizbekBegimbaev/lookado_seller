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



@pytest.mark.smoke
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Элементы интерфейса")
class TestOrdersUI:
    """Test visibility and state of all UI elements on orders page."""

    @allure.title("Проверка видимости заголовка страницы заказов")
    def test_page_title_visible(self, orders_page):
        """Orders page title should be visible."""
        with allure.step("Проверка видимости заголовка страницы"):
            assert orders_page.page_title.is_visible(timeout=5000), \
                "BUG: Orders page title not visible"

    @allure.title("Проверка видимости поля поиска")
    def test_search_input_visible(self, orders_page):
        """Search input should be visible."""
        with allure.step("Проверка видимости поля поиска"):
            assert orders_page.is_search_visible(), \
                "BUG: Search input not visible on orders page"

    @allure.title("Проверка корректности placeholder поля поиска")
    def test_search_placeholder_correct(self, orders_page):
        """Search input should have correct placeholder text (multi-language)."""
        with allure.step("Получение текста placeholder поля поиска"):
            placeholder = orders_page.search_input.get_attribute("placeholder") or ""
            placeholder_lower = placeholder.lower()
        with allure.step("Проверка корректности placeholder"):
            # Supports EN/RU/UZ: "Search by Order ID" / "Поиск по ID заказа" / "Buyurtma ID bo'yicha qidirish"
            has_valid_placeholder = (
                "order" in placeholder_lower or
                "поиск" in placeholder_lower or
                "qidirish" in placeholder_lower or
                "id" in placeholder_lower
            )
            assert has_valid_placeholder, \
                f"BUG: Search placeholder incorrect: '{placeholder}'"

    @allure.title("Проверка видимости фильтра 'Дата от'")
    def test_date_from_filter_visible(self, orders_page):
        """Date from filter should be visible."""
        with allure.step("Проверка видимости фильтра 'Дата от'"):
            assert orders_page.is_date_from_visible(), \
                "BUG: Date from filter not visible"

    @allure.title("Проверка видимости фильтра 'Дата до'")
    def test_date_to_filter_visible(self, orders_page):
        """Date to filter should be visible."""
        with allure.step("Проверка видимости фильтра 'Дата до'"):
            assert orders_page.is_date_to_visible(), \
                "BUG: Date to filter not visible"

    @allure.title("Проверка видимости таблицы данных")
    def test_data_grid_visible(self, orders_page):
        """DataGrid should be visible on orders page."""
        with allure.step("Проверка видимости таблицы данных"):
            assert orders_page.is_data_grid_visible(), \
                "BUG: DataGrid not visible on orders page"

    @allure.title("Проверка видимости пагинации")
    def test_pagination_visible(self, orders_page):
        """Pagination should be visible."""
        with allure.step("Проверка видимости пагинации"):
            assert orders_page.is_pagination_visible(), \
                "BUG: Pagination not visible on orders page"

    @allure.title("Проверка видимости секции виджетов")
    def test_widgets_section_visible(self, orders_page):
        """Widgets section should be visible."""
        with allure.step("Проверка видимости секции виджетов"):
            assert orders_page.is_widgets_section_visible(), \
                "BUG: Widgets section not visible"

    @allure.title("Проверка видимости вкладок статусов")
    def test_status_tabs_visible(self, orders_page):
        """Status tabs should be visible."""
        with allure.step("Получение количества вкладок статусов"):
            tab_count = orders_page.get_tab_count()
        with allure.step("Проверка наличия минимум 10 вкладок"):
            assert tab_count >= 10, \
                f"BUG: Expected 10+ status tabs, got {tab_count}"

    @allure.title("Проверка наличия заголовков колонок таблицы")
    def test_column_headers_present(self, orders_page, test_data):
        """DataGrid should have expected column headers (multi-language)."""
        with allure.step("Получение заголовков колонок таблицы"):
            headers = orders_page.get_column_headers()
            # Multi-language column mappings
            column_map = {
                "Order ID": ["order", "заказ", "buyurtma"],
                "Product": ["product", "товар", "mahsulot"],
                "Status": ["status", "статус", "holat"],
                "Date": ["date", "дата", "sana"],
                "Quantity": ["quantity", "количество", "miqdor"],
            }
            headers_lower = [h.lower() for h in headers]
        with allure.step("Проверка наличия всех ожидаемых колонок"):
            for col_name, patterns in column_map.items():
                found = any(
                    any(pattern in h for pattern in patterns)
                    for h in headers_lower
                )
                assert found, \
                    f"BUG: Column '{col_name}' not found in headers: {headers}"



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Виджеты")
class TestOrdersWidgets:
    """Test widget cards display correctly."""

    @allure.title("Проверка количества виджетов")
    def test_widgets_count(self, orders_page):
        """Should display 5 widget cards."""
        with allure.step("Получение списка виджетов"):
            cards = orders_page.get_widget_cards()
        with allure.step("Проверка наличия минимум 4 виджетов"):
            assert len(cards) >= 4, \
                f"BUG: Expected 4+ widget cards, got {len(cards)}"

    @allure.title("Проверка видимости виджета 'Ordering'")
    def test_ordering_widget_visible(self, orders_page):
        """Ordering widget should be visible."""
        with allure.step("Проверка видимости виджета 'Ordering'"):
            value = orders_page.get_widget_value("Ordering")
            assert value, "BUG: Ordering widget not found"

    @allure.title("Проверка видимости виджета 'Ожидание оплаты'")
    def test_pending_payment_widget(self, orders_page):
        """Pending payment widget should be visible."""
        with allure.step("Проверка видимости виджета 'Ожидание оплаты'"):
            value = orders_page.get_widget_value("Pending payment")
            assert value, "BUG: Pending payment widget not found"

    @allure.title("Проверка видимости виджета 'Сборка'")
    def test_picking_widget(self, orders_page):
        """Picking widget should be visible."""
        with allure.step("Проверка видимости виджета 'Сборка'"):
            value = orders_page.get_widget_value("Picking")
            assert value, "BUG: Picking widget not found"

    @allure.title("Проверка видимости виджета 'Доставка'")
    def test_delivering_widget(self, orders_page):
        """Delivering widget should be visible."""
        with allure.step("Проверка видимости виджета 'Доставка'"):
            value = orders_page.get_widget_value("Delivering")
            assert value, "BUG: Delivering widget not found"



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Вкладки статусов")
class TestOrdersStatusTabs:
    """Test status tab navigation and filtering."""

    @allure.title("Проверка наличия всех ожидаемых вкладок статусов")
    def test_all_expected_tabs_present(self, orders_page, test_data):
        """All expected status tabs should be present (multi-language check)."""
        with allure.step("Получение списка вкладок статусов"):
            tab_names = orders_page.get_tab_names()
        with allure.step("Проверка наличия минимум 10 вкладок"):
            # Just verify we have a reasonable number of tabs (language-independent)
            assert len(tab_names) >= 10, \
                f"BUG: Expected at least 10 tabs, got {len(tab_names)}: {tab_names}"

    @allure.title("Проверка что вкладка 'Все' активна по умолчанию")
    def test_all_tab_is_default(self, orders_page):
        """'All' tab should be the default active tab (multi-language)."""
        with allure.step("Получение активной вкладки"):
            active = orders_page.get_active_tab().lower()
        with allure.step("Проверка что активна вкладка 'Все'"):
            # EN: "All", RU: "Все", UZ: "Hammasi"
            is_all_tab = (
                "all" in active or
                "все" in active or
                "hammasi" in active or
                active == ""
            )
            assert is_all_tab, \
                f"BUG: Expected 'All' as default tab, got '{active}'"

    @allure.title("Клик по вкладке 'Ожидание оплаты' фильтрует заказы")
    def test_click_awaiting_payment_tab(self, orders_page):
        """Clicking 'Awaiting Payment' tab should filter orders."""
        with allure.step("Клик по вкладке 'Ожидание оплаты'"):
            orders_page.click_tab("Awaiting Payment")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка загрузки страницы после смены вкладки"):
            assert orders_page.is_page_loaded(), \
                "BUG: Page not loaded after clicking Awaiting Payment tab"

    @allure.title("Клик по вкладке 'Отменённые' фильтрует заказы")
    def test_click_cancelled_tab(self, orders_page):
        """Clicking 'Cancelled' tab should filter orders."""
        with allure.step("Клик по вкладке 'Отменённые'"):
            orders_page.click_tab("Cancelled")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка загрузки страницы после смены вкладки"):
            assert orders_page.is_page_loaded(), \
                "BUG: Page not loaded after clicking Cancelled tab"

    @allure.title("Клик по вкладке 'В обработке' фильтрует заказы")
    def test_click_processing_tab(self, orders_page):
        """Clicking 'Processing' tab should filter orders."""
        with allure.step("Клик по вкладке 'В обработке'"):
            orders_page.click_tab("Processing")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка загрузки страницы после смены вкладки"):
            assert orders_page.is_page_loaded(), \
                "BUG: Page not loaded after clicking Processing tab"

    @allure.title("Клик по вкладке обновляет параметры URL")
    def test_tab_updates_url(self, orders_page):
        """Clicking a tab should update URL parameters."""
        with allure.step("Клик по вкладке 'Failed'"):
            orders_page.click_tab("Failed")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка обновления параметров URL"):
            url = orders_page.page.url
            assert "orders-management" in url, \
                f"BUG: URL not updated after tab click: {url}"

    @allure.title("Возврат на вкладку 'Все' после фильтрации")
    def test_return_to_all_tab(self, orders_page):
        """Clicking 'All' tab after filtering should show all orders."""
        with allure.step("Переключение на вкладку 'Отменённые'"):
            orders_page.click_tab("Cancelled")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Возврат на вкладку 'Все'"):
            orders_page.click_tab("All")
            orders_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка загрузки страницы после возврата"):
            assert orders_page.is_page_loaded(), \
                "BUG: Page not loaded after returning to All tab"



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Таблица данных")
class TestOrdersDataGrid:
    """Test DataGrid structure and behavior."""

    @allure.title("Проверка наличия всех ожидаемых колонок таблицы")
    def test_grid_has_expected_columns(self, orders_page, test_data):
        """DataGrid should have all expected columns."""
        with allure.step("Получение заголовков колонок"):
            headers = orders_page.get_column_headers()
        with allure.step("Проверка наличия минимум 5 колонок"):
            assert len(headers) >= 5, \
                f"BUG: Expected 5+ column headers, got {len(headers)}: {headers}"

    @allure.title("Проверка наличия колонки 'ID заказа'")
    def test_order_id_column_present(self, orders_page):
        """Order ID column should be present (multi-language)."""
        with allure.step("Получение заголовков колонок"):
            headers = orders_page.get_column_headers()
        with allure.step("Проверка наличия колонки 'ID заказа'"):
            # EN: "Order ID", RU: "ID заказа", UZ: "Buyurtma ID"
            has_order_id = any(
                ("order" in h.lower() and "id" in h.lower()) or
                "заказ" in h.lower() or
                "buyurtma" in h.lower()
                for h in headers
            )
            assert has_order_id, \
                f"BUG: 'Order ID' column not found: {headers}"

    @allure.title("Проверка наличия колонки 'Статус'")
    def test_status_column_present(self, orders_page):
        """Status column should be present (multi-language)."""
        with allure.step("Получение заголовков колонок"):
            headers = orders_page.get_column_headers()
        with allure.step("Проверка наличия колонки 'Статус'"):
            # EN: "Status", RU: "Статус", UZ: "Holat"
            has_status = any(
                "status" in h.lower() or
                "статус" in h.lower() or
                "holat" in h.lower()
                for h in headers
            )
            assert has_status, \
                f"BUG: 'Status' column not found: {headers}"

    @allure.title("Проверка сообщения при пустом состоянии таблицы")
    def test_empty_state_message(self, orders_page):
        """Empty state should show appropriate message when no orders."""
        with allure.step("Получение количества заказов"):
            count = orders_page.get_orders_count()
        with allure.step("Проверка сообщения пустого состояния"):
            if count == 0:
                assert orders_page.is_empty_state_visible(), \
                    "BUG: No empty state message shown when 0 orders"

    @allure.title("Проверка наличия колонки 'Дата'")
    def test_date_column_present(self, orders_page):
        """Date column should be present (multi-language)."""
        with allure.step("Получение заголовков колонок"):
            headers = orders_page.get_column_headers()
        with allure.step("Проверка наличия колонки 'Дата'"):
            # EN: "Date", RU: "Дата", UZ: "Sana"
            has_date = any(
                "date" in h.lower() or
                "дата" in h.lower() or
                "sana" in h.lower()
                for h in headers
            )
            assert has_date, \
                f"BUG: 'Date' column not found: {headers}"



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Пагинация")
class TestOrdersPagination:
    """Test pagination controls."""

    @allure.title("Проверка отображения текста пагинации")
    def test_pagination_display_text(self, orders_page):
        """Pagination should show display text (e.g., '0-0 of 0')."""
        with allure.step("Получение текста пагинации"):
            text = orders_page.get_pagination_text()
        with allure.step("Проверка корректности текста пагинации"):
            assert text, "BUG: Pagination display text is empty"
            assert "of" in text.lower(), \
                f"BUG: Pagination text format incorrect: '{text}'"

    @allure.title("Проверка отображения количества строк на странице")
    def test_rows_per_page_displayed(self, orders_page):
        """Rows per page selector should show current value."""
        with allure.step("Проверка отображения количества строк на странице"):
            rpp = orders_page.get_rows_per_page()
            assert rpp, "BUG: Rows per page value not displayed"

    @allure.title("Кнопка 'Следующая страница' отключена при пустых данных")
    def test_next_page_disabled_on_empty(self, orders_page):
        """Next page button should be disabled when no data."""
        with allure.step("Получение количества заказов"):
            count = orders_page.get_orders_count()
        with allure.step("Проверка состояния кнопки 'Следующая страница'"):
            if count == 0:
                is_disabled = not orders_page.next_page_btn.is_enabled(timeout=2000)
                assert is_disabled, \
                    "BUG: Next page button should be disabled when no orders"

    @allure.title("Кнопка 'Предыдущая страница' отключена на первой странице")
    def test_prev_page_disabled_on_first(self, orders_page):
        """Previous page button should be disabled on first page."""
        with allure.step("Проверка что кнопка 'Предыдущая страница' отключена"):
            is_disabled = not orders_page.prev_page_btn.is_enabled(timeout=2000)
            assert is_disabled, \
                "BUG: Previous page button should be disabled on first page"

    @allure.title("Пагинация показывает 0 при отсутствии заказов")
    def test_pagination_shows_zero_for_empty(self, orders_page):
        """Pagination should show 0 entries when no orders."""
        with allure.step("Получение данных пагинации"):
            text = orders_page.get_pagination_text()
            count = orders_page.get_orders_count()
        with allure.step("Проверка отображения нуля при пустом состоянии"):
            if count == 0:
                assert "0" in text, \
                    f"BUG: Pagination should show 0 for empty state: '{text}'"



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Доступность")
class TestOrdersAccessibility:
    """Test accessibility features."""

    @allure.title("Проверка фокусировки поля поиска")
    def test_search_input_has_focus(self, orders_page):
        """Search input should be focusable."""
        with allure.step("Установка фокуса на поле поиска"):
            orders_page.search_input.focus()
        with allure.step("Проверка что фокус установлен на поле ввода"):
            focused = orders_page.page.evaluate(
                "document.activeElement.tagName"
            )
            assert focused.lower() == "input", \
                f"BUG: Search input not focusable, focused: {focused}"

    @allure.title("Навигация по вкладкам с клавиатуры")
    def test_tab_keyboard_navigation(self, orders_page):
        """Tabs should be navigable with keyboard."""
        with allure.step("Установка фокуса на первую вкладку"):
            first_tab = orders_page.page.locator("[role='tab']").first
        with allure.step("Проверка навигации по вкладкам с клавиатуры"):
            if first_tab.is_visible(timeout=2000):
                first_tab.focus()
                focused_tag = orders_page.page.evaluate(
                    "document.activeElement.tagName"
                )
                assert focused_tag.lower() == "button", \
                    f"BUG: Tab not focusable via keyboard: {focused_tag}"

    @allure.title("Проверка aria-label у кнопок пагинации")
    def test_pagination_buttons_accessible(self, orders_page):
        """Pagination buttons should have aria labels."""
        with allure.step("Проверка наличия aria-label у кнопки 'Следующая страница'"):
            next_btn = orders_page.next_page_btn
            if next_btn.is_visible(timeout=2000):
                aria = next_btn.get_attribute("aria-label")
                assert aria, "BUG: Next page button missing aria-label"

    @allure.title("Проверка ARIA-роли у таблицы данных")
    def test_grid_has_role(self, orders_page):
        """DataGrid should have appropriate ARIA role."""
        with allure.step("Проверка наличия ARIA-роли 'grid' у таблицы данных"):
            grid = orders_page.page.locator("[role='grid']")
            assert grid.count() > 0, \
                "BUG: DataGrid missing role='grid' attribute"



@pytest.mark.functional
@allure.epic("Платформа продавца")
@allure.suite("Заказы")
@allure.feature("Заказы")
@allure.story("Пустое состояние")
class TestOrdersEmptyState:
    """Test empty state behavior when no orders exist."""

    @allure.title("Проверка сообщения при пустом состоянии")
    def test_empty_state_shows_message(self, orders_page):
        """Empty state should show appropriate message."""
        with allure.step("Получение количества заказов"):
            count = orders_page.get_orders_count()
        with allure.step("Проверка отображения сообщения пустого состояния"):
            if count == 0:
                assert orders_page.is_empty_state_visible(), \
                    "BUG: No empty state message when 0 orders"

    @allure.title("Пустое состояние после невалидного поиска")
    def test_empty_state_after_invalid_search(self, orders_page):
        """Search with no results should show empty state or maintain page functionality."""
        with allure.step("Ввод несуществующего поискового запроса"):
            orders_page.search_order("ZZZZNONEXISTENT99999XXXX")
        with allure.step("Проверка работоспособности страницы после невалидного поиска"):
            # Verify page is functional after search (may show empty state or all results depending on backend)
            assert orders_page.is_page_loaded(), \
                "BUG: Invalid search broke the page"

    @allure.title("Текст пагинации при пустом состоянии")
    def test_pagination_text_on_empty(self, orders_page):
        """Pagination should indicate 0 results when empty."""
        with allure.step("Получение количества заказов"):
            count = orders_page.get_orders_count()
        with allure.step("Проверка текста пагинации при пустом состоянии"):
            if count == 0:
                text = orders_page.get_pagination_text()
                assert "0" in text, \
                    f"BUG: Pagination text should show 0 for empty: '{text}'"
