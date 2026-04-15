"""
Base page class containing common functionality for all page objects.
This module provides shared methods and properties used across all pages.
"""

import logging
import os
from playwright.sync_api import Page, expect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# ---------------------------
# Custom Exceptions
# ---------------------------
class PageLoadError(Exception):
    """Raised when page fails to load properly."""


class ElementNotFoundError(Exception):
    """Raised when required element is not found."""


class NavigationError(Exception):
    """Raised when navigation fails."""


# ---------------------------
# Configure logging
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ---------------------------
# Constants
# ---------------------------
class PageConstants:
    DEFAULT_TIMEOUT = 15000
    DEFAULT_NAVIGATION_TIMEOUT = 30000
    ELEMENT_WAIT_TIMEOUT = 15000
    CLICK_WAIT_TIME = 1000

    # Read BASE_URL from environment variable
    BASE_URL = os.getenv('BASE_URL', 'https://staging-seller.greatmall.uz')

    # Use 'load' instead of 'networkidle' - faster and more reliable
    NETWORK_IDLE = "load"
    VISIBLE_STATE = "visible"

    # Expected HTTP status codes during testing
    EXPECTED_ERROR_CODES = [400, 500]


# ---------------------------
# Base Page Class
# ---------------------------
class BasePage:
    """
    Base page object class providing common functionality.

    Purpose:
    - Provide navigation and interaction methods
    - Handle error checking and logging
    - Implement reusable wait and assertion methods
    """

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = PageConstants.BASE_URL

    # ---------------------------
    # Navigation
    # ---------------------------
    def navigate_to(self, path: str = "") -> None:
        """Navigate to specified path relative to base URL."""
        full_url = f"{self.base_url}{path}"
        logger.info(f"Navigating to: {full_url}")
        try:
            self.page.goto(full_url, wait_until=PageConstants.NETWORK_IDLE,
                           timeout=PageConstants.DEFAULT_NAVIGATION_TIMEOUT)
            logger.info(f"Successfully navigated to: {full_url}")
        except Exception as e:
            logger.error(f"Navigation failed to {full_url}: {str(e)}")
            raise NavigationError(f"Navigation failed to {full_url}: {str(e)}")

    def get_current_url(self) -> str:
        """Return current page URL."""
        return self.page.url

    # ---------------------------
    # Wait Methods (Explicit Waits - Replace Hard-coded Timeouts)
    # ---------------------------
    def wait_for_page_load(self, timeout: int = PageConstants.DEFAULT_TIMEOUT) -> None:
        """Wait for page to fully load."""
        try:
            self.page.wait_for_load_state(PageConstants.NETWORK_IDLE, timeout=timeout)
            logger.info("Page loaded successfully")
        except Exception as e:
            logger.warning(f"Page load timeout: {str(e)}")
            raise PageLoadError(f"Page failed to load within {timeout}ms: {str(e)}")

    def wait_for_element(self, locator: str, timeout: int = PageConstants.ELEMENT_WAIT_TIMEOUT) -> bool:
        """Wait for element to be visible on the page."""
        try:
            self.page.locator(locator).wait_for(state=PageConstants.VISIBLE_STATE, timeout=timeout)
            logger.info(f"Element visible: {locator}")
            return True
        except Exception as e:
            logger.warning(f"Element not found: {locator} - {str(e)}")
            return False

    def wait_for_network_idle(self, timeout: int = PageConstants.DEFAULT_TIMEOUT) -> None:
        """Wait for network to become idle (all requests completed)."""
        try:
            self.page.wait_for_load_state("networkidle", timeout=timeout)
        except Exception as e:
            logger.debug(f"Network idle timeout: {str(e)}")

    def wait_for_dom_ready(self, timeout: int = PageConstants.DEFAULT_TIMEOUT) -> None:
        """Wait for DOM content to be loaded."""
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=timeout)
        except Exception as e:
            logger.debug(f"DOM ready timeout: {str(e)}")

    def wait_for_url_contains(self, url_part: str, timeout: int = PageConstants.DEFAULT_TIMEOUT) -> bool:
        """Wait for URL to contain specified string."""
        try:
            self.page.wait_for_url(f"**{url_part}**", timeout=timeout)
            return True
        except Exception as e:
            logger.warning(f"URL wait timeout for '{url_part}': {str(e)}")
            return False

    def wait_for_selector(self, selector: str, state: str = "visible", timeout: int = PageConstants.ELEMENT_WAIT_TIMEOUT) -> bool:
        """
        Wait for element matching selector to reach specified state.

        Args:
            selector: CSS selector or Playwright selector
            state: One of 'attached', 'detached', 'visible', 'hidden'
            timeout: Maximum wait time in milliseconds
        """
        try:
            self.page.wait_for_selector(selector, state=state, timeout=timeout)
            return True
        except Exception as e:
            logger.debug(f"Selector wait timeout for '{selector}': {str(e)}")
            return False

    def wait_for_element_hidden(self, locator: str, timeout: int = PageConstants.ELEMENT_WAIT_TIMEOUT) -> bool:
        """Wait for element to become hidden or detached."""
        try:
            self.page.locator(locator).wait_for(state="hidden", timeout=timeout)
            return True
        except Exception as e:
            logger.debug(f"Element hide timeout for '{locator}': {str(e)}")
            return False

    def wait_for_text(self, text: str, timeout: int = PageConstants.ELEMENT_WAIT_TIMEOUT) -> bool:
        """Wait for text to appear on the page."""
        try:
            self.page.get_by_text(text).wait_for(state="visible", timeout=timeout)
            return True
        except Exception as e:
            logger.debug(f"Text wait timeout for '{text}': {str(e)}")
            return False

    def wait_for_button_enabled(self, button_selector: str, timeout: int = PageConstants.ELEMENT_WAIT_TIMEOUT) -> bool:
        """Wait for button to become enabled."""
        try:
            button = self.page.locator(button_selector)
            expect(button).to_be_enabled(timeout=timeout)
            return True
        except Exception as e:
            logger.debug(f"Button enable wait timeout: {str(e)}")
            return False

    def wait_after_click(self, timeout: int = PageConstants.DEFAULT_TIMEOUT) -> None:
        """Wait for page to stabilize after a click action."""
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=timeout)
        except Exception:
            pass  # Don't fail if already loaded

    # ---------------------------
    # Element Interactions
    # ---------------------------
    def click_element(self, locator: str, wait_for_navigation: bool = False) -> None:
        """Click on element with proper waiting and error handling."""
        try:
            element = self.page.locator(locator)
            element.wait_for(state=PageConstants.VISIBLE_STATE, timeout=5000)
            element.click()
            if wait_for_navigation:
                self.wait_for_dom_ready()
            logger.info(f"Clicked element: {locator}")
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {str(e)}")
            raise ElementNotFoundError(f"Could not click element {locator}: {str(e)}")

    def fill_input(self, locator: str, value: str, clear_first: bool = True) -> None:
        """Fill input field with specified value."""
        try:
            element = self.page.locator(locator)
            element.wait_for(state=PageConstants.VISIBLE_STATE, timeout=5000)
            if clear_first:
                element.clear()
            element.fill(value)
            logger.info(f"Filled input {locator} with: {value}")
        except Exception as e:
            logger.error(f"Failed to fill input {locator}: {str(e)}")
            raise ElementNotFoundError(f"Could not fill input {locator}: {str(e)}")

    def get_element_text(self, locator: str) -> str:
        """Get text content of specified element."""
        try:
            element = self.page.locator(locator)
            text = element.text_content() or ""
            logger.info(f"Retrieved text from {locator}: {text}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text from {locator}: {str(e)}")
            return ""

    def upload_file(self, locator: str, file_path: str) -> None:
        """Upload file to input field."""
        try:
            self.page.locator(locator).set_input_files(file_path)
            logger.info(f"Uploaded file {file_path} to {locator}")
        except Exception as e:
            logger.error(f"Failed to upload file: {str(e)}")
            raise ElementNotFoundError(f"Could not upload file {file_path} to {locator}: {str(e)}")

    # ---------------------------
    # Assertions
    # ---------------------------
    def assert_page_title(self, expected_title: str) -> None:
        """Assert that page title matches expected value."""
        try:
            expect(self.page).to_have_title(expected_title)
            logger.info(f"Page title verified: {expected_title}")
        except Exception as e:
            logger.error(f"Page title assertion failed: {str(e)}")
            raise AssertionError(f"Expected title '{expected_title}' not found: {str(e)}")

    # ---------------------------
    # Utilities
    # ---------------------------
    def take_screenshot(self, name: str) -> None:
        """Take screenshot of current page state."""
        try:
            self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)
            logger.info(f"Screenshot taken: {name}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")

