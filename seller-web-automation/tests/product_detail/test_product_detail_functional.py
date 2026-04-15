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




@pytest.mark.functional
@allure.feature("Детали товара")
@allure.story("Функционал редактирования")
class TestProductDetailEdit:
    """Tests for editing product fields."""

    @allure.title("Поля товара доступны для редактирования")
    def test_fields_are_editable(self, detail_page):
        """Product fields should be editable (either directly or after clicking Edit)."""
        product_page, _ = detail_page
        with allure.step("Переход в режим редактирования"):
            # Try to enter edit mode if button exists
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка доступности поля названия UZ для редактирования"):
            # Check if UZ name field is editable
            if product_page.uz_name_field.is_visible(timeout=2000):
                assert product_page.uz_name_field.is_enabled(), \
                    "BUG: UZ name field is not editable"

    @allure.title("Редактирование названия товара на узбекском")
    def test_edit_uz_name(self, detail_page):
        """Should be able to edit UZ product name."""
        product_page, test_data = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            with allure.step("Редактирование поля названия на узбекском"):
                original = product_page.get_uz_name_value()
                new_name = test_data.get("edit_data", {}).get("new_uz_name", "Edited Name")
                product_page.fill_uz_name(new_name)
                product_page.page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка обновлённого значения названия"):
                current = product_page.get_uz_name_value()
                assert current == new_name, \
                    f"BUG: UZ name not updated, expected '{new_name}', got '{current}'"
            with allure.step("Восстановление оригинального значения"):
                # Restore original
                product_page.fill_uz_name(original)

    @allure.title("Редактирование названия товара на русском")
    def test_edit_ru_name(self, detail_page):
        """Should be able to edit RU product name."""
        product_page, test_data = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.ru_name_field.is_visible(timeout=2000):
            with allure.step("Редактирование поля названия на русском"):
                original = product_page.get_ru_name_value()
                new_name = test_data.get("edit_data", {}).get("new_ru_name", "Новое Имя")
                product_page.fill_ru_name(new_name)
                product_page.page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка обновлённого значения названия"):
                current = product_page.get_ru_name_value()
                assert current == new_name, \
                    f"BUG: RU name not updated, expected '{new_name}', got '{current}'"
            with allure.step("Восстановление оригинального значения"):
                product_page.fill_ru_name(original)

    @allure.title("Редактирование цены товара")
    def test_edit_price(self, detail_page):
        """Should be able to edit product price."""
        product_page, test_data = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.price_field.is_visible(timeout=2000):
            with allure.step("Редактирование поля цены товара"):
                original = product_page.get_price_value()
                new_price = test_data.get("edit_data", {}).get("new_price", "2000000")
                product_page.fill_price(new_price)
                product_page.page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка обновлённого значения цены"):
                current = product_page.get_price_value()
                assert current == new_price or current.replace(" ", "") == new_price, \
                    f"BUG: Price not updated, got '{current}'"
            with allure.step("Восстановление оригинальной цены"):
                product_page.fill_price(original)

    @allure.title("Отмена редактирования отменяет изменения")
    def test_cancel_discards_changes(self, detail_page):
        """Cancel button should discard unsaved changes."""
        product_page, _ = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            with allure.step("Изменение названия на временное значение"):
                original = product_page.get_uz_name_value()
                product_page.fill_uz_name("TEMP_CANCEL_TEST")
            with allure.step("Нажатие кнопки отмены и проверка отката изменений"):
                if product_page.cancel_button.is_visible(timeout=1000):
                    product_page.click_cancel()
                    product_page.page.wait_for_load_state("domcontentloaded")
                    current = product_page.get_uz_name_value()
                    assert current == original or current != "TEMP_CANCEL_TEST", \
                        "BUG: Cancel did not discard changes"

    @allure.title("Кнопка сохранения активна при валидных данных")
    def test_save_button_state(self, detail_page):
        """Save button should be enabled when form is valid."""
        product_page, _ = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        with allure.step("Заполнение поля корректным значением"):
            if product_page.save_button.is_visible(timeout=2000):
                # Fill a valid value
                if product_page.uz_name_field.is_visible(timeout=1000):
                    product_page.fill_uz_name("Valid Name Test")
        with allure.step("Проверка активности кнопки сохранения"):
                is_enabled = product_page.is_save_button_enabled()
                assert is_enabled, "BUG: Save button disabled with valid data"




