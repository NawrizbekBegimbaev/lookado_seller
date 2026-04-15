"""
Utilities module for test automation framework.

Provides reusable helper functions and classes for:
- Smart wait strategies
- Test data loading with caching
- Logging configuration
- Browser helpers
- JSON schema validation
"""

from utils.logger import setup_logger
from utils.waits import SmartWaits
from utils.test_data_loader import TestDataLoader
from utils.browser_helpers import BrowserHelpers
from utils.validators import TestDataValidator
from utils.data_generator import ProductDataGenerator

__all__ = [
    "setup_logger",
    "SmartWaits",
    "TestDataLoader",
    "BrowserHelpers",
    "TestDataValidator",
    "ProductDataGenerator"
]