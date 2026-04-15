"""
Smart wait strategies for Playwright automation.

Provides intelligent waiting mechanisms that replace hardcoded time.sleep()
with condition-based waits, improving test speed and reliability.
"""

from typing import Callable, Any, Optional
import time
from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError
from config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class SmartWaits:
    """
    Collection of smart wait strategies for Playwright automation.

    These methods wait for specific conditions to be met instead of
    using hardcoded delays, making tests faster and more reliable.
    """

    @staticmethod
    def wait_for_element_visible(
        locator: Locator,
        timeout: int = settings.ELEMENT_WAIT_TIMEOUT,
        error_message: Optional[str] = None
    ) -> None:
        """
        Wait for element to be visible on the page.

        Args:
            locator: Playwright Locator object
            timeout: Maximum wait time in milliseconds
            error_message: Custom error message if wait fails

        Raises:
            AssertionError: If element not visible within timeout

        Example:
            >>> button = page.get_by_role("button", name="Submit")
            >>> SmartWaits.wait_for_element_visible(button)
        """
        try:
            expect(locator).to_be_visible(timeout=timeout)
            logger.debug(f"Element visible: {locator}")
        except AssertionError as e:
            msg = error_message or f"Element not visible within {timeout}ms: {locator}"
            logger.error(msg)
            raise AssertionError(msg) from e

    @staticmethod
    def wait_for_element_hidden(
        locator: Locator,
        timeout: int = settings.ELEMENT_WAIT_TIMEOUT
    ) -> None:
        """
        Wait for element to be hidden or removed from DOM.

        Args:
            locator: Playwright Locator object
            timeout: Maximum wait time in milliseconds

        Example:
            >>> loading_spinner = page.locator("[data-testid='loading']")
            >>> SmartWaits.wait_for_element_hidden(loading_spinner)
        """
        try:
            expect(locator).to_be_hidden(timeout=timeout)
            logger.debug(f"Element hidden: {locator}")
        except AssertionError as e:
            logger.error(f"Element still visible after {timeout}ms: {locator}")
            raise

    @staticmethod
    def wait_for_element_clickable(
        locator: Locator,
        timeout: int = settings.ELEMENT_WAIT_TIMEOUT
    ) -> None:
        """
        Wait for element to be visible, enabled, and in viewport (clickable).

        Args:
            locator: Playwright Locator object
            timeout: Maximum wait time in milliseconds

        Example:
            >>> submit_btn = page.get_by_role("button", name="Submit")
            >>> SmartWaits.wait_for_element_clickable(submit_btn)
            >>> submit_btn.click()
        """
        try:
            expect(locator).to_be_visible(timeout=timeout)
            expect(locator).to_be_enabled(timeout=timeout)
            locator.scroll_into_view_if_needed()
            logger.debug(f"Element clickable: {locator}")
        except AssertionError as e:
            logger.error(f"Element not clickable within {timeout}ms: {locator}")
            raise

    @staticmethod
    def wait_for_url_change(
        page: Page,
        expected_url_pattern: str,
        timeout: int = settings.NAVIGATION_TIMEOUT
    ) -> None:
        """
        Wait for URL to match specified pattern.

        Args:
            page: Playwright Page object
            expected_url_pattern: URL pattern to match (supports wildcards)
            timeout: Maximum wait time in milliseconds

        Example:
            >>> SmartWaits.wait_for_url_change(page, "**/dashboard/**")
        """
        try:
            page.wait_for_url(expected_url_pattern, timeout=timeout)
            logger.info(f"URL changed to match: {expected_url_pattern}")
        except PlaywrightTimeoutError as e:
            current_url = page.url
            logger.error(f"URL did not match '{expected_url_pattern}'. Current: {current_url}")
            raise AssertionError(
                f"Expected URL pattern '{expected_url_pattern}' not reached. "
                f"Current URL: {current_url}"
            ) from e

    @staticmethod
    def wait_for_network_idle(
        page: Page,
        timeout: int = settings.AJAX_TIMEOUT
    ) -> None:
        """
        Wait for network activity to finish (no active requests).

        Args:
            page: Playwright Page object
            timeout: Maximum wait time in milliseconds

        Example:
            >>> page.click("button")
            >>> SmartWaits.wait_for_network_idle(page)
        """
        try:
            page.wait_for_load_state("networkidle", timeout=timeout)
            logger.debug("Network idle achieved")
        except PlaywrightTimeoutError as e:
            logger.warning(f"Network did not become idle within {timeout}ms")
            raise

    @staticmethod
    def wait_for_dom_content_loaded(page: Page, timeout: int = settings.NAVIGATION_TIMEOUT) -> None:
        """
        Wait for DOM content to be fully loaded.

        Args:
            page: Playwright Page object
            timeout: Maximum wait time in milliseconds
        """
        try:
            page.wait_for_load_state("domcontentloaded", timeout=timeout)
            logger.debug("DOM content loaded")
        except PlaywrightTimeoutError as e:
            logger.error("DOM content did not load within timeout")
            raise

    @staticmethod
    def wait_for_text_content(
        locator: Locator,
        expected_text: str,
        timeout: int = settings.ELEMENT_WAIT_TIMEOUT
    ) -> None:
        """
        Wait for element to contain specific text.

        Args:
            locator: Playwright Locator object
            expected_text: Text that should appear in element
            timeout: Maximum wait time in milliseconds

        Example:
            >>> status = page.locator("#status")
            >>> SmartWaits.wait_for_text_content(status, "Success")
        """
        try:
            expect(locator).to_contain_text(expected_text, timeout=timeout)
            logger.debug(f"Text '{expected_text}' found in element")
        except AssertionError as e:
            actual_text = locator.text_content() or ""
            logger.error(
                f"Expected text '{expected_text}' not found. Actual: '{actual_text}'"
            )
            raise

    @staticmethod
    def wait_for_element_count(
        locator: Locator,
        expected_count: int,
        timeout: int = settings.ELEMENT_WAIT_TIMEOUT
    ) -> None:
        """
        Wait for specific number of matching elements.

        Args:
            locator: Playwright Locator object
            expected_count: Expected number of elements
            timeout: Maximum wait time in milliseconds

        Example:
            >>> items = page.locator(".list-item")
            >>> SmartWaits.wait_for_element_count(items, 5)
        """
        try:
            expect(locator).to_have_count(expected_count, timeout=timeout)
            logger.debug(f"Element count is {expected_count}")
        except AssertionError as e:
            actual_count = locator.count()
            logger.error(f"Expected {expected_count} elements, found {actual_count}")
            raise

    @staticmethod
    def wait_with_retry(
        action: Callable[[], Any],
        max_attempts: int = 3,
        delay_ms: int = 1000,
        acceptable_exceptions: tuple = (AssertionError, PlaywrightTimeoutError)
    ) -> Any:
        """
        Retry action if it fails, with configurable delay between attempts.

        Args:
            action: Callable to execute
            max_attempts: Maximum number of attempts
            delay_ms: Delay between attempts in milliseconds
            acceptable_exceptions: Exceptions that trigger retry

        Returns:
            Result of successful action execution

        Raises:
            Last exception if all attempts fail

        Example:
            >>> def click_flaky_button():
            ...     page.get_by_role("button", name="Submit").click()
            >>> SmartWaits.wait_with_retry(click_flaky_button, max_attempts=3)
        """
        last_exception = None

        for attempt in range(1, max_attempts + 1):
            try:
                result = action()
                if attempt > 1:
                    logger.info(f"Action succeeded on attempt {attempt}")
                return result
            except acceptable_exceptions as e:
                last_exception = e
                if attempt < max_attempts:
                    logger.warning(
                        f"Attempt {attempt}/{max_attempts} failed: {str(e)}. "
                        f"Retrying in {delay_ms}ms..."
                    )
                    time.sleep(delay_ms / 1000)
                else:
                    logger.error(f"All {max_attempts} attempts failed")

        raise last_exception

    @staticmethod
    def wait_for_no_loading_indicators(
        page: Page,
        loading_selector: str = "[data-testid='loading'], .loading-spinner, .MuiCircularProgress-root"
    ) -> None:
        """
        Wait for all loading indicators to disappear.

        Args:
            page: Playwright Page object
            loading_selector: CSS selector for loading indicators

        Example:
            >>> SmartWaits.wait_for_no_loading_indicators(page)
        """
        loading_indicators = page.locator(loading_selector)
        try:
            expect(loading_indicators).to_have_count(0, timeout=settings.AJAX_TIMEOUT)
            logger.debug("All loading indicators removed")
        except AssertionError:
            logger.warning("Loading indicators still present")
            # Don't fail - this is a soft wait