"""
Tests for Profile Settings page.
9 classes, ~43 methods, ~50+ test cases.

URL: /dashboard/settings or /dashboard/profile

Uses fresh_authenticated_page (function-scoped, isolated context).
"""

import pytest
import allure
from pages.profile_settings_page import ProfileSettingsPage


# ================================================================================
# Fixtures
# ================================================================================

@pytest.fixture
def profile_settings_page(fresh_authenticated_page) -> ProfileSettingsPage:
    """Navigate to profile settings page (tries multiple paths)."""
    page = fresh_authenticated_page

    # Navigate to dashboard first
    page.goto("https://staging-seller.greatmall.uz/dashboard",
              wait_until="networkidle", timeout=15000)

    psp = ProfileSettingsPage(page)
    # Try settings path first, fall back to profile path
    psp.navigate_to_settings()
    page.wait_for_load_state("networkidle")
    # If redirected to login or become-seller, try profile path
    if "/auth/login" in page.url:
        psp.navigate_to_profile()
        page.wait_for_load_state("networkidle")
    return psp
