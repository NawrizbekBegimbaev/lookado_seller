"""
Orders page object for managing orders.
Follows Page Object Model (POM) and SOLID principles.

URL: /dashboard/orders-management/orders?page=1&size=10
"""

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage, logger


class OrdersPage(BasePage):
    """
    Page Object Model for Orders Management Page.
    Handles order listing, search, filtering, status tabs, and details viewing.
    """

    ORDERS_PATH = "/dashboard/orders-management/orders"
    DEFAULT_PARAMS = "?page=1&size=10"

    # Status tab names (English -> Uzbek -> Russian mapping)
    STATUS_TABS_EN = [
        "All", "Awaiting Payment", "Processing", "Delivering",
        "Delivered", "Cancelled", "Failed", "Refunded",
        "Picking", "Packed", "Shipping", "Shipped to Courier", "Expired"
    ]
    STATUS_TABS_UZ = [
        "Hammasi", "To'lovni kutmoqda", "Tayyorlanmoqda", "Yetkazilmoqda",
        "Topshirildi", "Bekor qilindi", "Muvaffaqiyatsiz", "Qaytarildi",
        "Yig'ilmoqda", "Qadoqlandi", "Yetkazib berishda", "Kuryerga topshirildi", "Muddati o'tdi"
    ]
    STATUS_TABS_RU = [
        "Все", "Ожидает оплаты", "Обрабатывается", "Доставляется",
        "Доставлено", "Отменено", "Неудачно", "Возврат",
        "Сборка", "Упакован", "Доставка", "Передан курьеру", "Истёк"
    ]
    # Combined for compatibility
    STATUS_TABS = STATUS_TABS_EN + STATUS_TABS_UZ + STATUS_TABS_RU

    # EN to RU mapping for click_tab (Uzbek with apostrophes handled separately)
    TAB_NAME_MAP = {
        "All": ["Hammasi", "Все"],
        "Awaiting Payment": ["Ожидает оплаты"],  # UZ: "To'lovni kutmoqda" has apostrophe
        "Processing": ["Tayyorlanmoqda", "Обрабатывается"],
        "Delivering": ["Yetkazilmoqda", "Доставляется"],
        "Delivered": ["Topshirildi", "Доставлено"],
        "Cancelled": ["Bekor qilindi", "Отменено"],
        "Failed": ["Muvaffaqiyatsiz", "Неудачно"],
        "Refunded": ["Qaytarildi", "Возврат"],
        "Picking": ["Сборка"],  # UZ: "Yig'ilmoqda" has apostrophe
        "Packed": ["Qadoqlandi", "Упакован"],
        "Shipping": ["Yetkazib berishda", "Доставка"],
        "Shipped to Courier": ["Kuryerga topshirildi", "Передан курьеру"],
        "Expired": ["Истёк"],  # UZ: "Muddati o'tdi" has apostrophe
    }

    # Widget names (English, Uzbek, Russian)
    WIDGET_NAMES = [
        "Ordering", "Pending payment", "Picking", "Issued", "Delivering",
        "Rasmiylashtirilmoqda", "To'lovni kutmoqda", "Yig'ilmoqda", "Topshirildi", "Yetkazilmoqda",
        "Оформляется", "Ожидает оплаты", "Сборка", "Выдано", "Доставляется"
    ]

    # EN to RU/UZ widget name mapping (using partial matches to avoid apostrophe issues)
    WIDGET_NAME_MAP = {
        "Ordering": ["Rasmiylashtirilmoqda", "Оформляется"],
        "Pending payment": ["lovni kutmoqda", "Ожидает оплаты"],  # Partial match for "To'lovni kutmoqda"
        "Picking": ["ilmoqda", "Сборка"],  # Partial match for "Yig'ilmoqda"
        "Issued": ["Topshirildi", "Выдано"],
        "Delivering": ["Yetkazilmoqda", "Доставляется"],
    }

    def __init__(self, page: Page):
        """Initialize orders page with locators."""
        super().__init__(page)

    # ===============================
    # Locators (Properties)
    # ===============================

    @property
    def page_title(self) -> Locator:
        """Page title 'Orders' heading (EN/RU/UZ)."""
        return self.page.get_by_role("heading", name="Orders").or_(
            self.page.get_by_role("heading", name="Заказы")
        ).or_(
            self.page.get_by_role("heading", name="Buyurtmalar")
        ).first

    @property
    def search_input(self) -> Locator:
        """Search input field (multi-language: EN/RU/UZ)."""
        return self.page.locator("input[name='query']").or_(
            self.page.locator("input[placeholder*='Search']")
        ).or_(
            self.page.locator("input[placeholder*='Поиск']")
        ).or_(
            self.page.locator("input[placeholder*='Qidirish']")
        )

    @property
    def date_from_input(self) -> Locator:
        """Date from filter - MUI DatePicker hidden input (name=startAt)."""
        return self.page.locator("input[name='startAt']")

    @property
    def date_from_group(self) -> Locator:
        """Date from filter - visible group container."""
        return self.page.locator("input[name='startAt']").locator("..")

    @property
    def date_to_input(self) -> Locator:
        """Date to filter - MUI DatePicker hidden input (name=endAt)."""
        return self.page.locator("input[name='endAt']")

    @property
    def date_to_group(self) -> Locator:
        """Date to filter - visible group container."""
        return self.page.locator("input[name='endAt']").locator("..")

    @property
    def data_grid(self) -> Locator:
        """MUI DataGrid container."""
        return self.page.locator(".MuiDataGrid-root, [role='grid']").first

    @property
    def grid_rows(self) -> Locator:
        """DataGrid rows."""
        return self.page.locator(".MuiDataGrid-row, [role='row']:not([class*='header'])")

    @property
    def empty_state(self) -> Locator:
        """Empty state message when no orders."""
        return self.page.locator(
            ":text('Данные отсутствуют')"
        ).or_(self.page.locator(":text('No data')"))

    @property
    def pagination(self) -> Locator:
        """Pagination container."""
        return self.page.locator(".MuiPagination-root").or_(
            self.page.locator(".MuiTablePagination-root")
        )

    @property
    def rows_per_page_select(self) -> Locator:
        """Rows per page selector (MUI combobox)."""
        return self.page.locator(
            ".MuiSelect-select.MuiTablePagination-select"
        )

    @property
    def pagination_display_text(self) -> Locator:
        """Pagination display text (e.g. '0-0 of 0')."""
        return self.page.locator(".MuiTablePagination-displayedRows")

    @property
    def next_page_btn(self) -> Locator:
        """Next page button."""
        return self.page.locator(
            "button[aria-label='Go to next page']"
        ).or_(self.page.get_by_role("button", name="Go to next page"))

    @property
    def prev_page_btn(self) -> Locator:
        """Previous page button."""
        return self.page.locator(
            "button[aria-label='Go to previous page']"
        ).or_(self.page.get_by_role("button", name="Go to previous page"))

    # NOTE: Seller Instructions and Chat with Support buttons do not exist on this page

    @property
    def widgets_section(self) -> Locator:
        """Widgets section heading (multi-language: EN/RU/UZ)."""
        return self.page.locator("h6:text('Widgets')").or_(
            self.page.locator("h6:text('Виджеты')")
        ).or_(
            self.page.locator("h6:text('Vidjetlar')")
        ).first

    # ===============================
    # Navigation Methods
    # ===============================

    def navigate(self) -> None:
        """Navigate to orders page."""
        logger.info("Navigating to orders page...")
        self.navigate_to(f"{self.ORDERS_PATH}{self.DEFAULT_PARAMS}")
        self.wait_for_page_load()
        logger.info("Orders page loaded")

    def navigate_via_sidebar(self) -> None:
        """Navigate to orders page via sidebar menu."""
        logger.info("Navigating to orders via sidebar...")
        orders_menu = self.page.locator(":text('Orders and Returns')").first
        if orders_menu.is_visible(timeout=3000):
            orders_menu.click()
            self.page.wait_for_load_state("domcontentloaded")

            orders_link = self.page.locator(
                "a:has-text('Orders'):not(:has-text('Returns')):not(:has-text('and'))"
            ).first
            if orders_link.is_visible(timeout=2000):
                orders_link.click()
                self.page.wait_for_load_state("networkidle")
        logger.info("Navigated to orders via sidebar")

    def is_page_loaded(self) -> bool:
        """Check if orders page is loaded."""
        return (
            "orders-management/orders" in self.page.url
            or self.data_grid.is_visible(timeout=5000)
            or self.empty_state.is_visible(timeout=3000)
        )

    # ===============================
    # Widget Methods
    # ===============================

    def get_widget_cards(self) -> list:
        """Get all widget card elements."""
        return self.page.locator(
            ".MuiCard-root, .MuiPaper-root"
        ).filter(has=self.page.locator("h6")).all()

    def get_widget_value(self, widget_name: str) -> str:
        """Get value of a specific widget card (supports EN/RU/UZ)."""
        card = self.page.locator(f":has-text('{widget_name}')").filter(
            has=self.page.locator("h6")
        ).first
        if card.is_visible(timeout=2000):
            text = card.text_content(timeout=1000)
            return text or ""
        # Try alternative names from mapping
        alt_names = self.WIDGET_NAME_MAP.get(widget_name, [])
        for alt_name in alt_names:
            card = self.page.locator(f":has-text('{alt_name}')").filter(
                has=self.page.locator("h6")
            ).first
            if card.is_visible(timeout=1000):
                text = card.text_content(timeout=1000)
                return text or ""
        return ""

    def is_widgets_section_visible(self) -> bool:
        """Check if widgets section is visible."""
        return self.widgets_section.is_visible(timeout=3000)

    # ===============================
    # Tab Methods
    # ===============================

    def get_status_tabs(self) -> list:
        """Get all status tab elements."""
        return self.page.locator("[role='tab'], .MuiTab-root, button[class*='tab']").all()

    def get_tab_names(self) -> list:
        """Get names of all status tabs."""
        tabs = self.get_status_tabs()
        names = []
        for tab in tabs:
            try:
                text = tab.text_content(timeout=500)
                if text and text.strip():
                    names.append(text.strip())
            except Exception:
                pass
        return names

    def click_tab(self, tab_name: str) -> None:
        """Click on a specific status tab (supports EN/RU/UZ)."""
        logger.info(f"Clicking tab: {tab_name}")
        # Try using get_by_role with .first to handle multiple matches
        tab = self.page.get_by_role("tab", name=tab_name).first
        if tab.is_visible(timeout=2000):
            tab.click()
            self.page.wait_for_load_state("networkidle")
            return

        # Try alternative names from mapping (Russian first, more reliable)
        alt_names = self.TAB_NAME_MAP.get(tab_name, [])
        for alt_name in alt_names:
            tab = self.page.get_by_role("tab", name=alt_name).first
            if tab.is_visible(timeout=1000):
                tab.click()
                self.page.wait_for_load_state("networkidle")
                return

        # Fallback: try by index based on position
        tabs = self.get_status_tabs()
        for i, t in enumerate(tabs):
            text = t.text_content(timeout=500) or ""
            if tab_name.lower() in text.lower():
                t.click()
                self.page.wait_for_load_state("networkidle")
                return

        logger.warning(f"Tab '{tab_name}' not found, clicking first visible tab")
        if tabs:
            tabs[0].click()
            self.page.wait_for_load_state("networkidle")

    def get_active_tab(self) -> str:
        """Get currently active tab name."""
        active = self.page.locator(
            "[role='tab'][aria-selected='true'], .Mui-selected"
        ).first
        if active.is_visible(timeout=2000):
            return active.text_content(timeout=1000) or ""
        return ""

    def get_tab_count(self) -> int:
        """Get number of status tabs."""
        return len(self.get_status_tabs())

    # ===============================
    # Search Methods
    # ===============================

    def search_order(self, search_text: str) -> None:
        """Search for order by text."""
        logger.info(f"Searching for: {search_text}")
        self.search_input.wait_for(state="visible", timeout=5000)
        self.search_input.fill(search_text)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("networkidle")

    def clear_search(self) -> None:
        """Clear search input."""
        logger.info("Clearing search...")
        self.search_input.fill("")
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("networkidle")

    def get_search_value(self) -> str:
        """Get current search input value."""
        return self.search_input.input_value(timeout=2000)

    def is_search_visible(self) -> bool:
        """Check if search input is visible."""
        return self.search_input.is_visible(timeout=3000)

    # ===============================
    # Date Filter Methods
    # ===============================

    def set_date_from(self, date_str: str) -> None:
        """Set date from filter via MUI DatePicker hidden input."""
        logger.info(f"Setting date from: {date_str}")
        self.page.evaluate(
            """(value) => {
                const input = document.querySelector('input[name="startAt"]');
                if (input) {
                    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                        window.HTMLInputElement.prototype, 'value').set;
                    nativeInputValueSetter.call(input, value);
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }""", date_str
        )
        self.page.wait_for_load_state("domcontentloaded")

    def set_date_to(self, date_str: str) -> None:
        """Set date to filter via MUI DatePicker hidden input."""
        logger.info(f"Setting date to: {date_str}")
        self.page.evaluate(
            """(value) => {
                const input = document.querySelector('input[name="endAt"]');
                if (input) {
                    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                        window.HTMLInputElement.prototype, 'value').set;
                    nativeInputValueSetter.call(input, value);
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }""", date_str
        )
        self.page.wait_for_load_state("domcontentloaded")

    def set_date_range(self, date_from: str, date_to: str) -> None:
        """Set both date from and date to filters."""
        self.set_date_from(date_from)
        self.set_date_to(date_to)

    def is_date_from_visible(self) -> bool:
        """Check if date from picker is visible (group container)."""
        return self.date_from_group.is_visible(timeout=3000)

    def is_date_to_visible(self) -> bool:
        """Check if date to picker is visible (group container)."""
        return self.date_to_group.is_visible(timeout=3000)

    # ===============================
    # Grid/Table Methods
    # ===============================

    def get_orders_count(self) -> int:
        """Get number of orders in the grid."""
        self.page.wait_for_load_state("domcontentloaded")
        return self.grid_rows.count()

    def is_data_grid_visible(self) -> bool:
        """Check if DataGrid is visible."""
        return self.data_grid.is_visible(timeout=5000)

    def is_empty_state_visible(self) -> bool:
        """Check if empty state message is visible."""
        return self.empty_state.is_visible(timeout=3000)

    def get_column_headers(self) -> list:
        """Get DataGrid column header texts."""
        headers = self.page.locator(
            ".MuiDataGrid-columnHeaderTitle, [role='columnheader']"
        ).all()
        texts = []
        for h in headers:
            try:
                text = h.text_content(timeout=500)
                if text and text.strip():
                    texts.append(text.strip())
            except Exception:
                pass
        return texts

    def click_order_row(self, index: int = 0) -> None:
        """Click on order row to view details."""
        logger.info(f"Clicking order row {index}...")
        row = self.grid_rows.nth(index)
        row.wait_for(state="visible", timeout=3000)
        row.click()
        self.page.wait_for_load_state("networkidle")

    def get_pagination_text(self) -> str:
        """Get pagination display text."""
        if self.pagination_display_text.is_visible(timeout=2000):
            return self.pagination_display_text.text_content(timeout=1000) or ""
        return ""

    def is_pagination_visible(self) -> bool:
        """Check if pagination is visible."""
        return self.pagination.is_visible(timeout=3000)

    def get_rows_per_page(self) -> str:
        """Get current rows per page value."""
        if self.rows_per_page_select.is_visible(timeout=2000):
            return self.rows_per_page_select.text_content(timeout=1000) or ""
        return ""

    def go_to_next_page(self) -> None:
        """Go to next page in pagination."""
        if self.next_page_btn.is_enabled(timeout=2000):
            self.next_page_btn.click()
            self.page.wait_for_load_state("networkidle")

    def go_to_prev_page(self) -> None:
        """Go to previous page in pagination."""
        if self.prev_page_btn.is_enabled(timeout=2000):
            self.prev_page_btn.click()
            self.page.wait_for_load_state("networkidle")

    # ===============================
    # Validation Methods (MUI)
    # ===============================

    def get_validation_error_count(self) -> int:
        """Get count of MUI validation errors."""
        return self.page.locator(".MuiFormHelperText-root.Mui-error").count()

    def has_validation_errors(self) -> bool:
        """Check if form has validation errors."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """Get all error messages."""
        messages = []
        errors = self.page.locator(".MuiFormHelperText-root.Mui-error")
        for i in range(errors.count()):
            try:
                text = errors.nth(i).inner_text(timeout=1000)
                if text.strip():
                    messages.append(text.strip())
            except Exception:
                pass
        return messages

