"""
Products List Page Tests - Comprehensive test suite.

Tests for /dashboard/products page covering:
- UI elements and layout
- Search functionality
- Filtering and sorting
- Pagination
- Table interactions
- Bulk actions
- Security (XSS, SQL injection, etc.)
- Accessibility
- Performance
- E2E workflows

Total: ~278 tests
"""

import pytest
import json
import os
from playwright.sync_api import Page, expect

from pages.products_list_page import ProductsListPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils import setup_logger

logger = setup_logger(__name__)

# Load test data
TEST_DATA_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "test_data", "products_list_test_data.json"
)
with open(TEST_DATA_PATH, "r", encoding="utf-8") as f:
    TEST_DATA = json.load(f)


# ==================== FIXTURES ====================


@pytest.fixture
def products_page(fresh_authenticated_page: Page) -> ProductsListPage:
    """Navigate to products list page and return page object with Zara shop selected."""
    raw_page = fresh_authenticated_page

    # Always go to dashboard first to ensure clean state
    raw_page.goto("https://staging-seller.greatmall.uz/dashboard",
                  wait_until="domcontentloaded", timeout=15000)

    # Select Zara shop which has products
    shop_dropdown = raw_page.locator(
        "button:has-text('Active'), button:has-text('Faol'), "
        "button:has-text('Активный'), button:has-text('Test Shop')"
    ).first
    if shop_dropdown.is_visible(timeout=3000):
        shop_dropdown.click()
        raw_page.wait_for_load_state("domcontentloaded")
        zara_shop = raw_page.get_by_role("menuitem").filter(has_text="Zara").first
        if zara_shop.is_visible(timeout=2000):
            zara_shop.click()
            raw_page.wait_for_load_state("domcontentloaded")
            logger.info("Selected Zara shop for products list testing")

    page = ProductsListPage(raw_page)
    page.navigate()
    page.wait_for_loading_complete()
    return page
