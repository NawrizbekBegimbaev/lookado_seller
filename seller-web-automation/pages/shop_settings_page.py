"""
Shop Settings Page Object Model.
Handles shop settings interactions and configurations.
Follows KISS, DRY, SOLID principles.
"""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage, logger


class ShopSettingsPage(BasePage):
    """
    Shop Settings page object model.
    Handles shop configuration, editing, and management.
    """

    # URL paths
    SHOP_SETTINGS_PATH = "/dashboard/settings"
    SHOP_SETTINGS_ALT_PATH = "/dashboard/shop/settings"

    def __init__(self, page: Page):
        """Initialize shop settings page."""
        super().__init__(page)
        self._init_locators()

    def _init_locators(self) -> None:
        """Initialize page locators."""
        # Navigation
        self.settings_nav_link = self.page.locator("a:has-text('Настройки магазина')").or_(
            self.page.locator("a:has-text('Shop Settings')").or_(
            self.page.locator("a:has-text('Sozlamalar')"))
        )

        # Edit button (fields are read-only until Edit is clicked)
        self.edit_btn = self.page.get_by_role("button", name="Редактировать").or_(
            self.page.get_by_role("button", name="Edit").or_(
            self.page.get_by_role("button", name="Tahrirlash"))
        )

        # Shop info form - field name may vary
        self.shop_name_input = self.page.locator("input[name='title']").or_(
            self.page.locator("input[name='name']")
        ).or_(self.page.locator("input[name='shopName']")).or_(
            self.page.get_by_label("Shop name")
        ).or_(self.page.get_by_label("Название магазина")).or_(
            self.page.get_by_label("Do'kon nomi")
        )
        self.shop_slug_input = self.page.locator("input[name='slug']")
        self.shop_sku_input = self.page.locator("input[name='sku']")
        self.description_uz_input = self.page.locator("textarea[name='descriptionUz']")
        self.description_ru_input = self.page.locator("textarea[name='descriptionRu']")

        # Images
        self.logo_upload = self.page.locator("input[type='file']").first
        self.banner_upload = self.page.locator("input[type='file']").nth(1)

        # Buttons
        self.save_btn = self.page.locator(
            "button:has-text('Сохранить'), button:has-text('Save'), "
            "button:has-text('Saqlash'), button[type='submit']"
        ).first
        self.deactivate_btn = self.page.get_by_role("button", name="Деактивировать").or_(
            self.page.get_by_role("button", name="Deactivate")
        ).or_(self.page.get_by_role("button", name="Faolsizlantirish"))
        self.cancel_btn = self.page.get_by_role("button", name="Отмена").or_(
            self.page.get_by_role("button", name="Cancel")
        ).or_(self.page.get_by_role("button", name="Bekor qilish"))

        # Status
        self.shop_status = self.page.locator("[data-testid='shop-status']").or_(
            self.page.locator(".shop-status")
        )

    def navigate_to_shop_settings(self) -> None:
        """Navigate to shop settings page (tries multiple paths)."""
        logger.info("Navigating to shop settings")
        self.navigate_to(self.SHOP_SETTINGS_PATH)
        self.page.wait_for_load_state("domcontentloaded")
        # Check URL — if redirected away, try alternative path
        if "settings" not in self.page.url and "shop" not in self.page.url:
            logger.info("Redirected, trying alternative settings path")
            self.navigate_to(self.SHOP_SETTINGS_ALT_PATH)
            self.page.wait_for_load_state("domcontentloaded")

    def click_settings_nav_link(self) -> None:
        """Click shop settings navigation link."""
        logger.info("Clicking shop settings navigation link")
        if self.settings_nav_link.is_visible(timeout=3000):
            self.settings_nav_link.click()
            self.page.wait_for_load_state("domcontentloaded")

    def click_edit_button(self) -> bool:
        """Click Edit button to switch from read-only to edit mode. Returns True if clicked."""
        logger.info("Clicking edit button to enable editing...")
        if self.edit_btn.is_visible(timeout=5000):
            self.edit_btn.click()
            self.page.wait_for_load_state("domcontentloaded")
            # Ждём появления input полей (после клика read-only <p> заменяются на <input>)
            self.page.locator("input, textarea").first.wait_for(
                state="visible", timeout=10000
            )
            logger.info("Edit mode enabled — input fields visible")
            return True
        logger.warning("Edit button not found")
        return False

    def get_shop_name(self) -> str:
        """Get current shop name from input."""
        if self.shop_name_input.is_visible(timeout=3000):
            return self.shop_name_input.input_value()
        return ""

    def fill_shop_name(self, name: str) -> None:
        """Fill shop name input."""
        logger.info(f"Filling shop name: {name}")
        self.shop_name_input.fill(name)

    def get_shop_slug(self) -> str:
        """Get current shop slug."""
        if self.shop_slug_input.is_visible(timeout=3000):
            return self.shop_slug_input.input_value()
        return ""

    def fill_shop_slug(self, slug: str) -> None:
        """Fill shop slug input."""
        logger.info(f"Filling shop slug: {slug}")
        self.shop_slug_input.fill(slug)

    def get_shop_sku(self) -> str:
        """Get current shop SKU."""
        if self.shop_sku_input.is_visible(timeout=3000):
            return self.shop_sku_input.input_value()
        return ""

    def fill_description_uz(self, description: str) -> None:
        """Fill Uzbek description."""
        if description:
            logger.info("Filling Uzbek description")
            self.description_uz_input.fill(description)

    def fill_description_ru(self, description: str) -> None:
        """Fill Russian description."""
        if description:
            logger.info("Filling Russian description")
            self.description_ru_input.fill(description)

    def upload_logo(self, file_path: str) -> None:
        """Upload shop logo."""
        logger.info(f"Uploading logo: {file_path}")
        if self.logo_upload.is_visible(timeout=3000):
            self.logo_upload.set_input_files(file_path)
            self.page.wait_for_load_state("domcontentloaded")

    def upload_banner(self, file_path: str) -> None:
        """Upload shop banner."""
        logger.info(f"Uploading banner: {file_path}")
        if self.banner_upload.is_visible(timeout=3000):
            self.banner_upload.set_input_files(file_path)
            self.page.wait_for_load_state("domcontentloaded")

    def click_save(self) -> None:
        """Click save button."""
        logger.info("Clicking save button")
        if self.save_btn.is_visible(timeout=3000):
            self.save_btn.click()
            self.page.wait_for_load_state("domcontentloaded")

    def click_cancel(self) -> None:
        """Click cancel button."""
        logger.info("Clicking cancel button")
        if self.cancel_btn.is_visible(timeout=3000):
            self.cancel_btn.click()

    def is_settings_page_loaded(self) -> bool:
        """Check if settings page is loaded (works in both read-only and edit modes)."""
        url_ok = "settings" in self.page.url.lower() or "shop" in self.page.url.lower()
        has_edit_btn = self.edit_btn.is_visible(timeout=2000)
        has_inputs = self.shop_name_input.is_visible(timeout=2000)
        return url_ok or has_edit_btn or has_inputs

    def get_shop_status(self) -> str:
        """Get shop status (Active, Moderation, etc.)."""
        if self.shop_status.is_visible(timeout=3000):
            return self.shop_status.text_content() or ""

        # Try alternative status indicator
        status_badge = self.page.locator("span:has-text('Active')").or_(
            self.page.locator("span:has-text('Активен')")
        ).or_(self.page.locator("span:has-text('Faol')")).or_(
            self.page.locator("span:has-text('На модерации')")
        ).or_(self.page.locator("span:has-text('Moderatsiyada')"))

        if status_badge.first.is_visible(timeout=2000):
            return status_badge.first.text_content() or ""

        return ""

    def is_save_button_enabled(self) -> bool:
        """Check if save button is enabled."""
        return self.save_btn.is_enabled(timeout=3000)

    def is_success_message_visible(self) -> bool:
        """Check if success message is visible after save."""
        success = self.page.locator("text=/успешно|success/i").or_(
            self.page.locator(".success-message")
        ).or_(self.page.locator("[role='alert']"))
        return success.is_visible(timeout=3000)

    def is_error_message_visible(self) -> bool:
        """Check if error message is visible."""
        error = self.page.locator("text=/ошибка|error/i").or_(
            self.page.locator(".error-message")
        ).or_(self.page.locator(".MuiFormHelperText-root.Mui-error"))
        return error.is_visible(timeout=2000)

    # ==================== VALIDATION METHODS ====================

    def get_validation_error_count(self) -> int:
        """Get count of MUI validation errors on the page."""
        return self.page.locator(".MuiFormHelperText-root.Mui-error").count()

    def has_validation_errors(self) -> bool:
        """Check if there are any validation errors on the page."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """Get all validation error messages from the page."""
        errors = self.page.locator(".MuiFormHelperText-root.Mui-error").all()
        return [e.inner_text() for e in errors if e.is_visible()]

    def has_error_for_field(self, field_name: str) -> bool:
        """Check if a specific field has a validation error."""
        field = self.page.get_by_role("textbox", name=field_name)
        if field.count() > 0:
            parent = field.locator("xpath=ancestor::div[contains(@class,'MuiFormControl')]")
            if parent.count() > 0:
                error = parent.locator(".MuiFormHelperText-root.Mui-error")
                return error.count() > 0 and error.is_visible()
        return False
