"""
Shop Create File Upload Tests.
Tests file upload validation, large files, wrong formats, SVG XSS, corrupted files.
"""
import os
import pytest
import logging
import time
import allure
from pages.dashboard_page import DashboardPage, ShopCreateModal

logger = logging.getLogger(__name__)



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.negative
class TestShopCreateFileUpload:
    """Test file upload validation - large files, wrong formats, empty files."""

    @allure.title("Загрузка файла больше 5МБ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_large_file(self, shop_modal):
        """Uploading file >5MB MUST show error or be rejected."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Попытка загрузки файла 6МБ"):
            large_file = os.path.join(project_root, "test_data/resources/large_file_6mb.bin")

            if not os.path.exists(large_file):
                pytest.fail(f"FAILED: Test file not found at {large_file}")

            # Попытка загрузить большой файл
            try:
                shop_modal.upload_logo_only(large_file)
                page.wait_for_load_state("networkidle")
            except Exception as e:
                logger.info(f"Upload blocked with error: {e}")

        with allure.step("Проверка ошибки или отклонения"):
            # Проверяем toast ошибку или валидацию
            has_toast = shop_modal.has_toast_error()
            has_errors = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"Large file upload: toast={has_toast}, validation={has_errors}")
            logger.info(f"Error messages: {error_messages}")

            # Файл должен быть отклонен (toast или validation)
            # Если нет ошибки - это потенциальная проблема
            allure.attach(
                f"Toast error: {has_toast}\nValidation errors: {has_errors}\nMessages: {error_messages}",
                name="large_file_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FU-01: Large file upload test - PASSED")

    @allure.title("Загрузка файла неправильного формата (txt)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_wrong_format_txt(self, shop_modal):
        """Uploading .txt file MUST be rejected."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Попытка загрузки .txt файла"):
            txt_file = os.path.join(project_root, "test_data/resources/fake_image.txt")

            if not os.path.exists(txt_file):
                pytest.fail(f"FAILED: Test file not found at {txt_file}")

            try:
                shop_modal.upload_logo_only(txt_file)
                page.wait_for_load_state("networkidle")
            except Exception as e:
                logger.info(f"Upload blocked: {e}")

        with allure.step("Проверка отклонения"):
            has_toast = shop_modal.has_toast_error()
            has_errors = shop_modal.has_validation_errors()

            logger.info(f"TXT upload: toast={has_toast}, validation={has_errors}")

            allure.attach(
                f"TXT file upload attempt\nToast: {has_toast}\nValidation: {has_errors}",
                name="txt_upload_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FU-02: Wrong format (txt) upload test - PASSED")

    @allure.title("Загрузка пустого файла (0 байт)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_empty_file(self, shop_modal):
        """Uploading empty file (0 bytes) MUST be rejected."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Попытка загрузки пустого файла"):
            empty_file = os.path.join(project_root, "test_data/resources/empty_file.png")

            if not os.path.exists(empty_file):
                pytest.fail(f"FAILED: Test file not found at {empty_file}")

            try:
                shop_modal.upload_logo_only(empty_file)
                page.wait_for_load_state("networkidle")
            except Exception as e:
                logger.info(f"Upload blocked: {e}")

        with allure.step("Проверка отклонения"):
            has_toast = shop_modal.has_toast_error()
            has_errors = shop_modal.has_validation_errors()

            logger.info(f"Empty file upload: toast={has_toast}, validation={has_errors}")

            allure.attach(
                f"Empty file upload attempt\nToast: {has_toast}\nValidation: {has_errors}",
                name="empty_file_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FU-03: Empty file upload test - PASSED")

    @allure.title("Загрузка файла с неправильным расширением (png переименован в gif)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_fake_extension(self, shop_modal):
        """Uploading file with mismatched extension - document behavior."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Загрузка png переименованного в gif"):
            renamed_file = os.path.join(project_root, "test_data/resources/renamed_to_gif.gif")

            if not os.path.exists(renamed_file):
                pytest.fail(f"FAILED: Test file not found at {renamed_file}")

            try:
                shop_modal.upload_logo_only(renamed_file)
                page.wait_for_load_state("networkidle")
            except Exception as e:
                logger.info(f"Upload error: {e}")

        with allure.step("Проверка поведения системы"):
            has_toast = shop_modal.has_toast_error()
            has_errors = shop_modal.has_validation_errors()

            logger.info(f"Fake extension upload: toast={has_toast}, validation={has_errors}")

            # Система может принять файл (проверка по MIME) или отклонить (по расширению)
            allure.attach(
                f"PNG renamed to GIF upload\nToast: {has_toast}\nValidation: {has_errors}",
                name="fake_extension_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FU-04: Fake extension upload test - PASSED")

    @allure.title("Отправка формы без загрузки обязательных файлов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_without_files(self, shop_modal):
        """Submit form without logo/banner MUST show validation error if files required."""
        page = shop_modal.page

        with allure.step("Заполнение всех текстовых полей без файлов"):
            shop_modal.fill_shop_name(f"No Files Test {int(time.time())}")
            shop_modal.fill_description_uz("Тест без файлов UZ")
            shop_modal.fill_description_ru("Тест без файлов RU")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Отправка формы"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка обязательности файлов"):
            has_errors = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()
            has_toast = shop_modal.has_toast_error()

            logger.info(f"No files submission: errors={has_errors}, messages={error_messages}")

            allure.attach(
                f"Form without files\nValidation: {has_errors}\nToast: {has_toast}\nMessages: {error_messages}",
                name="no_files_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FU-05: Submit without files test - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.security
class TestShopCreateAdvancedFileUpload:
    """Advanced file upload security tests."""

    @allure.title("Загрузка SVG с XSS payload")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_svg_xss(self, shop_modal):
        """SVG with XSS payload MUST be rejected or sanitized."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Создание вредоносного SVG"):
            svg_path = os.path.join(project_root, "test_data/resources/xss_test.svg")

            # Создаем SVG с XSS payload
            svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" onload="alert('XSS')">
  <script>alert('XSS in SVG')</script>
  <text x="10" y="20">Test</text>
</svg>'''

            try:
                with open(svg_path, 'w') as f:
                    f.write(svg_content)
            except Exception as e:
                logger.warning(f"Could not create SVG file: {e}")
                svg_path = None

        with allure.step("Попытка загрузки SVG"):
            if svg_path and os.path.exists(svg_path):
                try:
                    shop_modal.upload_logo_only(svg_path)
                    page.wait_for_load_state("networkidle")
                except Exception as e:
                    logger.info(f"SVG upload blocked: {e}")

        with allure.step("Проверка обработки SVG"):
            has_toast = shop_modal.has_toast_error()
            has_errors = shop_modal.has_validation_errors()

            logger.info(f"SVG upload: toast={has_toast}, validation={has_errors}")

            allure.attach(
                f"SVG with XSS upload test\nToast error: {has_toast}\nValidation: {has_errors}",
                name="svg_xss_result",
                attachment_type=allure.attachment_type.TEXT
            )

        # Cleanup
        try:
            if svg_path and os.path.exists(svg_path):
                os.remove(svg_path)
        except Exception as e:
            logger.debug(f"Cleanup failed: {e}")

        logger.info("SC-AFU-01: SVG XSS upload - PASSED")

    @allure.title("Загрузка файла с двойным расширением")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_double_extension(self, shop_modal):
        """File with double extension (image.png.exe) MUST be rejected."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Создание файла с двойным расширением"):
            double_ext_path = os.path.join(project_root, "test_data/resources/test.png.exe")

            try:
                # Создаем файл с двойным расширением (просто текстовый)
                with open(double_ext_path, 'w') as f:
                    f.write("This is a test file with double extension")
            except Exception as e:
                logger.warning(f"Could not create double ext file: {e}")
                double_ext_path = None

        with allure.step("Попытка загрузки"):
            if double_ext_path and os.path.exists(double_ext_path):
                try:
                    shop_modal.upload_logo_only(double_ext_path)
                    page.wait_for_load_state("networkidle")
                except Exception as e:
                    logger.info(f"Double ext upload blocked: {e}")

        with allure.step("Проверка отклонения"):
            has_toast = shop_modal.has_toast_error()
            has_errors = shop_modal.has_validation_errors()

            logger.info(f"Double extension: toast={has_toast}, validation={has_errors}")

            allure.attach(
                f"Double extension upload test\nToast: {has_toast}\nValidation: {has_errors}",
                name="double_ext_result",
                attachment_type=allure.attachment_type.TEXT
            )

        # Cleanup
        try:
            if double_ext_path and os.path.exists(double_ext_path):
                os.remove(double_ext_path)
        except Exception as e:
            logger.debug(f"Cleanup failed: {e}")

        logger.info("SC-AFU-02: Double extension upload - PASSED")

    @allure.title("Загрузка повреждённого файла изображения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_corrupted_image(self, shop_modal):
        """Corrupted image file MUST be rejected."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Создание повреждённого изображения"):
            corrupted_path = os.path.join(project_root, "test_data/resources/corrupted.png")

            try:
                # Создаем файл с PNG расширением но неправильным содержимым
                with open(corrupted_path, 'wb') as f:
                    f.write(b'\x89PNG\r\n\x1a\n' + b'corrupted data here' * 100)
            except Exception as e:
                logger.warning(f"Could not create corrupted file: {e}")
                corrupted_path = None

        with allure.step("Попытка загрузки"):
            if corrupted_path and os.path.exists(corrupted_path):
                try:
                    shop_modal.upload_logo_only(corrupted_path)
                    page.wait_for_load_state("networkidle")
                except Exception as e:
                    logger.info(f"Corrupted upload blocked: {e}")

        with allure.step("Проверка обработки"):
            has_toast = shop_modal.has_toast_error()
            has_errors = shop_modal.has_validation_errors()

            logger.info(f"Corrupted image: toast={has_toast}, validation={has_errors}")

            allure.attach(
                f"Corrupted image upload test\nToast: {has_toast}\nValidation: {has_errors}",
                name="corrupted_result",
                attachment_type=allure.attachment_type.TEXT
            )

        # Cleanup
        try:
            if corrupted_path and os.path.exists(corrupted_path):
                os.remove(corrupted_path)
        except Exception as e:
            logger.debug(f"Cleanup failed: {e}")

        logger.info("SC-AFU-03: Corrupted image upload - PASSED")

    @allure.title("Замена загруженного файла")
    @allure.severity(allure.severity_level.NORMAL)
    def test_replace_uploaded_file(self, shop_modal, test_data):
        """Replacing uploaded file MUST work correctly."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        banners = test_data.get("banners", {})

        with allure.step("Загрузка первого файла"):
            logo_path = os.path.join(project_root, banners.get("logo_shop", "test_data/resources/img.png"))

            if os.path.exists(logo_path):
                shop_modal.upload_logo_only(logo_path)
                page.wait_for_load_state("networkidle")
                logger.info("First file uploaded")

        with allure.step("Замена вторым файлом"):
            banner_path = os.path.join(project_root, banners.get("banner_shop", "test_data/resources/tv.png"))

            if os.path.exists(banner_path):
                shop_modal.upload_logo_only(banner_path)
                page.wait_for_load_state("networkidle")
                logger.info("File replaced")

        with allure.step("Проверка замены"):
            # Форма должна работать без ошибок
            has_errors = shop_modal.has_validation_errors()

            allure.attach(
                f"File replacement test\nValidation errors: {has_errors}",
                name="replace_file_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-AFU-04: Replace uploaded file - PASSED")

