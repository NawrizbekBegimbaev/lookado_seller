"""
Shop Create test fixtures.
Provides dashboard_page and shop_modal fixtures for all shop create tests.
Uses fresh_authenticated_page (function-scoped, isolated context).
"""
import pytest
import logging
from pages.dashboard_page import DashboardPage, ShopCreatePage

logger = logging.getLogger(__name__)


@pytest.fixture
def dashboard_page(fresh_authenticated_page, test_data):
    """
    Initialize dashboard page with isolated authenticated context.
    FAILS if dashboard is not accessible (not SKIPPED).
    """
    page = fresh_authenticated_page
    dashboard = DashboardPage(page)

    # Navigate to dashboard - FAIL if not accessible
    dashboard.navigate_to_dashboard()
    page.wait_for_load_state("networkidle", timeout=15000)

    # Verify we are on dashboard - FAIL if not
    assert "dashboard" in page.url.lower(), \
        f"FAILED: Expected dashboard URL, got {page.url}"

    return dashboard


@pytest.fixture
def shop_modal(dashboard_page) -> ShopCreatePage:
    """
    Navigate to shop create page via dashboard dropdown.
    FAILS if shop create page cannot be loaded.
    """
    page = dashboard_page.page
    shop_page = ShopCreatePage(page)

    # Navigate via dashboard dropdown (proven path)
    dashboard_page.open_shop_dropdown()
    page.wait_for_load_state("domcontentloaded")
    dashboard_page.click_add_shop()
    page.wait_for_load_state("networkidle", timeout=15000)

    # Verify page is loaded - FAIL if not
    assert shop_page.is_page_loaded(), \
        f"FAILED: Shop create page did not load. URL: {page.url}"

    yield shop_page
