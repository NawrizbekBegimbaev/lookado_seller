"""
Reviews page object for managing product reviews.
Follows Page Object Model (POM) and SOLID principles.

URL: /dashboard/reviews?page=1&size=10
"""

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage, logger
from config.settings import settings


class ReviewsPage(BasePage):
    """
    Page Object Model for Reviews Page.
    Handles review listing, filtering, status tabs, and statistics.
    """

    REVIEWS_PATH = "/dashboard/reviews"
    DEFAULT_PARAMS = "?page=1&size=10"

    # Status tab names
    STATUS_TABS = ["All", "New", "Moderation", "Processed", "Rejected"]

    # Statistics card names
    STAT_CARDS = ["New", "With Responses", "Waiting Response", "My Rating"]

    # DataGrid column fields
    GRID_COLUMNS = ["product", "date", "status", "rating", "review"]

    def __init__(self, page: Page):
        """Initialize reviews page with locators."""
        super().__init__(page)

    # ===============================
    # Locators (Properties)
    # ===============================

    @property
    def page_title(self) -> Locator:
        """Page title 'Reviews' (EN/RU/UZ)."""
        return self.page.locator("text='Reviews'").or_(
            self.page.locator("text='Отзывы'")
        ).or_(self.page.locator("text='Sharhlar'")).first

    @property
    def statistics_section(self) -> Locator:
        """Reviews Statistics section (EN/RU/UZ)."""
        return self.page.locator("text='Reviews Statistics'").or_(
            self.page.locator("text='Статистика отзывов'")
        ).or_(self.page.locator("text='Sharhlar statistikasi'")).first

    @property
    def stat_new(self) -> Locator:
        """Statistics card: New reviews count (EN/RU/UZ)."""
        return self.page.locator(".MuiPaper-root:has-text('New')").or_(
            self.page.locator(".MuiPaper-root:has-text('Новые')")
        ).or_(self.page.locator(".MuiPaper-root:has-text('Yangi')")).first

    @property
    def stat_with_responses(self) -> Locator:
        """Statistics card: With Responses count (EN/RU/UZ)."""
        return self.page.locator(".MuiPaper-root:has-text('With Responses')").or_(
            self.page.locator(".MuiPaper-root:has-text('С ответами')")
        ).or_(self.page.locator(".MuiPaper-root:has-text('Javoblar bilan')")).first

    @property
    def stat_waiting_response(self) -> Locator:
        """Statistics card: Waiting Response count (EN/RU/UZ)."""
        return self.page.locator(".MuiPaper-root:has-text('Waiting Response')").or_(
            self.page.locator(".MuiPaper-root:has-text('Ожидает ответа')")
        ).or_(self.page.locator(".MuiPaper-root:has-text('Javob kutilmoqda')")).first

    @property
    def stat_my_rating(self) -> Locator:
        """Statistics card: My Rating value (EN/RU/UZ)."""
        return self.page.locator(".MuiPaper-root:has-text('My Rating')").or_(
            self.page.locator(".MuiPaper-root:has-text('Мой рейтинг')")
        ).or_(self.page.locator(".MuiPaper-root:has-text('Mening reytingim')")).first

    # NOTE: No search field on this page

    @property
    def date_from_input(self) -> Locator:
        """Date From filter input."""
        return self.page.locator("input[name='dateFrom']")

    @property
    def date_to_input(self) -> Locator:
        """Date To filter input."""
        return self.page.locator("input[name='dateTo']")

    @property
    def rating_select(self) -> Locator:
        """Review Rating filter select."""
        return self.page.locator("#mui-component-select-rating").or_(
            self.page.locator("[aria-labelledby*='rating-label']")
        )

    @property
    def review_type_select(self) -> Locator:
        """Review Type filter select."""
        return self.page.locator("#mui-component-select-reviewType").or_(
            self.page.locator("[aria-labelledby*='review-type-label']")
        )

    @property
    def time_period_select(self) -> Locator:
        """Time period (All Time) select."""
        return self.page.locator(".MuiSelect-root:has-text('All Time')").or_(
            self.page.locator(".MuiSelect-root:has-text('За все время')")
        ).or_(self.page.locator(".MuiSelect-root:has-text('Barcha vaqt')")).first

    @property
    def data_grid(self) -> Locator:
        """MUI DataGrid container."""
        return self.page.locator(".MuiDataGrid-root, [role='grid']").first

    @property
    def grid_rows(self) -> Locator:
        """DataGrid rows."""
        return self.page.locator("[role='row']:not([class*='header']):not(:has([role='columnheader']))")

    @property
    def column_headers(self) -> Locator:
        """DataGrid column headers."""
        return self.page.locator("[role='columnheader']")

    @property
    def empty_state(self) -> Locator:
        """Empty state message."""
        return self.page.locator("text='Данные отсутствуют'").or_(
            self.page.locator(".MuiDataGrid-overlay")
        )

    @property
    def pagination(self) -> Locator:
        """Pagination container."""
        return self.page.locator(".MuiTablePagination-root")

    @property
    def page_size_select(self) -> Locator:
        """Page size selector."""
        return self.page.locator(".MuiTablePagination-select").or_(
            self.page.locator(".MuiSelect-select.MuiTablePagination-select")
        )

    # ===============================
    # Navigation Methods
    # ===============================

    def navigate(self) -> None:
        """Navigate to reviews page."""
        logger.info("Navigating to reviews page...")
        self.navigate_to(f"{self.REVIEWS_PATH}{self.DEFAULT_PARAMS}")
        self.wait_for_page_load()
        logger.info("Reviews page loaded")

    def is_page_loaded(self) -> bool:
        """Check if reviews page is loaded."""
        return (
            "/reviews" in self.page.url
            and (self.data_grid.is_visible(timeout=5000)
                 or self.empty_state.is_visible(timeout=3000))
        )

    # ===============================
    # Tab Methods
    # ===============================

    def get_active_tab(self) -> str:
        """Get currently active status tab name."""
        active = self.page.locator("[role='tab'][aria-selected='true']")
        if active.is_visible(timeout=2000):
            return active.text_content().strip()
        return ""

    def click_tab(self, tab_name: str) -> None:
        """Click a status tab by name."""
        logger.info(f"Clicking tab: {tab_name}")
        tab = self.page.get_by_role("tab", name=tab_name, exact=True)
        tab.click()
        self.wait_for_network_idle()
        logger.info(f"Tab '{tab_name}' clicked")

    def get_all_tabs(self) -> list:
        """Get all tab elements."""
        return self.page.locator("[role='tab']").all()

    def is_tab_visible(self, tab_name: str) -> bool:
        """Check if a specific tab is visible."""
        tab = self.page.get_by_role("tab", name=tab_name, exact=True)
        return tab.is_visible(timeout=2000)

    # ===============================
    # Statistics Methods
    # ===============================

    def get_stat_value(self, stat_name: str) -> str:
        """Get the value from a statistics card."""
        card = self.page.locator(f".MuiPaper-root:has-text('{stat_name}')").first
        if card.is_visible(timeout=2000):
            text = card.text_content().strip()
            return text.replace(stat_name, "").strip()
        return ""

    def is_statistics_visible(self) -> bool:
        """Check if statistics section is visible."""
        return (
            self.stat_new.is_visible(timeout=3000)
            or self.stat_with_responses.is_visible(timeout=2000)
        )

    # ===============================
    # Filter Methods (no search on this page)
    # ===============================

    def set_date_from(self, date_str: str) -> None:
        """Set Date From filter (format: DD-MM-YYYY)."""
        logger.info(f"Setting date from: {date_str}")
        self.date_from_input.fill(date_str)
        self.page.wait_for_load_state("domcontentloaded")

    def set_date_to(self, date_str: str) -> None:
        """Set Date To filter (format: DD-MM-YYYY)."""
        logger.info(f"Setting date to: {date_str}")
        self.date_to_input.fill(date_str)
        self.page.wait_for_load_state("domcontentloaded")

    def select_rating(self, rating: str) -> None:
        """Select review rating filter."""
        logger.info(f"Selecting rating: {rating}")
        self.rating_select.click()
        self.page.wait_for_load_state("domcontentloaded")
        option = self.page.get_by_role("option", name=rating)
        if option.is_visible(timeout=2000):
            option.click()
        self.page.wait_for_load_state("domcontentloaded")

    def select_review_type(self, review_type: str) -> None:
        """Select review type filter."""
        logger.info(f"Selecting review type: {review_type}")
        self.review_type_select.click()
        self.page.wait_for_load_state("domcontentloaded")
        option = self.page.get_by_role("option", name=review_type)
        if option.is_visible(timeout=2000):
            option.click()
        self.page.wait_for_load_state("domcontentloaded")

    # ===============================
    # Grid Methods
    # ===============================

    def get_row_count(self) -> int:
        """Get number of visible rows in the grid."""
        return self.grid_rows.count()

    def get_column_count(self) -> int:
        """Get number of column headers."""
        return self.column_headers.count()

    def get_column_names(self) -> list:
        """Get all column header names."""
        headers = self.column_headers.all()
        return [h.text_content().strip() for h in headers]

    def is_empty_state_visible(self) -> bool:
        """Check if empty state is displayed."""
        return self.empty_state.is_visible(timeout=3000)

    def get_grid_text(self) -> str:
        """Get all text content from the grid."""
        if self.data_grid.is_visible(timeout=3000):
            return self.data_grid.text_content() or ""
        return ""

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
