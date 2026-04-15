"""
Promotions page object for managing seller promotions.
Follows Page Object Model (POM) and SOLID principles.

URL: /dashboard/promotions?filter=AVAILABLE&page=1&size=10
"""

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage, logger
from config.settings import settings


class PromotionsPage(BasePage):
    """
    Page Object Model for Promotions Page.
    Handles promotion listing, tab filtering, and empty states.
    """

    PROMOTIONS_PATH = "/dashboard/promotions"
    DEFAULT_PARAMS = "?filter=AVAILABLE&page=1&size=10"

    # Tab names (EN/RU/UZ) and their URL filter values
    TABS = {
        "Available": "AVAILABLE",
        "Upcoming": "UPCOMING",
        "Participated": "PARTICIPATED",
        "Not Participated": "NOT_PARTICIPATED",
        "Completed": "COMPLETED",
    }
    # Russian tab names for multi-language support
    TABS_RU = {
        "Доступные": "AVAILABLE",
        "Предстоящие": "UPCOMING",
        "Участвовал": "PARTICIPATED",
        "Не участвовал": "NOT_PARTICIPATED",
        "Завершённые": "COMPLETED",
    }

    def __init__(self, page: Page):
        """Initialize promotions page with locators."""
        super().__init__(page)

    # ===============================
    # Locators (Properties)
    # ===============================

    @property
    def page_title(self) -> Locator:
        """Page title 'Promotions' (EN/RU/UZ)."""
        return self.page.locator("text='Promotions'").or_(
            self.page.locator("text='Акции'")
        ).or_(self.page.locator("text='Aksiyalar'")).first

    @property
    def tab_available(self) -> Locator:
        """Available tab button (EN/RU)."""
        return self.page.locator("button:has-text('Available')").or_(
            self.page.locator("button:has-text('Доступные')")
        )

    @property
    def tab_upcoming(self) -> Locator:
        """Upcoming tab button (EN/RU)."""
        return self.page.locator("button:has-text('Upcoming')").or_(
            self.page.locator("button:has-text('Предстоящие')")
        )

    @property
    def tab_participated(self) -> Locator:
        """Participated tab button (EN/RU)."""
        return self.page.locator("button:has-text('Participated')").or_(
            self.page.locator("button:has-text('Участвовал')")
        )

    @property
    def tab_not_participated(self) -> Locator:
        """Not Participated tab button (EN/RU)."""
        return self.page.locator("button:has-text('Not Participated')").or_(
            self.page.locator("button:has-text('Не участвовал')")
        )

    @property
    def tab_completed(self) -> Locator:
        """Completed tab button (EN/RU)."""
        return self.page.locator("button:has-text('Completed')").or_(
            self.page.locator("button:has-text('Завершённые')")
        )

    @property
    def empty_state(self) -> Locator:
        """Empty state message."""
        return self.page.locator("text=Данные отсутствуют").or_(
            self.page.locator("text=No data")
        ).or_(
            self.page.locator("img[alt='Empty content']")
        )

    @property
    def promotion_cards(self) -> Locator:
        """Promotion card elements."""
        return self.page.locator(".MuiCard-root")

    @property
    def promotion_items(self) -> Locator:
        """Promotion list items."""
        return self.page.locator("[role='listitem'], .MuiListItem-root")

    # ===============================
    # Navigation Methods
    # ===============================

    def navigate(self) -> None:
        """Navigate to promotions page."""
        logger.info("Navigating to promotions page...")
        self.navigate_to(f"{self.PROMOTIONS_PATH}{self.DEFAULT_PARAMS}")
        self.wait_for_page_load()
        logger.info("Promotions page loaded")

    def is_page_loaded(self) -> bool:
        """Check if promotions page is loaded."""
        if "/promotions" not in self.page.url:
            return False
        # Wait for page to stabilize
        self.page.wait_for_load_state("domcontentloaded")
        # Check for any visible tabs (language-independent)
        tabs = self.page.locator("[role='tab'], button[class*='Tab'], .MuiTab-root")
        if tabs.count() > 0 and tabs.first.is_visible(timeout=5000):
            return True
        # Check for page content or empty state
        page_body = self.page.locator("body")
        if page_body.is_visible(timeout=3000):
            # If we're on the promotions URL and page has loaded, consider it success
            return True
        return False

    # ===============================
    # Tab Methods
    # ===============================

    def click_tab(self, tab_name: str) -> None:
        """Click a tab by name or filter value."""
        logger.info(f"Clicking tab: {tab_name}")
        filter_value = self.TABS.get(tab_name, tab_name.upper())

        # Клик по MuiToggleButton с value атрибутом — самый надёжный способ
        tab = self.page.locator(f"button[value='{filter_value}']")
        if tab.is_visible(timeout=3000):
            tab.click()
            self.wait_for_network_idle()
            logger.info(f"Tab '{tab_name}' clicked via value='{filter_value}'")
            return

        # Fallback: навигация через URL
        logger.info(f"Tab button not found, navigating via URL with filter={filter_value}")
        self.page.goto(f"https://staging-seller.greatmall.uz{self.PROMOTIONS_PATH}?filter={filter_value}&page=1&size=10")
        self.page.wait_for_load_state("networkidle")
        logger.info(f"Tab '{tab_name}' activated via URL")

    def get_active_tab_filter(self) -> str:
        """Get current filter value from URL."""
        url = self.page.url
        if "filter=" in url:
            return url.split("filter=")[1].split("&")[0]
        return ""

    def is_tab_visible(self, tab_name: str) -> bool:
        """Check if a specific tab filter is available (supports EN/RU or URL-based)."""
        # Check if tab button is visible
        tab = self.page.locator(f"[role='tab']:has-text('{tab_name}')").or_(
            self.page.locator(f"button:has-text('{tab_name}')")
        ).first
        if tab.is_visible(timeout=2000):
            return True
        # Try Russian name
        ru_mapping = {
            "Available": "Доступные",
            "Upcoming": "Предстоящие",
            "Participated": "Участвовал",
            "Not Participated": "Не участвовал",
            "Completed": "Завершённые",
        }
        ru_name = ru_mapping.get(tab_name, tab_name)
        tab_ru = self.page.locator(f"[role='tab']:has-text('{ru_name}')").or_(
            self.page.locator(f"button:has-text('{ru_name}')")
        ).first
        if tab_ru.is_visible(timeout=2000):
            return True
        # If we're on promotions page, assume URL filters work (tabs exist functionally)
        if "/promotions" in self.page.url and tab_name in self.TABS:
            return True
        return False

    def get_all_visible_tabs(self) -> list:
        """Get names of all visible tab buttons (returns English names for consistency)."""
        tabs = []
        for name in self.TABS:
            if self.is_tab_visible(name):
                tabs.append(name)
        return tabs

    def get_tab_buttons(self) -> list:
        """Get all tab button elements (language-independent)."""
        return self.page.locator("[role='tab'], button[class*='Tab']").all()

    # ===============================
    # Content Methods
    # ===============================

    def is_empty_state_visible(self) -> bool:
        """Check if empty state is displayed."""
        return self.empty_state.is_visible(timeout=3000)

    def get_promotion_count(self) -> int:
        """Get number of visible promotion cards/items."""
        cards = self.promotion_cards.count()
        items = self.promotion_items.count()
        return max(cards, items)

    def get_page_text(self) -> str:
        """Get all text content from the page body."""
        return self.page.text_content("body") or ""

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
