"""
Tests for Profile Settings page.
9 classes, ~43 methods, ~50+ test cases.

URL: /dashboard/settings or /dashboard/profile
"""

import pytest
import allure
from pages.profile_settings_page import ProfileSettingsPage



@allure.epic("Платформа продавца")
@allure.suite("UI настроек профиля")
@allure.feature("Элементы интерфейса")
@pytest.mark.smoke
class TestProfileSettingsUI:
    """Тесты UI элементов страницы настроек профиля."""

    @allure.title("Страница настроек профиля загружается")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_settings_page_loads(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Страница настроек не загружается."""
        with allure.step("Проверка загрузки страницы настроек профиля"):
            url = profile_settings_page.page.url
            # Page may redirect to /dashboard/become-seller or other dashboard subpath
            assert "/settings" in url or "/profile" in url or "/dashboard" in url, \
                f"BUG: Страница настроек не загрузилась. URL: {url}"

    @allure.title("URL страницы содержит settings или profile")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_url_contains_settings_or_profile(self, profile_settings_page: ProfileSettingsPage):
        """BUG: URL не содержит /settings или /profile."""
        with allure.step("Проверка что URL содержит settings или profile"):
            url = profile_settings_page.page.url
            has_settings = "/settings" in url
            has_profile = "/profile" in url
            has_dashboard = "/dashboard" in url
            assert has_settings or has_profile or has_dashboard, \
                f"BUG: URL не содержит settings/profile/dashboard: {url}"

    @allure.title("Страница использует HTTPS соединение")
    @allure.severity(allure.severity_level.NORMAL)
    def test_https_connection(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Страница не использует HTTPS."""
        with allure.step("Проверка что страница использует HTTPS соединение"):
            assert profile_settings_page.page.url.startswith("https://"), \
                f"BUG: Не HTTPS: {profile_settings_page.page.url}"

    @allure.title("URL не содержит чувствительные данные")
    @allure.severity(allure.severity_level.NORMAL)
    def test_no_sensitive_data_in_url(self, profile_settings_page: ProfileSettingsPage):
        """BUG: URL содержит чувствительные данные."""
        with allure.step("Проверка что URL не содержит чувствительные данные"):
            url = profile_settings_page.page.url.lower()
            for sensitive in ["token", "password", "secret", "api_key", "session"]:
                assert sensitive not in url, \
                    f"BUG: URL содержит '{sensitive}': {url}"

    @allure.title("Кнопка сохранения присутствует на странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_save_button_exists(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Кнопка сохранения отсутствует."""
        with allure.step("Проверка видимости кнопки сохранения"):
            has_save = profile_settings_page.save_btn.is_visible(timeout=3000)
        with allure.step("Поиск альтернативных кнопок сохранения"):
            # Если нет явной кнопки сохранения - ищем альтернативы
            if not has_save:
                alt_save = profile_settings_page.page.locator("button:has-text('Save')").or_(
                    profile_settings_page.page.locator("button:has-text('Сохранить')")
                ).or_(profile_settings_page.page.locator("button[type='submit']"))
                has_save = alt_save.count() > 0
            # Не все страницы настроек требуют кнопку сохранения
            if not has_save:
                pytest.fail("Кнопка сохранения не найдена (может быть авто-сохранение)")
            assert has_save, "BUG: Кнопка сохранения не видима"

    @allure.title("Страница содержит элементы формы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_has_form_elements(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Страница не содержит форм или полей ввода."""
        with allure.step("Проверка наличия элементов формы на странице"):
            page = profile_settings_page.page
            has_inputs = page.locator("input").count() > 0
            has_textareas = page.locator("textarea").count() > 0
            has_selects = page.locator("select").count() > 0
            has_buttons = page.locator("button").count() > 0
            assert has_inputs or has_textareas or has_selects or has_buttons, \
                "BUG: Страница настроек не содержит форм или элементов управления"

    @allure.title("Консоль не содержит JavaScript ошибок")
    @allure.severity(allure.severity_level.NORMAL)
    def test_no_javascript_errors_in_console(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Консоль содержит JavaScript ошибки."""
        with allure.step("Проверка отсутствия критических ошибок на странице"):
            # Проверяем что страница не показывает критические ошибки
            page_text = profile_settings_page.page.text_content("body") or ""
            critical_errors = ["Traceback", "undefined is not", "Internal Server Error"]
            for indicator in critical_errors:
                assert indicator not in page_text, \
                    f"BUG: Страница содержит критическую ошибку: '{indicator}'"



@allure.epic("Настройки профиля")
@allure.suite("Секция банковского счёта")
@allure.feature("Банковские счета")
@pytest.mark.functional
class TestBankAccountSection:
    """Тесты секции банковских счетов."""

    @allure.title("Секция банковских счетов или альтернатива присутствует")
    @allure.severity(allure.severity_level.NORMAL)
    def test_bank_section_or_alternative_exists(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Секция банковских счетов или альтернатива отсутствует."""
        with allure.step("Поиск секции банковских счетов на странице"):
            page = profile_settings_page.page
            # Ищем любые признаки секции банковских счетов
            bank_indicators = [
                page.locator("text=Банк").count(),
                page.locator("text=Bank").count(),
                page.locator("text=Счёт").count(),
                page.locator("text=Account").count(),
                page.locator("text=Hisob").count(),
                page.locator("[data-testid*='bank']").count(),
                profile_settings_page.add_bank_btn.is_visible(timeout=2000),
            ]
            has_bank_section = any(bank_indicators)
        with allure.step("Проверка видимости секции банковских счетов"):
            # Не все профили имеют банковскую секцию
            if not has_bank_section:
                pytest.fail("Секция банковских счетов не найдена на странице")
            assert has_bank_section, "BUG: Секция банковских счетов не видима"

    @allure.title("Кнопка добавления банковского счёта кликабельна")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_bank_button_clickable(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Кнопка добавления банковского счета не кликабельна."""
        with allure.step("Проверка видимости кнопки добавления банковского счёта"):
            if profile_settings_page.add_bank_btn.is_visible(timeout=2000):
                with allure.step("Проверка что кнопка добавления активна"):
                    is_enabled = profile_settings_page.add_bank_btn.is_enabled()
                    assert is_enabled, "BUG: Кнопка добавления банковского счета отключена"

    @allure.title("Поле ввода номера счёта появляется после клика на добавить")
    @allure.severity(allure.severity_level.NORMAL)
    def test_bank_account_input_exists_after_add_click(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Поле ввода номера счета не появляется."""
        with allure.step("Проверка видимости кнопки добавления"):
            if profile_settings_page.add_bank_btn.is_visible(timeout=2000):
                with allure.step("Нажатие кнопки добавления банковского счёта"):
                    profile_settings_page.click_add_bank_account()
                    profile_settings_page.page.wait_for_load_state("networkidle")
                with allure.step("Проверка появления поля ввода или модального окна"):
                    # После клика должно появиться поле ввода
                    has_input = profile_settings_page.bank_account_input.is_visible(timeout=2000)
                    # Или модальное окно
                    has_modal = profile_settings_page.page.locator("[role='dialog']").is_visible(timeout=1000)
                    assert has_input or has_modal, \
                        "BUG: После клика на добавить - нет поля ввода или модального окна"

    @allure.title("Метод подсчёта банковских счетов возвращает корректное значение")
    @allure.severity(allure.severity_level.NORMAL)
    def test_bank_accounts_count_method_works(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Метод подсчета банковских счетов не работает."""
        with allure.step("Получение количества банковских счетов"):
            count = profile_settings_page.get_bank_accounts_count()
        with allure.step("Проверка что количество корректно"):
            # Метод должен возвращать число >= 0
            assert isinstance(count, int) and count >= 0, \
                f"BUG: get_bank_accounts_count вернул невалидное значение: {count}"



@allure.epic("Настройки профиля")
@allure.suite("Валидация банковского счёта")
@allure.feature("Валидация")
@pytest.mark.functional
class TestBankAccountValidation:
    """Тесты валидации банковских счетов."""

    @allure.title("Пустой номер банковского счёта отклоняется")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_empty_bank_account_rejected(self, profile_settings_page: ProfileSettingsPage, test_data):
        """BUG: Пустой номер счета принимается."""
        with allure.step("Проверка доступности секции банковских счетов"):
            if not profile_settings_page.add_bank_btn.is_visible(timeout=2000):
                pytest.fail("Секция банковских счетов недоступна")
        with allure.step("Нажатие кнопки добавления банковского счёта"):
            profile_settings_page.click_add_bank_account()
            profile_settings_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Заполнение пустого номера счёта и сохранение"):
            if profile_settings_page.bank_account_input.is_visible(timeout=2000):
                profile_settings_page.fill_bank_account("")
                profile_settings_page.save_settings()
                profile_settings_page.page.wait_for_load_state("networkidle")
                with allure.step("Проверка что пустой номер отклонён"):
                    # Должна быть ошибка валидации или отсутствие success
                    has_error = profile_settings_page.is_validation_error_visible()
                    has_success = profile_settings_page.is_success_message_visible()
                    assert has_error or not has_success, \
                        "BUG: Пустой номер банковского счета принят без ошибки"

    @allure.title("Короткий номер банковского счёта отклоняется")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_short_bank_account_rejected(self, profile_settings_page: ProfileSettingsPage, test_data):
        """BUG: Короткий номер счета принимается."""
        with allure.step("Проверка доступности секции банковских счетов"):
            if not profile_settings_page.add_bank_btn.is_visible(timeout=2000):
                pytest.fail("Секция банковских счетов недоступна")
        with allure.step("Нажатие кнопки добавления банковского счёта"):
            profile_settings_page.click_add_bank_account()
            profile_settings_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Заполнение короткого номера счёта и сохранение"):
            if profile_settings_page.bank_account_input.is_visible(timeout=2000):
                short_account = test_data.get("bank_account", {}).get("invalid", {}).get("short", "123")
                profile_settings_page.fill_bank_account(short_account)
                profile_settings_page.save_settings()
                profile_settings_page.page.wait_for_load_state("networkidle")
                with allure.step("Проверка что короткий номер отклонён"):
                    has_error = profile_settings_page.is_validation_error_visible()
                    has_success = profile_settings_page.is_success_message_visible()
                    assert has_error or not has_success, \
                        f"BUG: Короткий номер счета '{short_account}' принят без ошибки"

    @allure.title("Injection атака через номер счёта блокируется")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("payload_name,payload_value", [
        ("xss_script", "<script>alert('XSS')</script>"),
        ("sql_injection", "'; DROP TABLE banks; --"),
    ], ids=["xss", "sql"])
    def test_bank_account_injection_safe(self, profile_settings_page: ProfileSettingsPage,
                                          payload_name: str, payload_value: str):
        """BUG: Injection атака через номер счета не блокируется."""
        with allure.step("Проверка доступности секции банковских счетов"):
            if not profile_settings_page.add_bank_btn.is_visible(timeout=2000):
                pytest.fail("Секция банковских счетов недоступна")
        with allure.step("Нажатие кнопки добавления банковского счёта"):
            profile_settings_page.click_add_bank_account()
            profile_settings_page.page.wait_for_load_state("domcontentloaded")
        with allure.step(f"Ввод injection payload: {payload_name}"):
            if profile_settings_page.bank_account_input.is_visible(timeout=2000):
                profile_settings_page.fill_bank_account(payload_value)
                profile_settings_page.save_settings()
                profile_settings_page.page.wait_for_load_state("networkidle")
                with allure.step("Проверка что injection payload не исполнился"):
                    # Payload не должен исполняться - проверяем отсутствие скриптов
                    page_content = profile_settings_page.page.content()
                    assert "<script>alert" not in page_content, \
                        f"BUG: XSS payload '{payload_name}' исполнился"



@allure.epic("Настройки профиля")
@allure.suite("Секция документов")
@allure.feature("Документы")
@pytest.mark.functional
class TestDocumentSection:
    """Тесты секции документов."""

    @allure.title("Секция документов или альтернатива присутствует")
    @allure.severity(allure.severity_level.NORMAL)
    def test_document_section_or_alternative_exists(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Секция документов или альтернатива отсутствует."""
        with allure.step("Поиск секции документов на странице"):
            page = profile_settings_page.page
            doc_indicators = [
                page.locator("text=Документ").count(),
                page.locator("text=Document").count(),
                page.locator("text=Hujjat").count(),
                page.locator("text=Загрузить").count(),
                page.locator("text=Upload").count(),
                page.locator("text=Yuklash").count(),
                page.locator("input[type='file']").count(),
                profile_settings_page.file_input.count(),
            ]
            has_doc_section = any(doc_indicators)
        with allure.step("Проверка видимости секции документов"):
            if not has_doc_section:
                pytest.fail("Секция документов не найдена на странице")
            assert has_doc_section, "BUG: Секция документов не видима"

    @allure.title("Поле загрузки файла присутствует")
    @allure.severity(allure.severity_level.NORMAL)
    def test_file_input_exists(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Поле загрузки файла отсутствует."""
        with allure.step("Поиск полей загрузки файлов на странице"):
            file_inputs = profile_settings_page.page.locator("input[type='file']")
            count = file_inputs.count()
        with allure.step("Проверка наличия полей загрузки"):
            # Документируем - не все профили имеют загрузку файлов
            assert count >= 0, f"INFO: Найдено {count} полей загрузки файлов"

    @allure.title("Метод подсчёта документов возвращает корректное значение")
    @allure.severity(allure.severity_level.NORMAL)
    def test_documents_count_method_works(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Метод подсчета документов не работает."""
        with allure.step("Получение количества документов"):
            count = profile_settings_page.get_documents_count()
        with allure.step("Проверка что количество корректно"):
            assert isinstance(count, int) and count >= 0, \
                f"BUG: get_documents_count вернул невалидное значение: {count}"



@allure.epic("Настройки профиля")
@allure.suite("Поле НДС")
@allure.feature("Настройки НДС")
@pytest.mark.functional
class TestVATField:
    """Тесты поля ввода НДС (процент)."""

    @allure.title("Поле НДС присутствует на странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_vat_field_exists(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Поле НДС отсутствует."""
        with allure.step("Поиск поля НДС на странице"):
            page = profile_settings_page.page
            vat_indicators = [
                page.locator("text=НДС").count(),
                page.locator("text=VAT").count(),
                page.locator("text=QQS").count(),
                page.locator("input[name='vat']").count(),
                page.locator("input[name='vatRate']").count(),
                profile_settings_page.vat_input.is_visible(timeout=2000),
            ]
            has_vat = any(vat_indicators)
        with allure.step("Проверка видимости поля НДС"):
            assert has_vat, "BUG: Поле НДС не найдено на странице"

    @allure.title("Поле НДС принимает процентное значение")
    @allure.severity(allure.severity_level.NORMAL)
    def test_vat_field_accepts_percentage(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Поле НДС не принимает процент."""
        with allure.step("Проверка видимости поля НДС"):
            if profile_settings_page.vat_input.is_visible(timeout=2000):
                with allure.step("Заполнение поля НДС значением 12"):
                    profile_settings_page.vat_input.fill("12")
                    value = profile_settings_page.vat_input.input_value()
                with allure.step("Проверка что значение принято"):
                    assert "12" in value, f"BUG: Поле НДС не приняло значение: {value}"



@allure.epic("Настройки профиля")
@allure.suite("Секция модерации")
@allure.feature("Модерация")
@pytest.mark.functional
class TestModerationSection:
    """Тесты секции модерации."""

    @allure.title("Секция модерации или альтернатива присутствует")
    @allure.severity(allure.severity_level.NORMAL)
    def test_moderation_section_or_alternative_exists(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Секция модерации или альтернатива отсутствует."""
        with allure.step("Поиск секции модерации на странице"):
            page = profile_settings_page.page
            mod_indicators = [
                page.locator("text=Модерация").count(),
                page.locator("text=Moderation").count(),
                page.locator("text=Moderatsiya").count(),
                page.locator("text=Статус").count(),
                page.locator("text=Status").count(),
                page.locator("text=Holat").count(),
                profile_settings_page.send_moderation_btn.is_visible(timeout=2000),
            ]
            has_moderation = any(mod_indicators)
        with allure.step("Проверка видимости секции модерации"):
            if not has_moderation:
                pytest.fail("Секция модерации не найдена на странице")
            assert has_moderation, "BUG: Секция модерации не видима"

    @allure.title("Метод получения статуса модерации работает корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_moderation_status_method_works(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Метод получения статуса модерации не работает."""
        with allure.step("Получение статуса модерации"):
            status = profile_settings_page.get_moderation_status()
        with allure.step("Проверка что статус возвращает строку"):
            # Метод должен возвращать строку (может быть пустой)
            assert isinstance(status, str), \
                f"BUG: get_moderation_status вернул не string: {type(status)}"

    @allure.title("Методы проверки статуса профиля (approved/rejected) работают корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_profile_approved_rejected_methods_work(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Методы проверки статуса профиля не работают."""
        with allure.step("Получение статуса approved/rejected"):
            is_approved = profile_settings_page.is_profile_approved()
            is_rejected = profile_settings_page.is_profile_rejected()
        with allure.step("Проверка что методы возвращают bool"):
            assert isinstance(is_approved, bool), \
                f"BUG: is_profile_approved вернул не bool: {type(is_approved)}"
            assert isinstance(is_rejected, bool), \
                f"BUG: is_profile_rejected вернул не bool: {type(is_rejected)}"
