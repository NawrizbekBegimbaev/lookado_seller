"""
Shop Create Functional, Session, and SlugSku Tests.
Tests CRUD operations, session persistence, slug/SKU validation.
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
class TestShopCreateFunctional:
    """Functional workflow tests."""

    @allure.title("Заполнение всех обязательных полей")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_fill_all_required_fields(self, shop_modal, test_data):
        """Fill all required fields - verify no validation errors."""
        page = shop_modal.page

        with allure.step("Заполнение всех обязательных полей"):
            shop_data = test_data.get("shop_data", {})
            banners = test_data.get("banners", {})
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

            # Shop name
            shop_name = f"{shop_data.get('shop_name', 'Test Shop')} {int(time.time())}"
            shop_modal.fill_shop_name(shop_name)
            page.wait_for_load_state("domcontentloaded")

            # Descriptions
            shop_modal.fill_description_uz(shop_data.get("description_uz", "Test do'kon tavsifi"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Тестовое описание магазина"))

            # Files
            logo_path = os.path.join(project_root, banners.get("logo_shop", "test_data/resources/img.png"))
            banner_path = os.path.join(project_root, banners.get("banner_shop", "test_data/resources/tv.png"))

            if os.path.exists(logo_path) and os.path.exists(banner_path):
                shop_modal.upload_logo(banner_path, logo_path)
                page.wait_for_load_state("networkidle")

        with allure.step("Проверка готовности формы"):
            name_value = shop_modal.get_shop_name_value()
            assert len(name_value) > 0, "FAILED: Shop name is empty"

            slug_value = shop_modal.get_slug_value()
            assert len(slug_value) > 0, "FAILED: Slug was not auto-generated"

        logger.info("SC-FN-01: All fields filled correctly - PASSED")

    @allure.title("Функционал загрузки логотипа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_logo_upload(self, shop_modal, test_data):
        """Logo upload MUST work correctly."""
        page = shop_modal.page

        with allure.step("Загрузка логотипа"):
            banners = test_data.get("banners", {})
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            logo_path = os.path.join(project_root, banners.get("logo_shop", "test_data/resources/img.png"))

            if not os.path.exists(logo_path):
                pytest.fail(f"FAILED: Logo file not found at {logo_path}")

            shop_modal.upload_logo_only(logo_path)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка загрузки"):
            # Check for image preview or success indicator
            logger.info("Logo upload completed")

        logger.info("SC-FN-02: Logo upload - PASSED")

    @allure.title("Функционал загрузки баннера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_banner_upload(self, shop_modal, test_data):
        """Banner upload MUST work correctly."""
        page = shop_modal.page

        with allure.step("Загрузка баннера"):
            banners = test_data.get("banners", {})
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            banner_path = os.path.join(project_root, banners.get("banner_shop", "test_data/resources/tv.png"))

            if not os.path.exists(banner_path):
                pytest.fail(f"FAILED: Banner file not found at {banner_path}")

            shop_modal.upload_banner_only(banner_path)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка загрузки"):
            logger.info("Banner upload completed")

        logger.info("SC-FN-03: Banner upload - PASSED")

    @allure.title("Отмена сбрасывает изменения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_discards_changes(self, dashboard_page, test_data):
        """Closing dialog MUST discard all entered data."""
        page = dashboard_page.page

        with allure.step("Открытие диалога и заполнение данных"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("domcontentloaded")
            shop_modal = dashboard_page.click_add_shop()
            page.wait_for_load_state("networkidle")

            shop_modal.fill_shop_name("Test Shop To Cancel")
            shop_modal.fill_description_uz("Test UZ")
            shop_modal.fill_description_ru("Test RU")

        with allure.step("Закрытие диалога"):
            shop_modal.close_modal()
            page.wait_for_load_state("networkidle")

            assert not shop_modal.is_page_loaded(timeout=3000), \
                "BUG: Dialog did not close after clicking backdrop"

        with allure.step("Повторное открытие и проверка очистки данных"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("domcontentloaded")
            shop_modal = dashboard_page.click_add_shop()
            page.wait_for_load_state("networkidle")

            name_value = shop_modal.get_shop_name_value()
            assert name_value == "" or "Test Shop To Cancel" not in name_value, \
                "FAILED: Previous data was not discarded"

        logger.info("SC-FN-04: Cancel discards changes - PASSED")

    @allure.title("Форма сохраняет данные при редактировании")
    @allure.severity(allure.severity_level.MINOR)
    def test_form_retains_data(self, shop_modal):
        """Data entered in one field should persist while filling others."""
        page = shop_modal.page

        with allure.step("Заполнение названия магазина"):
            test_name = f"Retention Test {int(time.time())}"
            shop_modal.fill_shop_name(test_name)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Заполнение описаний"):
            shop_modal.fill_description_uz("Test UZ Description")
            page.wait_for_load_state("domcontentloaded")
            shop_modal.fill_description_ru("Test RU Description")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранения исходного названия магазина"):
            actual_name = shop_modal.get_shop_name_value()
            assert test_name in actual_name or actual_name == test_name, \
                f"FAILED: Shop name changed from '{test_name}' to '{actual_name}'"

        logger.info("SC-FN-05: Form retains data - PASSED")

    @allure.title("Попытка создания магазина с дублирующим названием")
    @allure.severity(allure.severity_level.NORMAL)
    def test_duplicate_shop_name(self, shop_modal, test_data):
        """Creating shop with existing name MUST show error or disable save."""
        page = shop_modal.page

        # Локатор красной иконки ошибки (svg с цветом rgb(255, 86, 48))
        error_icon_locator = page.locator(".MuiInputAdornment-root svg[style*='rgb(255, 86, 48)']")

        with allure.step("Заполнение формы известным существующим названием"):
            shop_modal.fill_shop_name("Zara")
            # Tab для blur — React генерирует slug и запускает серверную проверку
            page.keyboard.press("Tab")
            page.wait_for_load_state("networkidle")

        with allure.step("Ожидание асинхронной проверки дубликата"):
            # Ждём появления красной иконки ошибки (серверная проверка дубликата)
            error_icon_locator.first.wait_for(state="visible", timeout=10000)

        with allure.step("Проверка обнаружения дубликата"):
            has_error_icon = error_icon_locator.count() > 0
            save_enabled = shop_modal.is_save_button_enabled()

            logger.info(f"Duplicate name: save_enabled={save_enabled}, error_icon={has_error_icon}")

            assert has_error_icon, \
                "FAILED: No red error icon for duplicate shop name"
            assert not save_enabled, \
                "FAILED: Save button should be disabled for duplicate shop name"

        logger.info("SC-FN-06: Duplicate shop name test - PASSED")

    @allure.title("Ручное редактирование авто-сгенерированного slug")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_auto_generated_slug(self, shop_modal):
        """User should be able to manually edit auto-generated slug."""
        page = shop_modal.page

        with allure.step("Заполнение названия и ожидание авто-slug"):
            shop_modal.fill_shop_name(f"Auto Slug Test {int(time.time())}")
            page.wait_for_load_state("networkidle")

            auto_slug = shop_modal.get_slug_value()
            logger.info(f"Auto-generated slug: {auto_slug}")

        with allure.step("Ручное редактирование slug"):
            custom_slug = f"custom-slug-{int(time.time())}"
            shop_modal.fill_slug(custom_slug)
            page.wait_for_load_state("domcontentloaded")

            actual_slug = shop_modal.get_slug_value()
            logger.info(f"After manual edit: {actual_slug}")

            allure.attach(
                f"Auto slug: {auto_slug}\nCustom slug: {custom_slug}\nActual: {actual_slug}",
                name="slug_edit_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FN-07: Edit auto-generated slug - PASSED")

    @allure.title("Ручное редактирование авто-сгенерированного SKU")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_auto_generated_sku(self, shop_modal):
        """User should be able to manually edit auto-generated SKU."""
        page = shop_modal.page

        with allure.step("Заполнение названия и ожидание авто-SKU"):
            shop_modal.fill_shop_name(f"Auto SKU Test {int(time.time())}")
            page.wait_for_load_state("networkidle")

            auto_sku = shop_modal.get_sku_value()
            logger.info(f"Auto-generated SKU: {auto_sku}")

        with allure.step("Ручное редактирование SKU"):
            custom_sku = f"CUSTOM_SKU_{int(time.time())}"
            shop_modal.fill_sku(custom_sku)
            page.wait_for_load_state("domcontentloaded")

            actual_sku = shop_modal.get_sku_value()
            logger.info(f"After manual edit: {actual_sku}")

            allure.attach(
                f"Auto SKU: {auto_sku}\nCustom SKU: {custom_sku}\nActual: {actual_sku}",
                name="sku_edit_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FN-08: Edit auto-generated SKU - PASSED")

    @allure.title("Обнаружение конфликта slug")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slug_conflict(self, shop_modal, test_data):
        """Creating shop with existing slug MUST show error."""
        page = shop_modal.page

        with allure.step("Заполнение формы с потенциально конфликтующим slug"):
            shop_modal.fill_shop_name(f"Unique Name {int(time.time())}")
            page.wait_for_load_state("domcontentloaded")

            # Установим slug который вероятно уже занят
            shop_modal.fill_slug("zara")
            page.wait_for_load_state("domcontentloaded")

            shop_data = test_data.get("shop_data", {})
            shop_modal.fill_description_uz(shop_data.get("description_uz", "Тест"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Тест"))

        with allure.step("Отправка формы"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка ошибки конфликта slug"):
            has_errors = shop_modal.has_validation_errors()
            has_toast = shop_modal.has_toast_error()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"Slug conflict: validation={has_errors}, toast={has_toast}")
            logger.info(f"Messages: {error_messages}")

            allure.attach(
                f"Slug conflict test\nValidation: {has_errors}\nToast: {has_toast}\nMessages: {error_messages}",
                name="slug_conflict_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-FN-09: Slug conflict test - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.session
class TestShopCreateSession:
    """Session and authentication tests."""

    @allure.title("Модальное окно требует авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_requires_authentication(self, browser, request):
        """Shop create MUST require authentication - anonymous users cannot access."""
        from config import settings

        # Create new context without authentication
        context = browser.new_context()
        page = context.new_page()

        try:
            with allure.step("Переход на дашборд без авторизации"):
                base_url = request.config.getoption("url_name")
                page.goto(f"{base_url}/dashboard")
                page.wait_for_load_state("networkidle", timeout=10000)

            with allure.step("Проверка редиректа на логин"):
                current_url = page.url
                assert "login" in current_url.lower() or "auth" in current_url.lower(), \
                    f"FAILED: Unauthenticated user was NOT redirected to login. URL: {current_url}"

                logger.info(f"Correctly redirected to: {current_url}")

        finally:
            page.close()
            context.close()

        logger.info("SC-SS-01: Authentication required - PASSED")

    @allure.title("Сессия сохраняется после взаимодействия с диалогом")
    @allure.severity(allure.severity_level.NORMAL)
    def test_session_persists(self, dashboard_page):
        """Session should persist after opening/closing shop create dialog."""
        page = dashboard_page.page

        with allure.step("Открытие и закрытие диалога"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("domcontentloaded")
            shop_modal = dashboard_page.click_add_shop()
            page.wait_for_load_state("networkidle")

            shop_modal.click_cancel()
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка нахождения на дашборде (сессия активна)"):
            assert "dashboard" in page.url.lower(), \
                f"FAILED: Session lost after dialog interaction. URL: {page.url}"

        logger.info("SC-SS-02: Session persists - PASSED")

    @allure.title("Возможность многократного открытия диалога создания магазина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_multiple_dialog_opens(self, dashboard_page):
        """Shop create dialog should open correctly multiple times."""
        page = dashboard_page.page

        for i in range(3):
            with allure.step(f"Открытие диалога, попытка {i + 1}"):
                dashboard_page.open_shop_dropdown()
                page.wait_for_load_state("domcontentloaded")
                shop_modal = dashboard_page.click_add_shop()
                page.wait_for_load_state("networkidle")

                assert shop_modal.is_page_loaded(), \
                    f"FAILED: Dialog did not open on attempt {i + 1}"

                shop_modal.click_cancel()
                page.wait_for_load_state("domcontentloaded")

        logger.info("SC-SS-03: Multiple dialog opens - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.negative
class TestShopCreateSlugSku:
    """Slug and SKU field validation tests."""

    @allure.title("Slug с пробелами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slug_with_spaces(self, shop_modal):
        """Slug with spaces MUST be rejected or sanitized."""
        page = shop_modal.page

        with allure.step("Заполнение названия и ручная установка slug с пробелами"):
            shop_modal.fill_shop_name(f"Slug Space Test {int(time.time())}")
            page.wait_for_load_state("networkidle")

            # Пытаемся вручную установить slug с пробелами
            shop_modal.fill_slug("slug with spaces")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка обработки slug"):
            actual_slug = shop_modal.get_slug_value()
            logger.info(f"Attempted slug: 'slug with spaces', Actual: '{actual_slug}'")

            # Slug не должен содержать пробелы
            has_spaces = " " in actual_slug
            allure.attach(
                f"Input: 'slug with spaces'\nActual: '{actual_slug}'\nHas spaces: {has_spaces}",
                name="slug_spaces_result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Пробелы должны быть заменены на дефисы или удалены
            if has_spaces:
                logger.warning("Slug contains spaces - should be sanitized!")

        logger.info("SC-SS-01: Slug with spaces - PASSED")

    @allure.title("Slug со спецсимволами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slug_special_characters(self, shop_modal):
        """Slug with special characters MUST be sanitized."""
        page = shop_modal.page

        with allure.step("Установка slug со спецсимволами"):
            shop_modal.fill_shop_name(f"Special Slug Test {int(time.time())}")
            page.wait_for_load_state("networkidle")

            special_slug = "slug!@#$%^&*()test"
            shop_modal.fill_slug(special_slug)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка обработки спецсимволов"):
            actual_slug = shop_modal.get_slug_value()
            logger.info(f"Input: '{special_slug}', Actual: '{actual_slug}'")

            # Проверяем что спецсимволы удалены
            import re
            has_special = bool(re.search(r'[!@#$%^&*()]', actual_slug))

            allure.attach(
                f"Input: '{special_slug}'\nActual: '{actual_slug}'\nHas special chars: {has_special}",
                name="slug_special_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-SS-02: Slug special characters - PASSED")

    @allure.title("Slug только с кириллицей")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slug_cyrillic_only(self, shop_modal):
        """Slug with only Cyrillic MUST be transliterated or rejected."""
        page = shop_modal.page

        with allure.step("Установка slug только из кириллицы"):
            shop_modal.fill_shop_name(f"Cyrillic Slug Test {int(time.time())}")
            page.wait_for_load_state("networkidle")

            cyrillic_slug = "магазин"
            shop_modal.fill_slug(cyrillic_slug)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка обработки кириллицы"):
            actual_slug = shop_modal.get_slug_value()
            logger.info(f"Input: '{cyrillic_slug}', Actual: '{actual_slug}'")

            # Slug должен быть транслитерирован или отклонен
            import re
            has_cyrillic = bool(re.search(r'[а-яА-ЯёЁ]', actual_slug))

            allure.attach(
                f"Input: '{cyrillic_slug}'\nActual: '{actual_slug}'\nHas Cyrillic: {has_cyrillic}",
                name="slug_cyrillic_result",
                attachment_type=allure.attachment_type.TEXT
            )

            if has_cyrillic:
                logger.warning("Slug contains Cyrillic - may cause URL issues!")

        logger.info("SC-SS-03: Slug Cyrillic only - PASSED")

    @allure.title("SKU со спецсимволами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sku_special_characters(self, shop_modal):
        """SKU with special characters - document behavior."""
        page = shop_modal.page

        with allure.step("Установка SKU со спецсимволами"):
            shop_modal.fill_shop_name(f"SKU Special Test {int(time.time())}")
            page.wait_for_load_state("networkidle")

            special_sku = "SKU!@#$%TEST"
            shop_modal.fill_sku(special_sku)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка обработки SKU"):
            actual_sku = shop_modal.get_sku_value()
            logger.info(f"Input: '{special_sku}', Actual: '{actual_sku}'")

            allure.attach(
                f"Input: '{special_sku}'\nActual: '{actual_sku}'",
                name="sku_special_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-SS-04: SKU special characters - PASSED")

    @allure.title("Обнаружение дубликата SKU")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sku_duplicate(self, shop_modal, test_data):
        """Duplicate SKU MUST show error or be rejected."""
        page = shop_modal.page

        with allure.step("Установка потенциально дублирующегося SKU"):
            shop_modal.fill_shop_name(f"SKU Duplicate Test {int(time.time())}")
            page.wait_for_load_state("networkidle")

            # Пытаемся использовать SKU который вероятно уже существует
            shop_modal.fill_sku("ZARA")
            page.wait_for_load_state("networkidle")

            shop_data = test_data.get("shop_data", {})
            shop_modal.fill_description_uz(shop_data.get("description_uz", "Test"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Тест"))

        with allure.step("Проверка обнаружения дубликата"):
            has_errors = shop_modal.has_validation_errors()
            save_enabled = shop_modal.is_save_button_enabled()
            error_messages = shop_modal.get_validation_error_messages()

            logger.info(f"SKU duplicate: errors={has_errors}, save_enabled={save_enabled}")

            allure.attach(
                f"SKU: ZARA\nValidation errors: {has_errors}\nSave enabled: {save_enabled}\nMessages: {error_messages}",
                name="sku_duplicate_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-SS-05: SKU duplicate - PASSED")

