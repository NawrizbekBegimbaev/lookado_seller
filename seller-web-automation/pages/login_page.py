"""
Login Page Object Model
Follows KISS and SOLID principles with clear separation of concerns.
"""

import logging
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Page Object for Login page following POM best practices."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/auth/login"

    # ===============================
    # Locators (Single Responsibility)
    # ===============================
    @property
    def email_field(self) -> Locator:
        """Email/phone input field - first textbox on login form."""
        return self.page.get_by_role("textbox").first

    @property
    def password_field(self) -> Locator:
        """Password input field - second textbox on login form."""
        return self.page.get_by_role("textbox").nth(1)

    @property
    def login_button(self) -> Locator:
        """Login submit button - uses type=submit (language-independent)."""
        return self.page.locator("button[type='submit']")

    @property
    def registration_link(self) -> Locator:
        """Registration navigation link - link to registration page (language-independent)."""
        return self.page.locator("a[href*='registration']")

    @property
    def error_message(self) -> Locator:
        """Error message display - ARIA alert role."""
        return self.page.get_by_role("alert")

    @property
    def password_helper_text(self) -> Locator:
        """Password field validation helper text (language-independent - uses MUI helper class)."""
        return self.page.locator(".MuiFormHelperText-root")

    # ===============================
    # Navigation Methods
    # ===============================
    def open_login_page(self) -> None:
        """Navigate to login page and verify it loads."""
        logger.info("Opening login page...")
        self.navigate_to(self.url)
        self.wait_for_page_load()

    def verify_on_login_screen(self) -> bool:
        """Verify user is on login screen."""
        return self.email_field.is_visible(timeout=5000)

    # ===============================
    # Action Methods
    # ===============================
    def enter_email(self, email: str) -> None:
        """Enter email/phone into email field."""
        logger.info(f"Entering email: {email}")
        self.email_field.wait_for(state="visible", timeout=10000)
        self.email_field.click()
        self.email_field.fill(email)

    def enter_password(self, password: str) -> None:
        """Enter password into password field."""
        logger.info("Entering password")
        self.password_field.wait_for(state="visible", timeout=10000)
        self.password_field.click()
        self.password_field.fill(password)

    def click_login(self) -> None:
        """Click login button to submit credentials."""
        logger.info("Clicking login button")
        self.login_button.wait_for(state="visible", timeout=10000)
        self.login_button.click()
        self.wait_for_network_idle()

    def click_registration_link(self) -> None:
        """Click registration link to navigate to registration page."""
        logger.info("Clicking registration link")
        self.registration_link.click()
        self.wait_for_url_contains("registration")

    def perform_login(self, email: str, password: str, wait_for_redirect: bool = True) -> None:
        """Complete login flow with given credentials."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        if wait_for_redirect:
            self.page.wait_for_url("**/dashboard*", timeout=15000)

    # ===============================
    # Verification Methods
    # ===============================
    def is_email_field_visible(self) -> bool:
        """Verify email field is visible."""
        return self.email_field.is_visible()

    def is_password_field_visible(self) -> bool:
        """Verify password field is visible."""
        return self.password_field.is_visible()

    def is_login_button_visible(self) -> bool:
        """Verify login button is visible."""
        return self.login_button.is_visible()

    def is_registration_link_visible(self) -> bool:
        """Verify registration link is visible."""
        return self.registration_link.is_visible()

    def is_error_displayed(self) -> bool:
        """Check if any error message is displayed (alert or helper text)."""
        try:
            # First try to find alert messages (backend errors)
            self.error_message.wait_for(
                state="visible",
                timeout=3000
            )
            return True
        except Exception:
            pass

        try:
            # Then try to find password helper text (client-side validation)
            self.password_helper_text.wait_for(
                state="visible",
                timeout=2000
            )
            return True
        except Exception:
            logger.warning("No error message found")
            return False

    def get_error_text(self) -> str:
        """Get error message text content."""
        try:
            text = self.error_message.text_content() or ""
            logger.info(f"Error message text: '{text}'")
            return text
        except Exception as e:
            logger.warning(f"Could not get error text: {e}")
            return ""

    def verify_error_contains(self, expected_message: str) -> bool:
        """Verify error message contains expected text."""
        actual_message = self.get_error_text()
        return expected_message.lower() in actual_message.lower()

    def is_forgot_password_link_present(self) -> bool:
        """Check if forgot password link exists (should be absent). Language-independent."""
        try:
            # Check by URL pattern - forgot password links typically go to /forgot or /reset
            forgot_link = self.page.locator("a[href*='forgot'], a[href*='reset-password']")
            return forgot_link.is_visible(timeout=2000)
        except Exception:
            return False

    def is_redirected_to_dashboard(self) -> bool:
        """Verify user is redirected to dashboard after login."""
        self.wait_for_url_contains("dashboard")
        current_url = self.get_current_url()
        return "dashboard" in current_url or "login" not in current_url

    def verify_url_equals(self, expected_url: str) -> bool:
        """Verify current URL matches expected URL."""
        current_url = self.get_current_url()
        return current_url == expected_url

    # ===============================
    # Validation Error Methods (MUI)
    # ===============================
    def get_validation_error_count(self) -> int:
        """Get count of MUI validation error messages displayed."""
        try:
            error_elements = self.page.locator(".MuiFormHelperText-root.Mui-error")
            return error_elements.count()
        except Exception:
            return 0

    def has_validation_errors(self) -> bool:
        """Check if form has any MUI validation errors displayed."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """Get all MUI validation error messages from the form."""
        messages = []
        try:
            error_elements = self.page.locator(".MuiFormHelperText-root.Mui-error")
            count = error_elements.count()
            for i in range(count):
                try:
                    text = error_elements.nth(i).inner_text(timeout=1000)
                    if text.strip():
                        messages.append(text.strip())
                except Exception:
                    pass
        except Exception:
            pass
        return messages

    def has_error_for_field(self, field_name: str) -> bool:
        """Check if a specific field has validation error (MUI Mui-error class on label)."""
        try:
            error_label = self.page.locator(f".Mui-error:has-text('{field_name}')")
            return error_label.count() > 0
        except Exception:
            return False

    def get_toast_error_message(self) -> str:
        """Get error message from toast/alert notification."""
        try:
            alert = self.page.locator("[role='alert']").first
            if alert.is_visible(timeout=2000):
                return alert.inner_text()
        except Exception:
            pass
        return ""

    def has_toast_error(self) -> bool:
        """Check if toast/alert error is displayed."""
        try:
            return self.page.locator("[role='alert']").first.is_visible(timeout=2000)
        except Exception:
            return False

    def get_api_error_message(self) -> str:
        """Get API error message (usually displayed in text after failed login)."""
        try:
            # Look for common error text patterns
            error_text = self.page.locator("text=/не найден|not found|invalid|ошибка|error/i").first
            if error_text.is_visible(timeout=2000):
                return error_text.inner_text()
        except Exception:
            pass
        return ""

    # ===============================
    # Utility Methods (DRY Principle)
    # ===============================
    def verify_all_ui_elements_visible(self) -> dict:
        """Verify all essential UI elements are present."""
        return {
            "email_field": self.is_email_field_visible(),
            "password_field": self.is_password_field_visible(),
            "login_button": self.is_login_button_visible(),
            "registration_link": self.is_registration_link_visible()
        }