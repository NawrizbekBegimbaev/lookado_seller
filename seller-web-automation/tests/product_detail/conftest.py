"""
Product Detail/Edit Page Tests - Comprehensive test suite.

Tests for /dashboard/products/[id] page covering:
- UI elements and layout
- Edit functionality
- Field validation (empty, boundary, invalid)
- Security (XSS, SQL injection)
- Price/Discount validation
- Delete workflow
- Session and accessibility
- Whitespace handling
- Robustness

Total: ~70 tests

Uses fresh_authenticated_page (function-scoped, isolated context).
"""

import pytest
import json
import os
import allure
from playwright.sync_api import Page

from pages.product_detail_page import ProductDetailPage
from pages.products_list_page import ProductsListPage
from pages.login_page import LoginPage
from utils import setup_logger, TestDataLoader

logger = setup_logger(__name__)


# ==================== FIXTURES ====================


@pytest.fixture
def detail_page(fresh_authenticated_page):
    """Navigate to first available product detail page (isolated context)."""
    from config import settings

    page = fresh_authenticated_page

    # Load test data
    data_path = os.path.join(
        os.path.dirname(__file__), "..", "..", "test_data", "product_detail_test_data.json"
    )
    with open(data_path, "r", encoding="utf-8") as f:
        test_data = json.load(f)

    staging = test_data.get("staging", {})
    shop_name = staging.get("shop_name", "Zara")

    # Navigate to dashboard (auth state handles login)
    page.goto(f"{settings.STAGING_URL}/dashboard", wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=15000)

    if "auth/login" in page.url:
        logger.warning("Cached auth state expired, re-authenticating")
        credentials = staging.get("credentials", {})
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.perform_login(
            email=credentials.get("email", "998001112233"),
            password=credentials.get("password", "76543217")
        )
        page.wait_for_load_state("networkidle")

    # Select shop
    product_page = ProductDetailPage(page)
    product_page.select_shop(shop_name)
    page.wait_for_load_state("networkidle")

    # Navigate to products list
    page.goto(f"{settings.STAGING_URL}/dashboard/products")
    page.wait_for_load_state("networkidle")

    # Re-authenticate if session expired
    if "auth/login" in page.url:
        logger.warning("Session expired, re-authenticating for product_detail tests")
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.perform_login("998001112233", "76543217")
        page.wait_for_load_state("load", timeout=15000)
        page.goto(f"{settings.STAGING_URL}/dashboard/products")
        page.wait_for_load_state("networkidle")

    # Check if there are products (not redirected to /add)
    if "/products/add" in page.url:
        pytest.fail("PRECONDITION: No products available in selected shop for testing")

    # Products are displayed as nested MuiCard cards inside a container card
    product_cards = page.locator(".MuiCard-root .MuiCard-root")
    product_cards.first.wait_for(state="visible", timeout=10000)
    card_count = product_cards.count()
    assert card_count > 0, "PRECONDITION: No product cards found in products list"

    # Click the first product card to get its URL, then navigate directly
    # (SPA click doesn't always fully render the detail page)
    product_cards.first.click()
    page.wait_for_url("**/products/**", timeout=10000)
    product_url = page.url
    page.goto(product_url, wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")

    assert product_page.is_on_detail_page(), \
        f"PRECONDITION: Failed to navigate to product detail, URL: {page.url}"

    return product_page, test_data


@pytest.fixture
def test_data():
    """Load product detail test data."""
    data_path = os.path.join(
        os.path.dirname(__file__), "..", "..", "test_data", "product_detail_test_data.json"
    )
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)
