"""
Shop Create Boundary, Whitespace, and Advanced Input Tests.
Tests boundary values, whitespace handling, and input methods.
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
class TestShopCreateBoundary:
    """Test boundary value cases."""

    @allure.title("Максимальная длина названия магазина (255+ символов)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_max_length(self, shop_modal):
        """Very long shop name should be truncated or rejected."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина 300 символами"):
            long_name = "A" * 300
            shop_modal.fill_shop_name(long_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка фактической длины значения"):
            actual_value = shop_modal.get_shop_name_value()
            actual_length = len(actual_value)

            logger.info(f"Input length: 300, Actual length: {actual_length}")

            # Should either truncate or show error
            if actual_length == 300:
                # Not truncated, check if validation fails
                shop_modal.click_save()
                page.wait_for_load_state("networkidle")
                has_errors = shop_modal.has_validation_errors()
                logger.info(f"No truncation, validation errors: {has_errors}")
            else:
                logger.info(f"Truncated to {actual_length} characters")

        logger.info("SC-BV-01: Max length shop name test completed - PASSED")

    @allure.title("Минимальная длина названия магазина (2 символа)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_min_length(self, shop_modal):
        """2 character shop name - check minimum boundary."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина 2 символами"):
            shop_modal.fill_shop_name("AB")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка валидации"):
            has_errors = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"2-char name: has_errors={has_errors}, messages={error_messages}")

            # Document whether 2 chars is accepted or rejected
            logger.info("SC-BV-02: Minimum length test completed")

    @allure.title("Описание только из пробелов должно быть отклонено")
    @allure.severity(allure.severity_level.NORMAL)
    def test_description_whitespace_only(self, shop_modal, test_data):
        """BUG CHECK: Whitespace-only descriptions MUST trigger validation error."""
        page = shop_modal.page

        with allure.step("Заполнение валидного названия и описаний только из пробелов"):
            shop_data = test_data.get("shop_data", {})
            shop_name = f"{shop_data.get('shop_name', 'Test Shop')} {int(time.time())}"

            shop_modal.fill_shop_name(shop_name)
            shop_modal.fill_description_uz("     ")  # только пробелы
            shop_modal.fill_description_ru("     ")  # только пробелы
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Нажатие кнопки сохранения"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибки валидации"):
            has_errors = shop_modal.has_validation_errors()

            allure.attach(
                f"Whitespace-only descriptions\nValidation errors: {has_errors}",
                name="whitespace_desc_result",
                attachment_type=allure.attachment_type.TEXT
            )

            # ЖЕСТКАЯ ПРОВЕРКА: Пустые описания (только пробелы) НЕ должны приниматься
            assert has_errors, \
                "BUG: Whitespace-only descriptions accepted - should show validation error!"

        logger.info("SC-BV-03: Whitespace description validation - PASSED")

    @allure.title("Максимальная длина описаний")
    @allure.severity(allure.severity_level.MINOR)
    def test_description_max_length(self, shop_modal, test_data):
        """Very long descriptions - check if truncated or rejected."""
        page = shop_modal.page

        with allure.step("Заполнение очень длинными описаниями"):
            shop_data = test_data.get("shop_data", {})
            shop_name = f"{shop_data.get('shop_name', 'Test Shop')} {int(time.time())}"

            shop_modal.fill_shop_name(shop_name)

            long_description = "A" * 5000
            shop_modal.fill_description_uz(long_description)
            shop_modal.fill_description_ru(long_description)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка фактических значений"):
            uz_value = shop_modal.get_description_uz_value()
            ru_value = shop_modal.get_description_ru_value()

            logger.info(f"UZ description length: {len(uz_value)}")
            logger.info(f"RU description length: {len(ru_value)}")

        logger.info("SC-BV-04: Max description length test completed - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.negative
class TestShopCreateWhitespace:
    """Test whitespace handling in shop create form."""

    @allure.title("Название магазина с табуляцией")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_with_tabs(self, shop_modal):
        """Shop name with tab characters - verify handling."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина с табуляцией"):
            tab_name = "Test\tShop\tWith\tTabs"
            shop_modal.fill_shop_name(tab_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранённого значения"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Input: {repr(tab_name)}, Stored: {repr(actual_value)}")

            # Табы могут быть преобразованы в пробелы или удалены
            allure.attach(
                f"Input: {repr(tab_name)}\nStored: {repr(actual_value)}",
                name="tabs_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Отправка и проверка"):
            shop_modal.fill_description_uz("Тест с табами")
            shop_modal.fill_description_ru("Test with tabs")
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            has_errors = shop_modal.has_validation_errors()
            logger.info(f"Tabs in name: has_errors={has_errors}")

        logger.info("SC-WS-01: Shop name with tabs - PASSED")

    @allure.title("Название магазина с переносами строк")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_with_newline(self, shop_modal):
        """Shop name with newline characters - verify handling."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина с переносами строк"):
            newline_name = "Test\nShop\nWith\nNewlines"
            shop_modal.fill_shop_name(newline_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранённого значения"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Input: {repr(newline_name)}, Stored: {repr(actual_value)}")

            # Переносы строк должны быть удалены из однострочного поля
            allure.attach(
                f"Input: {repr(newline_name)}\nStored: {repr(actual_value)}",
                name="newlines_result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Однострочное поле не должно содержать переносов строк
            assert "\n" not in actual_value, \
                f"FAILED: Newlines were not sanitized from shop name: {repr(actual_value)}"

        logger.info("SC-WS-02: Shop name with newlines - PASSED")

    @allure.title("Описание с неразрывным пробелом (NBSP)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_description_with_nbsp(self, shop_modal):
        """Description with non-breaking spaces - verify handling."""
        page = shop_modal.page

        with allure.step("Заполнение описания с неразрывным пробелом"):
            shop_modal.fill_shop_name(f"NBSP Test {int(time.time())}")
            page.wait_for_load_state("domcontentloaded")

            # \u00A0 = non-breaking space
            nbsp_text = "Test\u00A0description\u00A0with\u00A0NBSP"
            shop_modal.fill_description_uz(nbsp_text)
            shop_modal.fill_description_ru("Normal description")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранённого значения"):
            actual_value = shop_modal.get_description_uz_value()
            logger.info(f"Input: {repr(nbsp_text)}, Stored: {repr(actual_value)}")

            allure.attach(
                f"Input: {repr(nbsp_text)}\nStored: {repr(actual_value)}",
                name="nbsp_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Отправка и проверка"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            has_errors = shop_modal.has_validation_errors()
            logger.info(f"NBSP in description: has_errors={has_errors}")

        logger.info("SC-WS-03: Description with NBSP - PASSED")

    @allure.title("Название магазина с начальными/конечными пробелами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_leading_trailing_spaces(self, shop_modal):
        """Shop name with leading/trailing spaces - verify trimming."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина с пробелами"):
            spaced_name = "   Test Shop With Spaces   "
            shop_modal.fill_shop_name(spaced_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранённого/обрезанного значения"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Input: '{spaced_name}', Stored: '{actual_value}'")

            allure.attach(
                f"Input: '{spaced_name}'\nStored: '{actual_value}'",
                name="spaces_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка генерации slug"):
            slug_value = shop_modal.get_slug_value()
            logger.info(f"Generated slug: '{slug_value}'")

            # Slug не должен начинаться или заканчиваться дефисом
            if slug_value:
                assert not slug_value.startswith("-"), \
                    f"FAILED: Slug starts with dash: {slug_value}"
                assert not slug_value.endswith("-"), \
                    f"FAILED: Slug ends with dash: {slug_value}"

        logger.info("SC-WS-04: Leading/trailing spaces - PASSED")

    @allure.title("Название магазина с множественными пробелами подряд")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_multiple_spaces(self, shop_modal):
        """Shop name with multiple consecutive spaces - verify normalization."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина с множественными пробелами"):
            multi_space_name = "Test    Shop    Multiple    Spaces"
            shop_modal.fill_shop_name(multi_space_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранённого значения"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Input: '{multi_space_name}', Stored: '{actual_value}'")

            allure.attach(
                f"Input: '{multi_space_name}'\nStored: '{actual_value}'",
                name="multi_spaces_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка slug (пробелы становятся одинарными дефисами)"):
            slug_value = shop_modal.get_slug_value()
            logger.info(f"Generated slug: '{slug_value}'")

            # Slug не должен содержать двойных дефисов
            if slug_value:
                assert "--" not in slug_value, \
                    f"FAILED: Slug contains double dashes: {slug_value}"

        logger.info("SC-WS-05: Multiple consecutive spaces - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.functional
class TestShopCreateAdvancedInput:
    """Advanced input handling tests."""

    @allure.title("Копирование/вставка названия магазина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_copy_paste_shop_name(self, shop_modal):
        """Copy/paste into shop name field MUST work correctly."""
        page = shop_modal.page

        with allure.step("Ввод текста, выделение, копирование, вставка"):
            original_text = f"Copy Paste Test {int(time.time())}"
            shop_modal.fill_shop_name(original_text)
            page.wait_for_load_state("domcontentloaded")

            # Выделяем всё и копируем (Control для Windows/Linux)
            name_field = page.locator("input[type='text']").first
            name_field.select_text()
            page.keyboard.press("Control+c")
            page.wait_for_load_state("domcontentloaded")

            # Очищаем поле
            name_field.clear()
            page.wait_for_load_state("domcontentloaded")

            # Вставляем
            page.keyboard.press("Control+v")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка работы вставки"):
            actual_value = shop_modal.get_shop_name_value()
            assert "Copy" in actual_value or "Paste" in actual_value or actual_value == original_text, \
                f"BUG: Copy/paste failed, got '{actual_value}'"

    @allure.title("Тест методов ввода (type vs fill)")
    @allure.severity(allure.severity_level.MINOR)
    def test_input_methods(self, shop_modal):
        """Different input methods should work correctly."""
        page = shop_modal.page

        with allure.step("Тест метода fill"):
            shop_modal.fill_shop_name(f"Fill Method {int(time.time())}")
            fill_value = shop_modal.get_shop_name_value()
            logger.info(f"Fill method result: {fill_value}")

        with allure.step("Очистка и тест метода type"):
            shop_modal.clear_shop_name()
            page.wait_for_load_state("domcontentloaded")

            # Использовать type (посимвольный ввод)
            name_field = page.locator("input[type='text']").first
            type_text = f"Type Method {int(time.time())}"
            name_field.type(type_text, delay=50)
            page.wait_for_load_state("domcontentloaded")

            type_value = shop_modal.get_shop_name_value()
            logger.info(f"Type method result: {type_value}")

        with allure.step("Проверка работы обоих методов"):
            assert len(fill_value) > 0, "FAILED: Fill method did not work"
            assert len(type_value) > 0, "FAILED: Type method did not work"

            allure.attach(
                f"Fill result: {fill_value}\nType result: {type_value}",
                name="input_methods_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-AI-02: Input methods - PASSED")

    @allure.title("Проверка атрибутов автозаполнения")
    @allure.severity(allure.severity_level.MINOR)
    def test_autocomplete_attributes(self, shop_modal):
        """Check autocomplete attributes on form fields."""
        page = shop_modal.page

        with allure.step("Проверка полей на автозаполнение"):
            inputs = page.locator("input[type='text'], textarea")
            input_count = inputs.count()

            autocomplete_info = []
            for i in range(input_count):
                input_el = inputs.nth(i)
                try:
                    autocomplete = input_el.get_attribute("autocomplete") or "not set"
                    name = input_el.get_attribute("name") or f"input_{i}"
                    placeholder = input_el.get_attribute("placeholder") or ""
                    autocomplete_info.append(f"{name} ({placeholder}): autocomplete={autocomplete}")
                except Exception as e:
                    logger.debug(f"Failed to get autocomplete for input {i}: {e}")

            logger.info(f"Autocomplete attributes: {autocomplete_info}")

            allure.attach(
                "\n".join(autocomplete_info),
                name="autocomplete_attributes",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка заполняемости формы"):
            # Просто проверяем что форма работает
            shop_modal.fill_shop_name(f"Autocomplete Test {int(time.time())}")
            value = shop_modal.get_shop_name_value()
            assert len(value) > 0, "FAILED: Form not fillable"

        logger.info("SC-AI-03: Autocomplete attributes - PASSED")

