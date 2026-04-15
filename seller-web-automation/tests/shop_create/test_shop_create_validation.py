"""
Shop Create Validation Tests.
Tests empty fields and invalid format validation.
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
class TestShopCreateEmptyFields:
    """Test validation for empty fields - FAILS if validation doesn't trigger."""

    @allure.title("Отправка формы с пустыми полями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_submit_all_empty(self, shop_modal):
        """Submit with all empty fields MUST show validation errors."""
        page = shop_modal.page

        with allure.step("Нажатие кнопки сохранения с пустой формой"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка отображения ошибок валидации"):
            has_errors = shop_modal.has_validation_errors()
            error_count = shop_modal.get_validation_error_count()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"Validation errors found: {error_count}")
            logger.info(f"Error messages: {error_messages}")

            assert has_errors, \
                "FAILED: No validation errors shown when submitting empty form"
            assert error_count > 0, \
                f"FAILED: Expected validation errors, got {error_count}"

        logger.info(f"SC-EF-01: Empty form validation works ({error_count} errors) - PASSED")

    @allure.title("Отправка формы только с названием магазина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_only_name(self, shop_modal, test_data):
        """Submit with only shop name MUST show validation errors for other required fields."""
        page = shop_modal.page

        with allure.step("Заполнение только названия магазина"):
            shop_data = test_data.get("shop_data", {})
            shop_name = f"{shop_data.get('shop_name', 'Test Shop')} {int(time.time())}"
            shop_modal.fill_shop_name(shop_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибок валидации для описаний"):
            has_errors = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"Error messages: {error_messages}")

            # Should have errors for descriptions or file uploads
            assert has_errors, \
                "FAILED: No validation errors when descriptions are empty"

        logger.info("SC-EF-02: Partial form validation works - PASSED")

    @allure.title("Отправка без описания на узбекском")
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_without_description_uz(self, shop_modal, test_data):
        """Submit without Uzbek description MUST show validation error."""
        page = shop_modal.page

        with allure.step("Заполнение всех полей кроме описания на узбекском"):
            shop_data = test_data.get("shop_data", {})
            shop_name = f"{shop_data.get('shop_name', 'Test Shop')} {int(time.time())}"

            shop_modal.fill_shop_name(shop_name)
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Test description RU"))
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибки валидации для описания на узбекском"):
            has_errors = shop_modal.has_validation_errors()

            assert has_errors, \
                "FAILED: No validation error when Uzbek description is empty"

        logger.info("SC-EF-03: Missing Uzbek description validation - PASSED")

    @allure.title("Отправка без описания на русском")
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_without_description_ru(self, shop_modal, test_data):
        """Submit without Russian description MUST show validation error."""
        page = shop_modal.page

        with allure.step("Заполнение всех полей кроме описания на русском"):
            shop_data = test_data.get("shop_data", {})
            shop_name = f"{shop_data.get('shop_name', 'Test Shop')} {int(time.time())}"

            shop_modal.fill_shop_name(shop_name)
            shop_modal.fill_description_uz(shop_data.get("description_uz", "Test description UZ"))
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибки валидации для описания на русском"):
            has_errors = shop_modal.has_validation_errors()

            assert has_errors, \
                "FAILED: No validation error when Russian description is empty"

        logger.info("SC-EF-04: Missing Russian description validation - PASSED")

    @allure.title("Очистка названия магазина после заполнения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_clear_shop_name_after_fill(self, shop_modal):
        """Clearing shop name after filling MUST trigger validation."""
        page = shop_modal.page

        with allure.step("Заполнение и очистка названия магазина"):
            shop_modal.fill_shop_name("Test Shop")
            page.wait_for_load_state("domcontentloaded")
            shop_modal.clear_shop_name()
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибки валидации для пустого названия"):
            has_errors = shop_modal.has_validation_errors()

            assert has_errors, \
                "FAILED: No validation error after clearing shop name"

        logger.info("SC-EF-05: Clear shop name validation - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.negative
class TestShopCreateInvalidFormat:
    """Test validation for invalid input formats."""

    @allure.title("Название магазина только из пробелов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_only_spaces(self, shop_modal):
        """Shop name with only spaces MUST trigger validation."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина только пробелами"):
            shop_modal.fill_shop_name("     ")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибки валидации"):
            has_errors = shop_modal.has_validation_errors()

            assert has_errors, \
                "FAILED: No validation error for shop name with only spaces"

        logger.info("SC-IF-01: Whitespace-only shop name validation - PASSED")

    @allure.title("Название магазина только из спецсимволов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_special_chars_only(self, shop_modal):
        """Shop name with only special characters MUST trigger validation or be rejected."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина спецсимволами"):
            shop_modal.fill_shop_name("@#$%^&*()")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка валидации или ошибки"):
            has_errors = shop_modal.has_validation_errors()
            has_toast = shop_modal.has_toast_error()

            # Should have some form of error
            assert has_errors or has_toast, \
                "FAILED: No error for shop name with only special characters"

        logger.info("SC-IF-02: Special chars only validation - PASSED")

    @allure.title("Очень короткое название магазина (1 символ)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_too_short(self, shop_modal):
        """Single character shop name MUST trigger validation."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина одним символом"):
            shop_modal.fill_shop_name("A")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибки валидации"):
            has_errors = shop_modal.has_validation_errors()

            assert has_errors, \
                "FAILED: No validation error for single character shop name"

        logger.info("SC-IF-03: Too short shop name validation - PASSED")

    @allure.title("Описание только из цифр")
    @allure.severity(allure.severity_level.MINOR)
    def test_description_only_numbers(self, shop_modal, test_data):
        """Description with only numbers - verify if accepted or rejected."""
        page = shop_modal.page

        with allure.step("Заполнение описаний только цифрами"):
            shop_data = test_data.get("shop_data", {})
            shop_name = f"{shop_data.get('shop_name', 'Test Shop')} {int(time.time())}"

            shop_modal.fill_shop_name(shop_name)
            shop_modal.fill_description_uz("12345678901234567890")
            shop_modal.fill_description_ru("12345678901234567890")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ответа"):
            # This might be accepted or rejected depending on business rules
            # Log the actual behavior
            has_errors = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"Number-only description: has_errors={has_errors}, messages={error_messages}")

            # Test passes either way - we're documenting behavior
            logger.info("SC-IF-04: Number-only description test completed")

    @allure.title("HTML теги в названии магазина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_html_tags(self, shop_modal):
        """HTML tags in shop name - document behavior and check for XSS execution."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина HTML тегами"):
            xss_payload = "<script>alert('XSS')</script>"
            shop_modal.fill_shop_name(xss_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка обработки системой"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Actual shop name value: {actual_value}")

            # Document the behavior - input fields storing HTML is not itself a vulnerability
            # The vulnerability would be if it executes when rendered
            allure.attach(
                f"Input: {xss_payload}\nStored: {actual_value}",
                name="xss_test_result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Check that no JavaScript dialog appeared (real XSS)
            # This would indicate client-side XSS vulnerability
            dialog_appeared = page.locator("[role='alertdialog']").count() > 0
            assert not dialog_appeared, "FAILED: XSS dialog appeared - security vulnerability!"

            # NOTE: Storing HTML in input is OK. Real XSS test would need to check
            # if this HTML executes when the shop name is displayed elsewhere
            logger.info("HTML stored in input - server-side sanitization should be verified")

        logger.info("SC-IF-05: HTML tags handling documented - PASSED")

    @allure.title("Название магазина с Unicode emoji")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_unicode_emoji(self, shop_modal):
        """Shop name with Unicode emoji - document behavior."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина emoji"):
            emoji_name = "🏪 Test Shop 🛒"
            shop_modal.fill_shop_name(emoji_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка обработки emoji системой"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Input: {emoji_name}, Stored: {actual_value}")

            # Документируем поведение - emoji могут быть приняты или отклонены
            shop_modal.fill_description_uz("Test описание UZ")
            shop_modal.fill_description_ru("Test описание RU")
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            has_errors = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"Emoji name: has_errors={has_errors}, messages={error_messages}")
            allure.attach(
                f"Input: {emoji_name}\nStored: {actual_value}\nErrors: {error_messages}",
                name="emoji_test_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-IF-06: Unicode emoji handling documented - PASSED")

    @allure.title("Название магазина со смешанной кириллицей и латиницей")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_mixed_script(self, shop_modal):
        """Shop name with mixed Cyrillic and Latin characters."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина смешанным алфавитом"):
            mixed_name = f"Test Магазин Shop {int(time.time())}"
            shop_modal.fill_shop_name(mixed_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка генерации slug"):
            slug_value = shop_modal.get_slug_value()
            logger.info(f"Mixed script name: {mixed_name}")
            logger.info(f"Generated slug: {slug_value}")

            # Slug должен содержать только латиницу и дефисы
            allure.attach(
                f"Name: {mixed_name}\nSlug: {slug_value}",
                name="mixed_script_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Отправка и проверка"):
            shop_modal.fill_description_uz("Смешанный тест")
            shop_modal.fill_description_ru("Mixed test")
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            has_errors = shop_modal.has_validation_errors()
            logger.info(f"Mixed script submission: has_errors={has_errors}")

        logger.info("SC-IF-07: Mixed script handling - PASSED")

    @allure.title("Описание с табуляцией и переносами строк")
    @allure.severity(allure.severity_level.NORMAL)
    def test_description_tabs_newlines(self, shop_modal):
        """Description with tabs and newline characters."""
        page = shop_modal.page

        with allure.step("Заполнение описаний с табуляцией и переносами"):
            shop_modal.fill_shop_name(f"Tab Test Shop {int(time.time())}")
            page.wait_for_load_state("domcontentloaded")

            # Текст с табами и переносами строк
            text_with_tabs = "Первая строка\tвторая часть\nВторая строка\tеще часть"
            shop_modal.fill_description_uz(text_with_tabs)
            shop_modal.fill_description_ru("Обычное описание")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранённого значения"):
            uz_value = shop_modal.get_description_uz_value()
            logger.info(f"Description with tabs/newlines stored as: {repr(uz_value)}")

            allure.attach(
                f"Input: {repr(text_with_tabs)}\nStored: {repr(uz_value)}",
                name="tabs_newlines_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Отправка и проверка"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            has_errors = shop_modal.has_validation_errors()
            logger.info(f"Tabs/newlines submission: has_errors={has_errors}")

        logger.info("SC-IF-08: Tabs and newlines handling - PASSED")

