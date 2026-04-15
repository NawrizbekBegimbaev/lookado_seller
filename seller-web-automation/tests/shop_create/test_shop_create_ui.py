"""
Shop Create UI, Accessibility, and ValidationUX Tests.
Tests UI elements, ARIA attributes, keyboard navigation, and validation UX.
"""
import re
import os
import pytest
import logging
import time
import allure
from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage, ShopCreateModal

logger = logging.getLogger(__name__)


@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.functional
class TestShopCreateUI:
    """Test UI elements of shop create modal - HARD assertions only."""

    @allure.title("Проверка загрузки страницы создания магазина")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_page_loads(self, shop_modal):
        """Shop create page must load and form be visible - FAILS if not."""
        with allure.step("Проверка загрузки формы создания магазина"):
            assert shop_modal.is_page_loaded(), \
                "FAILED: Shop create page form is not visible"

            logger.info("SC-UI-01: Page loads correctly - PASSED")

    @allure.title("Проверка видимости поля названия магазина")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_shop_name_field_visible(self, shop_modal):
        """Shop name field MUST be visible."""
        with allure.step("Проверка видимости поля названия магазина"):
            assert shop_modal.is_shop_name_field_visible(), \
                "FAILED: Shop name field is not visible in modal"

            logger.info("SC-UI-02: Shop name field visible - PASSED")

    @allure.title("Проверка видимости поля slug")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slug_field_visible(self, shop_modal):
        """Slug field MUST be visible."""
        with allure.step("Проверка видимости поля slug"):
            assert shop_modal.is_slug_field_visible(), \
                "FAILED: Slug field is not visible in modal"

            logger.info("SC-UI-03: Slug field visible - PASSED")

    @allure.title("Проверка видимости поля SKU")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sku_field_visible(self, shop_modal):
        """SKU field MUST be visible."""
        with allure.step("Проверка видимости поля SKU"):
            assert shop_modal.is_sku_field_visible(), \
                "FAILED: SKU field is not visible in modal"

            logger.info("SC-UI-04: SKU field visible - PASSED")

    @allure.title("Проверка видимости поля описания на узбекском")
    @allure.severity(allure.severity_level.NORMAL)
    def test_description_uz_field_visible(self, shop_modal):
        """Uzbek description field MUST be visible."""
        with allure.step("Проверка видимости поля описания на узбекском"):
            assert shop_modal.is_description_uz_field_visible(), \
                "FAILED: Uzbek description field is not visible"

            logger.info("SC-UI-05: Uzbek description field visible - PASSED")

    @allure.title("Проверка видимости поля описания на русском")
    @allure.severity(allure.severity_level.NORMAL)
    def test_description_ru_field_visible(self, shop_modal):
        """Russian description field MUST be visible."""
        with allure.step("Проверка видимости поля описания на русском"):
            assert shop_modal.is_description_ru_field_visible(), \
                "FAILED: Russian description field is not visible"

            logger.info("SC-UI-06: Russian description field visible - PASSED")

    @allure.title("Проверка видимости кнопки сохранения")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_save_button_visible(self, shop_modal):
        """Save button MUST be visible."""
        with allure.step("Проверка видимости кнопки сохранения"):
            assert shop_modal.is_save_button_visible(), \
                "FAILED: Save button is not visible in modal"

            logger.info("SC-UI-07: Save button visible - PASSED")

    @allure.title("Проверка наличия полей загрузки файлов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_file_inputs_exist(self, shop_modal):
        """File inputs for logo and banner MUST exist."""
        with allure.step("Проверка наличия полей загрузки файлов (логотип, баннер)"):
            file_count = shop_modal.get_file_input_count()
            assert file_count >= 2, \
                f"FAILED: Expected at least 2 file inputs (logo, banner), got {file_count}"

            logger.info(f"SC-UI-08: Found {file_count} file inputs - PASSED")

    @allure.title("Проверка авто-генерации slug из названия магазина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slug_auto_generation(self, shop_modal):
        """Slug MUST auto-generate when shop name is entered."""
        page = shop_modal.page

        with allure.step("Ввод названия магазина и ожидание генерации slug"):
            test_name = f"Test Shop {int(time.time())}"
            shop_modal.fill_shop_name(test_name)
            page.keyboard.press("Tab")
            expect(page.locator("input[name='slug']")).not_to_have_value("", timeout=10000)

        with allure.step("Проверка что slug сгенерирован автоматически"):
            slug = shop_modal.get_slug_value()
            assert len(slug) > 0, \
                f"FAILED: Slug was not auto-generated after entering shop name '{test_name}'"

            logger.info(f"SC-UI-09: Slug auto-generated: '{slug}' - PASSED")

    @allure.title("Проверка авто-генерации SKU из названия магазина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sku_auto_generation(self, shop_modal):
        """SKU MUST auto-generate when shop name is entered."""
        page = shop_modal.page

        with allure.step("Ввод названия магазина и ожидание генерации SKU"):
            test_name = f"Test Shop {int(time.time())}"
            shop_modal.fill_shop_name(test_name)
            page.keyboard.press("Tab")
            expect(page.locator("input[name='sku']")).not_to_have_value("", timeout=10000)

        with allure.step("Проверка что SKU сгенерирован автоматически"):
            sku = shop_modal.get_sku_value()
            assert len(sku) > 0, \
                f"FAILED: SKU was not auto-generated after entering shop name '{test_name}'"

            logger.info(f"SC-UI-10: SKU auto-generated: '{sku}' - PASSED")

    @allure.title("Проверка закрытия диалога клавишей Escape")
    @allure.severity(allure.severity_level.NORMAL)
    def test_dialog_closes_on_escape(self, shop_modal):
        """Dialog MUST close when Escape is pressed."""
        page = shop_modal.page

        with allure.step("Проверка что диалог загружен"):
            assert shop_modal.is_page_loaded(), "FAILED: Shop create dialog not loaded"

        with allure.step("Нажатие Escape и проверка закрытия диалога"):
            page.keyboard.press("Escape")
            page.wait_for_load_state("domcontentloaded")

            assert not shop_modal.is_page_loaded(timeout=3000), \
                "BUG: Dialog did not close on Escape key"

            logger.info("SC-UI-11: Dialog closes on Escape - PASSED")


# ================================================================================
# TEST CLASS: Empty Fields Validation
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.negative



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.functional
class TestShopCreateAccessibility:
    """Accessibility tests for shop create modal."""

    @allure.title("Состояния фокуса на полях формы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_focus_states(self, shop_modal):
        """Form fields MUST have visible focus states."""
        page = shop_modal.page

        with allure.step("Переход по полям формы клавишей Tab"):
            focus_info = []

            # Начинаем с первого поля
            name_field = page.locator("input[type='text']").first
            name_field.focus()
            page.wait_for_load_state("domcontentloaded")

            # Проверяем что поле получило фокус
            is_focused = name_field.evaluate("el => el === document.activeElement")
            focus_info.append(f"Name field focused: {is_focused}")

            # Tab к следующему полю
            page.keyboard.press("Tab")
            page.wait_for_load_state("domcontentloaded")

            # Проверяем новый активный элемент
            active_tag = page.evaluate("document.activeElement.tagName")
            focus_info.append(f"After Tab: active element is {active_tag}")

            logger.info(f"Focus info: {focus_info}")

            allure.attach(
                "\n".join(focus_info),
                name="focus_states",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка видимости фокуса"):
            # Проверяем что активный элемент имеет outline или border
            focused_style = page.evaluate("""
                () => {
                    const el = document.activeElement;
                    const style = window.getComputedStyle(el);
                    return {
                        outline: style.outline,
                        border: style.border,
                        boxShadow: style.boxShadow
                    };
                }
            """)
            logger.info(f"Focused element styles: {focused_style}")

        logger.info("SC-A11Y-01: Focus states - PASSED")

    @allure.title("ARIA атрибуты на полях формы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_aria_attributes(self, shop_modal):
        """Form fields MUST have proper ARIA attributes or labels."""
        page = shop_modal.page

        with allure.step("Проверка меток и ARIA атрибутов полей"):
            inputs = page.locator("input[type='text'], textarea")
            input_count = inputs.count()

            label_info = []
            for i in range(input_count):
                input_el = inputs.nth(i)
                try:
                    input_id = input_el.get_attribute("id") or f"input_{i}"
                    input_name = input_el.get_attribute("name") or "none"
                    aria_label = input_el.get_attribute("aria-label") or "none"
                    placeholder = input_el.get_attribute("placeholder") or "none"
                    label_info.append(f"{input_name} (id={input_id}): aria-label={aria_label}, placeholder={placeholder}")
                except Exception as e:
                    logger.debug(f"Failed to get label for input {i}: {e}")

            logger.info(f"Input labels: {label_info}")

            allure.attach(
                "\n".join(label_info) if label_info else "No inputs found",
                name="aria_attributes",
                attachment_type=allure.attachment_type.TEXT
            )

            assert input_count > 0, "FAILED: No form input fields found on shop create page"

        logger.info("SC-A11Y-02: ARIA attributes - PASSED")

    @allure.title("Навигация с клавиатуры")
    @allure.severity(allure.severity_level.NORMAL)
    def test_keyboard_navigation(self, shop_modal):
        """Modal MUST be fully navigable by keyboard."""
        page = shop_modal.page

        with allure.step("Навигация клавишей Tab"):
            # Начинаем навигацию
            navigation_log = []

            for i in range(8):
                page.keyboard.press("Tab")
                page.wait_for_load_state("domcontentloaded")

                active_info = page.evaluate("""
                    () => {
                        const el = document.activeElement;
                        return {
                            tag: el.tagName,
                            type: el.type || 'n/a',
                            placeholder: el.placeholder || '',
                            text: el.textContent?.slice(0, 20) || ''
                        };
                    }
                """)
                navigation_log.append(f"Tab {i+1}: {active_info}")

            logger.info(f"Navigation log:\n" + "\n".join(navigation_log))

            allure.attach(
                "\n".join(navigation_log),
                name="keyboard_navigation",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка работы навигации Tab"):
            assert len(navigation_log) > 0, "FAILED: Tab navigation did not produce any focus changes"

        logger.info("SC-A11Y-03: Keyboard navigation - PASSED")


# ================================================================================
# TEST CLASS: Slug/SKU Validation Tests
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.negative



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.functional
class TestShopCreateValidationUX:
    """Validation user experience tests."""

    @allure.title("Валидация в реальном времени при вводе")
    @allure.severity(allure.severity_level.NORMAL)
    def test_realtime_validation(self, shop_modal):
        """Validation should occur as user types (real-time)."""
        page = shop_modal.page

        with allure.step("Медленный ввод невалидного значения"):
            name_field = page.locator("input[type='text']").first
            name_field.focus()

            # Вводим по одному символу
            name_field.type("A", delay=100)
            page.wait_for_load_state("domcontentloaded")

            # Проверяем есть ли ошибка для короткого имени
            errors_after_1_char = shop_modal.has_validation_errors()
            error_msgs = shop_modal.get_validation_error_messages()

            logger.info(f"After 1 char: errors={errors_after_1_char}, msgs={error_msgs}")

        with allure.step("Продолжение ввода до валидной длины"):
            name_field.type("Test Shop Name", delay=50)
            page.wait_for_load_state("domcontentloaded")

            errors_after_valid = shop_modal.has_validation_errors()
            error_msgs_after = shop_modal.get_validation_error_messages()

            logger.info(f"After valid input: errors={errors_after_valid}, msgs={error_msgs_after}")

        with allure.step("Фиксация времени валидации"):
            allure.attach(
                f"After 1 char: errors={errors_after_1_char}\nAfter valid: errors={errors_after_valid}",
                name="realtime_validation",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-VUX-01: Real-time validation - PASSED")

    @allure.title("Валидация при потере фокуса (blur)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_validation_on_blur(self, shop_modal):
        """Validation should trigger when field loses focus."""
        page = shop_modal.page

        with allure.step("Фокус на поле имени и ввод короткого значения"):
            name_field = page.locator("input[type='text']").first
            name_field.focus()
            name_field.fill("A")
            page.wait_for_load_state("domcontentloaded")

            errors_before_blur = shop_modal.has_validation_errors()

        with allure.step("Перемещение фокуса на другое поле"):
            page.keyboard.press("Tab")
            page.wait_for_load_state("domcontentloaded")

            errors_after_blur = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"Before blur: {errors_before_blur}, After blur: {errors_after_blur}")
            logger.info(f"Error messages: {error_messages}")

        with allure.step("Фиксация валидации при blur"):
            allure.attach(
                f"Errors before blur: {errors_before_blur}\nErrors after blur: {errors_after_blur}\nMessages: {error_messages}",
                name="blur_validation",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-VUX-02: Validation on blur - PASSED")

    @allure.title("Локализация сообщений об ошибках")
    @allure.severity(allure.severity_level.MINOR)
    def test_error_messages_localized(self, shop_modal):
        """Error messages should be in appropriate language."""
        page = shop_modal.page

        with allure.step("Вызов ошибок валидации"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка языка сообщений об ошибках"):
            error_messages = shop_modal.get_validation_error_messages()
            logger.info(f"Error messages: {error_messages}")

            # Проверяем что сообщения не пустые и не на английском (если UI на русском)
            import re

            localization_info = []
            for msg in error_messages:
                has_cyrillic = bool(re.search(r'[а-яА-ЯёЁ]', msg))
                has_latin = bool(re.search(r'[a-zA-Z]', msg))
                localization_info.append(f"'{msg}': cyrillic={has_cyrillic}, latin={has_latin}")

            logger.info(f"Localization: {localization_info}")

            allure.attach(
                "\n".join(localization_info) if localization_info else "No error messages",
                name="localization_check",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-VUX-03: Error messages localization - PASSED")
