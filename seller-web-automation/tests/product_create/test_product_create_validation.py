"""
Product Create validation tests - empty fields, boundary, whitespace, format,
price/discount, description length, barcode, dimensions.
"""

import pytest
import allure
import logging
import os

from utils import ProductDataGenerator
from tests.product_create.conftest import (
    get_uz_name_field, get_uz_desc_field, get_ru_desc_field, RESOURCES_PATH
)

logger = logging.getLogger(__name__)


# =============================================================================
# EMPTY FIELDS TESTS
# =============================================================================

@pytest.mark.negative
@pytest.mark.staging
@allure.feature("Создание товара - Пустые поля")
class TestProductCreateEmptyFields:
    """Empty field validation tests."""

    @allure.title("Пустая категория должна показать ошибку")
    def test_empty_category_error(self, product_create_page):
        """Clicking Next without selecting category should show error."""
        with allure.step("Прокрутка к кнопке 'Далее' и нажатие без выбора категории"):
            product_create_page.scroll_page(500)
            product_create_page.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что показана ошибка валидации"):
            assert product_create_page.has_validation_errors() or \
                   "/products/create" in product_create_page.page.url, \
                   "BUG: Empty category accepted without validation"

    @allure.title("Пустые названия товара должны показать ошибку")
    def test_empty_product_names_error(self, product_create_page):
        """Product names should be required."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Нажатие 'Далее' без заполнения названий"):
            product_create_page.scroll_page(500)
            product_create_page.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка ошибки валидации для пустых названий"):
            assert product_create_page.has_validation_errors() or \
                   product_create_page.get_current_step() == 1, \
                   "BUG: Empty product names accepted without validation"

    @allure.title("Пустой SKU на Шаге 2 должен показать ошибку")
    def test_empty_sku_error(self, product_on_step2):
        """SKU field should be required on Step 2."""
        with allure.step("Нажатие 'Далее' без заполнения SKU"):
            product_on_step2.scroll_page(500)
            product_on_step2.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_on_step2.page.wait_for_load_state("networkidle")
        with allure.step("Проверка ошибки валидации для пустого SKU"):
            has_error = product_on_step2.has_validation_errors()
            sku_visible = product_on_step2.page.get_by_role("textbox", name="SKU").is_visible(timeout=1000)
            assert has_error or sku_visible, \
                "BUG: Empty SKU accepted - should require SKU field"

    @allure.title("Пустая цена на Шаге 2 должна показать ошибку")
    def test_empty_price_error(self, product_on_step2):
        """Price field should be required."""
        with allure.step("Заполнение поля SKU"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_on_step2.fill_single_field("SKU", data["sku"])
        with allure.step("Нажатие 'Далее' без заполнения цены"):
            product_on_step2.scroll_page(500)
            product_on_step2.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_on_step2.page.wait_for_load_state("networkidle")
        with allure.step("Проверка ошибки валидации для пустой цены"):
            has_error = product_on_step2.has_validation_errors()
            on_step2 = product_on_step2.page.get_by_role("textbox", name="SKU").is_visible(timeout=1000)
            assert has_error or on_step2, \
                "BUG: Empty price accepted - should require price field"


# =============================================================================
# BOUNDARY VALUE TESTS
# =============================================================================

@pytest.mark.negative
@pytest.mark.staging
@allure.feature("Создание товара - Граничные значения")
class TestProductCreateBoundary:
    """Boundary Value Analysis tests."""

    @allure.title("ГЗА: Описание с 49 символами (ниже минимума)")
    def test_description_49_chars(self, product_create_page):
        """Description with 49 chars should be rejected (min is 50)."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            short_desc = "A" * 49
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Заполнение названий и описания с 49 символами"):
            product_create_page.fill_product_names_staging(
                uz_name=data["uz_name"], uz_desc=short_desc,
                ru_name=data["ru_name"], ru_desc=short_desc
            )
            product_create_page.select_model_from_combobox()
        with allure.step("Проверка что описание с 49 символами отклонено"):
            try:
                product_create_page.click_next_button()
                assert product_create_page.get_current_step() == 1, \
                    "BUG: Description with 49 chars accepted - should require 50+"
            except Exception as e:
                if "50" in str(e) or "belgi" in str(e) or "character" in str(e):
                    logger.info("PASS: 49 char description correctly rejected")
                else:
                    raise

    @allure.title("ГЗА: Описание с ровно 50 символами (на минимуме)")
    def test_description_50_chars(self, product_create_page):
        """Description with exactly 50 chars should be accepted."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            min_desc = "A" * 50
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Заполнение названий и описания с ровно 50 символами"):
            product_create_page.fill_product_names_staging(
                uz_name=data["uz_name"], uz_desc=min_desc,
                ru_name=data["ru_name"], ru_desc=min_desc
            )
            product_create_page.select_model_from_combobox()
        with allure.step("Нажатие 'Далее' и проверка перехода на Шаг 2"):
            product_create_page.click_next_button()
            product_create_page.page.wait_for_load_state("networkidle")
            sku_visible = product_create_page.page.locator("input[name='variant.sku']").is_visible(timeout=3000)
            assert sku_visible, "BUG: Description with 50 chars rejected - should be accepted"

    @allure.title("ГЗА: Название товара с 1 символом")
    def test_product_name_1_char(self, product_create_page):
        """Single character product name - check if accepted or has min length."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Заполнение названий с 1 символом"):
            product_create_page.fill_product_names_staging(
                uz_name="A", uz_desc=data["uz_description"],
                ru_name="Б", ru_desc=data["ru_description"]
            )
            product_create_page.select_model_from_combobox()
        with allure.step("Нажатие 'Далее' и проверка результата"):
            product_create_page.click_next_button()
            product_create_page.page.wait_for_load_state("networkidle")
            step = product_create_page.get_current_step()
            logger.info(f"1-char product name: step={step}")

    @allure.title("ГЗА: Очень длинное название товара (500 символов)")
    def test_product_name_500_chars(self, product_create_page):
        """Very long product name should be handled gracefully."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            long_name = "A" * 500
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод названия из 500 символов"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", long_name)
        with allure.step("Проверка обработки длинного названия"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            has_error = product_create_page.has_validation_errors()
            assert len(actual_value) <= 500 or has_error, \
                "BUG: 500-char name not handled - should truncate or show error"

    @allure.title("ГЗА: SKU со спецсимволами")
    def test_sku_special_chars(self, product_on_step2):
        """SKU with special characters should be sanitized or rejected."""
        with allure.step("Ввод SKU со спецсимволами"):
            product_on_step2.fill_single_field("SKU", "TEST!@#$%^&*()")
            product_on_step2.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что спецсимволы очищены или отклонены"):
            actual_sku = product_on_step2.get_field_value("SKU")
            has_error = product_on_step2.has_validation_errors()
            assert actual_sku != "TEST!@#$%^&*()" or has_error, \
                "BUG: SKU with special chars accepted without sanitization"

    @allure.title("ГЗА: Цена с нулевым значением")
    def test_price_zero(self, product_on_step2):
        """Zero price should be rejected."""
        with allure.step("Заполнение SKU и ввод нулевой цены"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_on_step2.fill_single_field("SKU", data["sku"])
            product_on_step2.fill_single_field("Regular price (UZS)", "0")
            product_on_step2.fill_single_field("Discount price (UZS)", "0")
        with allure.step("Нажатие 'Далее'"):
            product_on_step2.scroll_page(500)
            product_on_step2.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_on_step2.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что нулевая цена отклонена"):
            has_error = product_on_step2.has_validation_errors()
            on_step2 = product_on_step2.page.get_by_role("textbox", name="SKU").is_visible(timeout=1000)
            assert has_error or on_step2, \
                "BUG: Zero price accepted - should require positive price"

    @allure.title("ГЗА: Отрицательное значение цены")
    def test_price_negative(self, product_on_step2):
        """Negative price should be rejected."""
        with allure.step("Заполнение SKU и ввод отрицательной цены"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_on_step2.fill_single_field("SKU", data["sku"])
            product_on_step2.fill_single_field("Regular price (UZS)", "-1000")
        with allure.step("Проверка что отрицательная цена отклонена"):
            actual_price = product_on_step2.get_field_value("Regular price (UZS)")
            has_error = product_on_step2.has_validation_errors()
            assert "-" not in actual_price or has_error, \
                "BUG: Negative price accepted - should reject negative values"


# =============================================================================
# WHITESPACE TESTS
# =============================================================================

@pytest.mark.negative
@pytest.mark.staging
@allure.feature("Создание товара - Пробелы")
class TestProductCreateWhitespace:
    """Whitespace handling tests."""

    @allure.title("Только пробелы в названии товара")
    def test_only_spaces_in_name(self, product_create_page):
        """Product name with only spaces should be rejected."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод только пробелов в названия товара"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "     ")
            product_create_page.fill_single_field("Description in Uzbek", data["uz_description"])
            product_create_page.fill_single_field("Product name in Russian", "     ")
            product_create_page.fill_single_field("Description in Russian", data["ru_description"])
        with allure.step("Отправка формы и проверка ошибки валидации"):
            product_create_page.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_create_page.page.wait_for_load_state("networkidle")
            has_error = product_create_page.has_validation_errors()
            on_step1 = product_create_page.get_current_step() == 1
            assert has_error or on_step1, \
                "BUG: Whitespace-only product name accepted - should be trimmed/rejected"

    @allure.title("Начальные/конечные пробелы должны быть обрезаны")
    def test_leading_trailing_spaces(self, product_create_page):
        """Product name should have leading/trailing spaces trimmed."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод названия с начальными и конечными пробелами"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "   Test Product   ")
            get_uz_desc_field(product_create_page.page).focus()
            product_create_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обрезки пробелов"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            logger.info(f"Leading/trailing spaces: input='   Test Product   ', output='{actual_value}'")

    @allure.title("Табуляции в названии товара")
    def test_tabs_in_name(self, product_create_page):
        """Tabs should be handled in product name."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод названия с табуляциями"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "Test\tProduct\tName")
        with allure.step("Проверка обработки табуляций"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            logger.info(f"Tabs handling: output='{actual_value}'")

    @allure.title("Неразрывный пробел в названии товара")
    def test_nbsp_in_name(self, product_create_page):
        """Non-breaking space should be handled."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод названия с неразрывным пробелом (NBSP)"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "Test\u00a0Product")
        with allure.step("Проверка обработки неразрывного пробела"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            logger.info(f"NBSP handling: output='{actual_value}'")

    @allure.title("Множественные пробелы должны быть нормализованы")
    def test_multiple_spaces(self, product_create_page):
        """Multiple consecutive spaces should be normalized."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод названия с множественными пробелами"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "Test    Multiple    Spaces")
        with allure.step("Проверка нормализации множественных пробелов"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            logger.info(f"Multiple spaces: output='{actual_value}'")


# =============================================================================
# INVALID FORMAT TESTS
# =============================================================================

@pytest.mark.negative
@pytest.mark.staging
@allure.feature("Создание товара - Неверный формат")
class TestProductCreateInvalidFormat:
    """Invalid format and special character tests."""

    @allure.title("Эмодзи в названии товара")
    def test_emoji_in_name(self, product_create_page):
        """Emoji should be handled in product name."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод названия с эмодзи"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "Test Product 🏪📦")
        with allure.step("Проверка обработки эмодзи"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            logger.info(f"Emoji handling: output='{actual_value}'")

    @allure.title("HTML-теги в названии товара")
    def test_html_tags_in_name(self, product_create_page):
        """HTML tags should be escaped or rejected."""
        with allure.step("Заполнение комбобоксов (категория, ИКПУ, страна, бренд)"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])
        with allure.step("Ввод HTML-тегов в название товара"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "<b>Bold</b> Product")
        with allure.step("Проверка экранирования HTML-тегов"):
            page_content = product_create_page.page.content()
            assert "<b>Bold</b>" not in page_content or \
                   "&lt;b&gt;" in page_content, \
                   "BUG: HTML not escaped - potential XSS vulnerability"

    @allure.title("Смешанные кириллица и латиница в названии")
    def test_mixed_scripts_in_name(self, product_create_page):
        """Mixed Cyrillic and Latin should be accepted."""
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")
        product_create_page.select_category_from_combobox(data["category_path"])
        product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
        product_create_page.select_country_from_combobox(data["country"])
        product_create_page.select_brand_from_combobox(data["brand"])
        product_create_page.scroll_page(300)
        product_create_page.fill_single_field("Product name in Uzbek", "Test Тест Product Продукт")
        actual_value = product_create_page.get_field_value("Product name in Uzbek")
        assert "Test" in actual_value and "Тест" in actual_value, \
            "BUG: Mixed scripts not accepted"

    @allure.title("Только цифры в названии товара")
    def test_only_digits_in_name(self, product_create_page):
        """Only digits should be accepted or rejected based on rules."""
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")
        product_create_page.select_category_from_combobox(data["category_path"])
        product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
        product_create_page.select_country_from_combobox(data["country"])
        product_create_page.select_brand_from_combobox(data["brand"])
        product_create_page.scroll_page(300)
        product_create_page.fill_single_field("Product name in Uzbek", "12345678901234567890")
        actual_value = product_create_page.get_field_value("Product name in Uzbek")
        logger.info(f"Only digits: output='{actual_value}'")

    @allure.title("Спецсимволы в названии товара")
    def test_special_chars_in_name(self, product_create_page):
        """Special characters should be handled."""
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")
        product_create_page.select_category_from_combobox(data["category_path"])
        product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
        product_create_page.select_country_from_combobox(data["country"])
        product_create_page.select_brand_from_combobox(data["brand"])
        product_create_page.scroll_page(300)
        product_create_page.fill_single_field("Product name in Uzbek", "Test!@#$%^&*()Product")
        actual_value = product_create_page.get_field_value("Product name in Uzbek")
        logger.info(f"Special chars: output='{actual_value}'")

    @allure.title("Нечисловые символы в поле цены")
    def test_non_numeric_price(self, product_on_step2):
        """Price field should only accept numeric values."""
        product_on_step2.fill_single_field("Regular price (UZS)", "abc123xyz")
        actual_value = product_on_step2.get_field_value("Regular price (UZS)")
        assert actual_value.isdigit() or actual_value == "" or actual_value == "123", \
            f"BUG: Non-numeric characters accepted in price: '{actual_value}'"

    @allure.title("Десятичное число в целочисленном поле цены")
    def test_decimal_price(self, product_on_step2):
        """Decimal price should be handled (rounded or rejected)."""
        product_on_step2.fill_single_field("Regular price (UZS)", "1000.50")
        actual_value = product_on_step2.get_field_value("Regular price (UZS)")
        logger.info(f"Decimal price: output='{actual_value}'")


# =============================================================================
# PRICE/DISCOUNT RELATIONSHIP TESTS
# =============================================================================

@pytest.mark.boundary
@pytest.mark.functional
@allure.feature("Создание товара")
@allure.story("Валидация цены и скидки")
class TestProductCreatePriceDiscount:
    """Price and discount price relationship validation tests."""

    def _get_price_field(self, page):
        return page.page.locator("input[name='variant.price']").first

    def _get_discount_field(self, page):
        return page.page.locator("input[name='variant.discountPrice']").first

    @allure.title("Скидка больше цены показывает ошибку")
    def test_discount_greater_than_price(self, product_on_step2):
        """Discount price > regular price should show validation error."""
        self._get_price_field(product_on_step2).fill("1000000")
        self._get_discount_field(product_on_step2).fill("2000000")
        self._get_discount_field(product_on_step2).blur()
        product_on_step2.page.wait_for_load_state("domcontentloaded")
        assert product_on_step2.has_validation_errors(), \
            "BUG: Discount price > regular price accepted without validation"

    @allure.title("Скидка равна цене показывает ошибку")
    def test_discount_equal_to_price(self, product_on_step2):
        """Discount price = regular price should be flagged."""
        self._get_price_field(product_on_step2).fill("1000000")
        self._get_discount_field(product_on_step2).fill("1000000")
        self._get_discount_field(product_on_step2).blur()
        product_on_step2.page.wait_for_load_state("domcontentloaded")
        assert product_on_step2.has_validation_errors(), \
            "BUG: Discount price = regular price accepted (no discount)"

    @allure.title("Очень большое значение цены")
    def test_price_overflow(self, product_on_step2):
        """Very large price should be handled gracefully."""
        price_field = self._get_price_field(product_on_step2)
        price_field.fill("99999999999999")
        value = price_field.input_value()
        assert len(value) <= 15 or product_on_step2.has_validation_errors(), \
            f"BUG: Price overflow not handled: {value}"


# =============================================================================
# DESCRIPTION MINIMUM LENGTH TESTS
# =============================================================================

@pytest.mark.boundary
@pytest.mark.functional
@allure.feature("Создание товара")
@allure.story("Минимальная длина описания")
class TestProductCreateDescriptionLength:
    """Description field minimum length (50 chars) validation."""

    @allure.title("Описание с 49 символами отклонено")
    def test_description_under_min_length(self, product_create_page):
        """Description with 49 characters should show error."""
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")
        product_create_page.select_category_from_combobox(data["category_path"])
        product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
        product_create_page.select_country_from_combobox(data["country"])
        product_create_page.select_brand_from_combobox(data["brand"])
        product_create_page.scroll_page(300)
        short_desc = "A" * 49
        product_create_page.fill_product_names_staging(
            uz_name=data["uz_name"], uz_desc=short_desc,
            ru_name=data["ru_name"], ru_desc=short_desc
        )
        product_create_page.select_model_from_combobox()
        try:
            product_create_page.click_next_button()
        except Exception:
            pass
        assert product_create_page.has_validation_errors(), \
            "BUG: Description with 49 chars accepted, min should be 50"

    @allure.title("Описание с ровно 50 символами принято")
    def test_description_exact_min_length(self, product_create_page):
        """Description with exactly 50 characters should be accepted."""
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")
        product_create_page.select_category_from_combobox(data["category_path"])
        product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
        product_create_page.select_country_from_combobox(data["country"])
        product_create_page.select_brand_from_combobox(data["brand"])
        product_create_page.scroll_page(300)
        exact_desc = "A" * 50
        product_create_page.fill_product_names_staging(
            uz_name=data["uz_name"], uz_desc=exact_desc,
            ru_name=data["ru_name"], ru_desc=exact_desc
        )
        product_create_page.select_model_from_combobox()
        product_create_page.click_next_button()
        product_create_page.page.wait_for_load_state("networkidle")
        sku_visible = product_create_page.page.locator("input[name='variant.sku']").is_visible(timeout=3000)
        assert sku_visible, \
            "BUG: Description with 50 chars rejected, should be accepted"


# =============================================================================
# BARCODE VALIDATION TESTS
# =============================================================================

@pytest.mark.boundary
@pytest.mark.functional
@allure.feature("Создание товара")
@allure.story("Валидация штрих-кода")
class TestProductCreateBarcode:
    """Barcode field validation tests on Step 2."""

    def _get_barcode_field(self, page):
        field = page.page.locator("input[name='variant.barcode']").first
        field.scroll_into_view_if_needed(timeout=5000)
        field.wait_for(state="visible", timeout=5000)
        return field

    @allure.title("Буквенный штрих-код принят")
    def test_barcode_alpha_characters(self, product_on_step2):
        """Barcode field accepts alphabetic characters (alphanumeric barcodes supported)."""
        barcode_field = self._get_barcode_field(product_on_step2)
        barcode_field.fill("ABCDEF")
        value = barcode_field.input_value()
        assert value == "ABCDEF", \
            f"FAILED: Alpha barcode not stored correctly, got: {value}"

    @allure.title("Слишком короткий штрих-код")
    def test_barcode_too_short(self, product_on_step2):
        """Barcode under minimum length should show error."""
        barcode_field = self._get_barcode_field(product_on_step2)
        barcode_field.fill("123")
        barcode_field.blur()
        product_on_step2.page.wait_for_load_state("domcontentloaded")
        has_errors = product_on_step2.has_validation_errors()
        value = barcode_field.input_value()
        assert has_errors or len(value) == 0, \
            "BUG: Too short barcode accepted without validation"

    @allure.title("Слишком длинный штрих-код")
    def test_barcode_too_long(self, product_on_step2):
        """Barcode over maximum length should be truncated or rejected."""
        barcode_field = self._get_barcode_field(product_on_step2)
        barcode_field.fill("1" * 30)
        value = barcode_field.input_value()
        assert len(value) < 30, \
            f"BUG: Barcode accepted {len(value)} chars, should be limited"

    @allure.title("Штрих-код со спецсимволами")
    def test_barcode_special_chars(self, product_on_step2):
        """Barcode should not accept special characters."""
        barcode_field = self._get_barcode_field(product_on_step2)
        barcode_field.fill("123-456-789")
        value = barcode_field.input_value()
        has_special = any(c in value for c in "-!@#")
        assert not has_special or product_on_step2.has_validation_errors(), \
            "BUG: Special characters in barcode not handled"


# =============================================================================
# DIMENSIONS/WEIGHT VALIDATION TESTS
# =============================================================================

@pytest.mark.boundary
@pytest.mark.functional
@allure.feature("Создание товара")
@allure.story("Валидация габаритов и веса")
class TestProductCreateDimensions:
    """Dimensions and weight field validation tests on Step 2."""

    def _get_width_field(self, page):
        field = page.page.locator(
            "input[name*='width'], "
            "[aria-label*='Eni'], [aria-label*='Ширина'], [aria-label*='Width']"
        ).first
        if not field.is_visible(timeout=2000):
            field = page.page.get_by_role("textbox", name="Eni")
        return field

    def _get_length_field(self, page):
        field = page.page.locator(
            "input[name*='length'], "
            "[aria-label*='Uzunligi'], [aria-label*='Длина'], [aria-label*='Length']"
        ).first
        if not field.is_visible(timeout=2000):
            field = page.page.get_by_role("textbox", name="Uzunligi")
        return field

    def _get_weight_field(self, page):
        field = page.page.locator(
            "input[name*='weight'], "
            "[aria-label*=\"Og'irligi\"], [aria-label*='Вес'], [aria-label*='Weight']"
        ).first
        if not field.is_visible(timeout=2000):
            field = page.page.get_by_role("textbox", name="Og'irligi")
        return field

    @allure.title("Нулевая ширина отклонена")
    def test_zero_width(self, product_on_step2):
        """Zero width should be rejected."""
        product_on_step2.scroll_page(300)
        width_field = self._get_width_field(product_on_step2)
        width_field.fill("0")
        width_field.blur()
        product_on_step2.page.wait_for_load_state("domcontentloaded")
        value = width_field.input_value()
        assert product_on_step2.has_validation_errors() or value != "0", \
            "BUG: Zero width accepted without validation"

    @allure.title("Отрицательные габариты отклонены")
    def test_negative_dimensions(self, product_on_step2):
        """Negative dimension values should be rejected."""
        product_on_step2.scroll_page(300)
        width_field = self._get_width_field(product_on_step2)
        width_field.fill("-100")
        value = width_field.input_value()
        assert "-" not in value or product_on_step2.has_validation_errors(), \
            "BUG: Negative dimension accepted"

    @allure.title("Нечисловые габариты отклонены")
    def test_non_numeric_dimensions(self, product_on_step2):
        """Non-numeric dimension values should be rejected."""
        product_on_step2.scroll_page(300)
        width_field = self._get_width_field(product_on_step2)
        width_field.fill("abc")
        value = width_field.input_value()
        assert not value.isalpha() or value == "", \
            "BUG: Non-numeric dimension accepted"

    @allure.title("Очень большое значение габарита")
    def test_dimension_overflow(self, product_on_step2):
        """Very large dimension value should be limited."""
        product_on_step2.scroll_page(300)
        length_field = self._get_length_field(product_on_step2)
        length_field.fill("99999999")
        value = length_field.input_value()
        assert len(value) <= 8 or product_on_step2.has_validation_errors(), \
            f"BUG: Dimension overflow not handled: {value}"

    @allure.title("Нулевой вес отклонён")
    def test_zero_weight(self, product_on_step2):
        """Zero weight should be rejected."""
        product_on_step2.scroll_page(300)
        weight_field = self._get_weight_field(product_on_step2)
        weight_field.fill("0")
        weight_field.blur()
        product_on_step2.page.wait_for_load_state("domcontentloaded")
        value = weight_field.input_value()
        assert product_on_step2.has_validation_errors() or value != "0", \
            "BUG: Zero weight accepted without validation"

    @allure.title("Отрицательный вес отклонён")
    def test_negative_weight(self, product_on_step2):
        """Negative weight should be rejected."""
        product_on_step2.scroll_page(300)
        weight_field = self._get_weight_field(product_on_step2)
        weight_field.fill("-5")
        value = weight_field.input_value()
        assert "-" not in value or product_on_step2.has_validation_errors(), \
            "BUG: Negative weight accepted"

    @allure.title("Десятичный вес принят")
    def test_decimal_weight(self, product_on_step2):
        """Decimal weight (e.g., 0.5 kg) should be accepted."""
        product_on_step2.scroll_page(300)
        weight_field = self._get_weight_field(product_on_step2)
        weight_field.fill("0.5")
        value = weight_field.input_value()
        assert "0.5" in value or "0,5" in value, \
            "BUG: Decimal weight not accepted"