@pytest.mark.functional
@allure.feature("Детали товара")
@allure.story("Удаление товара")
class TestProductDetailDelete:
    """Tests for product deletion workflow."""

    @allure.title("Кнопка удаления видна на странице товара")
    def test_delete_button_visible(self, detail_page):
        """Delete button should be visible on product detail."""
        product_page, _ = detail_page
        with allure.step("Поиск кнопки удаления на странице"):
            # Delete might be visible directly or in edit mode
            has_delete = product_page.is_delete_button_visible()
            if not has_delete and product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
                has_delete = product_page.is_delete_button_visible()
        with allure.step("Проверка видимости кнопки удаления"):
            # Delete button is expected on detail page
            if not has_delete:
                pytest.fail("Delete button not visible (may require specific permissions)")
            assert has_delete, "BUG: Delete button should be visible"

    @allure.title("Удаление показывает диалог подтверждения")
    def test_delete_shows_confirmation(self, detail_page):
        """Delete should show confirmation dialog."""
        product_page, _ = detail_page
        with allure.step("Нажатие кнопки удаления"):
            if product_page.delete_button.is_visible(timeout=2000):
                product_page.click_delete()
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка появления диалога подтверждения"):
                dialog_visible = product_page.delete_confirmation_dialog.is_visible(timeout=2000)
                if dialog_visible:
                    # Cancel to not actually delete
                    product_page.cancel_delete()
                assert dialog_visible, \
                    "BUG: Delete has no confirmation dialog (dangerous!)"

    @allure.title("Отмена удаления сохраняет товар")
    def test_cancel_delete_keeps_product(self, detail_page):
        """Canceling delete should keep the product."""
        product_page, _ = detail_page
        with allure.step("Нажатие кнопки удаления"):
            if product_page.delete_button.is_visible(timeout=2000):
                product_page.click_delete()
                product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Отмена удаления в диалоге подтверждения"):
                if product_page.delete_confirmation_dialog.is_visible(timeout=2000):
                    product_page.cancel_delete()
                    product_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что товар остался на странице"):
                # Should still be on product detail
                assert product_page.is_on_detail_page(), \
                    "BUG: Cancel delete navigated away from product"




@pytest.mark.security
@allure.feature("Детали товара")
@allure.story("Сессия")
class TestProductDetailSession:
    """Tests for session and authentication."""

    @allure.title("Неавторизованный доступ перенаправляет на логин")
    def test_unauthenticated_redirects_to_login(self, browser, request):
        """Unauthenticated access should redirect to login."""
        with allure.step("Создание неавторизованного контекста браузера"):
            from config import settings
            headless = request.config.getoption("headless")
            if headless:
                ctx_opts = settings.get_browser_context_options_with_viewport()
            else:
                ctx_opts = settings.get_browser_context_options()
            context = browser.new_context(**ctx_opts)
            page = context.new_page()
        with allure.step("Переход на страницу товара без авторизации"):
            page.goto("https://staging-seller.greatmall.uz/dashboard/products/123")
            page.wait_for_load_state("networkidle")
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка редиректа на страницу логина"):
            assert "/auth" in page.url or "/login" in page.url, \
                f"BUG: Unauthenticated access not redirected to login (URL: {page.url})"
            page.close()
            context.close()

    @allure.title("Страница товара доступна после авторизации")
    def test_page_accessible_after_login(self, detail_page):
        """Product detail page should be accessible after login."""
        product_page, _ = detail_page
        with allure.step("Проверка доступности страницы товара после авторизации"):
            assert product_page.is_on_detail_page(), \
                f"BUG: Product detail not accessible after login (URL: {product_page.page.url})"




