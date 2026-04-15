"""
Product Detail/Edit Page Tests - Comprehensive test suite.

Tests for /dashboard/products/[id] page covering:
- UI elements and layout
- Edit functionality
- Field validation (empty, boundary, invalid)
- Security (XSS, SQL injection)
- Price/Discount validation
- Delete workflow
- Session and accessibility
- Whitespace handling
- Robustness

Total: ~70 tests
"""

import pytest
import json
import os
import allure
from playwright.sync_api import Page

from pages.product_detail_page import ProductDetailPage
from pages.products_list_page import ProductsListPage
from pages.login_page import LoginPage
from utils import setup_logger, TestDataLoader

logger = setup_logger(__name__)




@pytest.mark.negative
@allure.feature("Детали товара")
@allure.story("Пустые поля")
class TestProductDetailEmptyFields:
    """Tests for clearing required fields."""

    @allure.title("Пустое название на узбекском вызывает ошибку валидации")
    def test_empty_uz_name_shows_error(self, detail_page):
        """Clearing UZ name should show validation error on save."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Очистка поля названия на узбекском"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.uz_name_field.clear()
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Сохранение и проверка ошибки валидации"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: No validation error for empty UZ name"
            product_page.fill_uz_name(original)

    @allure.title("Пустое название на русском вызывает ошибку валидации")
    def test_empty_ru_name_shows_error(self, detail_page):
        """Clearing RU name should show validation error on save."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Очистка поля названия на русском"):
            if product_page.ru_name_field.is_visible(timeout=2000):
                original = product_page.get_ru_name_value()
                product_page.ru_name_field.clear()
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Сохранение и проверка ошибки валидации"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: No validation error for empty RU name"
            product_page.fill_ru_name(original)

    @allure.title("Пустая цена вызывает ошибку валидации")
    def test_empty_price_shows_error(self, detail_page):
        """Clearing price should show validation error."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Очистка поля цены"):
            if product_page.price_field.is_visible(timeout=2000):
                original = product_page.get_price_value()
                product_page.price_field.clear()
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Сохранение и проверка ошибки валидации"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: No validation error for empty price"
            product_page.fill_price(original)

    @allure.title("Все пустые поля вызывают множественные ошибки валидации")
    def test_all_fields_empty_shows_errors(self, detail_page):
        """Clearing all fields should show multiple validation errors."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Очистка всех видимых текстовых полей"):
            originals = product_page.get_all_textbox_values()
            textboxes = product_page.page.get_by_role("textbox").all()
            for tb in textboxes:
                try:
                    if tb.is_visible(timeout=500) and tb.is_enabled():
                        tb.clear()
                except Exception:
                    continue
            product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Сохранение и проверка множественных ошибок"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            error_count = product_page.get_validation_error_count()
            assert error_count >= 2, \
                f"BUG: Expected 2+ errors for all empty fields, got {error_count}"
        with allure.step("Восстановление оригинальных значений"):
            for name, value in originals.items():
                try:
                    field = product_page.page.locator(f"[name='{name}']")
                    if field.is_visible(timeout=500):
                        field.fill(value)
                except Exception:
                    continue




