"""
Browser helper utilities for Playwright automation.

Provides reusable helper methods for common browser operations:
- Screenshot capture
- Console log collection
- Network request monitoring
- Cookie and localStorage management
- File downloads and uploads
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from playwright.sync_api import Page, BrowserContext, Download
from config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class BrowserHelpers:
    """
    Collection of browser helper utilities for test automation.
    """

    @staticmethod
    def capture_screenshot(
        page: Page,
        name: str,
        full_page: bool = True
    ) -> Path:
        """
        Capture screenshot of current page state.

        Args:
            page: Playwright Page object
            name: Screenshot name (without extension)
            full_page: Whether to capture full scrollable page

        Returns:
            Path to saved screenshot

        Example:
            >>> screenshot_path = BrowserHelpers.capture_screenshot(page, "login_error")
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        screenshot_path = settings.SCREENSHOTS_DIR / filename

        try:
            page.screenshot(path=str(screenshot_path), full_page=full_page)
            logger.info(f"Screenshot saved: {screenshot_path.name}")
            return screenshot_path
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
            raise

    @staticmethod
    def get_console_logs(page: Page) -> List[Dict[str, Any]]:
        """
        Get captured console logs from page.

        Requires console logging to be set up via fixture.

        Args:
            page: Playwright Page object

        Returns:
            List of console log entries

        Example:
            >>> logs = BrowserHelpers.get_console_logs(page)
            >>> errors = [log for log in logs if log['type'] == 'error']
        """
        if hasattr(page, '_console_logs'):
            return page._console_logs
        else:
            logger.warning("Console logs not available. Set up capture_console_logs fixture")
            return []

    @staticmethod
    def get_failed_requests(page: Page) -> List[Dict[str, Any]]:
        """
        Get captured failed network requests (status >= 400).

        Requires network monitoring to be set up via fixture.

        Args:
            page: Playwright Page object

        Returns:
            List of failed request entries

        Example:
            >>> failed = BrowserHelpers.get_failed_requests(page)
            >>> for req in failed:
            ...     print(f"{req['method']} {req['url']} - {req['status']}")
        """
        if hasattr(page, '_failed_requests'):
            return page._failed_requests
        else:
            logger.warning("Failed requests not available. Set up capture_network_requests fixture")
            return []

    @staticmethod
    def clear_browser_storage(page: Page) -> None:
        """
        Clear all browser storage (cookies, localStorage, sessionStorage).

        Args:
            page: Playwright Page object

        Example:
            >>> BrowserHelpers.clear_browser_storage(page)
        """
        try:
            # Clear cookies
            page.context.clear_cookies()

            # Clear localStorage and sessionStorage
            page.evaluate("""
                () => {
                    window.localStorage.clear();
                    window.sessionStorage.clear();
                }
            """)

            logger.info("Browser storage cleared (cookies, localStorage, sessionStorage)")
        except Exception as e:
            logger.error(f"Failed to clear browser storage: {e}")
            raise

    @staticmethod
    def get_local_storage(page: Page) -> Dict[str, str]:
        """
        Get all localStorage items.

        Args:
            page: Playwright Page object

        Returns:
            Dictionary of localStorage items

        Example:
            >>> storage = BrowserHelpers.get_local_storage(page)
            >>> token = storage.get('auth_token')
        """
        try:
            storage = page.evaluate("""
                () => {
                    let items = {};
                    for (let i = 0; i < window.localStorage.length; i++) {
                        let key = window.localStorage.key(i);
                        items[key] = window.localStorage.getItem(key);
                    }
                    return items;
                }
            """)
            return storage
        except Exception as e:
            logger.error(f"Failed to get localStorage: {e}")
            return {}

    @staticmethod
    def set_local_storage(page: Page, key: str, value: str) -> None:
        """
        Set localStorage item.

        Args:
            page: Playwright Page object
            key: Storage key
            value: Storage value

        Example:
            >>> BrowserHelpers.set_local_storage(page, 'theme', 'dark')
        """
        try:
            page.evaluate(
                f"window.localStorage.setItem('{key}', '{value}')"
            )
            logger.debug(f"Set localStorage: {key} = {value}")
        except Exception as e:
            logger.error(f"Failed to set localStorage: {e}")
            raise

    @staticmethod
    def get_cookies(context: BrowserContext) -> List[Dict[str, Any]]:
        """
        Get all cookies from browser context.

        Args:
            context: Playwright BrowserContext object

        Returns:
            List of cookie dictionaries

        Example:
            >>> cookies = BrowserHelpers.get_cookies(page.context)
            >>> session_cookie = next(c for c in cookies if c['name'] == 'session_id')
        """
        try:
            cookies = context.cookies()
            logger.debug(f"Retrieved {len(cookies)} cookies")
            return cookies
        except Exception as e:
            logger.error(f"Failed to get cookies: {e}")
            return []

    @staticmethod
    def set_cookie(
        context: BrowserContext,
        name: str,
        value: str,
        url: Optional[str] = None
    ) -> None:
        """
        Set a cookie in browser context.

        Args:
            context: Playwright BrowserContext object
            name: Cookie name
            value: Cookie value
            url: Optional URL scope for cookie

        Example:
            >>> BrowserHelpers.set_cookie(
            ...     page.context,
            ...     'session_id',
            ...     'abc123',
            ...     url='https://example.com'
            ... )
        """
        try:
            cookie = {
                'name': name,
                'value': value,
                'url': url or settings.BASE_URL
            }
            context.add_cookies([cookie])
            logger.debug(f"Set cookie: {name}")
        except Exception as e:
            logger.error(f"Failed to set cookie: {e}")
            raise

    @staticmethod
    def wait_for_download(page: Page, trigger_action: callable) -> Download:
        """
        Wait for file download triggered by action.

        Args:
            page: Playwright Page object
            trigger_action: Callable that triggers download (e.g., button click)

        Returns:
            Download object

        Example:
            >>> def click_download():
            ...     page.get_by_role("button", name="Download").click()
            >>> download = BrowserHelpers.wait_for_download(page, click_download)
            >>> download.save_as("/path/to/file.pdf")
        """
        with page.expect_download() as download_info:
            trigger_action()

        download = download_info.value
        logger.info(f"Download started: {download.suggested_filename}")
        return download

    @staticmethod
    def upload_file(page: Page, file_input_selector: str, file_path: str) -> None:
        """
        Upload file to file input element.

        Args:
            page: Playwright Page object
            file_input_selector: Selector for file input element
            file_path: Path to file to upload

        Example:
            >>> BrowserHelpers.upload_file(
            ...     page,
            ...     "input[type='file']",
            ...     "/path/to/document.pdf"
            ... )
        """
        try:
            file_input = page.locator(file_input_selector)
            file_input.set_input_files(file_path)
            logger.info(f"File uploaded: {Path(file_path).name}")
        except Exception as e:
            logger.error(f"Failed to upload file: {e}")
            raise

    @staticmethod
    def execute_script(page: Page, script: str) -> Any:
        """
        Execute JavaScript on page.

        Args:
            page: Playwright Page object
            script: JavaScript code to execute

        Returns:
            Result of script execution

        Example:
            >>> title = BrowserHelpers.execute_script(page, "return document.title")
        """
        try:
            result = page.evaluate(script)
            logger.debug(f"Executed script: {script[:50]}...")
            return result
        except Exception as e:
            logger.error(f"Failed to execute script: {e}")
            raise

    @staticmethod
    def scroll_to_element(page: Page, selector: str) -> None:
        """
        Scroll element into view.

        Args:
            page: Playwright Page object
            selector: CSS selector for element

        Example:
            >>> BrowserHelpers.scroll_to_element(page, "#footer")
        """
        try:
            page.locator(selector).scroll_into_view_if_needed()
            logger.debug(f"Scrolled to element: {selector}")
        except Exception as e:
            logger.error(f"Failed to scroll to element: {e}")
            raise

    @staticmethod
    def get_viewport_size(page: Page) -> Dict[str, int]:
        """
        Get current viewport dimensions.

        Args:
            page: Playwright Page object

        Returns:
            Dictionary with 'width' and 'height' keys

        Example:
            >>> size = BrowserHelpers.get_viewport_size(page)
            >>> print(f"{size['width']}x{size['height']}")
        """
        viewport = page.viewport_size
        logger.debug(f"Viewport size: {viewport}")
        return viewport

    @staticmethod
    def set_viewport_size(page: Page, width: int, height: int) -> None:
        """
        Set viewport size.

        Args:
            page: Playwright Page object
            width: Viewport width in pixels
            height: Viewport height in pixels

        Example:
            >>> BrowserHelpers.set_viewport_size(page, 1280, 720)
        """
        try:
            page.set_viewport_size({"width": width, "height": height})
            logger.info(f"Viewport size set to: {width}x{height}")
        except Exception as e:
            logger.error(f"Failed to set viewport size: {e}")
            raise