"""
Dashboard page object and Shop Create page component.
Handles dashboard navigation and shop creation workflow.
"""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage, logger


class ShopCreatePage:
    """
    Shop Create page component with full validation support.
    Handles shop creation form interactions on the full create page.

    Follows QA Senior Engineer standards:
    - Hard assertions (FAILED not SKIPPED)
    - Real validation error checking
    - Complete field coverage
    """

    # URL
    SHOP_CREATE_PATH = "/dashboard/shops/create"

    # Locators
    SHOP_NAME_INPUT = "input[name='title']"
    SHOP_SLUG_INPUT = "input[name='slug']"
    SHOP_SKU_INPUT = "input[name='sku']"
    DESCRIPTION_UZ_INPUT = "textarea[name='descriptionUz']"
    DESCRIPTION_RU_INPUT = "textarea[name='descriptionRu']"
    SAVE_BTN = "button:has-text('Save and Submit for Moderation'), button:has-text('Сохранить и отправить на модерацию'), button:has-text('Saqlash va moderatsiyaga yuborish')"
    CANCEL_BTN = "button:has-text('Cancel'), button:has-text('Отмена'), button:has-text('Bekor qilish')"
    PAGE_TITLE = "h2, h3, h1"

    # Validation locators
    VALIDATION_ERROR = ".MuiFormHelperText-root.Mui-error"
    FIELD_ERROR_CLASS = ".Mui-error"
    TOAST_ERROR = ".MuiAlert-standardError, [role='alert']"

    def __init__(self, page: Page):
        """Initialize shop create page with page instance."""
        self.page = page

    # ================================================================================
    # Page State Methods
    # ================================================================================

    def is_page_loaded(self, timeout: int = 5000) -> bool:
        """Check if shop create page is loaded (form visible)."""
        try:
            return self.page.locator(self.SHOP_NAME_INPUT).is_visible(timeout=timeout)
        except Exception:
            return False

    # Backward compatibility alias
    def is_modal_visible(self, timeout: int = 5000) -> bool:
        """Alias for is_page_loaded (backward compatibility)."""
        return self.is_page_loaded(timeout=timeout)

    def wait_for_page(self, timeout: int = 10000) -> None:
        """Wait for shop create page to be loaded."""
        logger.info("Waiting for shop create page...")
        self.page.locator(self.SHOP_NAME_INPUT).wait_for(state="visible", timeout=timeout)
        logger.info("Shop create page is loaded")

    # Backward compatibility alias
    def wait_for_modal(self, timeout: int = 10000) -> None:
        """Alias for wait_for_page (backward compatibility)."""
        self.wait_for_page(timeout=timeout)

    def get_page_title(self) -> str:
        """Get page title text."""
        try:
            title = self.page.locator(self.PAGE_TITLE).first
            if title.is_visible(timeout=2000):
                return title.inner_text()
        except Exception:
            pass
        return ""

    # Backward compatibility alias
    def get_modal_title(self) -> str:
        """Alias for get_page_title (backward compatibility)."""
        return self.get_page_title()

    def close_modal(self) -> None:
        """Close shop create dialog by clicking outside it."""
        logger.info("Closing shop create dialog")
        try:
            self.page.mouse.click(10, 10)
            # Wait for dialog to actually close (MUI animation takes ~300ms)
            self.page.locator(self.SHOP_NAME_INPUT).wait_for(state="hidden", timeout=3000)
        except Exception as e:
            logger.warning(f"Dialog close wait: {e}")

    # ================================================================================
    # Form Field Methods
    # ================================================================================

    def fill_shop_name(self, name: str) -> None:
        """Fill shop name input field."""
        logger.info(f"Filling shop name: {name}")
        field = self.page.locator(self.SHOP_NAME_INPUT)
        field.clear()
        field.fill(name)

    def get_shop_name_value(self) -> str:
        """Get current value of shop name field."""
        return self.page.locator(self.SHOP_NAME_INPUT).input_value()

    def clear_shop_name(self) -> None:
        """Clear shop name field."""
        self.page.locator(self.SHOP_NAME_INPUT).clear()

    def get_slug_value(self) -> str:
        """Get current value of slug input field."""
        value = self.page.locator(self.SHOP_SLUG_INPUT).input_value()
        logger.info(f"Retrieved slug value: {value}")
        return value

    def get_sku_value(self) -> str:
        """Get current value of SKU input field."""
        value = self.page.locator(self.SHOP_SKU_INPUT).input_value()
        logger.info(f"Retrieved SKU value: {value}")
        return value

    def fill_slug(self, slug: str) -> None:
        """Заполнить поле slug вручную."""
        logger.info(f"Filling slug: {slug}")
        field = self.page.locator(self.SHOP_SLUG_INPUT)
        field.clear()
        field.fill(slug)

    def fill_sku(self, sku: str) -> None:
        """Заполнить поле SKU вручную."""
        logger.info(f"Filling SKU: {sku}")
        field = self.page.locator(self.SHOP_SKU_INPUT)
        field.clear()
        field.fill(sku)

    def verify_slug_auto_filled(self) -> None:
        """Verify slug field is auto-filled (not empty)."""
        logger.info("Verifying slug auto-filled")
        expect(self.page.locator(self.SHOP_SLUG_INPUT)).not_to_have_value("")

    def verify_sku_auto_filled(self) -> None:
        """Verify SKU field is auto-filled (not empty)."""
        logger.info("Verifying SKU auto-filled")
        expect(self.page.locator(self.SHOP_SKU_INPUT)).not_to_have_value("")

    def fill_description_uz(self, description: str) -> None:
        """Fill Uzbek description field."""
        logger.info(f"Filling Uzbek description: {description[:30]}...")
        field = self.page.locator(self.DESCRIPTION_UZ_INPUT)
        field.clear()
        field.fill(description)

    def get_description_uz_value(self) -> str:
        """Get current value of Uzbek description field."""
        return self.page.locator(self.DESCRIPTION_UZ_INPUT).input_value()

    def clear_description_uz(self) -> None:
        """Clear Uzbek description field."""
        self.page.locator(self.DESCRIPTION_UZ_INPUT).clear()

    def fill_description_ru(self, description: str) -> None:
        """Fill Russian description field."""
        logger.info(f"Filling Russian description: {description[:30]}...")
        field = self.page.locator(self.DESCRIPTION_RU_INPUT)
        field.clear()
        field.fill(description)

    def get_description_ru_value(self) -> str:
        """Get current value of Russian description field."""
        return self.page.locator(self.DESCRIPTION_RU_INPUT).input_value()

    def clear_description_ru(self) -> None:
        """Clear Russian description field."""
        self.page.locator(self.DESCRIPTION_RU_INPUT).clear()

    def clear_all_fields(self) -> None:
        """Clear all form fields."""
        logger.info("Clearing all shop create form fields")
        self.clear_shop_name()
        self.clear_description_uz()
        self.clear_description_ru()

    # ================================================================================
    # File Upload Methods
    # ================================================================================

    def upload_logo(self, banner_shop: str, logo_shop: str) -> None:
        """Upload logo and banner images."""
        logger.info("Starting document upload process...")

        # Wait for modal to be visible
        self.page.wait_for_selector("input[type='file']", state="attached", timeout=5000)

        # 1. Logo - try English first, then Russian
        logger.info(f"Uploading logo: {logo_shop}")
        try:
            logo_input = self.page.locator("text=Logo").locator("..").locator("input[type='file']").first
            logo_input.set_input_files(logo_shop, timeout=10000)
        except Exception:
            logo_input = self.page.locator("h6:has-text('Лого')").locator("..").locator("input[type='file']").first
            logo_input.set_input_files(logo_shop, timeout=10000)
        logger.info("Logo uploaded, waiting for UI update...")
        self.page.wait_for_load_state("domcontentloaded")

        # 2. Banner - try English first, then Russian
        logger.info(f"Uploading banner: {banner_shop}")
        try:
            banner_input = self.page.locator("text=Banner").locator("..").locator("input[type='file']").first
            banner_input.set_input_files(banner_shop, timeout=10000)
        except Exception:
            banner_input = self.page.locator("h6:has-text('Баннер')").locator("..").locator("input[type='file']").first
            banner_input.set_input_files(banner_shop, timeout=10000)
        logger.info("Banner uploaded, waiting for UI update...")
        self.page.wait_for_load_state("domcontentloaded")

        logger.info("All documents uploaded successfully")

    def upload_logo_only(self, logo_path: str) -> None:
        """Upload only logo image."""
        logger.info(f"Uploading logo only: {logo_path}")
        try:
            logo_input = self.page.locator("text=Logo").locator("..").locator("input[type='file']").first
            logo_input.set_input_files(logo_path, timeout=10000)
        except Exception:
            logo_input = self.page.locator("h6:has-text('Лого')").locator("..").locator("input[type='file']").first
            logo_input.set_input_files(logo_path, timeout=10000)
        self.page.wait_for_load_state("domcontentloaded")

    def upload_banner_only(self, banner_path: str) -> None:
        """Upload only banner image."""
        logger.info(f"Uploading banner only: {banner_path}")
        try:
            banner_input = self.page.locator("text=Banner").locator("..").locator("input[type='file']").first
            banner_input.set_input_files(banner_path, timeout=10000)
        except Exception:
            banner_input = self.page.locator("h6:has-text('Баннер')").locator("..").locator("input[type='file']").first
            banner_input.set_input_files(banner_path, timeout=10000)
        self.page.wait_for_load_state("domcontentloaded")

    def is_logo_uploaded(self) -> bool:
        """Check if logo has been uploaded (preview visible)."""
        try:
            # Look for image preview in logo section
            logo_section = self.page.locator("text=Logo").or_(self.page.locator("h6:has-text('Лого')")).or_(self.page.locator("h6:has-text('Logo')")).locator("..")
            img = logo_section.locator("img")
            return img.count() > 0 and img.first.is_visible(timeout=2000)
        except Exception:
            return False

    def is_banner_uploaded(self) -> bool:
        """Check if banner has been uploaded (preview visible)."""
        try:
            # Look for image preview in banner section
            banner_section = self.page.locator("text=Banner").or_(self.page.locator("h6:has-text('Баннер')")).or_(self.page.locator("h6:has-text('Banner')")).locator("..")
            img = banner_section.locator("img")
            return img.count() > 0 and img.first.is_visible(timeout=2000)
        except Exception:
            return False

    # ================================================================================
    # Button Methods
    # ================================================================================

    def click_save(self) -> None:
        """Click save button to create shop."""
        logger.info("Clicking save button")
        self.page.locator(self.SAVE_BTN).click()

    def click_cancel(self) -> None:
        """Close dialog by clicking outside (no cancel button in UI)."""
        logger.info("Closing dialog via backdrop click")
        self.close_modal()

    def is_save_button_enabled(self) -> bool:
        """Check if save button is enabled."""
        try:
            return self.page.locator(self.SAVE_BTN).is_enabled(timeout=2000)
        except Exception:
            return False

    def is_save_button_visible(self) -> bool:
        """Check if save button is visible."""
        try:
            return self.page.locator(self.SAVE_BTN).is_visible(timeout=2000)
        except Exception:
            return False

    # ================================================================================
    # Validation Methods - QA Senior Engineer Standards
    # ================================================================================

    def get_validation_error_count(self) -> int:
        """
        Get count of validation error messages displayed on the form.

        Returns:
            Number of validation error elements
        """
        try:
            error_elements = self.page.locator(self.VALIDATION_ERROR)
            return error_elements.count()
        except Exception:
            return 0

    def has_validation_errors(self) -> bool:
        """
        Check if form has any validation errors displayed.

        Returns:
            True if validation errors are visible
        """
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """
        Get all validation error messages from the form.

        Returns:
            List of error message strings
        """
        messages = []
        try:
            error_elements = self.page.locator(self.VALIDATION_ERROR)
            count = error_elements.count()
            for i in range(count):
                try:
                    text = error_elements.nth(i).inner_text(timeout=1000)
                    if text.strip():
                        messages.append(text.strip())
                except Exception:
                    pass
        except Exception:
            pass
        return messages

    def has_error_for_field(self, field_name: str) -> bool:
        """
        Check if a specific field has validation error.

        Args:
            field_name: Part of field label to search for (e.g., "title", "Shop name")

        Returns:
            True if field has error styling
        """
        try:
            # MUI adds Mui-error class to labels when field is invalid
            error_label = self.page.locator(f".Mui-error:has-text('{field_name}')")
            if error_label.count() > 0:
                return True

            # Also check for error helper text containing field name
            error_helper = self.page.locator(f".MuiFormHelperText-root.Mui-error")
            for i in range(error_helper.count()):
                text = error_helper.nth(i).inner_text(timeout=500)
                if field_name.lower() in text.lower():
                    return True

            return False
        except Exception:
            return False

    def get_field_error_message(self, field_name: str) -> str:
        """
        Get error message for a specific field.

        Args:
            field_name: Field name to get error for

        Returns:
            Error message string or empty string
        """
        try:
            # Find form control containing the field
            if "name" in field_name.lower() or "title" in field_name.lower():
                field = self.page.locator(self.SHOP_NAME_INPUT)
            elif "uz" in field_name.lower():
                field = self.page.locator(self.DESCRIPTION_UZ_INPUT)
            elif "ru" in field_name.lower():
                field = self.page.locator(self.DESCRIPTION_RU_INPUT)
            else:
                return ""

            # Find parent form control and get helper text
            parent = field.locator("xpath=ancestor::div[contains(@class, 'MuiFormControl')]")
            helper_text = parent.locator(".MuiFormHelperText-root.Mui-error")
            if helper_text.is_visible(timeout=1000):
                return helper_text.inner_text()
        except Exception:
            pass
        return ""

    def has_toast_error(self) -> bool:
        """Check if toast/alert error is displayed."""
        try:
            return self.page.locator(self.TOAST_ERROR).is_visible(timeout=2000)
        except Exception:
            return False

    def get_toast_error_message(self) -> str:
        """Get toast/alert error message."""
        try:
            toast = self.page.locator(self.TOAST_ERROR).first
            if toast.is_visible(timeout=2000):
                return toast.inner_text()
        except Exception:
            pass
        return ""

    def wait_for_validation_errors(self, timeout: int = 3000) -> bool:
        """
        Wait for validation errors to appear after form submission.

        Returns:
            True if validation errors appeared
        """
        try:
            self.page.locator(self.VALIDATION_ERROR).first.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    # ================================================================================
    # UI Element Visibility Methods
    # ================================================================================

    def is_shop_name_field_visible(self) -> bool:
        """Check if shop name field is visible."""
        try:
            return self.page.locator(self.SHOP_NAME_INPUT).is_visible(timeout=2000)
        except Exception:
            return False

    def is_slug_field_visible(self) -> bool:
        """Check if slug field is visible."""
        try:
            return self.page.locator(self.SHOP_SLUG_INPUT).is_visible(timeout=2000)
        except Exception:
            return False

    def is_sku_field_visible(self) -> bool:
        """Check if SKU field is visible."""
        try:
            return self.page.locator(self.SHOP_SKU_INPUT).is_visible(timeout=2000)
        except Exception:
            return False

    def is_description_uz_field_visible(self) -> bool:
        """Check if Uzbek description field is visible."""
        try:
            return self.page.locator(self.DESCRIPTION_UZ_INPUT).is_visible(timeout=2000)
        except Exception:
            return False

    def is_description_ru_field_visible(self) -> bool:
        """Check if Russian description field is visible."""
        try:
            return self.page.locator(self.DESCRIPTION_RU_INPUT).is_visible(timeout=2000)
        except Exception:
            return False

    def get_file_input_count(self) -> int:
        """Get count of file input elements on the page."""
        try:
            return self.page.locator("input[type='file']").count()
        except Exception:
            return 0