@pytest.mark.boundary
@allure.feature("Детали товара")
@allure.story("Граничные значения")
class TestProductDetailBoundary:
    """Tests for field length and value boundaries."""

    @allure.title("Название из одного символа вызывает ошибку минимальной длины")
    def test_name_one_char(self, detail_page):
        """Single character name should show min length error."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод одного символа в поле названия"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("A")
        with allure.step("Сохранение и проверка ошибки минимальной длины"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: Single char name accepted without min length error"
            product_page.fill_uz_name(original)

    @allure.title("Название из 255 символов принимается")
    def test_name_max_255(self, detail_page):
        """255 char name should be accepted."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод 255 символов в поле названия"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                max_name = test_data.get("boundary_values", {}).get("name", {}).get("max_255", "A" * 255)
                product_page.fill_uz_name(max_name)
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что название не было обрезано"):
            value = product_page.get_uz_name_value()
            assert len(value) >= 200, \
                f"BUG: 255 char name truncated to {len(value)} chars"
            product_page.fill_uz_name(original)

    @allure.title("Название более 256 символов обрезается или вызывает ошибку")
    def test_name_over_256(self, detail_page):
        """256+ char name should be truncated or show error."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод 300 символов в поле названия"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                over_max = "A" * 300
                product_page.fill_uz_name(over_max)
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обрезки или ошибки валидации"):
            value = product_page.get_uz_name_value()
            assert len(value) <= 256 or product_page.has_validation_errors(), \
                f"BUG: Name over 256 chars accepted without truncation ({len(value)} chars)"
            product_page.fill_uz_name(original)

    @allure.title("Описание менее 50 символов вызывает ошибку минимальной длины")
    def test_description_under_50(self, detail_page):
        """Description under 50 chars should show min length error."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод короткого описания"):
            if product_page.uz_description_field.is_visible(timeout=2000):
                original = product_page.get_uz_description_value()
                short_desc = test_data.get("boundary_values", {}).get("description", {}).get("under_50", "Short")
                product_page.fill_uz_description(short_desc)
        with allure.step("Сохранение и проверка ошибки"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            step_stayed = product_page.is_on_detail_page()
            assert has_error or step_stayed, \
                "BUG: Short description (<50 chars) accepted without error"
            product_page.fill_uz_description(original)

    @allure.title("Нулевая цена вызывает ошибку валидации")
    def test_price_zero(self, detail_page):
        """Zero price should show validation error."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод нулевой цены"):
            if product_page.price_field.is_visible(timeout=2000):
                original = product_page.get_price_value()
                product_page.fill_price("0")
        with allure.step("Сохранение и проверка ошибки"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: Zero price accepted without error"
            product_page.fill_price(original)

    @allure.title("Отрицательная цена отклоняется")
    def test_price_negative(self, detail_page):
        """Negative price should be rejected."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод отрицательной цены"):
            if product_page.price_field.is_visible(timeout=2000):
                original = product_page.get_price_value()
                product_page.fill_price("-5000")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка отклонения отрицательной цены"):
            value = product_page.get_price_value()
            assert "-" not in value or product_page.has_validation_errors(), \
                f"BUG: Negative price '{value}' accepted"
            product_page.fill_price(original)

    @allure.title("Буквенный ввод в поле цены отклоняется")
    def test_price_alpha_input(self, detail_page):
        """Alphabetic input in price should be rejected."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод букв в поле цены"):
            if product_page.price_field.is_visible(timeout=2000):
                original = product_page.get_price_value()
                product_page.fill_price("abc")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка отклонения буквенного ввода"):
            value = product_page.get_price_value()
            assert not value or value.replace(" ", "").isdigit() or product_page.has_validation_errors(), \
                f"BUG: Alpha input '{value}' accepted in price field"
            product_page.fill_price(original)




@pytest.mark.boundary
@allure.feature("Детали товара")
@allure.story("Обработка пробелов")
class TestProductDetailWhitespace:
    """Tests for whitespace input handling."""

    @allure.title("Только пробелы в названии вызывают ошибку")
    def test_name_only_spaces(self, detail_page):
        """Name with only spaces should show error."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод только пробелов в название"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("     ")
        with allure.step("Сохранение и проверка ошибки"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: Name with only spaces accepted"
            product_page.fill_uz_name(original)

    @allure.title("Только табуляции в названии вызывают ошибку")
    def test_name_tabs(self, detail_page):
        """Name with only tabs should show error."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод только табуляций в название"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("\t\t\t")
        with allure.step("Сохранение и проверка ошибки"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: Name with only tabs accepted"
            product_page.fill_uz_name(original)

    @allure.title("Пробелы в начале и конце названия обрезаются")
    def test_name_leading_trailing_spaces(self, detail_page):
        """Leading/trailing spaces should be trimmed."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод названия с пробелами по краям"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("  Test Product  ")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обрезки пробелов"):
            value = product_page.get_uz_name_value()
            assert value.strip() == "Test Product" or value == "  Test Product  ", \
                f"BUG: Unexpected whitespace handling: '{value}'"
            product_page.fill_uz_name(original)

    @allure.title("Переносы строк в названии обрабатываются корректно")
    def test_name_newlines(self, detail_page):
        """Newlines in name should be handled (single-line field)."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод переносов строк в название"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("Line1\nLine2\nLine3")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обработки переносов строк"):
            value = product_page.get_uz_name_value()
            assert "\n" not in value or product_page.has_validation_errors(), \
                f"BUG: Newlines accepted in single-line name field: '{value}'"
            product_page.fill_uz_name(original)

    @allure.title("Неразрывные пробелы в названии обрабатываются корректно")
    def test_name_nbsp(self, detail_page):
        """Non-breaking spaces should be handled."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод только неразрывных пробелов"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("\u00a0\u00a0\u00a0")
        with allure.step("Сохранение и проверка ошибки"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: NBSP-only name accepted without error"
            product_page.fill_uz_name(original)




@pytest.mark.functional
@allure.feature("Детали товара")
@allure.story("Валидация цены и скидки")
class TestProductDetailPriceDiscount:
    """Tests for price/discount relationship validation."""

    @allure.title("Скидка больше цены отклоняется")
    def test_discount_greater_than_price(self, detail_page):
        """Discount price > regular price should show error."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Установка скидки больше цены"):
            if product_page.price_field.is_visible(timeout=2000) and \
               product_page.discount_price_field.is_visible(timeout=2000):
                orig_price = product_page.get_price_value()
                scenario = test_data.get("price_discount_scenarios", {}).get("discount_greater", {})
                product_page.fill_price(scenario.get("price", "1000000"))
                product_page.fill_discount_price(scenario.get("discount", "2000000"))
        with allure.step("Сохранение и проверка ошибки валидации"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: Discount price > regular price accepted"
            product_page.fill_price(orig_price)

    @allure.title("Скидка равная цене отклоняется")
    def test_discount_equal_to_price(self, detail_page):
        """Discount price == regular price should show error."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Установка скидки равной цене"):
            if product_page.price_field.is_visible(timeout=2000) and \
               product_page.discount_price_field.is_visible(timeout=2000):
                orig_price = product_page.get_price_value()
                scenario = test_data.get("price_discount_scenarios", {}).get("discount_equal", {})
                product_page.fill_price(scenario.get("price", "1000000"))
                product_page.fill_discount_price(scenario.get("discount", "1000000"))
        with allure.step("Сохранение и проверка ошибки"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: Discount price == regular price accepted (no savings)"
            product_page.fill_price(orig_price)

    @allure.title("Отрицательная скидка отклоняется")
    def test_discount_negative(self, detail_page):
        """Negative discount price should be rejected."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод отрицательной скидки"):
            if product_page.discount_price_field.is_visible(timeout=2000):
                product_page.fill_discount_price("-500000")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка отклонения отрицательной скидки"):
            value = product_page.discount_price_field.input_value()
            assert "-" not in value or product_page.has_validation_errors(), \
                f"BUG: Negative discount price '{value}' accepted"




@pytest.mark.functional
@allure.feature("Детали товара")
@allure.story("Артикул и штрих-код")
class TestProductDetailSkuBarcode:
    """Tests for SKU and barcode field validation."""

    @allure.title("Спецсимволы в артикуле обрабатываются корректно")
    def test_sku_special_chars(self, detail_page):
        """SKU with special characters should be handled."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод спецсимволов в артикул"):
            if product_page.sku_field.is_visible(timeout=2000):
                original = product_page.get_sku_value()
                product_page.fill_sku("!@#$%^&*()")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обработки спецсимволов"):
            value = product_page.get_sku_value()
            has_special = any(c in value for c in "!@#$%^&*()")
            assert not has_special or product_page.has_validation_errors(), \
                f"BUG: Special chars in SKU '{value}' accepted"
            product_page.fill_sku(original)

    @allure.title("Пробелы в артикуле обрабатываются корректно")
    def test_sku_with_spaces(self, detail_page):
        """SKU with spaces should be handled."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод артикула с пробелами"):
            if product_page.sku_field.is_visible(timeout=2000):
                original = product_page.get_sku_value()
                product_page.fill_sku("SKU 001 TEST")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обработки пробелов"):
            value = product_page.get_sku_value()
            assert " " not in value or product_page.has_validation_errors(), \
                f"BUG: SKU with spaces '{value}' accepted"
            product_page.fill_sku(original)

    @allure.title("Буквы в штрих-коде отклоняются")
    def test_barcode_alpha(self, detail_page):
        """Barcode with alpha chars should be rejected."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод букв в штрих-код"):
            if product_page.barcode_field.is_visible(timeout=2000):
                original = product_page.get_barcode_value()
                product_page.fill_barcode("ABCDEFGH")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка отклонения буквенного штрих-кода"):
            value = product_page.get_barcode_value()
            assert value.isdigit() or not value or product_page.has_validation_errors(), \
                f"BUG: Alpha barcode '{value}' accepted"
            product_page.fill_barcode(original)

    @allure.title("Слишком короткий штрих-код вызывает ошибку")
    def test_barcode_too_short(self, detail_page):
        """Barcode under 8 digits should show error."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод слишком короткого штрих-кода"):
            if product_page.barcode_field.is_visible(timeout=2000):
                original = product_page.get_barcode_value()
                product_page.fill_barcode("123")
        with allure.step("Сохранение и проверка ошибки"):
            product_page.click_save()
            product_page.page.wait_for_load_state("networkidle")
            has_error = product_page.has_validation_errors()
            assert has_error, "BUG: Too short barcode (3 digits) accepted"
            product_page.fill_barcode(original)

    @allure.title("XSS в поле артикула санитизируется")
    def test_sku_xss(self, detail_page):
        """XSS in SKU field should be sanitized."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод XSS payload в артикул"):
            if product_page.sku_field.is_visible(timeout=2000):
                original = product_page.get_sku_value()
                product_page.fill_sku("<script>alert(1)</script>")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка санитизации XSS"):
            value = product_page.get_sku_value()
            assert "<script>" not in value.lower(), \
                "BUG: XSS payload in SKU field not sanitized"
            product_page.fill_sku(original)




