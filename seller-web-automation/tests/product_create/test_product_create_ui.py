"""
Product Create UI tests - Step 1 and Step 2 element visibility.
"""

import pytest
import allure
import logging

logger = logging.getLogger(__name__)


# =============================================================================
# UI TESTS - STEP 1
# =============================================================================

@pytest.mark.ui
@pytest.mark.staging
@allure.feature("Создание товара - Интерфейс")
class TestProductCreateUIStep1:
    """UI element visibility tests for Step 1."""

    @allure.title("Комбобокс категории виден")
    def test_category_combobox_visible(self, product_create_page):
        """Category selection combobox should be visible on Step 1."""
        with allure.step("Проверка видимости комбобокса категории на Шаге 1"):
            assert product_create_page.is_category_combobox_visible(), \
                "BUG: Category combobox not visible on Step 1"

    @allure.title("Комбобокс ИКПУ виден")
    def test_ikpu_combobox_visible(self, product_create_page):
        """IKPU combobox should be visible."""
        with allure.step("Проверка видимости комбобокса ИКПУ"):
            ikpu = product_create_page.page.get_by_role("combobox").nth(1)
            assert ikpu.is_visible(timeout=3000), "BUG: IKPU combobox not visible"

    @allure.title("Комбобокс страны виден")
    def test_country_combobox_visible(self, product_create_page):
        """Country combobox should be visible."""
        with allure.step("Проверка видимости комбобокса страны"):
            country = product_create_page.page.get_by_role("combobox").nth(2)
            assert country.is_visible(timeout=3000), "BUG: Country combobox not visible"

    @allure.title("Комбобокс бренда виден")
    def test_brand_combobox_visible(self, product_create_page):
        """Brand combobox should be visible."""
        with allure.step("Проверка видимости комбобокса бренда"):
            brand = product_create_page.page.get_by_role("combobox").nth(3)
            assert brand.is_visible(timeout=3000), "BUG: Brand combobox not visible"

    @allure.title("Поле названия товара на узбекском видно")
    def test_uz_name_field_visible(self, product_create_page):
        """Uzbek product name field should be visible."""
        with allure.step("Прокрутка страницы к полям ввода"):
            product_create_page.scroll_page(300)
        with allure.step("Проверка видимости поля названия товара на узбекском"):
            field = product_create_page.page.locator("input").first
            if not field.is_visible(timeout=2000):
                field = product_create_page.page.get_by_label("узбекском", exact=False).or_(
                    product_create_page.page.get_by_label("o'zbek", exact=False)
                ).first
            assert field.is_visible(timeout=3000), "BUG: UZ name field not visible"

    @allure.title("Поле названия товара на русском видно")
    def test_ru_name_field_visible(self, product_create_page):
        """Russian product name field should be visible."""
        with allure.step("Прокрутка страницы к полям ввода"):
            product_create_page.scroll_page(300)
        with allure.step("Проверка видимости поля названия товара на русском"):
            inputs = product_create_page.page.locator("input").all()
            has_ru_input = len(inputs) >= 2
            if not has_ru_input:
                field = product_create_page.page.get_by_label("русском", exact=False).or_(
                    product_create_page.page.get_by_label("rus", exact=False)
                ).first
                has_ru_input = field.is_visible(timeout=2000)
            assert has_ru_input, "BUG: RU name field not visible"

    @allure.title("Поле описания на узбекском видно")
    def test_uz_description_field_visible(self, product_create_page):
        """Uzbek description field should be visible."""
        with allure.step("Прокрутка страницы к полям описания"):
            product_create_page.scroll_page(300)
        with allure.step("Проверка видимости поля описания на узбекском"):
            field = product_create_page.page.locator("textarea").first
            assert field.is_visible(timeout=3000), "BUG: UZ description field not visible"

    @allure.title("Поле описания на русском видно")
    def test_ru_description_field_visible(self, product_create_page):
        """Russian description field should be visible."""
        with allure.step("Прокрутка страницы к полям описания"):
            product_create_page.scroll_page(400)
        with allure.step("Проверка видимости поля описания на русском"):
            textareas = product_create_page.page.locator("textarea").all()
            has_ru_textarea = len(textareas) >= 2
            assert has_ru_textarea, "BUG: RU description field not visible"

    @allure.title("Кнопка 'Далее' видна")
    def test_next_button_visible(self, product_create_page):
        """Next button should be visible on Step 1."""
        with allure.step("Прокрутка страницы к кнопке 'Далее'"):
            product_create_page.scroll_page(500)
        with allure.step("Проверка видимости кнопки 'Далее'"):
            next_btn = product_create_page.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last
            assert next_btn.is_visible(timeout=3000), "BUG: Next button not visible"

    @allure.title("URL страницы корректен для Шага 1")
    def test_page_url_step1(self, product_create_page):
        """URL should contain /products/create."""
        with allure.step("Проверка что URL содержит /products/create"):
            assert "/products/create" in product_create_page.page.url, \
                f"BUG: Wrong URL, expected /products/create, got {product_create_page.page.url}"


