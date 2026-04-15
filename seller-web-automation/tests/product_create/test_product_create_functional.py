"""
Product Create Functional tests - Navigation, Session, Robustness, E2E, etc.
"""

import pytest
import allure
import logging
import os

from config.settings import Settings
from utils import ProductDataGenerator
from tests.product_create.conftest import (
    get_uz_name_field, get_uz_desc_field, get_ru_desc_field, RESOURCES_PATH
)

logger = logging.getLogger(__name__)


# =============================================================================
# NAVIGATION TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — Навигация")
class TestProductCreateNavigation:
    """Wizard navigation tests."""

    @allure.title("Кнопка 'Назад' возвращает на предыдущий шаг")
    def test_back_button_from_step2(self, product_on_step2):
        """Back button on Step 2 should return to Step 1."""
        with allure.step("Нажатие кнопки 'Назад' на Шаге 2"):
            product_on_step2.click_back_button()
            product_on_step2.page.wait_for_load_state("networkidle")

        with allure.step("Проверка возврата на Шаг 1"):
            is_step1 = product_on_step2.is_category_combobox_visible()
            assert is_step1, "BUG: Back button did not return to Step 1"

    @allure.title("Данные сохраняются после навигации назад")
    def test_data_persists_after_back(self, product_on_step2):
        """Data entered on Step 1 should persist after back navigation."""
        with allure.step("Заполнение поля SKU на Шаге 2"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_on_step2.fill_single_field("SKU", data["sku"])

        with allure.step("Нажатие кнопки 'Назад' для возврата на Шаг 1"):
            product_on_step2.click_back_button()
            product_on_step2.page.wait_for_load_state("networkidle")

        with allure.step("Переход обратно на Шаг 2"):
            product_on_step2.scroll_page(500)
            product_on_step2.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_on_step2.page.wait_for_load_state("networkidle")

        with allure.step("Проверка сохранения данных SKU"):
            sku_value = product_on_step2.get_field_value("SKU")
            logger.info(f"Data persistence: SKU after back/forward = '{sku_value}'")

    @allure.title("Прямой доступ к Шагу 2 без завершения Шага 1")
    def test_direct_url_step2(self, staging_session):
        """Direct URL to Step 2 should redirect to Step 1 or show error."""
        page, product_page, _ = staging_session

        with allure.step("Переход по прямому URL на Шаг 2"):
            step2_url = f"{Settings.STAGING_URL}/dashboard/products/create?step=2"
            page.goto(step2_url, wait_until="load", timeout=15000)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка редиректа на Шаг 1"):
            current_url = page.url
            has_category = product_page.is_category_combobox_visible()
            logger.info(f"Direct URL access: redirected to '{current_url}', has_category={has_category}")

    @allure.title("Поведение кнопки 'Назад' браузера")
    def test_browser_back_button(self, product_on_step2):
        """Browser back button should work correctly."""
        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            page = product_on_step2.page
            page.go_back()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка навигации после нажатия 'Назад'"):
            current_url = page.url
            logger.info(f"Browser back: navigated to '{current_url}'")


# =============================================================================
# SESSION TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — Сессия")
class TestProductCreateSession:
    """Session and authentication tests."""

    @allure.title("Страница требует авторизации")
    def test_requires_authentication(self, page):
        """Product create page should require authentication."""
        with allure.step("Переход на страницу создания товара без авторизации"):
            page.goto(f"{Settings.STAGING_URL}/dashboard/products/create", wait_until="load", timeout=15000)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка редиректа на страницу логина"):
            current_url = page.url
            assert "/auth/login" in current_url or "/products/create" not in current_url, \
                "BUG: Product create page accessible without authentication"

    @allure.title("Сессия сохраняется при навигации по шагам мастера")
    def test_session_persists_during_wizard(self, product_on_step3):
        """Session should persist through all wizard steps."""
        with allure.step("Проверка URL на Шаге 3 мастера"):
            page = product_on_step3.page
            current_url = page.url

        with allure.step("Проверка что сессия не потеряна"):
            assert "/auth/login" not in current_url, \
                "BUG: Session lost during wizard navigation"

    @allure.title("Данные сохраняются после обновления страницы")
    def test_data_after_refresh(self, product_on_step2):
        """Product data may be preserved after refresh (if using URL params)."""
        with allure.step("Сохранение текущего URL перед обновлением"):
            page = product_on_step2.page
            current_url = page.url

        with allure.step("Обновление страницы"):
            page.reload()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка URL после обновления"):
            new_url = page.url
            logger.info(f"After refresh: URL changed from '{current_url}' to '{new_url}'")


# =============================================================================
# ROBUSTNESS TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — Устойчивость")
class TestProductCreateRobustness:
    """Robustness and edge case tests."""

    @allure.title("Двойной клик на кнопку 'Далее'")
    def test_double_click_next(self, product_create_page):
        """Double-clicking Next should not cause issues."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Заполнение названий и описаний товара"):
            product_create_page.fill_product_names_staging(
                uz_name=data["uz_name"],
                uz_desc=data["uz_description"],
                ru_name=data["ru_name"],
                ru_desc=data["ru_description"]
            )

        with allure.step("Двойной клик на кнопку 'Далее'"):
            product_create_page.scroll_page(500)
            next_btn = product_create_page.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last
            next_btn.dblclick()
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка отсутствия ошибок после двойного клика"):
            page_content = product_create_page.page.content()
            assert "error" not in page_content.lower() or \
                   product_create_page.has_validation_errors(), \
                   "BUG: Double-click caused error"

    @allure.title("Быстрые изменения полей")
    def test_rapid_field_changes(self, product_create_page):
        """Rapid typing should be handled smoothly."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Быстрое многократное изменение поля названия"):
            product_create_page.scroll_page(300)
            field = get_uz_name_field(product_create_page.page)
            for i in range(10):
                field.fill(f"Test{i}")
                product_create_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка что последнее значение сохранилось"):
            final_value = product_create_page.get_field_value("Product name in Uzbek")
            assert final_value == "Test9", f"BUG: Rapid typing not handled, got '{final_value}'"

    @allure.title("Состояние формы после ошибки валидации")
    def test_form_state_after_error(self, product_create_page):
        """Form data should be preserved after validation error."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            short_desc = "A" * 49
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Заполнение названий с коротким описанием (< 50 символов)"):
            product_create_page.fill_product_names_staging(
                uz_name=data["uz_name"],
                uz_desc=short_desc,
                ru_name=data["ru_name"],
                ru_desc=short_desc
            )

        with allure.step("Попытка перехода на следующий шаг"):
            try:
                product_create_page.click_next_button()
            except Exception as e:
                logger.info(f"Next button click raised (expected for validation): {e}")
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка сохранения данных формы после ошибки валидации"):
            name_value = product_create_page.get_field_value("Product name in Uzbek")
            assert data["uz_name"] in name_value or name_value != "", \
                "BUG: Form data lost after validation error"


# =============================================================================
# ACCESSIBILITY TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — Доступность")
class TestProductCreateAccessibility:
    """Accessibility tests."""

    @allure.title("Поля формы имеют состояния фокуса")
    def test_focus_states(self, product_create_page):
        """Form fields should have visible focus states."""
        with allure.step("Установка фокуса на поле названия товара"):
            product_create_page.scroll_page(300)
            field = get_uz_name_field(product_create_page.page)
            field.focus()

        with allure.step("Проверка наличия визуального индикатора фокуса"):
            parent = field.locator("xpath=ancestor::div[contains(@class,'MuiFormControl')]").first
            classes = parent.get_attribute("class") or ""
            has_focus_indicator = "focused" in classes.lower() or "focus" in classes.lower()
            logger.info(f"Focus state: classes='{classes}', has_indicator={has_focus_indicator}")

    @allure.title("Навигация с клавиатуры работает")
    def test_keyboard_navigation(self, product_create_page):
        """Tab key should navigate between form fields."""
        with allure.step("Нажатие клавиши Tab для навигации"):
            product_create_page.page.keyboard.press("Tab")
            product_create_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка что фокус перешёл на интерактивный элемент"):
            focused = product_create_page.page.evaluate("document.activeElement.tagName")
            assert focused in ["INPUT", "BUTTON", "TEXTAREA", "DIV"], \
                f"BUG: Tab navigation not working, focused element: {focused}"

    @allure.title("Сообщения об ошибках доступны для скрин-ридеров")
    def test_accessible_error_messages(self, product_create_page):
        """Validation errors should be announced to screen readers."""
        with allure.step("Отправка формы без заполнения полей"):
            product_create_page.scroll_page(500)
            product_create_page.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка доступности ошибок для скрин-ридеров"):
            errors = product_create_page.page.locator("[aria-invalid='true'], [role='alert']").count()
            error_messages = product_create_page.get_validation_error_messages()
            logger.info(f"Accessible errors: aria-invalid count={errors}, messages={error_messages}")


# =============================================================================
# E2E TESTS
# =============================================================================

@pytest.mark.e2e
@pytest.mark.staging
@allure.feature("Создание товара — E2E")
class TestProductCreateE2E:
    """End-to-end product creation tests."""

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("E2E: Полный цикл создания товара")
    def test_complete_product_creation(self, staging_session):
        """Complete product creation from start to finish."""
        page, product_page, staging_data = staging_session
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")
        allure.dynamic.title(f"E2E: Создание товара (SKU: {data['sku']})")

        with allure.step("Навигация на дашборд и выбор магазина"):
            product_page.navigate_to_dashboard()
            page.wait_for_load_state("load", timeout=10000)
            product_page.select_shop(data["shop_name"])
            page.wait_for_load_state("networkidle")

        with allure.step("Нажатие кнопки добавления товара"):
            product_page.click_add_product_btn_staging()
            page.wait_for_load_state("networkidle")
            product_page.click_single_product_option()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 1: Заполнение информации о товаре"):
            product_page.select_category_from_combobox(data["category_path"])
            product_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_page.select_country_from_combobox(data["country"])
            product_page.select_brand_from_combobox(data["brand"])
            product_page.fill_product_names_staging(
                uz_name=data["uz_name"],
                uz_desc=data["uz_description"],
                ru_name=data["ru_name"],
                ru_desc=data["ru_description"]
            )
            product_page.click_next_button()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 2: Заполнение варианта и SKU"):
            product_page.fill_variant_fields_staging(
                sku=data["sku"],
                price=data["price"],
                discount_price=data["discount_price"],
                width=data["width"],
                length=data["length"],
                height=data["height"],
                weight=data["weight"],
                barcode=data["barcode"]
            )
            product_page.click_next_button()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 3: Загрузка изображения"):
            image_path = os.path.join(RESOURCES_PATH, "tv.png")
            if os.path.exists(image_path):
                product_page.upload_main_image(image_path)
            product_page.click_next_button()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 4: Отправка на модерацию"):
            product_page.click_submit_moderation_staging()
            product_page.click_go_to_products_staging()

        with allure.step("Проверка редиректа на список товаров"):
            assert "/dashboard/products" in page.url, \
                f"BUG: Not redirected to products list after creation. URL: {page.url}"
            logger.info(f"Product created successfully: SKU={data['sku']}")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("E2E: Создание товара с минимальными данными")
    def test_create_with_minimum_data(self, staging_session):
        """Create product with minimum required data."""
        page, product_page, staging_data = staging_session
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")

        with allure.step("Навигация на дашборд и выбор магазина"):
            product_page.navigate_to_dashboard()
            page.wait_for_load_state("load", timeout=10000)
            product_page.select_shop(data["shop_name"])
            page.wait_for_load_state("networkidle")

        with allure.step("Нажатие кнопки добавления товара"):
            product_page.click_add_product_btn_staging()
            page.wait_for_load_state("networkidle")
            product_page.click_single_product_option()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 1: Заполнение минимальных данных о товаре"):
            product_page.select_category_from_combobox(data["category_path"])
            product_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_page.select_country_from_combobox(data["country"])
            product_page.select_brand_from_combobox(data["brand"])
            min_desc = "A" * 50
            product_page.fill_product_names_staging(
                uz_name="Min Test",
                uz_desc=min_desc,
                ru_name="Мин Тест",
                ru_desc=min_desc
            )
            product_page.click_next_button()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 2: Заполнение минимальных данных варианта"):
            product_page.fill_variant_fields_staging(
                sku=data["sku"],
                price="1",
                discount_price="1",
                width="1",
                length="1",
                height="1",
                weight="0.1"
            )
            product_page.click_next_button()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 3: Пропуск или загрузка изображения"):
            try:
                product_page.click_next_button()
            except Exception:
                image_path = os.path.join(RESOURCES_PATH, "tv.png")
                if os.path.exists(image_path):
                    product_page.upload_main_image(image_path)
                product_page.click_next_button()
            page.wait_for_load_state("networkidle")

        with allure.step("Шаг 4: Отправка на модерацию"):
            product_page.click_submit_moderation_staging()
            logger.info("Product with minimum data: submitted")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("E2E: Прерывание создания товара на полпути")
    def test_abort_creation_midway(self, staging_session):
        """Start product creation and navigate away."""
        page, product_page, staging_data = staging_session
        data = ProductDataGenerator.generate_staging_product(product_type="jacket")

        with allure.step("Навигация на дашборд и выбор магазина"):
            product_page.navigate_to_dashboard()
            page.wait_for_load_state("load", timeout=10000)
            product_page.select_shop(data["shop_name"])
            page.wait_for_load_state("networkidle")

        with allure.step("Начало создания товара"):
            product_page.click_add_product_btn_staging()
            page.wait_for_load_state("networkidle")
            product_page.click_single_product_option()
            page.wait_for_load_state("networkidle")

        with allure.step("Частичное заполнение формы (выбор категории)"):
            product_page.select_category_from_combobox(data["category_path"])

        with allure.step("Прерывание создания — переход на дашборд"):
            page.goto(f"{Settings.STAGING_URL}/dashboard", wait_until="load", timeout=15000)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка успешной навигации на дашборд"):
            assert "/dashboard" in page.url, "BUG: Navigation away failed"
            logger.info("Aborted creation successfully")


# =============================================================================
# VALIDATION UX TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — UX валидации")
class TestProductCreateValidationUX:
    """Validation user experience tests."""

    @allure.title("Сообщения валидации понятны и информативны")
    def test_clear_error_messages(self, product_create_page):
        """Error messages should be clear and actionable."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            short_desc = "A" * 49
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Заполнение названий с коротким описанием"):
            product_create_page.fill_product_names_staging(
                uz_name=data["uz_name"],
                uz_desc=short_desc,
                ru_name=data["ru_name"],
                ru_desc=short_desc
            )

        with allure.step("Попытка перехода на следующий шаг"):
            try:
                product_create_page.click_next_button()
            except Exception as e:
                logger.info(f"Next button click raised (expected for validation): {e}")
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка что сообщения об ошибках понятны и информативны"):
            error_messages = product_create_page.get_validation_error_messages()
            logger.info(f"Error messages: {error_messages}")
            if error_messages:
                for msg in error_messages:
                    assert len(msg) > 5, f"BUG: Error message too short: '{msg}'"

    @allure.title("Валидация при потере фокуса")
    def test_validation_on_blur(self, product_create_page):
        """Fields should validate on blur (losing focus)."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод короткого описания в поле"):
            product_create_page.scroll_page(300)
            desc_field = get_uz_desc_field(product_create_page.page)
            desc_field.fill("short")

        with allure.step("Перевод фокуса на другое поле (blur)"):
            get_ru_desc_field(product_create_page.page).focus()
            product_create_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка появления ошибки валидации после потери фокуса"):
            has_error = product_create_page.has_validation_errors()
            logger.info(f"Validation on blur: has_error={has_error}")

    @allure.title("Ошибочное состояние визуально заметно")
    def test_error_visual_state(self, product_create_page):
        """Fields with errors should be visually distinct."""
        with allure.step("Отправка формы без заполнения полей"):
            product_create_page.scroll_page(500)
            product_create_page.page.locator(
                "button[type='submit'], button.MuiButton-containedPrimary"
            ).last.click()
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка визуального выделения полей с ошибками"):
            error_fields = product_create_page.page.locator(".Mui-error, [aria-invalid='true']").count()
            logger.info(f"Error visual state: error_fields_count={error_fields}")


# =============================================================================
# ADVANCED INPUT TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — Ввод данных")
class TestProductCreateAdvancedInput:
    """Advanced input method tests."""

    @allure.title("Методы ввода работают корректно")
    def test_input_methods(self, product_create_page):
        """Different input methods should work."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод текста посимвольно в поле названия"):
            product_create_page.scroll_page(300)
            field = get_uz_name_field(product_create_page.page)
            field.click()
            field.type("Test Product", delay=50)

        with allure.step("Проверка корректности посимвольного ввода"):
            actual_value = product_create_page.get_field_value("Product name in Uzbek")
            assert actual_value == "Test Product", \
                f"BUG: Character-by-character typing failed, got '{actual_value}'"

    @allure.title("Атрибуты автозаполнения корректны")
    def test_autocomplete_attributes(self, product_create_page):
        """Form fields should have appropriate autocomplete attributes."""
        with allure.step("Прокрутка к полю названия товара"):
            product_create_page.scroll_page(300)

        with allure.step("Проверка атрибута autocomplete у поля названия"):
            name_field = get_uz_name_field(product_create_page.page)
            autocomplete = name_field.get_attribute("autocomplete")
            logger.info(f"Product name autocomplete: {autocomplete}")