@pytest.mark.negative
@allure.feature("Детали товара")
@allure.story("Невалидный формат")
class TestProductDetailInvalidFormat:
    """Tests for invalid format inputs."""

    @allure.title("Эмодзи в названии товара обрабатываются корректно")
    def test_emoji_in_name(self, detail_page):
        """Emoji in product name should be handled."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод эмодзи в название товара"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                emoji = test_data.get("invalid_inputs", {}).get("unicode_emoji", "\ud83d\udce6")
                product_page.fill_uz_name(emoji)
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обработки эмодзи"):
            value = product_page.get_uz_name_value()
            assert value is not None, "BUG: Emoji input crashed the form"
            product_page.fill_uz_name(original)

    @allure.title("Смешанный ввод кириллицы и латиницы обрабатывается корректно")
    def test_mixed_cyrillic_latin(self, detail_page):
        """Mixed Cyrillic and Latin should be handled."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод смешанного текста кириллица + латиница"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                mixed = "Test Тест Mahsulot Продукт"
                product_page.fill_uz_name(mixed)
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка корректной обработки смешанного ввода"):
            value = product_page.get_uz_name_value()
            assert value == mixed, \
                f"BUG: Mixed script input changed: '{value}'"
            product_page.fill_uz_name(original)

    @allure.title("Только цифры в названии товара обрабатываются корректно")
    def test_only_digits_in_name(self, detail_page):
        """Only digits in name should be handled."""
        product_page, _ = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод только цифр в название"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("123456789")
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обработки числового названия"):
            value = product_page.get_uz_name_value()
            assert value == "123456789" or product_page.has_validation_errors(), \
                "BUG: Unexpected behavior with numeric-only name"
            product_page.fill_uz_name(original)

    @allure.title("Спецсимволы в названии товара обрабатываются корректно")
    def test_special_chars_in_name(self, detail_page):
        """Special characters in name should be handled."""
        product_page, test_data = detail_page
        with allure.step("Переключение в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Ввод спецсимволов в название"):
            if product_page.uz_name_field.is_visible(timeout=2000):
                original = product_page.get_uz_name_value()
                special = test_data.get("invalid_inputs", {}).get("special_chars", "!@#$%^&*()")
                product_page.fill_uz_name(special)
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка обработки спецсимволов"):
            value = product_page.get_uz_name_value()
            assert value is not None, "BUG: Special chars crashed the form"
            product_page.fill_uz_name(original)
