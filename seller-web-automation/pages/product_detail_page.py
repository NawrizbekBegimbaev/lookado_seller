"""
Product Detail/Edit page object model.
Handles product viewing, editing, and deletion at /dashboard/products/[id].

Uses language-agnostic locators (URL patterns, roles, indices).
Inherits common navigation from BasePage.
"""

from typing import List, Optional
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage, logger


class ProductDetailPage(BasePage):
    """
    Page Object for Product Detail/Edit page.
    Manages product viewing, editing, and status operations.
    """

    PRODUCT_DETAIL_PATH = "/dashboard/products/"
    PRODUCTS_LIST_PATH = "/dashboard/products"

    def __init__(self, page: Page):
        """Initialize product detail page."""
        super().__init__(page)

    # ==================== NAVIGATION ====================

    def navigate_to_product(self, product_id: str) -> None:
        """Navigate to a specific product detail page."""
        logger.info(f"Navigating to product: {product_id}")
        self.navigate_to(f"{self.PRODUCT_DETAIL_PATH}{product_id}")
        self.page.wait_for_load_state("networkidle", timeout=15000)

    def select_shop(self, shop_name: str) -> None:
        """Select a specific shop from the header dropdown."""
        logger.info(f"Selecting shop: {shop_name}")
        try:
            shop_dropdown = self.page.locator("button").filter(
                has=self.page.locator("img")
            ).first
            if not shop_dropdown.is_visible(timeout=3000):
                shop_dropdown = self.page.locator("header button").first
            shop_dropdown.click()
            self.page.wait_for_load_state("domcontentloaded")

            shop_item = self.page.get_by_role("menuitem").filter(has_text=shop_name).first
            shop_item.click()
            self.wait_for_network_idle()
            logger.info(f"Shop '{shop_name}' selected")
        except Exception as e:
            logger.error(f"Failed to select shop: {str(e)}")

    def navigate_back_to_list(self) -> None:
        """Navigate back to products list."""
        back_btn = self.back_button
        if back_btn.is_visible(timeout=2000):
            back_btn.click()
            self.wait_for_network_idle()
        else:
            self.navigate_to(self.PRODUCTS_LIST_PATH)

    def is_on_detail_page(self) -> bool:
        """Check if currently on product detail page."""
        url = self.page.url
        return "/dashboard/products/" in url and "/add" not in url and "/create" not in url

    def get_product_id_from_url(self) -> str:
        """Extract product ID from current URL."""
        url = self.page.url
        if "/dashboard/products/" in url:
            parts = url.split("/dashboard/products/")[1]
            return parts.split("?")[0].split("/")[0]
        return ""

    # ==================== LOCATORS (Properties) ====================

    # --- Page Header ---
    @property
    def page_title(self) -> Locator:
        """Product name displayed as page title."""
        return self.page.locator("h4, h5, h6").first

    @property
    def back_button(self) -> Locator:
        """Back/return button to products list."""
        return self.page.locator("button:has(svg)").filter(
            has=self.page.locator("[data-testid='ArrowBackIcon'], [data-testid='ArrowBackIosIcon']")
        ).first.or_(
            self.page.locator("a[href*='/dashboard/products']").filter(has_text="").first
        )

    @property
    def status_badge(self) -> Locator:
        """Product status badge (Active/Inactive/Pending/Rejected)."""
        return self.page.locator(".MuiChip-root, .status-badge, [class*='badge']").first

    # --- Action Buttons ---
    @property
    def edit_button(self) -> Locator:
        """Edit product button."""
        return self.page.get_by_role("button", name="Edit").or_(
            self.page.get_by_role("button", name="Tahrirlash")
        ).or_(self.page.get_by_role("button", name="Редактировать"))

    @property
    def save_button(self) -> Locator:
        """Save/Update button."""
        return self.page.get_by_role("button", name="Save", exact=True).or_(
            self.page.get_by_role("button", name="Saqlash", exact=True)
        ).or_(self.page.get_by_role("button", name="Сохранить", exact=True)).or_(
            self.page.get_by_role("button", name="Сохранить и выйти")
        )

    @property
    def delete_button(self) -> Locator:
        """Delete product button."""
        return self.page.get_by_role("button", name="Delete").or_(
            self.page.get_by_role("button", name="O'chirish")
        ).or_(self.page.get_by_role("button", name="Удалить"))

    @property
    def cancel_button(self) -> Locator:
        """Cancel edit button."""
        return self.page.get_by_role("button", name="Cancel").or_(
            self.page.get_by_role("button", name="Bekor qilish")
        ).or_(self.page.get_by_role("button", name="Отмена"))

    # --- Product Info Fields ---
    @property
    def uz_name_field(self) -> Locator:
        """Product name in Uzbek."""
        return self.page.get_by_role("textbox", name="Nomi").or_(
            self.page.get_by_role("textbox", name="Name")
        ).first

    @property
    def ru_name_field(self) -> Locator:
        """Product name in Russian."""
        return self.page.get_by_role("textbox", name="Название").or_(
            self.page.get_by_role("textbox", name="Nomi")
        ).nth(1)

    @property
    def uz_description_field(self) -> Locator:
        """Product description in Uzbek."""
        return self.page.get_by_role("textbox", name="Tavsif").or_(
            self.page.get_by_role("textbox", name="Description")
        ).first

    @property
    def ru_description_field(self) -> Locator:
        """Product description in Russian."""
        return self.page.get_by_role("textbox", name="Описание").or_(
            self.page.get_by_role("textbox", name="Tavsif")
        ).nth(1)

    @property
    def category_field(self) -> Locator:
        """Category combobox/display."""
        return self.page.get_by_role("combobox").first

    @property
    def country_field(self) -> Locator:
        """Country of origin field."""
        return self.page.get_by_role("combobox", name="Davlat").or_(
            self.page.get_by_role("combobox", name="Country")
        ).or_(self.page.get_by_role("combobox", name="Страна"))

    @property
    def brand_field(self) -> Locator:
        """Brand/model combobox."""
        return self.page.get_by_role("combobox", name="Brend").or_(
            self.page.get_by_role("combobox", name="Brand")
        )

    # --- Price Fields ---
    @property
    def price_field(self) -> Locator:
        """Product price input."""
        return self.page.get_by_role("textbox", name="Narx").or_(
            self.page.get_by_role("textbox", name="Price")
        ).or_(self.page.get_by_role("textbox", name="Цена"))

    @property
    def discount_price_field(self) -> Locator:
        """Discounted price input."""
        return self.page.get_by_role("textbox", name="Chegirma").or_(
            self.page.get_by_role("textbox", name="Discount")
        ).or_(self.page.get_by_role("textbox", name="Скидка"))

    # --- SKU / Barcode ---
    @property
    def sku_field(self) -> Locator:
        """SKU input field."""
        return self.page.get_by_role("textbox", name="SKU").or_(
            self.page.locator("input[name*='sku']")
        )

    @property
    def barcode_field(self) -> Locator:
        """Barcode input field."""
        return self.page.get_by_role("textbox", name="Shtrix-kod").or_(
            self.page.get_by_role("textbox", name="Barcode")
        ).or_(self.page.locator("input[name*='barcode']"))

    # --- Images ---
    @property
    def product_images(self) -> Locator:
        """Product images displayed on page."""
        return self.page.locator("img[src*='product'], img[alt*='product'], .product-image")

    @property
    def image_upload_area(self) -> Locator:
        """Image upload drop zone or button."""
        return self.page.locator("input[type='file']").or_(
            self.page.locator("[class*='dropzone'], [class*='upload']")
        )

    @property
    def delete_image_buttons(self) -> Locator:
        """Delete buttons on individual images."""
        return self.page.locator("button[aria-label='Delete image'], button[aria-label='Remove']").or_(
            self.page.locator(".image-delete-btn, [data-testid='delete-image']")
        )

    # --- Tabs (if any) ---
    @property
    def info_tab(self) -> Locator:
        """Product info tab."""
        return self.page.get_by_role("tab", name="Info").or_(
            self.page.get_by_role("tab", name="Ma'lumot")
        )

    @property
    def variants_tab(self) -> Locator:
        """Product variants tab."""
        return self.page.get_by_role("tab", name="Variants").or_(
            self.page.get_by_role("tab", name="Variantlar")
        )

    @property
    def characteristics_tab(self) -> Locator:
        """Product characteristics tab."""
        return self.page.get_by_role("tab", name="Characteristics").or_(
            self.page.get_by_role("tab", name="Xususiyatlar")
        )

    # --- Variants Grid ---
    @property
    def variants_grid(self) -> Locator:
        """Variants data grid."""
        return self.page.locator(".MuiDataGrid-root")

    @property
    def variant_rows(self) -> Locator:
        """Variant grid rows."""
        return self.page.locator(".MuiDataGrid-row")

    # --- Delete Confirmation ---
    @property
    def confirm_delete_button(self) -> Locator:
        """Confirm delete button in modal."""
        return self.page.get_by_role("button", name="Delete").or_(
            self.page.get_by_role("button", name="O'chirish")
        ).or_(self.page.get_by_role("button", name="Удалить")).last

    @property
    def cancel_delete_button(self) -> Locator:
        """Cancel delete button in modal."""
        return self.page.get_by_role("button", name="Cancel").or_(
            self.page.get_by_role("button", name="Bekor")
        ).last

    @property
    def delete_confirmation_dialog(self) -> Locator:
        """Delete confirmation modal/dialog."""
        return self.page.get_by_role("dialog").or_(
            self.page.locator(".MuiDialog-root, .MuiModal-root")
        )

    # ==================== ACTION METHODS ====================

    def click_edit(self) -> None:
        """Click edit button to enter edit mode."""
        logger.info("Clicking edit button")
        self.edit_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_save(self) -> None:
        """Click save button to save changes."""
        logger.info("Clicking save button")
        self.save_button.click()
        self.wait_for_network_idle()

    def click_delete(self) -> None:
        """Click delete button."""
        logger.info("Clicking delete button")
        self.delete_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    def confirm_delete(self) -> None:
        """Confirm product deletion in dialog."""
        logger.info("Confirming delete")
        self.confirm_delete_button.click()
        self.wait_for_network_idle()

    def cancel_delete(self) -> None:
        """Cancel product deletion."""
        logger.info("Canceling delete")
        self.cancel_delete_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_cancel(self) -> None:
        """Click cancel button to discard edits."""
        logger.info("Clicking cancel button")
        self.cancel_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    # ==================== FIELD METHODS ====================

    def fill_uz_name(self, name: str) -> None:
        """Fill product UZ name."""
        self.uz_name_field.fill(name)

    def fill_ru_name(self, name: str) -> None:
        """Fill product RU name."""
        self.ru_name_field.fill(name)

    def fill_uz_description(self, desc: str) -> None:
        """Fill product UZ description."""
        self.uz_description_field.fill(desc)

    def fill_ru_description(self, desc: str) -> None:
        """Fill product RU description."""
        self.ru_description_field.fill(desc)

    def fill_price(self, price: str) -> None:
        """Fill product price."""
        self.price_field.fill(price)

    def fill_discount_price(self, discount: str) -> None:
        """Fill discounted price."""
        self.discount_price_field.fill(discount)

    def fill_sku(self, sku: str) -> None:
        """Fill SKU field."""
        self.sku_field.fill(sku)

    def fill_barcode(self, barcode: str) -> None:
        """Fill barcode field."""
        self.barcode_field.fill(barcode)

    def get_uz_name_value(self) -> str:
        """Get current UZ name value."""
        try:
            return self.uz_name_field.input_value()
        except Exception:
            return ""

    def get_ru_name_value(self) -> str:
        """Get current RU name value."""
        try:
            return self.ru_name_field.input_value()
        except Exception:
            return ""

    def get_uz_description_value(self) -> str:
        """Get current UZ description value."""
        try:
            return self.uz_description_field.input_value()
        except Exception:
            return ""

    def get_ru_description_value(self) -> str:
        """Get current RU description value."""
        try:
            return self.ru_description_field.input_value()
        except Exception:
            return ""

    def get_price_value(self) -> str:
        """Get current price value."""
        try:
            return self.price_field.input_value()
        except Exception:
            return ""

    def get_sku_value(self) -> str:
        """Get current SKU value."""
        try:
            return self.sku_field.input_value()
        except Exception:
            return ""

    def get_barcode_value(self) -> str:
        """Get current barcode value."""
        try:
            return self.barcode_field.input_value()
        except Exception:
            return ""

    def get_status_text(self) -> str:
        """Get product status text from badge."""
        try:
            if self.status_badge.is_visible(timeout=2000):
                return self.status_badge.inner_text().strip()
        except Exception:
            pass
        return ""

    # ==================== VALIDATION METHODS ====================

    def get_validation_error_count(self) -> int:
        """Get count of validation errors on page."""
        return self.page.locator(".MuiFormHelperText-root.Mui-error").count()

    def has_validation_errors(self) -> bool:
        """Check if there are any validation errors."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> List[str]:
        """Get all validation error messages."""
        errors = []
        elements = self.page.locator(".MuiFormHelperText-root.Mui-error").all()
        for el in elements:
            try:
                text = el.text_content()
                if text:
                    errors.append(text.strip())
            except Exception:
                pass
        return errors

    def get_error_for_field(self, field_label: str) -> Optional[str]:
        """Get validation error for a specific field by label."""
        try:
            field = self.page.get_by_role("textbox", name=field_label)
            if not field.is_visible(timeout=1000):
                field = self.page.get_by_role("combobox", name=field_label)
            parent = field.locator("xpath=ancestor::div[contains(@class, 'MuiFormControl')]")
            error = parent.locator(".MuiFormHelperText-root.Mui-error")
            if error.is_visible(timeout=500):
                return error.text_content()
        except Exception:
            pass
        return None

    def has_error_for_field(self, field_label: str) -> bool:
        """Check if a specific field has validation error."""
        return self.get_error_for_field(field_label) is not None

    # ==================== STATE CHECKS ====================

    def is_in_edit_mode(self) -> bool:
        """Check if page is in edit mode (fields are editable)."""
        try:
            if self.save_button.is_visible(timeout=1000):
                return True
            # Check if fields are enabled
            if self.uz_name_field.is_visible(timeout=1000):
                return self.uz_name_field.is_enabled()
        except Exception:
            pass
        return False

    def is_page_loaded(self) -> bool:
        """Check if product detail page loaded successfully."""
        try:
            return self.is_on_detail_page() and (
                self.page_title.is_visible(timeout=3000) or
                self.uz_name_field.is_visible(timeout=3000) or
                self.edit_button.is_visible(timeout=3000)
            )
        except Exception:
            return False

    def has_product_data(self) -> bool:
        """Check if product data is displayed (not empty page)."""
        try:
            name = self.get_uz_name_value()
            if name:
                return True
            # Check if any text content is present in main area
            main_text = self.page.locator("main").inner_text()
            return len(main_text.strip()) > 50
        except Exception:
            return False

    def get_variant_count(self) -> int:
        """Get number of variants displayed."""
        try:
            return self.variant_rows.count()
        except Exception:
            return 0

    def get_image_count(self) -> int:
        """Get number of product images displayed."""
        try:
            return self.product_images.count()
        except Exception:
            return 0

    def is_save_button_enabled(self) -> bool:
        """Check if save button is enabled."""
        try:
            return self.save_button.is_visible(timeout=1000) and self.save_button.is_enabled()
        except Exception:
            return False

    def is_delete_button_visible(self) -> bool:
        """Check if delete button is visible."""
        try:
            return self.delete_button.is_visible(timeout=2000)
        except Exception:
            return False

    def get_all_textbox_values(self) -> dict:
        """Get values of all visible textbox fields."""
        values = {}
        textboxes = self.page.get_by_role("textbox").all()
        for i, tb in enumerate(textboxes):
            try:
                if tb.is_visible(timeout=500):
                    name = tb.get_attribute("name") or tb.get_attribute("aria-label") or f"field_{i}"
                    values[name] = tb.input_value()
            except Exception:
                pass
        return values

    def get_combobox_count(self) -> int:
        """Get count of comboboxes on page."""
        return self.page.get_by_role("combobox").count()

    def get_textbox_count(self) -> int:
        """Get count of textboxes on page."""
        return self.page.get_by_role("textbox").count()

    def wait_for_save_complete(self, timeout: int = 5000) -> bool:
        """Wait for save operation to complete (loading indicator disappears)."""
        try:
            # Wait for any loading spinner to disappear
            self.page.locator(".MuiCircularProgress-root").wait_for(state="hidden", timeout=timeout)
            return True
        except Exception:
            return True  # No spinner found, assume save complete

    def get_toast_message(self) -> str:
        """Get toast/snackbar notification message."""
        try:
            toast = self.page.locator(".MuiSnackbar-root, .MuiAlert-message, [role='alert']").first
            if toast.is_visible(timeout=3000):
                return toast.inner_text().strip()
        except Exception:
            pass
        return ""
