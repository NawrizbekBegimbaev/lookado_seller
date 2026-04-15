"""
Orders Page Test Cases - Comprehensive coverage.
Tests UI elements, search, filters, tabs, pagination, security, accessibility.

URL: /dashboard/orders-management/orders?page=1&size=10

Uses fresh_authenticated_page (function-scoped, isolated context).
"""

import pytest
import logging
import allure
from pages.orders_page import OrdersPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


# ===============================
# Fixtures
# ===============================

@pytest.fixture
def orders_page(fresh_authenticated_page):
    """Function fixture: isolated page, navigate to orders page."""
    from config import settings

    page = fresh_authenticated_page

    # Navigate to dashboard (auth state handles login)
    page.goto(f"{settings.STAGING_URL}/dashboard", wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=15000)

    if "auth/login" in page.url:
        logger.warning("Cached auth state expired, re-authenticating")
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.perform_login("998001112233", "76543217")
        page.wait_for_load_state("load", timeout=15000)
        if "auth/login" in page.url:
            pytest.fail("PRECONDITION: Login failed for orders tests")

    # Select Zara shop (required for orders access)
    try:
        shop_btn = page.locator("button:has-text('Faol'), button:has-text('Active'), button:has-text('Активный')").first
        shop_btn.click()
        page.wait_for_load_state("domcontentloaded")
        page.get_by_role("menuitem", name="Zara").click()
        page.wait_for_load_state("networkidle")
        logger.info("Selected Zara shop for orders tests")
    except Exception as e:
        logger.warning(f"Could not select Zara shop: {e}")

    orders = OrdersPage(page)
    orders.navigate()
    page.wait_for_load_state("networkidle")

    assert orders.is_page_loaded(), \
        "PRECONDITION: Orders page failed to load"

    return orders
