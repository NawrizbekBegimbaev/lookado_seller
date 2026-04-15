"""
Product Create page object model.
Handles product creation form interactions and validation.

Uses language-agnostic locators (URL patterns, roles, indices).
"""

from typing import Optional
from playwright.sync_api import Page
from pages.base_page import BasePage, logger


class ProductCreatePage(BasePage):
    """
    Product Create page object model.
    Manages product creation workflow and form validations.
    """

    # URL patterns
    dashboard_path = "/dashboard"
    PRODUCT_CREATE_PATH = "/dashboard/products/create"
    ADD_PRODUCTS_PATH = "/dashboard/products/add"

    def __init__(self, page: Page):
        """Initialize product create page."""
        super().__init__(page)

    # ==================== NAVIGATION ====================

    def navigate_to_dashboard(self) -> None:
        """Navigate to dashboard."""
        self.navigate_to(self.dashboard_path)

    def select_shop(self, shop_name: str) -> None:
        """
        Select a specific shop from the dropdown menu.

        Args:
            shop_name: Name of the shop to select
        """
        logger.info(f"Selecting shop: {shop_name}")
        try:
            shop_btn = self.page.locator("button").filter(has_text=shop_name).first
            if not shop_btn.is_visible(timeout=2000):
                shop_dropdown = self.page.locator("button").filter(
                    has=self.page.locator("img")
                ).first
                shop_dropdown.click()
                self.page.wait_for_load_state("domcontentloaded")

                shop_item = self.page.get_by_role("menuitem", name=shop_name)
                shop_item.click()
                self.wait_for_network_idle()

            logger.info(f"✓ Shop '{shop_name}' selected")
        except Exception as e:
            logger.error(f"Failed to select shop: {str(e)}")
            raise

    def click_add_product_btn_staging(self) -> None:
        """Click 'Add Products' button (multi-language support)."""
        logger.info("Clicking 'Add Products' button (staging)")
        try:
            self.page.wait_for_load_state("load", timeout=10000)
            # Support multiple languages: English, Russian, Uzbek
            add_btn = self.page.locator(
                "a[href*='/products/add'], "
                "a:has-text('Add Products'), "
                "a:has-text('Tovar qo\\'shish'), "
                "a:has-text('Добавить товары'), "
                "a:has-text('Добавить товар')"
            ).first
            add_btn.wait_for(state="visible", timeout=10000)
            add_btn.click()
            logger.info("✓ 'Add Products' button clicked")
        except Exception as e:
            logger.error(f"Failed to click add product button: {str(e)}")
            raise

    def click_single_product_option(self) -> None:
        """Click single product option (language-independent via URL pattern)."""
        logger.info("Clicking single product option")
        try:
            single_product = self.page.locator("a[href*='/products/create']").first
            single_product.wait_for(state="visible", timeout=10000)
            single_product.click()
            self.page.wait_for_load_state("load", timeout=15000)
            self.wait_for_network_idle()
            logger.info("✓ Single product option selected")
        except Exception as e:
            logger.error(f"Failed to click single product option: {str(e)}")
            raise

    # ==================== STEP 1: PRODUCT INFO ====================

    def select_category_from_combobox(self, category_path: list[str]) -> None:
        """
        Select category using MUI Autocomplete tree-style dropdown.

        Structure:
        - Parent categories: option > generic (text) + svg (chevron)
        - Leaf categories: option > generic (text) only
        - Back button: option with text starting "... Назад"

        Args:
            category_path: Category hierarchy e.g., ["Kiyim", "Erkaklar uchun", "Ustki kiyim"]
        """
        path_display = [str(p[0]) if isinstance(p, (tuple, list)) else str(p) for p in category_path]
        logger.info(f"Selecting category path: {' → '.join(path_display)}")

        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=15000)
            self.page.keyboard.press("Escape")
            self.page.wait_for_load_state("domcontentloaded")

            # Open dropdown
            combobox = self.page.get_by_role("combobox").first
            combobox.wait_for(state="visible", timeout=15000)
            combobox.click()
            self.page.wait_for_load_state("domcontentloaded")

            # Wait for listbox
            self.page.get_by_role("listbox").wait_for(state="visible", timeout=15000)
            self.page.get_by_role("option").first.wait_for(state="visible", timeout=10000)
            logger.info("✓ Dropdown opened")

            # Navigate to root level by clicking back buttons
            for _ in range(10):
                first_opt = self.page.get_by_role("option").first
                first_text = first_opt.inner_text().strip()
                if first_text.startswith("...") or "Назад" in first_text:
                    first_opt.click()
                    self.page.wait_for_load_state("domcontentloaded")
                    logger.info("✓ Back to parent")
                else:
                    break
            logger.info("✓ At root level")

            # Navigate through category path
            # Each element can be a string or tuple of alternatives (UZ, RU)
            for idx, name_entry in enumerate(category_path):
                is_last = idx == len(category_path) - 1
                self.page.wait_for_load_state("domcontentloaded")

                # Support multi-language: name can be str or tuple/list of alternatives
                names = [name_entry] if isinstance(name_entry, str) else list(name_entry)

                all_options = self.page.get_by_role("option")
                option_count = all_options.count()

                target_idx = None
                for i in range(option_count):
                    opt = all_options.nth(i)
                    text = opt.inner_text().strip()
                    if text.startswith("...") or "Назад" in text:
                        continue
                    # Handle category names with count suffix like "Телефоны(10)"
                    clean_text = text.split("(")[0].strip() if "(" in text else text
                    for name in names:
                        if text == name or clean_text == name or text.startswith(f"{name}(") or text.startswith(f"{name} ("):
                            target_idx = i
                            break
                    if target_idx is not None:
                        break

                if target_idx is None:
                    available = [all_options.nth(i).inner_text().strip()[:40]
                                 for i in range(min(5, option_count))]
                    raise Exception(f"'{names}' not found. Available: {available}")

                target = all_options.nth(target_idx)

                matched_name = names[0]  # For logging
                if is_last:
                    target.click()
                    logger.info(f"✓ Selected '{matched_name}'")
                else:
                    # Click SVG chevron to expand (not IMG - actual element is SVG)
                    chevron = target.locator("svg")
                    if chevron.count() > 0:
                        chevron.click()
                        logger.info(f"✓ Expanded '{matched_name}'")
                    else:
                        target.click()
                        logger.info(f"✓ Clicked '{matched_name}' (no chevron)")
                    # Wait for subcategories to load in dropdown
                    self.page.wait_for_load_state("domcontentloaded")
                    # Wait for at least 2 options (back button + first subcategory)
                    self.page.locator("[role='option']").nth(1).wait_for(
                        state="visible", timeout=10000
                    )

            logger.info("✓ Category selection complete")
            # Close dropdown to prevent it from blocking subsequent combobox clicks
            self.page.keyboard.press("Escape")
            self.page.wait_for_load_state("domcontentloaded")

        except Exception as e:
            logger.error(f"Category selection failed: {str(e)}")
            raise

    def select_ikpu_from_combobox(self, search_term: str) -> None:
        """
        Select IKPU using MUI Autocomplete combobox.

        Args:
            search_term: IKPU search term (e.g., "kurtkalar")
        """
        logger.info(f"Selecting IKPU: {search_term}")
        try:
            ikpu_input = self.page.get_by_role("combobox").nth(1)
            ikpu_input.wait_for(state="visible", timeout=5000)
            ikpu_input.click()
            ikpu_input.fill(search_term)
            self.page.wait_for_load_state("domcontentloaded")

            first_option = self.page.get_by_role("option").first
            first_option.wait_for(state="visible", timeout=15000)
            first_option.click()
            logger.info(f"✓ IKPU selected: {search_term}")
            self.page.wait_for_load_state("domcontentloaded")
        except Exception as e:
            logger.error(f"Failed to select IKPU: {str(e)}")
            raise

    def select_country_from_combobox(self, country_name: str) -> None:
        """
        Select country using MUI Autocomplete combobox.

        Args:
            country_name: Country name (e.g., "Turkiya")
        """
        logger.info(f"Selecting country: {country_name}")
        try:
            country_input = self.page.get_by_role("combobox").nth(2)
            country_input.wait_for(state="visible", timeout=5000)
            country_input.click()
            self.page.wait_for_load_state("domcontentloaded")

            option = self.page.get_by_role("option", name=country_name)
            option.wait_for(state="visible", timeout=10000)
            option.click()
            logger.info(f"✓ Country selected: {country_name}")
            self.page.wait_for_load_state("domcontentloaded")
        except Exception as e:
            logger.error(f"Failed to select country: {str(e)}")
            raise

    def select_brand_from_combobox(self, brand_name: str) -> None:
        """
        Select brand using MUI Autocomplete combobox.

        Args:
            brand_name: Brand name (e.g., "Zara")
        """
        logger.info(f"Selecting brand: {brand_name}")
        try:
            brand_input = self.page.get_by_role("combobox").nth(3)
            brand_input.wait_for(state="visible", timeout=5000)
            brand_input.click()
            brand_input.fill(brand_name)
            self.page.wait_for_load_state("domcontentloaded")

            option = self.page.get_by_role("option", name=brand_name)
            option.wait_for(state="visible", timeout=10000)
            option.click()
            logger.info(f"✓ Brand selected: {brand_name}")
            self.page.wait_for_load_state("domcontentloaded")
        except Exception as e:
            logger.error(f"Failed to select brand: {str(e)}")
            raise

    def fill_product_names_staging(
        self, uz_name: str, uz_desc: str, ru_name: str, ru_desc: str
    ) -> None:
        """
        Fill product names and descriptions (multi-language UI support).

        Args:
            uz_name: Product name in Uzbek
            uz_desc: Product description in Uzbek
            ru_name: Product name in Russian
            ru_desc: Product description in Russian
        """
        logger.info("Filling product names and descriptions")
        try:
            self.page.evaluate("window.scrollBy(0, 300)")
            self.page.wait_for_load_state("domcontentloaded")

            # UZ name: English "Product name in Uzbek" or Uzbek "Mahsulot nomi o'zbek tilida"
            uz_name_field = self.page.locator("input[name='nameUz']").or_(
                self.page.get_by_role("textbox", name="Product name in Uzbek")
            ).or_(
                self.page.get_by_role("textbox", name="Mahsulot nomi o'zbek tilida")
            )
            uz_name_field.scroll_into_view_if_needed()
            uz_name_field.fill(uz_name)
            logger.info(f"Filled UZ name: {uz_name}")

            # UZ description: English or Uzbek
            uz_desc_field = self.page.locator("textarea[name='descriptionUz'], input[name='descriptionUz']").or_(
                self.page.get_by_role("textbox", name="Description in Uzbek")
            ).or_(
                self.page.get_by_role("textbox", name="O'zbek tilidagi tavsif")
            )
            uz_desc_field.scroll_into_view_if_needed()
            uz_desc_field.fill(uz_desc)
            logger.info(f"Filled UZ description ({len(uz_desc)} chars)")

            # RU name: English or Uzbek
            ru_name_field = self.page.locator("input[name='nameRu']").or_(
                self.page.get_by_role("textbox", name="Product name in Russian")
            ).or_(
                self.page.get_by_role("textbox", name="Mahsulot nomi rus tilida")
            )
            ru_name_field.scroll_into_view_if_needed()
            ru_name_field.fill(ru_name)
            logger.info(f"Filled RU name: {ru_name}")

            # RU description: English or Uzbek
            ru_desc_field = self.page.locator("textarea[name='descriptionRu'], input[name='descriptionRu']").or_(
                self.page.get_by_role("textbox", name="Description in Russian")
            ).or_(
                self.page.get_by_role("textbox", name="Rus tilidagi tavsif")
            )
            ru_desc_field.scroll_into_view_if_needed()
            ru_desc_field.fill(ru_desc)
            logger.info(f"Filled RU description ({len(ru_desc)} chars)")

            logger.info("✓ Product names and descriptions filled")
        except Exception as e:
            logger.error(f"Failed to fill product names: {str(e)}")
            raise

    def select_model_from_combobox(self, search_text: str = "Model") -> None:
        """Select model from combobox autocomplete (optional — not all categories have it)."""
        logger.info(f"Selecting model: {search_text}")
        try:
            model_input = self.page.locator("#modelId-rhf-autocomplete")
            if not model_input.is_visible(timeout=3000):
                logger.info("Model field not present for this category, skipping")
                return
            model_input.scroll_into_view_if_needed(timeout=5000)
            model_input.click()
            model_input.fill(search_text)

            listbox = self.page.locator("[role='listbox']")
            listbox.wait_for(state="visible", timeout=10000)

            first_option = listbox.locator("[role='option']").first
            first_option.wait_for(state="visible", timeout=5000)
            first_option.click()

            self.wait_for_network_idle()
            logger.info(f"✓ Model selected")
        except Exception as e:
            logger.warning(f"Model selection skipped: {str(e)}")

    def click_next_button(self) -> None:
        """Click 'Next' button to proceed to next step."""
        logger.info("Clicking 'Next' button")
        try:
            next_btn = self.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last
            next_btn.wait_for(state="visible", timeout=5000)
            next_btn.scroll_into_view_if_needed()
            next_btn.click()

            self.wait_for_network_idle()
            self.page.wait_for_load_state("domcontentloaded", timeout=15000)

            # Проверяем ошибки валидации, которые могут блокировать переход
            self.page.wait_for_timeout(1000)
            errors = self.page.locator(".MuiFormHelperText-root.Mui-error")
            if errors.count() > 0:
                error_texts = [e.text_content() for e in errors.all()[:5]]
                logger.warning(f"Validation errors blocking step transition: {error_texts}")
                raise Exception(f"Validation errors prevent step transition: {error_texts}")

            logger.info("✓ Clicked 'Next' button")
        except Exception as e:
            logger.error(f"Failed to click 'Next' button: {str(e)}")
            raise

    # ==================== STEP 2: VARIANT/SKU INFO ====================

    def fill_variant_fields_staging(
        self,
        sku: str,
        price: str,
        discount_price: str,
        width: str,
        length: str,
        height: str,
        weight: str,
        barcode: str = None,
    ) -> None:
        """
        Fill variant/SKU fields (English UI labels).

        Args:
            sku: SKU code
            price: Regular price in sum
            discount_price: Discounted price in sum
            width: Width in mm
            length: Length in mm
            height: Height in mm
            weight: Weight in kg
            barcode: Product barcode (optional)
        """
        logger.info("Filling variant fields")
        try:
            self.wait_for_network_idle()

            # Используем точные name атрибуты из реального HTML Step 2
            sku_field = self.page.locator("input[name='variant.sku']").first
            sku_field.wait_for(state="visible", timeout=10000)
            logger.info("✓ Confirmed on variant page (Step 2)")
            sku_field.fill(sku)
            logger.info(f"Filled SKU: {sku}")

            if barcode:
                barcode_field = self.page.locator("input[name='variant.barcode']").first
                barcode_field.scroll_into_view_if_needed(timeout=5000)
                barcode_field.fill(barcode)
                logger.info(f"Filled barcode: {barcode}")

            price_field = self.page.locator("input[name='variant.price']").first
            price_field.scroll_into_view_if_needed(timeout=5000)
            price_field.fill(price)
            logger.info(f"Filled price: {price}")

            discount_field = self.page.locator("input[name='variant.discountPrice']").first
            discount_field.scroll_into_view_if_needed(timeout=5000)
            discount_field.fill(discount_price)
            logger.info(f"Filled discount price: {discount_price}")

            self.page.evaluate("window.scrollBy(0, 300)")
            self.page.wait_for_load_state("domcontentloaded")

            width_field = self.page.locator("input[name='variant.widthMm']").first
            width_field.scroll_into_view_if_needed(timeout=5000)
            width_field.fill(width)

            length_field = self.page.locator("input[name='variant.lengthMm']").first
            length_field.scroll_into_view_if_needed(timeout=5000)
            length_field.fill(length)

            height_field = self.page.locator("input[name='variant.heightMm']").first
            height_field.scroll_into_view_if_needed(timeout=5000)
            height_field.fill(height)

            weight_field = self.page.locator("input[name='variant.weightGm']").first
            weight_field.scroll_into_view_if_needed(timeout=5000)
            weight_field.fill(weight)

            logger.info(f"Filled dimensions: {width}x{length}x{height}, weight: {weight}")
            logger.info("✓ Variant fields filled")
            self.page.wait_for_load_state("domcontentloaded")
        except Exception as e:
            logger.error(f"Failed to fill variant fields: {str(e)}")
            raise

    # ==================== STEP 3: IMAGE UPLOAD ====================

    def upload_main_image(self, image_path: str) -> None:
        """
        Upload main product image.

        Args:
            image_path: Absolute path to image file
        """
        logger.info(f"Uploading main image: {image_path}")
        try:
            self.page.wait_for_load_state("load", timeout=10000)
            self.wait_for_network_idle()

            file_input = self.page.locator("input[type='file']").first
            file_input.set_input_files(image_path)
            self.wait_for_network_idle()
            logger.info("✓ Main image uploaded")
        except Exception as e:
            logger.error(f"Failed to upload main image: {str(e)}")
            raise

    # ==================== STEP 4: SUBMIT ====================

    def click_submit_moderation_staging(self) -> None:
        """Click submit for moderation button."""
        logger.info("Clicking submit for moderation button")
        try:
            submit_btn = self.page.locator("button[type='button']:not([disabled])").last
            if not submit_btn.is_visible(timeout=2000):
                submit_btn = self.page.locator("button[type='submit']").last
            submit_btn.click()
            self.wait_for_network_idle()
            logger.info("✓ Product submitted for moderation")
        except Exception as e:
            logger.error(f"Failed to submit for moderation: {str(e)}")
            raise

    def click_go_to_products_staging(self) -> None:
        """Click 'Go to products list' button in success dialog."""
        logger.info("Clicking 'Go to products list' button")
        try:
            products_btn = self.page.locator(
                "button.MuiButton-containedInherit, button:has-text('product')"
            ).first
            if products_btn.is_visible(timeout=3000):
                products_btn.click()
            else:
                self.navigate_to("/dashboard/products")
            self.page.wait_for_load_state("load", timeout=10000)
            logger.info("✓ Navigated to products list")
        except Exception as e:
            logger.error(f"Failed to navigate to products list: {str(e)}")
            raise

    # ==================== UTILITY ====================

    def scroll_page(self, pixels: int = 300) -> None:
        """
        Scroll page by specified pixels.

        Args:
            pixels: Number of pixels to scroll down
        """
        logger.info(f"Scrolling page by {pixels}px")
        try:
            self.page.evaluate(f"window.scrollBy(0, {pixels})")
            logger.info(f"✓ Page scrolled by {pixels}px")
            self.page.wait_for_load_state("domcontentloaded")
        except Exception as e:
            logger.error(f"Failed to scroll page: {str(e)}")
            raise

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

    def get_error_for_field(self, field_label: str) -> Optional[str]:
        """Get validation error for a specific field by label."""
        field = self.page.get_by_role("textbox", name=field_label)
        if field.count() > 0:
            parent = field.locator("xpath=ancestor::div[contains(@class,'MuiFormControl')]")
            if parent.count() > 0:
                error = parent.locator(".MuiFormHelperText-root.Mui-error")
                if error.count() > 0 and error.is_visible():
                    return error.inner_text()
        return None

    def is_field_required_error_shown(self, field_label: str) -> bool:
        """Check if required field error is shown."""
        error = self.get_error_for_field(field_label)
        if error:
            return "required" in error.lower() or "обязательно" in error.lower()
        return False

    def is_on_step(self, step_number: int) -> bool:
        """Check if currently on a specific wizard step."""
        url = self.page.url
        if step_number == 1:
            return "/products/create" in url and "step=2" not in url
        elif step_number == 2:
            return "step=2" in url or self.page.get_by_role("textbox", name="SKU").is_visible(timeout=1000)
        elif step_number == 3:
            file_input = self.page.locator("input[type='file']")
            return file_input.is_visible(timeout=1000)
        elif step_number == 4:
            submit_btn = self.page.locator("text=Submit for moderation, text=На модерацию").first
            return submit_btn.is_visible(timeout=1000)
        return False

    def get_current_step(self) -> int:
        """Get current wizard step number (1-4)."""
        for step in range(4, 0, -1):
            if self.is_on_step(step):
                return step
        return 1

    def is_next_button_enabled(self) -> bool:
        """Check if Next button is enabled."""
        next_btn = self.page.locator(
            "button[type='submit'], button.MuiButton-containedPrimary"
        ).last
        return not next_btn.is_disabled() if next_btn.is_visible(timeout=1000) else False

    def click_back_button(self) -> None:
        """Click Back button to go to previous step (multi-language: UZ/RU/EN)."""
        logger.info("Clicking 'Back' button")
        try:
            # Multi-language: Ortga (UZ), Назад (RU), Back (EN)
            back_btn = self.page.locator(
                "button:text-matches('Ortga|Назад|Back', 'i')"
            ).first
            back_btn.wait_for(state="visible", timeout=5000)
            back_btn.click()
            self.wait_for_network_idle()
            logger.info("✓ Clicked 'Back' button")
        except Exception as e:
            logger.error(f"Failed to click 'Back' button: {str(e)}")
            raise

    def navigate_to_create(self) -> None:
        """Navigate directly to product create page."""
        self.navigate_to(self.PRODUCT_CREATE_PATH)
        self.page.wait_for_load_state("load", timeout=15000)

    def is_category_combobox_visible(self) -> bool:
        """Check if category combobox is visible."""
        return self.page.get_by_role("combobox").first.is_visible(timeout=2000)

    def is_page_loaded(self) -> bool:
        """Check if product create page is loaded."""
        return "/products/create" in self.page.url or "/products/add" in self.page.url

    # Field label mapping: English -> (Uzbek label, input name)
    # UI labels confirmed: Eni (width), Uzunligi (length), Balandligi (height), Og'irligi (weight)
    FIELD_MAPPING = {
        # Step 1 fields
        "Product name in Uzbek": ("Mahsulot nomi o'zbek tilida", "nameUz"),
        "Description in Uzbek": ("O'zbek tilidagi tavsif", "descriptionUz"),
        "Product name in Russian": ("Mahsulot nomi rus tilida", "nameRu"),
        "Description in Russian": ("Rus tilidagi tavsif", "descriptionRu"),
        # Step 2 fields (variant.* name attributes)
        "SKU": ("SKU", "variant.sku"),
        "Barcode number": ("Shtrix-kod raqami", "variant.barcode"),
        "Regular price (UZS)": ("Oddiy narx (so'm)", "variant.price"),
        "Discount price (UZS)": ("Chegirmali narx (so'm)", "variant.discountPrice"),
        "Width (mm)": ("Eni (mm)", "variant.widthMm"),
        "Length (mm)": ("Uzunligi (mm)", "variant.lengthMm"),
        "Height (mm)": ("Balandligi (mm)", "variant.heightMm"),
        "Weight (kg)": ("Og'irligi (kg)", "variant.weightGm"),
    }

    def _get_field_locator(self, field_label: str):
        """Get field locator with multi-language support."""
        mapping = self.FIELD_MAPPING.get(field_label)
        if mapping:
            uz_label, input_name = mapping
            # Try by input name first (most reliable), then by labels
            return self.page.locator(f"input[name='{input_name}'], textarea[name='{input_name}']").or_(
                self.page.get_by_role("textbox", name=field_label)
            ).or_(
                self.page.get_by_role("textbox", name=uz_label)
            )
        # Fallback to original label
        return self.page.get_by_role("textbox", name=field_label)

    def get_field_value(self, field_label: str) -> str:
        """Get current value of a textbox field (multi-language support)."""
        field = self._get_field_locator(field_label)
        if field.first.is_visible(timeout=2000):
            return field.first.input_value()
        return ""

    def clear_field(self, field_label: str) -> None:
        """Clear a textbox field (multi-language support)."""
        field = self._get_field_locator(field_label)
        if field.first.is_visible(timeout=2000):
            field.first.clear()

    def fill_single_field(self, field_label: str, value: str) -> None:
        """Fill a single textbox field by label (multi-language support)."""
        field = self._get_field_locator(field_label)
        field.first.wait_for(state="visible", timeout=5000)
        field.first.fill(value)

    def is_file_uploaded(self) -> bool:
        """Check if a file has been uploaded (image preview visible)."""
        preview = self.page.locator("img[src*='blob:'], img[src*='data:'], .MuiAvatar-root img")
        return preview.is_visible(timeout=2000)

    def get_upload_error_message(self) -> Optional[str]:
        """Get file upload error message if any."""
        error = self.page.locator("text=/size|format|invalid|ошибка|размер|формат/i").first
        if error.is_visible(timeout=1000):
            return error.inner_text()
        return None

    def is_success_dialog_visible(self) -> bool:
        """Check if product creation success dialog is visible."""
        success = self.page.locator(
            "text=/success|successfully|успешно|created/i, .MuiDialog-root"
        ).first
        return success.is_visible(timeout=3000)
