"""
Centralized configuration management for test automation framework.

This module provides a single source of truth for all configuration settings,
including URLs, timeouts, browser options, and reporting settings.
"""

import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@dataclass
class Settings:
    """
    Application settings for test automation framework.

    All settings can be overridden via environment variables.
    """

    # ==================== Base URLs (UI) ====================
    # NOTE: Always use STAGING for testing, not DEV
    BASE_URL: str = os.getenv('BASE_URL', 'https://staging-seller.greatmall.uz')
    DEV_URL: str = 'https://dev-seller.greatmall.uz'
    STAGING_URL: str = 'https://staging-seller.greatmall.uz'
    PROD_URL: str = 'https://seller.greatmall.uz'

    # ==================== API URLs ====================
    # User Service API (authentication, user management, seller registration)
    # NOTE: Always use STAGING for testing, not DEV
    API_BASE_URL: str = os.getenv('API_BASE_URL', 'https://staging-api.greatmall.uz/user-api')
    API_DEV_URL: str = 'https://dev-api.greatmall.uz/user-api'
    API_STAGING_URL: str = 'https://staging-api.greatmall.uz/user-api'
    API_PROD_URL: str = 'https://api.aralash.uz/user-api'

    # Seller Service API (products, invoices, categories)
    # NOTE: Always use STAGING for testing, not DEV
    SELLER_API_BASE_URL: str = os.getenv('SELLER_API_BASE_URL', 'https://staging-api.greatmall.uz/seller-api')
    SELLER_API_DEV_URL: str = 'https://dev-api.greatmall.uz/seller-api'
    SELLER_API_STAGING_URL: str = 'https://staging-api.greatmall.uz/seller-api'
    SELLER_API_PROD_URL: str = 'https://api.aralash.uz/seller-api'

    # ==================== Browser Settings ====================
    BROWSER: str = os.getenv('BROWSER', 'chromium')  # chromium, firefox, webkit
    HEADLESS: bool = os.getenv('HEADLESS', 'false').lower() == 'true'
    SLOW_MO: int = int(os.getenv('SLOW_MO', '0'))  # Milliseconds to slow down operations

    # Browser viewport
    VIEWPORT_WIDTH: int = 1920
    VIEWPORT_HEIGHT: int = 1080

    # ==================== Timeouts (milliseconds) ====================
    DEFAULT_TIMEOUT: int = 10000  # 10 seconds
    NAVIGATION_TIMEOUT: int = 30000  # 30 seconds
    ELEMENT_WAIT_TIMEOUT: int = 10000  # 10 seconds
    AJAX_TIMEOUT: int = 30000  # 30 seconds for AJAX requests

    # UI Element timeouts
    SHORT_TIMEOUT: int = 2000   # 2 seconds - quick visibility checks
    MEDIUM_TIMEOUT: int = 5000  # 5 seconds - element appearance
    LONG_TIMEOUT: int = 10000   # 10 seconds - page loads, slow elements

    # ==================== Directories ====================
    PROJECT_ROOT: Path = Path(__file__).parent.parent
    TEST_DATA_DIR: Path = PROJECT_ROOT / "test_data"
    SCREENSHOTS_DIR: Path = PROJECT_ROOT / "screenshots"
    LOGS_DIR: Path = PROJECT_ROOT / "logs"
    REPORTS_DIR: Path = PROJECT_ROOT / "reports"

    # ==================== Reporting ====================
    # Allure
    ALLURE_RESULTS_DIR: str = "allure-results"
    ALLURE_REPORT_DIR: str = "allure-report"

    # Allure TestOps
    ALLURE_ENDPOINT: Optional[str] = os.getenv('ALLURE_ENDPOINT')
    ALLURE_TOKEN: Optional[str] = os.getenv('ALLURE_TOKEN')
    ALLURE_PROJECT_ID: Optional[str] = os.getenv('ALLURE_PROJECT_ID')

    # ==================== Test Credentials ====================
    # IMPORTANT: Never commit credentials to repository!
    # Use environment variables or secrets manager
    TEST_USER_EMAIL: str = os.getenv('TEST_USER_EMAIL', '')
    TEST_USER_PASSWORD: str = os.getenv('TEST_USER_PASSWORD', '')

    # ==================== Logging ====================
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOG_FILE_MAX_BYTES: int = 10 * 1024 * 1024  # 10MB
    LOG_BACKUP_COUNT: int = 5

    # ==================== Parallel Execution ====================
    PARALLEL_WORKERS: int = int(os.getenv('PARALLEL_WORKERS', '4'))

    # ==================== Feature Flags ====================
    ENABLE_SCREENSHOTS_ON_FAILURE: bool = True
    ENABLE_VIDEO_RECORDING: bool = os.getenv('ENABLE_VIDEO', 'false').lower() == 'true'
    ENABLE_CONSOLE_LOG_CAPTURE: bool = True
    ENABLE_NETWORK_HAR: bool = os.getenv('ENABLE_HAR', 'false').lower() == 'true'

    def __post_init__(self):
        """Create necessary directories after initialization."""
        self.SCREENSHOTS_DIR.mkdir(exist_ok=True, parents=True)
        self.LOGS_DIR.mkdir(exist_ok=True, parents=True)
        self.REPORTS_DIR.mkdir(exist_ok=True, parents=True)

    @classmethod
    def get_url_for_env(cls, env: str) -> str:
        """
        Get base URL for specified environment.

        Args:
            env: Environment name ('dev', 'staging', 'prod')

        Returns:
            Base URL for the environment

        Example:
            >>> Settings.get_url_for_env('staging')
            'https://staging-seller.greatmall.uz'
        """
        urls = {
            'dev': cls.BASE_URL,
            'staging': cls.STAGING_URL,
            'prod': cls.PROD_URL
        }
        return urls.get(env.lower(), cls.BASE_URL)

    @classmethod
    def get_api_url_for_env(cls, env: str) -> str:
        """
        Get API base URL for specified environment.

        Args:
            env: Environment name ('dev', 'staging', 'prod')

        Returns:
            API base URL for the environment
        """
        urls = {
            'dev': cls.API_BASE_URL,
            'staging': cls.API_STAGING_URL,
            'prod': cls.API_PROD_URL
        }
        return urls.get(env.lower(), cls.API_BASE_URL)

    @classmethod
    def get_seller_api_url_for_env(cls, env: str) -> str:
        """
        Get Seller API base URL for specified environment.

        Args:
            env: Environment name ('dev', 'staging', 'prod')

        Returns:
            Seller API base URL for the environment
        """
        urls = {
            'dev': cls.SELLER_API_BASE_URL,
            'staging': cls.SELLER_API_STAGING_URL,
            'prod': cls.SELLER_API_PROD_URL
        }
        return urls.get(env.lower(), cls.SELLER_API_BASE_URL)

    def get_browser_launch_options(self) -> dict:
        """
        Get browser launch options as dictionary.

        Returns:
            Dictionary of browser launch options
        """
        return {
            'headless': self.HEADLESS,
            'slow_mo': self.SLOW_MO,
            'args': [
                '--start-maximized',
                '--disable-blink-features=AutomationControlled',
            ]
        }

    def get_browser_context_options(self) -> dict:
        """
        Get browser context options as dictionary.

        Returns:
            Dictionary of browser context options
        """
        options = {
            # Use no_viewport=True with --start-maximized for full screen
            'no_viewport': True,
        }

        if self.ENABLE_VIDEO_RECORDING:
            options['record_video_dir'] = str(self.SCREENSHOTS_DIR / 'videos')

        if self.ENABLE_NETWORK_HAR:
            options['record_har_path'] = str(self.SCREENSHOTS_DIR / 'network.har')

        return options

    def get_browser_context_options_with_viewport(self) -> dict:
        """
        Get browser context options with fixed viewport (for headless mode).

        Returns:
            Dictionary of browser context options with viewport
        """
        options = {
            'viewport': {
                'width': self.VIEWPORT_WIDTH,
                'height': self.VIEWPORT_HEIGHT
            }
        }

        if self.ENABLE_VIDEO_RECORDING:
            options['record_video_dir'] = str(self.SCREENSHOTS_DIR / 'videos')

        if self.ENABLE_NETWORK_HAR:
            options['record_har_path'] = str(self.SCREENSHOTS_DIR / 'network.har')

        return options


# Global settings instance
# Use this throughout the project: from config import settings
settings = Settings()