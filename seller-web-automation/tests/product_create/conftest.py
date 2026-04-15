"""
Product Create test fixtures and helpers.
Shared across all product_create test files.
Uses fresh_authenticated_page (function-scoped, isolated context).
"""

import pytest
import logging
import os

from pages.productcreate_page import ProductCreatePage
from pages.login_page import LoginPage
from config.settings import Settings
from utils import ProductDataGenerator

logger = logging.getLogger(__name__)

# Test data paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESOURCES_PATH = os.path.join(PROJECT_ROOT, "test_data", "resources")


# =============================================================================
# MULTI-LANGUAGE FIELD HELPERS
# =============================================================================

def get_uz_name_field(page):
    """Get UZ product name field (multi-language: EN/UZ)."""
    return page.locator(
        "input[name='nameUz']"
    ).or_(
        page.get_by_role("textbox", name="Product name in Uzbek")
    ).or_(
        page.get_by_role("textbox", name="Mahsulot nomi o'zbek tilida")
    ).first


def get_uz_desc_field(page):
    """Get UZ description field (multi-language: EN/UZ)."""
    return page.locator(
        "textarea[name='descriptionUz'], input[name='descriptionUz']"
    ).or_(
        page.get_by_role("textbox", name="Description in Uzbek")
    ).or_(
        page.get_by_role("textbox", name="O'zbek tilidagi tavsif")
    ).first


def get_ru_desc_field(page):
    """Get RU description field (multi-language: EN/UZ)."""
    return page.locator(
        "textarea[name='descriptionRu'], input[name='descriptionRu']"
    ).or_(
        page.get_by_role("textbox", name="Description in Russian")
    ).or_(
        page.get_by_role("textbox", name="Rus tilidagi tavsif")
    ).first


def get_price_field(page):
    """Get regular price field (multi-language: EN/UZ)."""
    return page.locator(
        "input[name='price']"
    ).or_(
        page.get_by_role("textbox", name="Regular price (UZS)")
    ).or_(
        page.get_by_role("textbox", name="Oddiy narx (UZS)")
    ).first


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture
def staging_session(fresh_authenticated_page, test_data):
    """Staging session fixture - isolated page with cached auth state."""
    page = fresh_authenticated_page
    staging_data = test_data.get("staging", {})

    product_page = ProductCreatePage(page)
    return page, product_page, staging_data


@pytest.fixture
def product_create_page(staging_session) -> ProductCreatePage:
    """Navigate to product create page Step 1."""
    page, product_page, staging_data = staging_session

    from config import settings

    # Navigate to dashboard
    page.goto(f"{settings.STAGING_URL}/dashboard", wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")

    # Select Zara shop
    try:
        shop_btn = page.locator(
            "button:has-text('Faol'), button:has-text('Active'), button:has-text('Активный')"
        ).first
        if shop_btn.is_visible(timeout=5000):
            shop_btn.click()
            page.wait_for_load_state("domcontentloaded")
            zara_item = page.get_by_role("menuitem", name="Zara")
            zara_item.wait_for(state="visible", timeout=5000)
            zara_item.click()
            page.wait_for_load_state("networkidle")
            logger.info("Zara shop selected successfully")
    except Exception as e:
        logger.warning(f"Shop selection failed: {e}")

    # Navigate directly to single product create page
    page.goto(f"{settings.STAGING_URL}/dashboard/products/create", wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")

    return product_page


@pytest.fixture
def product_on_step2(product_create_page, test_data) -> ProductCreatePage:
    """Navigate to Step 2 (Variant/SKU)."""
    product_page = product_create_page
    data = ProductDataGenerator.generate_staging_product(product_type="jacket")

    product_page.select_category_from_combobox(data["category_path"])
    product_page.select_ikpu_from_combobox(data["ikpu_search"])
    product_page.select_country_from_combobox(data["country"])
    product_page.select_brand_from_combobox(data["brand"])

    product_page.fill_product_names_staging(
        uz_name=data["uz_name"],
        uz_desc=data["uz_description"],
        ru_name=data["ru_name"],
        ru_desc=data["ru_description"]
    )

    product_page.select_model_from_combobox()

    product_page.click_next_button()
    product_page.page.wait_for_load_state("networkidle")

    sku_field = product_page.page.locator("input[name='variant.sku']")
    sku_field.wait_for(state="visible", timeout=15000)
    logger.info("Confirmed on Step 2 (variant.sku field visible)")

    return product_page


@pytest.fixture
def product_on_step3(product_on_step2) -> ProductCreatePage:
    """Navigate to Step 3 (Image Upload)."""
    product_page = product_on_step2
    data = ProductDataGenerator.generate_staging_product(product_type="jacket")

    product_page.fill_variant_fields_staging(
        sku=data["sku"],
        price=data["price"],
        discount_price=data["discount_price"],
        width=data["width"],
        length=data["length"],
        height=data["height"],
        weight=data["weight"],
        barcode=data["barcode"]
    )

    product_page.click_next_button()
    product_page.page.wait_for_load_state("networkidle")

    return product_page
