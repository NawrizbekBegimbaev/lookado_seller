"""
Returns Test Cases - Returns Management Functionality.
Tests returns listing, tabs, filtering, pagination.
Follows KISS, DRY, SOLID principles with POM pattern.

NOTE: This page has NO search field. Only tabs and filters.

Uses fresh_authenticated_page (function-scoped, isolated context).
"""

import pytest
import logging
import allure
from playwright.sync_api import expect
from pages.returns_page import ReturnsPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


@pytest.fixture
def returns_page(fresh_authenticated_page) -> ReturnsPage:
    """Navigate to returns page (isolated context per test)."""
    from config import settings

    page = fresh_authenticated_page

    page.goto(f"{settings.STAGING_URL}/dashboard", wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle", timeout=15000)

    if "auth/login" in page.url:
        logger.warning("Cached auth state expired, re-authenticating")
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.perform_login("998001112233", "76543217")
        page.wait_for_load_state("load", timeout=15000)
        if "auth/login" in page.url:
            pytest.fail("PRECONDITION: Login failed for returns tests")

    rp = ReturnsPage(page)
    rp.navigate()
    page.wait_for_load_state("networkidle")
    return rp