# =============================================================================
# UI TESTS - STEP 2
# =============================================================================

@pytest.mark.ui
@pytest.mark.staging
@allure.feature("Создание товара - Интерфейс Шаг 2")
class TestProductCreateUIStep2:
    """UI element visibility tests for Step 2 (Variant/SKU)."""

    @allure.title("Поле SKU видно на Шаге 2")
    def test_sku_field_visible(self, product_on_step2):
        """SKU field should be visible on Step 2."""
        with allure.step("Проверка видимости поля SKU на Шаге 2"):
            sku = product_on_step2.page.get_by_role("textbox", name="SKU")
            assert sku.is_visible(timeout=5000), "BUG: SKU field not visible on Step 2"

    @allure.title("Поле штрих-кода видно")
    def test_barcode_field_visible(self, product_on_step2):
        """Barcode field should be visible."""
        with allure.step("Проверка видимости поля штрих-кода"):
            barcode = product_on_step2.page.locator("input[name='variant.barcode']").first
            assert barcode.is_visible(timeout=3000), "BUG: Barcode field not visible"

    @allure.title("Поле цены видно")
    def test_price_field_visible(self, product_on_step2):
        """Regular price field should be visible."""
        with allure.step("Проверка видимости поля цены"):
            price = product_on_step2.page.locator("input[name='variant.price']").first
            assert price.is_visible(timeout=3000), "BUG: Price field not visible"

    @allure.title("Поле цены со скидкой видно")
    def test_discount_price_field_visible(self, product_on_step2):
        """Discount price field should be visible."""
        with allure.step("Проверка видимости поля цены со скидкой"):
            discount = product_on_step2.page.locator("input[name='variant.discountPrice']").first
            assert discount.is_visible(timeout=3000), "BUG: Discount price field not visible"

    @allure.title("Поля габаритов видны")
    def test_dimension_fields_visible(self, product_on_step2):
        """Width, Length, Height fields should be visible."""
        with allure.step("Прокрутка страницы к полям габаритов"):
            product_on_step2.scroll_page(300)
        with allure.step("Поиск полей ширины, длины и высоты"):
            width = product_on_step2.page.locator(
                "input[name='width'], [aria-label*='Width'], [aria-label*='Eni']"
            ).first.or_(
                product_on_step2.page.get_by_role("textbox", name="Eni (mm)")
            )
            length = product_on_step2.page.locator(
                "input[name='length'], [aria-label*='Length'], [aria-label*='Uzunligi']"
            ).first.or_(
                product_on_step2.page.get_by_role("textbox", name="Uzunligi (mm)")
            )
            height = product_on_step2.page.locator(
                "input[name='height'], [aria-label*='Height'], [aria-label*='Balandligi']"
            ).first.or_(
                product_on_step2.page.get_by_role("textbox", name="Balandligi (mm)")
            )
        with allure.step("Проверка видимости полей габаритов"):
            assert width.is_visible(timeout=3000), "BUG: Width field not visible"
            assert length.is_visible(timeout=3000), "BUG: Length field not visible"
            assert height.is_visible(timeout=3000), "BUG: Height field not visible"

    @allure.title("Поле веса видно")
    def test_weight_field_visible(self, product_on_step2):
        """Weight field should be visible."""
        with allure.step("Прокрутка страницы к полю веса"):
            product_on_step2.scroll_page(300)
        with allure.step("Проверка видимости поля веса"):
            weight = product_on_step2.page.locator(
                "input[name='weight'], [aria-label*='Weight'], [aria-label*=\"Og'irligi\"]"
            ).first.or_(
                product_on_step2.page.get_by_role("textbox", name="Weight (kg)")
            ).or_(
                product_on_step2.page.get_by_role("textbox", name="Og'irligi (kg)")
            )
            assert weight.is_visible(timeout=3000), "BUG: Weight field not visible"
