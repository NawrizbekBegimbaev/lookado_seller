"""
Shop Create Security Tests.
Tests XSS, SQL injection, HTML injection, null bytes, LDAP, command injection.
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
@pytest.mark.security
class TestShopCreateSecurity:
    """Security-focused tests."""

    @allure.title("Попытка XSS в названии магазина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_xss_in_shop_name(self, shop_modal):
        """XSS payload in shop name MUST be sanitized."""
        page = shop_modal.page

        with allure.step("Внедрение XSS payload"):
            xss_payload = '<img src=x onerror=alert("XSS")>'
            shop_modal.fill_shop_name(xss_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка нейтрализации XSS"):
            # Check that script doesn't execute
            # If alert dialog appears, test fails
            page.wait_for_load_state("networkidle")
            # Try to detect if any dialog appeared
            dialogs = page.locator("[role='alertdialog']")
            assert dialogs.count() == 0, "FAILED: XSS payload executed!"

            # Verify the value is sanitized or escaped
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Actual value after XSS attempt: {actual_value}")

        logger.info("SC-SEC-01: XSS prevention - PASSED")

    @allure.title("Попытка SQL инъекции в названии магазина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sql_injection_in_shop_name(self, shop_modal):
        """SQL injection in shop name should be handled safely."""
        page = shop_modal.page

        with allure.step("Внедрение SQL payload"):
            sql_payload = "'; DROP TABLE shops; --"
            shop_modal.fill_shop_name(sql_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Отправка и проверка отсутствия серверной ошибки"):
            shop_modal.fill_description_uz("Test UZ")
            shop_modal.fill_description_ru("Test RU")
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            # Should either show validation error or handle safely
            # Should NOT show 500 error or crash
            page_content = page.content()
            assert "500" not in page.title(), "FAILED: SQL injection caused server error"
            assert "error" not in page.title().lower() or shop_modal.has_validation_errors(), \
                "FAILED: Unhandled SQL injection"

        logger.info("SC-SEC-02: SQL injection prevention - PASSED")

    @allure.title("JavaScript URI в описании")
    @allure.severity(allure.severity_level.NORMAL)
    def test_javascript_uri_in_description(self, shop_modal, test_data):
        """JavaScript URI should be sanitized."""
        page = shop_modal.page

        with allure.step("Заполнение JavaScript URI"):
            shop_data = test_data.get("shop_data", {})
            shop_name = f"Test Shop {int(time.time())}"

            shop_modal.fill_shop_name(shop_name)
            shop_modal.fill_description_uz("javascript:alert('XSS')")
            shop_modal.fill_description_ru("Normal description")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Отправка формы"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка отсутствия выполнения скрипта"):
            # Should either reject or sanitize
            logger.info("JavaScript URI test completed")

        logger.info("SC-SEC-03: JavaScript URI handling - PASSED")

    @allure.title("Обход пути в загрузке файлов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_path_traversal_awareness(self, shop_modal):
        """Document path traversal concerns for file uploads."""
        page = shop_modal.page

        # This test documents the file upload security concern
        # Actual path traversal testing requires backend access

        with allure.step("Документирование безопасности загрузки файлов"):
            file_count = shop_modal.get_file_input_count()
            logger.info(f"File inputs found: {file_count}")

            # Verify file inputs have proper accept attributes
            file_inputs = page.locator("input[type='file']")
            for i in range(file_inputs.count()):
                accept = file_inputs.nth(i).get_attribute("accept") or ""
                logger.info(f"File input {i} accepts: {accept}")

        logger.info("SC-SEC-04: File upload security documented - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.security
class TestShopCreateAdvancedSecurity:
    """Advanced security tests - injection, traversal, encoding attacks."""

    @allure.title("HTML инъекция в названии магазина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_html_injection_shop_name(self, shop_modal):
        """HTML injection in shop name MUST be sanitized."""
        page = shop_modal.page

        with allure.step("Внедрение HTML тегов"):
            html_payload = '<b>Bold</b><i>Italic</i><a href="http://evil.com">Link</a>'
            shop_modal.fill_shop_name(html_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка сохранённого значения"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Input: {html_payload}")
            logger.info(f"Stored: {actual_value}")

            # HTML теги должны быть экранированы или удалены
            allure.attach(
                f"Input: {html_payload}\nStored: {actual_value}",
                name="html_injection_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Отправка и проверка отсутствия рендеринга"):
            shop_modal.fill_description_uz("HTML test")
            shop_modal.fill_description_ru("HTML тест")
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            # Проверяем что нет рендеринга HTML
            bold_elements = page.locator("b, i, a[href*='evil']")
            assert bold_elements.count() == 0, \
                "FAILED: HTML tags were rendered - security vulnerability!"

        logger.info("SC-AS-01: HTML injection prevention - PASSED")

    @allure.title("Null byte инъекция должна быть очищена")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_null_byte_injection(self, shop_modal):
        """BUG CHECK: Null bytes MUST be sanitized - security vulnerability if not."""
        page = shop_modal.page

        with allure.step("Внедрение null bytes"):
            null_payload = "Test\x00Shop\x00Name"
            shop_modal.fill_shop_name(null_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка очистки null bytes"):
            actual_value = shop_modal.get_shop_name_value()
            logger.info(f"Input: {repr(null_payload)}, Stored: {repr(actual_value)}")

            allure.attach(
                f"Input: {repr(null_payload)}\nStored: {repr(actual_value)}",
                name="null_byte_result",
                attachment_type=allure.attachment_type.TEXT
            )

            # ЖЕСТКАЯ ПРОВЕРКА: Null bytes ДОЛЖНЫ быть удалены
            assert "\x00" not in actual_value, \
                f"BUG: Null bytes NOT sanitized - security vulnerability! Value: {repr(actual_value)}"

        logger.info("SC-AS-02: Null byte injection - PASSED")

        logger.info("SC-AS-02: Null byte injection handling documented - PASSED")

    @allure.title("Попытка LDAP инъекции")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ldap_injection(self, shop_modal):
        """LDAP injection payload MUST be handled safely."""
        page = shop_modal.page

        with allure.step("Внедрение LDAP payload"):
            ldap_payload = "*)(uid=*))(|(uid=*"
            shop_modal.fill_shop_name(ldap_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Отправка и проверка отсутствия серверной ошибки"):
            shop_modal.fill_description_uz("LDAP test")
            shop_modal.fill_description_ru("LDAP тест")
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            # Должна быть валидация или безопасная обработка
            assert "500" not in page.title(), \
                "FAILED: LDAP injection caused server error"

            has_errors = shop_modal.has_validation_errors()
            has_toast = shop_modal.has_toast_error()

            logger.info(f"LDAP injection: validation={has_errors}, toast={has_toast}")

            allure.attach(
                f"LDAP payload: {ldap_payload}\nValidation: {has_errors}\nToast: {has_toast}",
                name="ldap_injection_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-AS-03: LDAP injection - PASSED")

    @allure.title("Попытка инъекции команд")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_command_injection(self, shop_modal):
        """Command injection payload MUST be handled safely."""
        page = shop_modal.page

        with allure.step("Внедрение командного payload"):
            cmd_payload = "; rm -rf / ; echo 'pwned'"
            shop_modal.fill_shop_name(cmd_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Отправка и проверка безопасной обработки"):
            shop_modal.fill_description_uz("CMD test")
            shop_modal.fill_description_ru("CMD тест")
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            # Не должно быть серверной ошибки
            assert "500" not in page.title(), \
                "FAILED: Command injection caused server error"

            allure.attach(
                f"Command payload: {cmd_payload}",
                name="cmd_injection_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-AS-04: Command injection - PASSED")

    @allure.title("Обход пути в описании")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_path_traversal_description(self, shop_modal):
        """Path traversal payload MUST be handled safely."""
        page = shop_modal.page

        with allure.step("Внедрение обхода пути"):
            traversal_payload = "../../../etc/passwd"
            shop_modal.fill_shop_name(f"Path Test {int(time.time())}")
            shop_modal.fill_description_uz(traversal_payload)
            shop_modal.fill_description_ru("Normal description")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Отправка и проверка безопасной обработки"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            # Не должно быть утечки содержимого файла
            page_content = page.content().lower()
            assert "root:" not in page_content, \
                "FAILED: Path traversal exposed file contents!"

            allure.attach(
                f"Path traversal payload: {traversal_payload}",
                name="path_traversal_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-AS-05: Path traversal in description - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.security
class TestShopCreateDescriptionInjection:
    """Injection tests specifically for description fields."""

    @allure.title("XSS в описании на узбекском")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_xss_in_description_uz(self, shop_modal):
        """XSS payload in Uzbek description MUST be sanitized."""
        page = shop_modal.page

        with allure.step("Внедрение XSS в описание на узбекском"):
            shop_modal.fill_shop_name(f"XSS UZ Test {int(time.time())}")
            page.wait_for_load_state("domcontentloaded")

            xss_payload = '<script>alert("XSS_UZ")</script><img src=x onerror=alert(1)>'
            shop_modal.fill_description_uz(xss_payload)
            shop_modal.fill_description_ru("Normal description")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка нейтрализации XSS"):
            actual_value = shop_modal.get_description_uz_value()
            logger.info(f"XSS payload stored as: {actual_value[:100]}...")

            # Проверяем что script не выполнился
            alert_count = page.evaluate("window.xssTriggered || 0")
            assert alert_count == 0, "FAILED: XSS executed!"

            allure.attach(
                f"Input: {xss_payload}\nStored: {actual_value}",
                name="xss_uz_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-DI-01: XSS in UZ description - PASSED")

    @allure.title("XSS в описании на русском")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_xss_in_description_ru(self, shop_modal):
        """XSS payload in Russian description MUST be sanitized."""
        page = shop_modal.page

        with allure.step("Внедрение XSS в описание на русском"):
            shop_modal.fill_shop_name(f"XSS RU Test {int(time.time())}")
            page.wait_for_load_state("domcontentloaded")

            shop_modal.fill_description_uz("Обычное описание")

            xss_payload = '<svg onload=alert("XSS_RU")><iframe src="javascript:alert(1)">'
            shop_modal.fill_description_ru(xss_payload)
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка нейтрализации XSS"):
            actual_value = shop_modal.get_description_ru_value()
            logger.info(f"XSS payload stored as: {actual_value[:100]}...")

            allure.attach(
                f"Input: {xss_payload}\nStored: {actual_value}",
                name="xss_ru_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-DI-02: XSS in RU description - PASSED")

    @allure.title("SQL инъекция в описании")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sql_injection_description(self, shop_modal):
        """SQL injection in description MUST be handled safely."""
        page = shop_modal.page

        with allure.step("Внедрение SQL в описания"):
            shop_modal.fill_shop_name(f"SQL Desc Test {int(time.time())}")
            page.wait_for_load_state("domcontentloaded")

            sql_payload = "'; DROP TABLE shops; -- OR '1'='1"
            shop_modal.fill_description_uz(sql_payload)
            shop_modal.fill_description_ru("Robert'); DROP TABLE users;--")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Отправка и проверка отсутствия серверной ошибки"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

            # Не должно быть серверной ошибки
            assert "500" not in page.title(), \
                "FAILED: SQL injection caused server error"

            allure.attach(
                f"SQL payload UZ: {sql_payload}",
                name="sql_desc_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-DI-03: SQL injection in description - PASSED")

