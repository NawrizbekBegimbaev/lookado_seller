"""
Returns page object for managing returns (Qaytarishlar).
Follows Page Object Model (POM) and SOLID principles.

URL: /dashboard/orders-management/returns?page=1&size=10

Page Structure (verified 2026-01-25):
- Widgets: Total return amount, Return count, Return share
- Tabs: All, Under Review, Approved by Seller, Rejected by Seller, Marketplace Help, etc.
- Search: "Search by order ID, customer, shop, product"
- Date filters: Date from, Date to
- Filters button
- DataGrid with columns: Order ID, Product, Status, Date, Quantity, Price, Total, Return reason
"""

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage, logger


class ReturnsPage(BasePage):
    """
    Page Object Model for Returns Management Page.
    Handles returns listing, filtering, approval/rejection.
    """

    RETURNS_PATH = "/dashboard/orders-management/returns"
    DEFAULT_PARAMS = "?page=1&size=10"

    def __init__(self, page: Page):
        """Initialize returns page with locators."""
        super().__init__(page)

    # ===============================
    # Locators (Properties)
    # ===============================

    @property
    def page_title(self) -> Locator:
        """Page title 'Returns' (EN/RU/UZ)."""
        return self.page.locator("h1:has-text('Returns'), h2:has-text('Returns')").or_(
            self.page.locator("h1:has-text('Возвраты'), h2:has-text('Возвраты')")
        ).or_(self.page.locator("h1:has-text('Qaytarishlar'), h2:has-text('Qaytarishlar')"))

    @property
    def returns_nav_link(self) -> Locator:
        """Returns link in sidebar submenu."""
        return self.page.locator("a:has-text('Returns'), [href*='returns']").first

    # --- Widgets ---

    @property
    def widgets_section(self) -> Locator:
        """Widgets section container (EN/RU/UZ)."""
        return self.page.locator("text=Widgets").or_(
            self.page.locator("text=Виджеты")
        ).or_(self.page.locator("text=Vidjetlar")).locator("..")

    @property
    def total_return_amount_widget(self) -> Locator:
        """Total return amount widget (EN/RU/UZ)."""
        return self.page.locator("text=Total return amount").or_(
            self.page.locator("text=Общая сумма возвратов")
        ).or_(self.page.locator("text=Qaytarishlarning umumiy summasi")).locator("..")

    @property
    def return_count_widget(self) -> Locator:
        """Return count widget (EN/RU/UZ)."""
        return self.page.locator("text=Return count").or_(
            self.page.locator("text=Количество возвратов")
        ).or_(self.page.locator("text=Qaytarishlar soni")).locator("..")

    @property
    def return_share_widget(self) -> Locator:
        """Return share widget (EN/RU/UZ)."""
        return self.page.locator("text=Return share").or_(
            self.page.locator("text=Доля возвратов")
        ).or_(self.page.locator("text=Qaytarishlar ulushi")).locator("..")

    # --- Status Tabs (Russian UI) ---

    @property
    def status_tabs(self) -> Locator:
        """All status tab buttons."""
        return self.page.locator("[role='tab']")

    @property
    def all_tab(self) -> Locator:
        """'All' status tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Все").or_(
            self.page.get_by_role("tab", name="All")
        ).or_(self.page.get_by_role("tab", name="Hammasi"))

    @property
    def under_review_tab(self) -> Locator:
        """'Under review' status tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="На рассмотрении").or_(
            self.page.get_by_role("tab", name="Under review")
        ).or_(self.page.get_by_role("tab", name="Ko'rib chiqilmoqda"))

    @property
    def approved_by_seller_tab(self) -> Locator:
        """'Approved by seller' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Одобрено продавцом").or_(
            self.page.get_by_role("tab", name="Approved by seller")
        ).or_(self.page.get_by_role("tab", name="Sotuvchi tomonidan tasdiqlangan"))

    @property
    def rejected_by_seller_tab(self) -> Locator:
        """'Rejected by seller' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Отклонено продавцом").or_(
            self.page.get_by_role("tab", name="Rejected by seller")
        ).or_(self.page.get_by_role("tab", name="Sotuvchi tomonidan rad etilgan"))

    @property
    def marketplace_help_tab(self) -> Locator:
        """'Marketplace help' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Помощь маркетплейса").or_(
            self.page.get_by_role("tab", name="Marketplace help")
        ).or_(self.page.get_by_role("tab", name="Marketplace yordami"))

    @property
    def approved_by_marketplace_tab(self) -> Locator:
        """'Approved by marketplace' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Одобрено маркетплейсом").or_(
            self.page.get_by_role("tab", name="Approved by marketplace")
        ).or_(self.page.get_by_role("tab", name="Marketplace tomonidan tasdiqlangan"))

    @property
    def rejected_by_marketplace_tab(self) -> Locator:
        """'Rejected by marketplace' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Отклонено маркетплейсом").or_(
            self.page.get_by_role("tab", name="Rejected by marketplace")
        ).or_(self.page.get_by_role("tab", name="Marketplace tomonidan rad etilgan"))

    @property
    def received_by_warehouse_tab(self) -> Locator:
        """'Received by warehouse' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Получено складом").or_(
            self.page.get_by_role("tab", name="Received by warehouse")
        ).or_(self.page.get_by_role("tab", name="Ombor tomonidan qabul qilingan"))

    @property
    def rejected_by_warehouse_tab(self) -> Locator:
        """'Rejected by warehouse' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Отклонено складом").or_(
            self.page.get_by_role("tab", name="Rejected by warehouse")
        ).or_(self.page.get_by_role("tab", name="Ombor tomonidan rad etilgan"))

    @property
    def returned_tab(self) -> Locator:
        """'Returned' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Возвращено").or_(
            self.page.get_by_role("tab", name="Returned")
        ).or_(self.page.get_by_role("tab", name="Qaytarilgan"))

    @property
    def cancelled_tab(self) -> Locator:
        """'Cancelled' tab (RU/EN/UZ)."""
        return self.page.get_by_role("tab", name="Отменено").or_(
            self.page.get_by_role("tab", name="Cancelled")
        ).or_(self.page.get_by_role("tab", name="Bekor qilingan"))

    # --- Filters (no search on this page) ---

    @property
    def filters_btn(self) -> Locator:
        """Filters button."""
        return self.page.get_by_role("button", name="Фильтры").or_(
            self.page.get_by_role("button", name="Filters")
        )

    # --- Table/DataGrid ---

    @property
    def returns_table(self) -> Locator:
        """Returns DataGrid/table."""
        return self.page.locator(".MuiDataGrid-root").or_(
            self.page.locator("table")
        ).or_(self.page.locator("[role='grid']"))

    @property
    def table_rows(self) -> Locator:
        """Table/DataGrid rows."""
        return self.page.locator(".MuiDataGrid-row").or_(
            self.page.locator("tbody tr")
        )

    @property
    def column_headers(self) -> Locator:
        """Column headers."""
        return self.page.locator(".MuiDataGrid-columnHeader, th, [role='columnheader']")

    # --- Pagination ---

    @property
    def pagination(self) -> Locator:
        """Pagination container."""
        return self.page.locator(".MuiTablePagination-root, [class*='pagination']")

    @property
    def next_page_btn(self) -> Locator:
        """Next page button."""
        return self.page.get_by_role("button", name="Go to next page")

    @property
    def prev_page_btn(self) -> Locator:
        """Previous page button."""
        return self.page.get_by_role("button", name="Go to previous page")

    # --- Action Buttons ---

    @property
    def seller_instructions_btn(self) -> Locator:
        """Seller Instructions button."""
        return self.page.get_by_role("button", name="Seller Instructions")

    @property
    def chat_with_support_btn(self) -> Locator:
        """Chat with Support button."""
        return self.page.get_by_role("button", name="Chat with Support")

    # ===============================
    # Navigation Methods
    # ===============================

    def navigate(self) -> None:
        """Navigate to returns page."""
        logger.info("Navigating to returns page...")
        self.navigate_to(f"{self.RETURNS_PATH}{self.DEFAULT_PARAMS}")
        self.page.wait_for_load_state("networkidle")
        logger.info("Returns page loaded")

    def click_returns_nav_link(self) -> None:
        """Navigate to returns page via direct URL (sidebar link is unreliable)."""
        logger.info("Navigating to returns page...")
        # Direct navigation is more reliable than clicking sidebar menu
        # The sidebar Returns link doesn't have proper navigation href
        self.navigate()
        logger.info("Navigated to returns page")

    # ===============================
    # Tab Methods
    # ===============================

    def click_tab(self, tab_name: str) -> None:
        """Click on a status tab by name."""
        logger.info(f"Clicking tab: {tab_name}")
        tab = self.page.locator(f"button:has-text('{tab_name}')").first
        if tab.is_visible(timeout=3000):
            tab.click()
            self.page.wait_for_load_state("networkidle")
        logger.info(f"Clicked tab: {tab_name}")

    def get_active_tab(self) -> str:
        """Get currently active tab name."""
        # Active tab usually has different styling or aria-selected
        active = self.page.locator("button[class*='selected'], button[aria-selected='true']").first
        if active.is_visible(timeout=2000):
            return active.text_content() or ""
        return ""

    def get_tab_count(self) -> int:
        """Get number of visible tabs."""
        tabs = self.page.locator("button:has-text('All'), button:has-text('Under Review'), button:has-text('Approved'), button:has-text('Rejected'), button:has-text('Marketplace')")
        return tabs.count()

    # ===============================
    # Filter Methods (no search on this page)
    # ===============================

    def click_filters(self) -> None:
        """Click Filters button."""
        logger.info("Clicking Filters button...")
        if self.filters_btn.is_visible(timeout=3000):
            self.filters_btn.click()
            self.page.wait_for_load_state("domcontentloaded")
            logger.info("Filters button clicked")
        else:
            logger.warning("Filters button not visible")

    # ===============================
    # Table Methods
    # ===============================

    def get_returns_count(self) -> int:
        """Get number of returns in the list."""
        self.page.wait_for_load_state("domcontentloaded")
        count = self.table_rows.count()
        logger.info(f"Returns count: {count}")
        return count

    def click_return_row(self, index: int = 0) -> None:
        """Click on return row to view details."""
        logger.info(f"Clicking return row {index}...")
        row = self.table_rows.nth(index)
        row.wait_for(state="visible", timeout=3000)
        row.click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Return row clicked")

    def get_column_headers(self) -> list:
        """Get list of column header texts."""
        headers = self.column_headers.all()
        return [h.text_content().strip() for h in headers if h.text_content()]

    # ===============================
    # Widget Methods
    # ===============================

    def is_widgets_visible(self) -> bool:
        """Check if widgets section is visible (EN/RU/UZ)."""
        return self.page.locator("text=Widgets").or_(
            self.page.locator("text=Виджеты")
        ).or_(self.page.locator("text=Vidjetlar")).is_visible(timeout=3000)

    def get_total_return_amount(self) -> str:
        """Get total return amount from widget."""
        widget = self.total_return_amount_widget
        if widget.is_visible(timeout=2000):
            return widget.text_content() or ""
        return ""

    def get_return_count_from_widget(self) -> str:
        """Get return count from widget."""
        widget = self.return_count_widget
        if widget.is_visible(timeout=2000):
            return widget.text_content() or ""
        return ""

    # ===============================
    # Validation Methods
    # ===============================

    def is_on_returns_page(self) -> bool:
        """Check if currently on returns page."""
        return "returns" in self.page.url

    def is_empty_state_visible(self) -> bool:
        """Check if empty state / no data message is visible."""
        empty = self.page.locator("text=/No data|No returns|Нет данных|Ma'lumot yo'q/i")
        return empty.is_visible(timeout=2000)

    def is_page_loaded(self) -> bool:
        """Check if returns page is fully loaded (EN/RU/UZ)."""
        try:
            has_title = self.page.locator("text=Returns").or_(
                self.page.locator("text=Возвраты")
            ).or_(self.page.locator("text=Qaytarishlar")).first.is_visible(timeout=3000)
            has_table = self.returns_table.is_visible(timeout=2000)
            return has_title or has_table
        except Exception:
            return False

    # ==================== VALIDATION METHODS ====================

    def get_validation_error_count(self) -> int:
        """Get count of MUI validation errors on the page."""
        return self.page.locator(".MuiFormHelperText-root.Mui-error").count()

    def has_validation_errors(self) -> bool:
        """Check if there are any validation errors on the page."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """Get all validation error messages from the page."""
        errors = self.page.locator(".MuiFormHelperText-root.Mui-error").all()
        return [e.inner_text() for e in errors if e.is_visible()]

    def has_error_for_field(self, field_name: str) -> bool:
        """Check if a specific field has a validation error."""
        field = self.page.get_by_role("textbox", name=field_name)
        if field.count() > 0:
            parent = field.locator("xpath=ancestor::div[contains(@class,'MuiFormControl')]")
            if parent.count() > 0:
                error = parent.locator(".MuiFormHelperText-root.Mui-error")
                return error.count() > 0 and error.is_visible()
        return False
