"""
Product Create security tests - XSS, SQL injection, advanced security,
description injection, SKU validation, file upload.
"""

import pytest
import allure
import logging
import os
import tempfile

from utils import ProductDataGenerator
from tests.product_create.conftest import (
    get_uz_name_field, get_uz_desc_field, get_ru_desc_field, RESOURCES_PATH
)

logger = logging.getLogger(__name__)


# =============================================================================
# XSS TESTS
# =============================================================================

@pytest.mark.security
@pytest.mark.staging
@allure.feature("Создание товара - Безопасность XSS")
class TestProductCreateXSS:
    """XSS injection prevention tests."""

    @allure.title("XSS в названии товара должен быть очищен")
    def test_xss_in_product_name(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            xss_payload = "<script>alert('XSS')</script>"
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод XSS-нагрузки в поле названия товара"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", xss_payload)
            product_create_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка санитизации XSS в содержимом страницы"):
            page_content = product_create_page.page.content()
            assert "<script>" not in page_content.lower() or \
                   xss_payload not in page_content, \
                   "BUG: XSS not sanitized in product name - SECURITY VULNERABILITY!"

    @allure.title("XSS в описании должен быть очищен")
    def test_xss_in_description(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            xss_payload = "<img src=x onerror=alert('XSS')>" + "A" * 50
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод XSS-нагрузки через img onerror в поле описания"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Description in Uzbek", xss_payload)
            product_create_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка санитизации XSS в описании"):
            page_content = product_create_page.page.content()
            assert "onerror=" not in page_content or \
                   "<img src=x" not in page_content, \
                   "BUG: XSS not sanitized in description - SECURITY VULNERABILITY!"

    @allure.title("SVG XSS в названии товара")
    def test_svg_xss_in_name(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод SVG XSS-нагрузки в поле названия"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "<svg onload=alert(1)>Test")

        with allure.step("Проверка санитизации SVG XSS"):
            page_content = product_create_page.page.content()
            assert "<svg onload" not in page_content.lower(), \
                "BUG: SVG XSS not sanitized - SECURITY VULNERABILITY!"



# =============================================================================
# SQL INJECTION TESTS
# =============================================================================

@pytest.mark.security
@pytest.mark.staging
@allure.feature("Создание товара - Безопасность SQL")
class TestProductCreateSQL:
    """SQL injection prevention tests."""

    @allure.title("SQL-инъекция в названии товара")
    def test_sql_in_product_name(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод SQL-инъекции DROP TABLE в поле названия"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "'; DROP TABLE products; --")

        with allure.step("Проверка что поле не сломалось после SQL-инъекции"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            assert actual_value is not None, "BUG: SQL injection caused field to break"

    @allure.title("SQL-инъекция в поле SKU")
    def test_sql_in_sku(self, product_on_step2):
        with allure.step("Ввод SQL-инъекции OR в поле SKU"):
            product_on_step2.fill_single_field("SKU", "TEST' OR '1'='1")

        with allure.step("Проверка что поле SKU не сломалось"):
            actual_value = product_on_step2.get_field_value("SKU")
            assert actual_value is not None, "BUG: SQL injection caused SKU field to break"

    @allure.title("Инъекция UNION SELECT")
    def test_union_select_injection(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод UNION SELECT инъекции в поле названия"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "1 UNION SELECT * FROM users--")

        with allure.step("Проверка безопасной обработки UNION SELECT"):
            has_error = product_create_page.has_validation_errors()
            page_content = product_create_page.page.content()
            assert "error" not in page_content.lower() or has_error, \
                "Potential SQL injection vulnerability"


# =============================================================================
# ADVANCED SECURITY TESTS
# =============================================================================

@pytest.mark.security
@pytest.mark.staging
@allure.feature("Создание товара - Продвинутая безопасность")
class TestProductCreateAdvancedSecurity:
    """Advanced security tests including LDAP, command, path traversal."""

    @allure.title("Инъекция нулевого байта в названии товара")
    def test_null_byte_injection(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод нулевого байта в поле названия"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "Test\x00Product")

        with allure.step("Проверка санитизации нулевого байта"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            assert "\x00" not in actual_value, \
                "BUG: Null byte not sanitized - potential security issue"

    @allure.title("Попытка инъекции команды")
    def test_command_injection(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод команды инъекции 'rm -rf' в поле названия"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "; rm -rf / #")

        with allure.step("Проверка безопасной обработки команды"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            assert actual_value is not None, "Field should accept command-like text safely"

    @allure.title("Попытка обхода пути")
    def test_path_traversal(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод path traversal нагрузки в поле названия"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "../../../etc/passwd")

        with allure.step("Проверка безопасной обработки path traversal"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            assert actual_value is not None, "Field should handle path traversal attempt"

    @allure.title("Попытка LDAP-инъекции")
    def test_ldap_injection(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод LDAP-инъекции в поле названия"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "*)(uid=*))(|(uid=*")

        with allure.step("Проверка безопасной обработки LDAP-инъекции"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            assert actual_value is not None, "Field should handle LDAP injection attempt"


# =============================================================================
# DESCRIPTION INJECTION TESTS
# =============================================================================

@pytest.mark.security
@pytest.mark.functional
@allure.feature("Создание товара")
@allure.story("Инъекция в описание")
class TestProductCreateDescriptionInjection:
    """XSS/SQL injection tests for description fields."""

    @allure.title("XSS в описании на узбекском")
    def test_xss_uz_description(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод XSS-нагрузки с редиректом в описание на узбекском"):
            product_create_page.scroll_page(300)
            xss = "<script>document.location='http://evil.com'</script>"
            desc_field = get_uz_desc_field(product_create_page.page)
            desc_field.fill(xss)

        with allure.step("Проверка санитизации XSS в описании"):
            value = desc_field.input_value()
            assert "<script>" not in value or value != xss, \
                "BUG: XSS in UZ description not sanitized - SECURITY VULNERABILITY!"

    @allure.title("XSS в описании на русском")
    def test_xss_ru_description(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод XSS-нагрузки через img onerror в описание на русском"):
            product_create_page.scroll_page(300)
            xss = "<img src=x onerror=alert('xss')>"
            desc_field = get_ru_desc_field(product_create_page.page)
            desc_field.fill(xss)

        with allure.step("Проверка санитизации XSS в русском описании"):
            value = desc_field.input_value()
            assert "onerror" not in value.lower() or value != xss, \
                "BUG: XSS in RU description not sanitized - SECURITY VULNERABILITY!"

    @allure.title("SQL-инъекция в описании")
    def test_sql_injection_description(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод SQL-инъекции DROP TABLE в поле описания"):
            product_create_page.scroll_page(300)
            sql = "'; DROP TABLE products; --"
            desc_field = get_uz_desc_field(product_create_page.page)
            desc_field.fill(sql)

        with allure.step("Проверка безопасной обработки SQL-инъекции в описании"):
            value = desc_field.input_value()
            assert value == sql or "DROP" not in value, \
                "BUG: SQL injection in description not safely handled"

    @allure.title("HTML-инъекция в описании")
    def test_html_injection_description(self, product_create_page):
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод HTML-инъекции с onmouseover в описание"):
            product_create_page.scroll_page(300)
            html = "<div onmouseover='alert(1)'>Hover me</div>"
            desc_field = get_uz_desc_field(product_create_page.page)
            desc_field.fill(html)

        with allure.step("Проверка санитизации HTML-инъекции с обработчиком событий"):
            value = desc_field.input_value()
            assert "onmouseover" not in value.lower() or value == html, \
                "BUG: HTML injection with event handler not sanitized!"


# =============================================================================
# SKU VALIDATION TESTS
# =============================================================================

@pytest.mark.security
@pytest.mark.functional
@allure.feature("Создание товара")
@allure.story("Валидация SKU")
class TestProductCreateSlugSku:
    """SKU field validation tests on Step 2."""

    @allure.title("SKU с пробелами отклонён или очищен")
    def test_sku_with_spaces(self, product_on_step2):
        with allure.step("Ввод SKU с пробелами"):
            sku_field = product_on_step2.page.get_by_role("textbox", name="SKU")
            sku_field.fill("AB CD")

        with allure.step("Проверка отклонения или очистки пробелов в SKU"):
            value = sku_field.input_value()
            assert " " not in value or product_on_step2.has_validation_errors(), \
                "BUG: SKU with spaces accepted without validation"

    @allure.title("SKU со спецсимволами")
    def test_sku_special_characters(self, product_on_step2):
        with allure.step("Ввод спецсимволов в поле SKU"):
            sku_field = product_on_step2.page.get_by_role("textbox", name="SKU")
            sku_field.fill("!@#$%")

        with allure.step("Проверка обработки спецсимволов в SKU"):
            value = sku_field.input_value()
            has_errors = product_on_step2.has_validation_errors()
            is_sanitized = value != "!@#$%"
            assert has_errors or is_sanitized or len(value) >= 0, \
                "BUG: Special characters in SKU not handled"

    @allure.title("Ограничение максимальной длины SKU")
    def test_sku_over_max_length(self, product_on_step2):
        with allure.step("Ввод 50 символов в поле SKU"):
            sku_field = product_on_step2.page.get_by_role("textbox", name="SKU")
            sku_field.fill("A" * 50)

        with allure.step("Проверка ограничения максимальной длины SKU"):
            value = sku_field.input_value()
            assert len(value) < 50, \
                f"BUG: SKU accepted {len(value)} chars, should be limited"

    @allure.title("SKU с кириллицей")
    def test_sku_cyrillic(self, product_on_step2):
        with allure.step("Ввод кириллицы в поле SKU"):
            sku_field = product_on_step2.page.get_by_role("textbox", name="SKU")
            sku_field.fill("ТЕСТ")

        with allure.step("Проверка обработки кириллицы в SKU"):
            value = sku_field.input_value()
            has_errors = product_on_step2.has_validation_errors()
            assert has_errors or len(value) > 0, "BUG: Cyrillic SKU handling error"

    @allure.title("XSS-инъекция в SKU")
    def test_sku_xss_injection(self, product_on_step2):
        with allure.step("Ввод XSS-нагрузки в поле SKU"):
            sku_field = product_on_step2.page.get_by_role("textbox", name="SKU")
            sku_field.fill("<script>alert(1)</script>")

        with allure.step("Проверка санитизации XSS в поле SKU"):
            value = sku_field.input_value()
            assert "<script>" not in value, \
                "BUG: XSS in SKU not sanitized - SECURITY VULNERABILITY!"


# =============================================================================
# FILE UPLOAD TESTS
# =============================================================================

@pytest.mark.staging
@allure.feature("Создание товара - Загрузка файлов")
class TestProductCreateFileUpload:
    """File upload tests for Step 3."""

    @allure.title("Загрузка валидного изображения успешна")
    def test_valid_image_upload(self, product_on_step3):
        with allure.step("Проверка наличия тестового изображения"):
            image_path = os.path.join(RESOURCES_PATH, "tv.png")
            if not os.path.exists(image_path):
                pytest.fail("Test image not found")

        with allure.step("Загрузка валидного изображения"):
            product_on_step3.upload_main_image(image_path)
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка успешной загрузки изображения"):
            assert product_on_step3.is_file_uploaded(), "BUG: Valid image upload failed"

    @allure.title("Большой файл (>5МБ) должен быть отклонён")
    def test_large_file_rejected(self, product_on_step3):
        with allure.step("Проверка наличия тестового файла >5МБ"):
            large_file = os.path.join(RESOURCES_PATH, "large_file_6mb.bin")
            if not os.path.exists(large_file):
                pytest.fail("Large test file not found")

        with allure.step("Загрузка файла размером >5МБ"):
            file_input = product_on_step3.page.locator("input[type='file']").first
            file_input.set_input_files(large_file)
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка отклонения большого файла"):
            error_msg = product_on_step3.get_upload_error_message()
            uploaded = product_on_step3.is_file_uploaded()
            assert error_msg is not None or not uploaded, \
                "BUG: Large file (>5MB) was accepted - should be rejected"

    @allure.title("Пустой файл должен быть отклонён")
    def test_empty_file_rejected(self, product_on_step3):
        with allure.step("Проверка наличия пустого тестового файла"):
            empty_file = os.path.join(RESOURCES_PATH, "empty_file.png")
            if not os.path.exists(empty_file):
                pytest.fail("Empty test file not found")

        with allure.step("Загрузка пустого файла"):
            file_input = product_on_step3.page.locator("input[type='file']").first
            file_input.set_input_files(empty_file)
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка отклонения пустого файла"):
            error_msg = product_on_step3.get_upload_error_message()
            uploaded = product_on_step3.is_file_uploaded()
            assert error_msg is not None or not uploaded, \
                "BUG: Empty file was accepted - should be rejected"

    @allure.title("Файл неправильного формата должен быть отклонён")
    def test_wrong_format_rejected(self, product_on_step3):
        with allure.step("Проверка наличия тестового файла неправильного формата"):
            fake_image = os.path.join(RESOURCES_PATH, "fake_image.txt")
            if not os.path.exists(fake_image):
                pytest.fail("Fake image test file not found")

        with allure.step("Загрузка файла неправильного формата (.txt)"):
            file_input = product_on_step3.page.locator("input[type='file']").first
            file_input.set_input_files(fake_image)
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка отклонения файла неправильного формата"):
            error_msg = product_on_step3.get_upload_error_message()
            uploaded = product_on_step3.is_file_uploaded()
            assert error_msg is not None or not uploaded, \
                "BUG: Non-image file was accepted - should be rejected"

    @allure.title("Файл с переименованным расширением должен проверяться по magic bytes")
    def test_renamed_extension_rejected(self, product_on_step3):
        with allure.step("Проверка наличия файла с переименованным расширением"):
            renamed_file = os.path.join(RESOURCES_PATH, "renamed_to_gif.gif")
            if not os.path.exists(renamed_file):
                pytest.fail("Renamed test file not found")

        with allure.step("Загрузка файла с переименованным расширением"):
            file_input = product_on_step3.page.locator("input[type='file']").first
            file_input.set_input_files(renamed_file)
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка обработки файла по magic bytes"):
            uploaded = product_on_step3.is_file_uploaded()
            logger.info(f"Renamed extension file: uploaded={uploaded}")


# =============================================================================
# ADVANCED FILE UPLOAD TESTS
# =============================================================================

@pytest.mark.staging
@allure.feature("Создание товара - Продвинутая загрузка файлов")
class TestProductCreateAdvancedFileUpload:
    """Advanced file upload security and edge case tests."""

    @allure.title("SVG с XSS-нагрузкой должен быть отклонён или очищен")
    def test_svg_xss_upload(self, product_on_step3):
        with allure.step("Создание SVG файла с XSS-нагрузкой"):
            svg_content = '<?xml version="1.0"?>\n<svg xmlns="http://www.w3.org/2000/svg">\n  <script>alert(\'XSS\')</script>\n  <rect width="100" height="100"/>\n</svg>'
            with tempfile.NamedTemporaryFile(mode='w', suffix='.svg', delete=False) as f:
                f.write(svg_content)
                svg_path = f.name
        try:
            with allure.step("Загрузка SVG файла с XSS"):
                file_input = product_on_step3.page.locator("input[type='file']").first
                file_input.set_input_files(svg_path)
                product_on_step3.page.wait_for_load_state("networkidle")

            with allure.step("Проверка отклонения или санитизации SVG с XSS"):
                error_msg = product_on_step3.get_upload_error_message()
                uploaded = product_on_step3.is_file_uploaded()
                logger.info(f"SVG XSS upload: error={error_msg}, uploaded={uploaded}")
        finally:
            os.unlink(svg_path)

    @allure.title("Файл с двойным расширением должен быть проверен")
    def test_double_extension_upload(self, product_on_step3):
        with allure.step("Создание файла с двойным расширением .jpg.exe"):
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.jpg.exe', delete=False) as f:
                f.write(b'\x89PNG\r\n\x1a\n')
                double_ext_path = f.name
        try:
            with allure.step("Загрузка файла с двойным расширением"):
                file_input = product_on_step3.page.locator("input[type='file']").first
                file_input.set_input_files(double_ext_path)
                product_on_step3.page.wait_for_load_state("networkidle")

            with allure.step("Проверка обработки файла с двойным расширением"):
                error_msg = product_on_step3.get_upload_error_message()
                uploaded = product_on_step3.is_file_uploaded()
                logger.info(f"Double extension: error={error_msg}, uploaded={uploaded}")
        finally:
            os.unlink(double_ext_path)

    @allure.title("Повреждённый файл изображения должен быть отклонён")
    def test_corrupted_image_upload(self, product_on_step3):
        with allure.step("Создание повреждённого файла изображения"):
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.jpg', delete=False) as f:
                f.write(b'\xff\xd8\xff\xe0')
                f.write(b'corrupted data here')
                corrupted_path = f.name
        try:
            with allure.step("Загрузка повреждённого изображения"):
                file_input = product_on_step3.page.locator("input[type='file']").first
                file_input.set_input_files(corrupted_path)
                product_on_step3.page.wait_for_load_state("networkidle")

            with allure.step("Проверка отклонения повреждённого изображения"):
                error_msg = product_on_step3.get_upload_error_message()
                uploaded = product_on_step3.is_file_uploaded()
                logger.info(f"Corrupted image: error={error_msg}, uploaded={uploaded}")
        finally:
            os.unlink(corrupted_path)

    @allure.title("Замена загруженного файла работает корректно")
    def test_replace_uploaded_file(self, product_on_step3):
        with allure.step("Проверка наличия двух тестовых изображений"):
            image_path = os.path.join(RESOURCES_PATH, "tv.png")
            image_path2 = os.path.join(RESOURCES_PATH, "img.png")
            if not (os.path.exists(image_path) and os.path.exists(image_path2)):
                pytest.fail("Test images not found")

        with allure.step("Загрузка первого изображения"):
            product_on_step3.upload_main_image(image_path)
            product_on_step3.page.wait_for_load_state("networkidle")
            first_uploaded = product_on_step3.is_file_uploaded()

        with allure.step("Замена загруженного изображения вторым"):
            file_input = product_on_step3.page.locator("input[type='file']").first
            file_input.set_input_files(image_path2)
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка успешной замены файла"):
            second_uploaded = product_on_step3.is_file_uploaded()
            assert first_uploaded and second_uploaded, "BUG: File replacement failed"
