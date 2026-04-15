"""
Order Detail Page Tests.
Tests for /dashboard/orders-management/orders/[order_id] page.

8 classes, 36 methods, ~40 test cases.
Page Object: pages/order_detail_page.py

Uses fresh_authenticated_page (function-scoped, isolated context).
"""

import logging
import pytest
import allure
from pages.order_detail_page import OrderDetailPage
from pages.orders_page import OrdersPage

logger = logging.getLogger(__name__)


# ================================================================================
# Fixtures
# ================================================================================

@pytest.fixture
def order_detail_page(fresh_authenticated_page) -> OrderDetailPage:
    """Navigate to first available order detail page."""
    page = fresh_authenticated_page

    # Select Zara shop first (has orders)
    page.goto("https://staging-seller.greatmall.uz/dashboard")
    page.wait_for_load_state("networkidle")
    try:
        shop_btn = page.locator("button:has-text('Faol'), button:has-text('Active'), button:has-text('Активный')").first
        if shop_btn.is_visible(timeout=3000):
            shop_btn.click()
            page.wait_for_load_state("domcontentloaded")
            page.get_by_role("menuitem", name="Zara").click()
            page.wait_for_load_state("networkidle")
    except Exception as e:
        logger.warning(f"Shop selection failed: {e}")

    orders_page = OrdersPage(page)

    # Navigate to orders list first
    orders_page.navigate()
    page.wait_for_load_state("networkidle")

    # Get first order ID
    order_rows = page.locator(".MuiDataGrid-row[data-id]").all()
    if len(order_rows) == 0:
        pytest.fail("No orders available for testing")

    order_id = order_rows[0].get_attribute("data-id")

    # Navigate to order detail
    odp = OrderDetailPage(page)
    odp.navigate_to_order_detail(order_id)
    page.wait_for_load_state("networkidle")

    return odp


@pytest.fixture
def get_first_order_id(fresh_authenticated_page) -> str:
    """Get first order ID from orders list."""
    page = fresh_authenticated_page

    # Select Zara shop first (has orders)
    page.goto("https://staging-seller.greatmall.uz/dashboard")
    page.wait_for_load_state("networkidle")
    try:
        shop_btn = page.locator("button:has-text('Faol'), button:has-text('Active'), button:has-text('Активный')").first
        if shop_btn.is_visible(timeout=3000):
            shop_btn.click()
            page.wait_for_load_state("domcontentloaded")
            page.get_by_role("menuitem", name="Zara").click()
            page.wait_for_load_state("networkidle")
    except Exception as e:
        logger.warning(f"Shop selection failed: {e}")

    orders_page = OrdersPage(page)
    orders_page.navigate()
    page.wait_for_load_state("networkidle")

    order_rows = page.locator(".MuiDataGrid-row[data-id]").all()
    if len(order_rows) == 0:
        pytest.fail("No orders available for testing")

    return order_rows[0].get_attribute("data-id")