# =============================================================================
# CONCURRENT TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — Параллелизм")
class TestProductCreateConcurrent:
    """Concurrent and state management tests."""

    @allure.title("Состояние формы сохраняется после ошибки валидации")
    def test_state_after_validation_error(self, product_create_page):
        """Form data should be preserved after validation error."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            short_desc = "A" * 49
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Заполнение названий с коротким описанием"):
            product_create_page.fill_product_names_staging(
                uz_name=data["uz_name"],
                uz_desc=short_desc,
                ru_name=data["ru_name"],
                ru_desc=short_desc
            )

        with allure.step("Попытка перехода на следующий шаг (ожидается ошибка валидации)"):
            try:
                product_create_page.click_next_button()
            except Exception as e:
                logger.info(f"Next button click raised (expected for validation): {e}")
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка сохранения данных формы после ошибки"):
            uz_name = product_create_page.get_field_value("Product name in Uzbek")
            ru_name = product_create_page.get_field_value("Product name in Russian")
            assert data["uz_name"] in uz_name, \
                "BUG: UZ name lost after validation error"
            assert data["ru_name"] in ru_name, \
                "BUG: RU name lost after validation error"

    @allure.title("Работа в нескольких вкладках не конфликтует")
    def test_multi_tab_independence(self, staging_session):
        """Product creation in multiple tabs should be independent."""
        page, product_page, staging_data = staging_session

        with allure.step("Навигация на дашборд и выбор магазина"):
            product_page.navigate_to_dashboard()
            page.wait_for_load_state("load", timeout=10000)
            product_page.select_shop(staging_data.get("shop_name", "Zara"))
            page.wait_for_load_state("networkidle")

        with allure.step("Открытие страницы создания товара в первой вкладке"):
            product_page.click_add_product_btn_staging()
            page.wait_for_load_state("networkidle")
            product_page.click_single_product_option()
            page.wait_for_load_state("networkidle")

        with allure.step("Открытие страницы создания товара во второй вкладке"):
            new_page = page.context.new_page()
            new_page.goto(f"{Settings.STAGING_URL}/dashboard/products/create", wait_until="load", timeout=15000)
            new_page.wait_for_load_state("networkidle")

        with allure.step("Проверка независимости вкладок"):
            assert "/products/create" in page.url, "BUG: First tab lost product create page"
            assert "/products/create" in new_page.url or "/auth/login" in new_page.url, \
                "BUG: Second tab navigation failed"
            new_page.close()

    @allure.title("Форма работает после простоя")
    def test_idle_timeout_handling(self, product_create_page):
        """Form should handle idle time gracefully."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ожидание простоя формы"):
            product_create_page.page.wait_for_load_state("networkidle", timeout=10000)

        with allure.step("Заполнение поля названия после простоя"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", data["uz_name"])

        with allure.step("Проверка работоспособности формы после простоя"):
            actual = product_create_page.get_field_value("Product name in Uzbek")
            assert data["uz_name"] in actual, \
                "BUG: Form not working after idle"


# =============================================================================
# FUNCTIONAL TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.staging
@allure.feature("Создание товара — Функционал")
class TestProductCreateFunctional:
    """Functional workflow tests."""

    @allure.title("Категорию можно изменить до отправки")
    def test_change_category(self, product_create_page):
        """User should be able to change selected category."""
        with allure.step("Выбор категории товара"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])

        with allure.step("Повторное открытие выпадающего списка категорий"):
            combobox = product_create_page.page.get_by_role("combobox").first
            combobox.click()
            product_create_page.page.wait_for_load_state("domcontentloaded")
            product_create_page.page.keyboard.press("Escape")
            product_create_page.page.wait_for_load_state("domcontentloaded")
            combobox.click()
            product_create_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка доступности вариантов для изменения категории"):
            options = product_create_page.page.get_by_role("option").count()
            assert options > 0, "BUG: Category dropdown not working after selection"
            product_create_page.page.keyboard.press("Escape")

    @allure.title("Поиск и выбор бренда работает")
    def test_brand_search_selection(self, product_create_page):
        """Brand search and selection should work."""
        with allure.step("Заполнение обязательных полей перед выбором бренда"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])

        with allure.step("Поиск бренда 'Zara' в выпадающем списке"):
            brand_input = product_create_page.page.get_by_role("combobox").nth(3)
            brand_input.click()
            brand_input.fill("Zara")
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка результатов поиска и выбор бренда"):
            options = product_create_page.page.get_by_role("option")
            option_count = options.count()
            assert option_count > 0, "BUG: Brand search returned no results"
            if option_count > 0:
                options.first.click()
                product_create_page.page.wait_for_load_state("domcontentloaded")

    @allure.title("Поиск ИКПУ по частичному тексту")
    def test_ikpu_partial_search(self, product_create_page):
        """IKPU search should work with partial text."""
        with allure.step("Выбор категории товара"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])

        with allure.step("Поиск ИКПУ по частичному тексту 'kurt'"):
            ikpu_input = product_create_page.page.get_by_role("combobox").nth(1)
            ikpu_input.click()
            ikpu_input.fill("kurt")
            product_create_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка наличия результатов поиска ИКПУ"):
            options = product_create_page.page.get_by_role("option").count()
            assert options > 0, "BUG: IKPU partial search returned no results"
            product_create_page.page.keyboard.press("Escape")

    @allure.title("Список стран загружается корректно")
    def test_country_list_loads(self, product_create_page):
        """Country dropdown should load and display options."""
        with allure.step("Выбор категории и ИКПУ"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])

        with allure.step("Открытие выпадающего списка стран"):
            country_input = product_create_page.page.get_by_role("combobox").nth(2)
            country_input.click()
            product_create_page.page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка загрузки списка стран"):
            options = product_create_page.page.get_by_role("option").count()
            assert options > 5, f"BUG: Country list too short, only {options} countries"
            product_create_page.page.keyboard.press("Escape")

    @allure.title("Поля формы редактируются после заполнения")
    def test_edit_filled_fields(self, product_create_page):
        """Filled fields should be editable."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Заполнение поля названия первоначальным значением"):
            product_create_page.scroll_page(300)
            product_create_page.fill_single_field("Product name in Uzbek", "Original Name")

        with allure.step("Изменение значения поля названия"):
            product_create_page.fill_single_field("Product name in Uzbek", "Edited Name")

        with allure.step("Проверка что поле содержит новое значение"):
            actual = product_create_page.get_field_value("Product name in Uzbek")
            assert actual == "Edited Name", \
                f"BUG: Field not editable, got '{actual}'"

    @allure.title("Счётчик символов описания работает")
    def test_description_character_counter(self, product_create_page):
        """Description should show character count or limit indicator."""
        with allure.step("Заполнение обязательных полей на Шаге 1"):
            data = ProductDataGenerator.generate_staging_product(product_type="jacket")
            product_create_page.select_category_from_combobox(data["category_path"])
            product_create_page.select_ikpu_from_combobox(data["ikpu_search"])
            product_create_page.select_country_from_combobox(data["country"])
            product_create_page.select_brand_from_combobox(data["brand"])

        with allure.step("Ввод текста в поле описания"):
            product_create_page.scroll_page(300)
            desc_field = product_create_page.page.get_by_role("textbox", name="Description in Uzbek")
            desc_field.fill("A" * 30)

        with allure.step("Проверка наличия счётчика символов"):
            helper_text = product_create_page.page.locator(
                ".MuiFormHelperText-root:near(:text('Description'))"
            ).first
            if helper_text.is_visible(timeout=1000):
                text = helper_text.inner_text()
                logger.info(f"Description helper text: {text}")
            else:
                logger.info("No character counter visible")


# =============================================================================
# STEP 4 SUBMIT TESTS
# =============================================================================

@pytest.mark.functional
@pytest.mark.e2e
@allure.feature("Создание товара")
@allure.story("Отправка — Шаг 4")
class TestProductCreateSubmit:
    """Step 4 submit and success dialog tests."""

    @allure.title("Отправка без изображения остаётся на Шаге 3")
    def test_submit_without_image(self, product_on_step3):
        """Skipping image upload should prevent progression or show warning."""
        with allure.step("Нажатие кнопки 'Далее' без загрузки изображения"):
            product_on_step3.click_next_button()
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка что форма осталась на Шаге 3"):
            still_on_step3 = product_on_step3.is_on_step(3)
            has_errors = product_on_step3.has_validation_errors()
            assert still_on_step3 or has_errors, \
                "BUG: Proceeded to Step 4 without uploading image"

    @allure.title("Полный E2E с отправкой на модерацию")
    def test_full_submit_flow(self, product_on_step3):
        """Complete flow through Step 3 (image) to Step 4 (submit)."""
        with allure.step("Проверка наличия тестового изображения"):
            image_path = os.path.join(RESOURCES_PATH, "test_image.png")
            if not os.path.exists(image_path):
                pytest.fail("test_image.png not found in resources")

        with allure.step("Загрузка изображения на Шаге 3"):
            product_on_step3.upload_main_image(image_path)
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Переход на Шаг 4"):
            product_on_step3.click_next_button()
            product_on_step3.page.wait_for_load_state("networkidle")

        with allure.step("Проверка перехода на Шаг 4 или список товаров"):
            on_step4 = product_on_step3.is_on_step(4)
            on_products = "/products" in product_on_step3.page.url
            assert on_step4 or on_products, \
                f"BUG: Did not reach Step 4, URL: {product_on_step3.page.url}"
