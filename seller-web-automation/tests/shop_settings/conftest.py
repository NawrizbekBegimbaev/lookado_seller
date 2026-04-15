"""
Tests for Shop Settings page.
9 classes, ~41 methods, ~50+ test cases.

URL: /dashboard/settings

Uses fresh_authenticated_page (function-scoped, isolated context).
"""

import pytest
import allure
from pages.shop_settings_page import ShopSettingsPage
from pages.dashboard_page import DashboardPage


# ================================================================================
# Fixtures
# ================================================================================

@pytest.fixture
def shop_settings_page(fresh_authenticated_page) -> ShopSettingsPage:
    """Navigate to shop settings page (select Zara shop first, click Edit)."""
    page = fresh_authenticated_page

    # Navigate to dashboard first for clean state
    page.goto("https://staging-seller.greatmall.uz/dashboard",
              wait_until="domcontentloaded", timeout=15000)

    # Select a registered shop (Zara) that has settings
    shop_btn = page.locator(
        "button:has-text('Active'), button:has-text('Faol'), "
        "button:has-text('Активный'), button:has-text('Test Shop')"
    ).first
    if shop_btn.is_visible(timeout=3000):
        shop_btn.click()
        page.wait_for_load_state("domcontentloaded")
        zara = page.get_by_role("menuitem").filter(has_text="Zara").first
        if zara.is_visible(timeout=2000):
            zara.click()
            page.wait_for_load_state("domcontentloaded")

    ssp = ShopSettingsPage(page)

    # Navigate directly to shop settings (correct URL is /dashboard/settings)
    page.goto("https://staging-seller.greatmall.uz/dashboard/settings",
              wait_until="domcontentloaded", timeout=15000)

    # Wait for page content to render (read-only mode shows <p> elements, not inputs)
    page.wait_for_selector("button, p, h4, h6", state="visible", timeout=10000)

    # Click Edit button to switch from read-only to edit mode
    ssp.click_edit_button()

    return ssp