# Backward compatibility alias
ShopCreateModal = ShopCreatePage


class DashboardPage(BasePage):
    """
    Dashboard page object model.
    Handles dashboard navigation and shop dropdown interactions.
    Follows Open/Closed Principle - extends BasePage without modifying it.
    """

    # URL path
    DASHBOARD_PATH = "/dashboard"

    # Locators - Shop dropdown contains shop name + status (multi-language)
    # English: "Active", Uzbek: "Faol", Russian: "Активный"
    SHOP_DROPDOWN_BTN = "button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')"
    SHOP_DROPDOWN_MENU = "div[role='menu']"
    ADD_SHOP_BTN = "button:has-text('Add Shop'), button:has-text('Do\\'kon qo\\'shish'), button:has-text('Добавить магазин')"


    def __init__(self, page: Page):
        """Initialize dashboard page with nested shop create page."""
        super().__init__(page)
        self.shop_modal = ShopCreatePage(page)

    def navigate_to_dashboard(self) -> None:
        """Navigate to dashboard page."""
        self.navigate_to(self.DASHBOARD_PATH)

    def ensure_on_page(self) -> None:
        """Navigate to dashboard only if not already there (realistic user behavior)."""
        # First close any open dropdown/modal
        self.close_any_dropdown()

        current_url = self.page.url
        if self.DASHBOARD_PATH not in current_url:
            logger.info("Not on dashboard, navigating...")
            self.navigate_to_dashboard()
            self.wait_for_network_idle()
        else:
            logger.info("Already on dashboard page")

    def open_shop_dropdown(self) -> None:
        """Click shop dropdown button to reveal menu."""
        logger.info("Opening shop dropdown")
        # First close any open dropdown/modal
        self.close_any_dropdown()
        self.click_element(self.SHOP_DROPDOWN_BTN)

    def close_any_dropdown(self) -> None:
        """Close any open dropdown or modal by pressing Escape."""
        try:
            backdrop = self.page.locator(".MuiBackdrop-root").first
            if backdrop.is_visible(timeout=500):
                logger.info("Closing open dropdown/modal")
                self.page.keyboard.press("Escape")
                self.page.wait_for_load_state("domcontentloaded")
        except Exception:
            pass  # No dropdown open

    def verify_shop_visible_in_dropdown(self, shop_name: str) -> None:
        """Verify specific shop is visible in dropdown menu."""
        logger.info(f"Verifying shop '{shop_name}' visible in dropdown")
        # Use partial match in case name is truncated
        base_shop_name = shop_name.split()[0]  # Get first word (e.g., "Test" from "Test Shop Automation 1759372520")
        shop_locator = f"{self.SHOP_DROPDOWN_MENU} span"

        # Get all shop names from dropdown
        shop_elements = self.page.locator(shop_locator).all()
        logger.info(f"Found {len(shop_elements)} shops in dropdown")

        # Check if any shop contains our shop name or base name
        found = False
        for element in shop_elements:
            text = element.text_content()
            logger.info(f"Checking shop: {text}")
            if shop_name in text or base_shop_name in text:
                found = True
                logger.info(f"✓ Found matching shop: {text}")
                break

        assert found, f"Shop '{shop_name}' not found in dropdown"

    def click_add_shop(self) -> ShopCreatePage:
        """
        Click 'Add Shop' button in dropdown menu.
        Returns ShopCreatePage instance for page interactions.
        """
        logger.info("Clicking 'Add Shop' button")
        self.click_element(self.ADD_SHOP_BTN)
        return self.shop_modal

    def get_shop_modal(self) -> ShopCreatePage:
        """Return shop create page instance."""
        return self.shop_modal

    def select_shop(self, shop_name: str) -> None:
        """
        Select a specific shop from the dropdown menu.

        Args:
            shop_name: Name of the shop to select (e.g., "netshop")

        This method opens the shop dropdown and clicks on the specified shop.
        Used to switch between shops when the current shop doesn't have
        the required permissions (e.g., unregistered shop can't add products).
        """
        logger.info(f"Selecting shop: {shop_name}")
        try:
            # Open the shop dropdown
            self.open_shop_dropdown()
            self.wait_for_selector("div[role='menu']", state="visible")

            # Click on the shop menu item
            shop_item = self.page.get_by_role("menuitem", name=shop_name)
            shop_item.wait_for(state="visible", timeout=5000)
            shop_item.click()

            logger.info(f"Shop '{shop_name}' selected")
            self.wait_for_network_idle()  # Wait for shop switch to complete
        except Exception as e:
            logger.error(f"Failed to select shop '{shop_name}': {str(e)}")
            raise

    def get_current_shop_name(self) -> str:
        """
        Get the name of the currently selected shop.

        Returns:
            str: Name of the current shop displayed in the dropdown button
        """
        try:
            # The shop dropdown button contains: img (logo), span (name), span (status), svg
            # Target the button that has status text (multi-language)
            shop_btn = self.page.locator(self.SHOP_DROPDOWN_BTN).first
            shop_btn.wait_for(state="visible", timeout=5000)

            # Get all text spans inside the button
            spans = shop_btn.locator("div > div").all()
            if spans:
                # First span is usually the shop name
                shop_name = spans[0].text_content()
                logger.info(f"Current shop: {shop_name}")
                return shop_name or ""

            # Fallback: get button's accessible name which includes shop name
            button_name = shop_btn.get_attribute("aria-label") or shop_btn.text_content() or ""
            # Extract shop name from button text (format: "ShopName Active/Faol")
            for status in ["Active", "Faol", "Активный"]:
                if status in button_name:
                    shop_name = button_name.split(status)[0].strip()
                    # Remove duplicate name if present
                    words = shop_name.split()
                    if len(words) >= 2:
                        mid = len(words) // 2
                        first_half = " ".join(words[:mid])
                        second_half = " ".join(words[mid:])
                        if first_half == second_half:
                            shop_name = first_half
                    logger.info(f"Current shop (from button text): {shop_name}")
                    return shop_name

            return button_name
        except Exception as e:
            logger.warning(f"Could not get current shop name: {str(e)}")
            return ""

    def is_shop_registered(self) -> bool:
        """
        Check if the current shop is registered (can add products).

        Returns:
            bool: True if shop is registered and can add products
        """
        try:
            # Check if "Добавить товары" button is visible
            add_product_btn = self.page.locator("a[href='/dashboard/products/create']:has-text('Добавить товары')")
            return add_product_btn.is_visible(timeout=3000)
        except Exception:
            return False