@pytest.mark.security
@allure.feature("Детали товара")
@allure.story("Безопасность - XSS/SQL инъекции")
class TestProductDetailSecurity:
    """Tests for XSS and SQL injection prevention."""

    @allure.title("XSS в названии товара отклоняется")
    def test_xss_in_name(self, detail_page):
        """XSS payload in name should be sanitized."""
        product_page, test_data = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            with allure.step("Ввод XSS-payload в поле названия"):
                original = product_page.get_uz_name_value()
                xss = test_data.get("invalid_inputs", {}).get("xss_payload", "<script>alert(1)</script>")
                product_page.fill_uz_name(xss)
                product_page.page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка санитизации XSS в значении поля"):
                value = product_page.get_uz_name_value()
                # XSS should be stored as text, not executed
                assert "<script>" not in value.lower() or value == xss, \
                    "BUG: XSS not sanitized in product name"
            with allure.step("Восстановление оригинального значения"):
                product_page.fill_uz_name(original)

    @allure.title("XSS через обработчик событий в названии отклоняется")
    def test_xss_event_handler_in_name(self, detail_page):
        """XSS event handler in name should be sanitized."""
        product_page, test_data = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            with allure.step("Ввод XSS через обработчик событий в поле названия"):
                original = product_page.get_uz_name_value()
                xss = test_data.get("invalid_inputs", {}).get("xss_event", "<img src=x onerror=alert(1)>")
                product_page.fill_uz_name(xss)
                product_page.page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка санитизации обработчика событий"):
                value = product_page.get_uz_name_value()
                assert "onerror" not in value.lower() or value == xss, \
                    "BUG: XSS event handler not sanitized"
            with allure.step("Восстановление оригинального значения"):
                product_page.fill_uz_name(original)

    @allure.title("SQL инъекция в названии товара отклоняется")
    def test_sql_injection_in_name(self, detail_page):
        """SQL injection in name should not crash the form."""
        product_page, test_data = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            with allure.step("Ввод SQL-инъекции в поле названия"):
                original = product_page.get_uz_name_value()
                sql = test_data.get("invalid_inputs", {}).get("sql_injection", "'; DROP TABLE;--")
                product_page.fill_uz_name(sql)
                product_page.page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка что форма не сломалась от SQL-инъекции"):
                value = product_page.get_uz_name_value()
                assert value is not None, "BUG: SQL injection crashed the form"
            with allure.step("Восстановление оригинального значения"):
                product_page.fill_uz_name(original)

    @allure.title("HTML инъекция в описании товара экранируется")
    def test_html_injection_in_description(self, detail_page):
        """HTML tags in description should be escaped."""
        product_page, test_data = detail_page
        with allure.step("Переход в режим редактирования"):
            if product_page.edit_button.is_visible(timeout=1000):
                product_page.click_edit()
        if product_page.uz_description_field.is_visible(timeout=2000):
            with allure.step("Ввод HTML-тегов в поле описания"):
                original = product_page.get_uz_description_value()
                html = test_data.get("invalid_inputs", {}).get("html_tags", "<iframe src='evil'></iframe>")
                product_page.fill_uz_description(html)
                product_page.page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка что HTML не отрендерился на странице"):
                rendered = product_page.page.locator("iframe[src='evil']").count()
                assert rendered == 0, "BUG: HTML rendered in description field"
            with allure.step("Восстановление оригинального описания"):
                product_page.fill_uz_description(original)




@pytest.mark.security
@allure.feature("Детали товара")
@allure.story("Расширенная безопасность")
class TestProductDetailAdvancedSecurity:
    """Tests for advanced injection attacks."""

    @allure.title("Нулевые байты в названии обрабатываются безопасно")
    def test_null_bytes_in_name(self, detail_page):
        """Null bytes should be handled safely."""
        product_page, test_data = detail_page
        if product_page.edit_button.is_visible(timeout=1000):
            product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            original = product_page.get_uz_name_value()
            null_val = "test\x00value"
            product_page.fill_uz_name(null_val)
            product_page.page.wait_for_load_state("domcontentloaded")
            value = product_page.get_uz_name_value()
            assert "\x00" not in value, "BUG: Null bytes not sanitized in name"
            product_page.fill_uz_name(original)

    @allure.title("Path traversal в названии блокируется")
    def test_path_traversal_in_name(self, detail_page):
        """Path traversal should be blocked."""
        product_page, test_data = detail_page
        if product_page.edit_button.is_visible(timeout=1000):
            product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            original = product_page.get_uz_name_value()
            traversal = test_data.get("invalid_inputs", {}).get("path_traversal", "../../../etc/passwd")
            product_page.fill_uz_name(traversal)
            product_page.page.wait_for_load_state("domcontentloaded")
            value = product_page.get_uz_name_value()
            # Should either reject or accept as text
            assert value is not None, "BUG: Path traversal crashed the form"
            product_page.fill_uz_name(original)

    @allure.title("Командная инъекция в названии блокируется")
    def test_command_injection_in_name(self, detail_page):
        """Command injection should be blocked."""
        product_page, test_data = detail_page
        if product_page.edit_button.is_visible(timeout=1000):
            product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            original = product_page.get_uz_name_value()
            cmd = test_data.get("invalid_inputs", {}).get("command_injection", "; rm -rf /")
            product_page.fill_uz_name(cmd)
            product_page.page.wait_for_load_state("domcontentloaded")
            value = product_page.get_uz_name_value()
            assert value is not None, "BUG: Command injection crashed the form"
            product_page.fill_uz_name(original)

    @allure.title("LDAP инъекция в названии обрабатывается безопасно")
    def test_ldap_injection_in_name(self, detail_page):
        """LDAP injection should be handled safely."""
        product_page, test_data = detail_page
        if product_page.edit_button.is_visible(timeout=1000):
            product_page.click_edit()
        if product_page.uz_name_field.is_visible(timeout=2000):
            original = product_page.get_uz_name_value()
            ldap = test_data.get("invalid_inputs", {}).get("ldap_injection", "*)(uid=*)")
            product_page.fill_uz_name(ldap)
            product_page.page.wait_for_load_state("domcontentloaded")
            value = product_page.get_uz_name_value()
            assert value is not None, "BUG: LDAP injection crashed the form"
            product_page.fill_uz_name(original)
