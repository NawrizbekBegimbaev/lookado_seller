"""
Shared helper functions for product create tests.
Multi-language field locators used across multiple test files.
"""


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
