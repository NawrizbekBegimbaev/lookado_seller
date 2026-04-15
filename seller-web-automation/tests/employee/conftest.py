"""
Staff Management tests — isolated fixtures for parallel execution.

Fixtures use fresh_authenticated_page (function-scoped, isolated context).
"""

import pytest
import allure
from pages.employee_page import EmployeePage


# ================================================================================
# Fixtures
# ================================================================================

@pytest.fixture
def employee_page(fresh_authenticated_page) -> EmployeePage:
    """Navigate to staff list page and return EmployeePage instance."""
    page = fresh_authenticated_page

    # Navigate to dashboard first for clean state
    page.goto("https://staging-seller.greatmall.uz/dashboard",
              wait_until="networkidle", timeout=15000)

    # Select Zara shop which has staff management enabled
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
            page.wait_for_load_state("networkidle")

    ep = EmployeePage(page)
    ep.navigate()
    page.wait_for_load_state("networkidle")
    return ep


@pytest.fixture
def employee_create_page(fresh_authenticated_page) -> EmployeePage:
    """Navigate to staff creation form and return EmployeePage instance."""
    page = fresh_authenticated_page

    # Navigate to dashboard first for clean state
    page.goto("https://staging-seller.greatmall.uz/dashboard",
              wait_until="networkidle", timeout=15000)

    # Select Zara shop which has staff management enabled
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
            page.wait_for_load_state("networkidle")

    ep = EmployeePage(page)
    ep.navigate()
    page.wait_for_load_state("domcontentloaded")
    ep.click_add_employee()
    page.wait_for_load_state("domcontentloaded")
    return ep
