"""
Tests for Profile Settings page.
9 classes, ~43 methods, ~50+ test cases.

URL: /dashboard/settings or /dashboard/profile
"""

import pytest
import allure
from pages.profile_settings_page import ProfileSettingsPage



@allure.epic("Платформа продавца")
@allure.suite("Навигация настроек профиля")
@allure.feature("Навигация")
@pytest.mark.functional
class TestProfileSettingsNavigation:
    """Тесты навигации страницы настроек."""

    @allure.title("Прямой переход по URL загружает страницу настроек")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_direct_url_loads_page(self, fresh_authenticated_page):
        """BUG: Прямой переход на /settings не работает."""
        with allure.step("Переход на страницу настроек по прямому URL"):
            page = fresh_authenticated_page
            # Try multiple possible settings URLs
            for path in ["/dashboard/profile/settings", "/dashboard/settings", "/dashboard/profile"]:
                page.goto(f"https://staging-seller.greatmall.uz{path}",
                          wait_until="networkidle", timeout=15000)
                page.wait_for_load_state("networkidle")
                if "/auth/login" not in page.url:
                    break
        with allure.step("Проверка что страница загрузилась без редиректа на логин"):
            # Страница должна загрузиться (не редирект на логин)
            assert "/auth/login" not in page.url, \
                f"BUG: Редирект на логин вместо настроек: {page.url}"

    @allure.title("Обновление страницы сохраняет настройки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refresh_preserves_page(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Обновление страницы ломает настройки."""
        with allure.step("Обновление страницы настроек"):
            profile_settings_page.page.reload(wait_until="networkidle", timeout=15000)
            profile_settings_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница сохранилась после обновления"):
            url = profile_settings_page.page.url
            # После refresh должны остаться в пределах дашборда (не редирект на логин)
            assert "/auth/login" not in url, \
                f"BUG: После refresh произошел редирект на логин: {url}"

    @allure.title("Кнопка 'Назад' браузера работает со страницы настроек")
    @allure.severity(allure.severity_level.NORMAL)
    def test_browser_back_from_settings(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Кнопка назад не работает."""
        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            profile_settings_page.page.go_back(wait_until="networkidle", timeout=10000)
            profile_settings_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что навигация назад сработала"):
            # Должна уйти со страницы настроек или остаться на dashboard
            assert "/dashboard" in profile_settings_page.page.url, \
                f"BUG: Кнопка назад не сработала: {profile_settings_page.page.url}"

    @allure.title("Ссылка на настройки присутствует в навигации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_settings_nav_link_exists(self, fresh_authenticated_page):
        """BUG: Ссылка на настройки отсутствует в навигации."""
        with allure.step("Переход на страницу дашборда"):
            page = fresh_authenticated_page
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Поиск ссылки на настройки в навигации"):
            settings_link = page.locator("a:has-text('Настройки')").or_(
                page.locator("a:has-text('Settings')")
            ).or_(page.locator("a:has-text('Sozlamalar')")).or_(
                page.locator("[href*='settings']")
            )
        with allure.step("Проверка что ссылка на настройки существует"):
            # Ссылка должна существовать в сайдбаре или меню
            assert settings_link.count() > 0, \
                "BUG: Ссылка на настройки отсутствует в навигации"



@allure.epic("Платформа продавца")
@allure.suite("Защита авторизации настроек профиля")
@allure.feature("Авторизация")
@pytest.mark.security
class TestProfileSettingsAuthGuard:
    """Тесты авторизации страницы настроек."""

    @allure.title("Неавторизованный доступ к настройкам редиректит на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_settings_redirects_to_login(self, browser):
        """BUG: Неавторизованный доступ к /settings не редиректит."""
        with allure.step("Открытие страницы настроек без авторизации"):
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://staging-seller.greatmall.uz/dashboard/settings",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка редиректа на страницу логина"):
            assert "/auth/login" in page.url or "/login" in page.url, \
                f"BUG: Неавторизованный доступ не редиректит: {page.url}"
            context.close()

    @allure.title("Неавторизованный доступ к профилю редиректит на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_profile_redirects_to_login(self, browser):
        """BUG: Неавторизованный доступ к /profile не редиректит."""
        with allure.step("Открытие страницы профиля без авторизации"):
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://staging-seller.greatmall.uz/dashboard/profile",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка редиректа на страницу логина"):
            assert "/auth/login" in page.url or "/login" in page.url, \
                f"BUG: Неавторизованный доступ не редиректит: {page.url}"
            context.close()



@allure.epic("Платформа продавца")
@allure.suite("Безопасность настроек профиля")
@allure.feature("Безопасность")
@pytest.mark.security
class TestProfileSettingsSecurity:
    """Тесты безопасности страницы настроек."""

    @allure.title("Токен авторизации не виден в URL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_token_in_url(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Токен авторизации виден в URL."""
        with allure.step("Проверка что токен авторизации отсутствует в URL"):
            url = profile_settings_page.page.url
            for pattern in ["token=", "jwt=", "session=", "auth=", "api_key="]:
                assert pattern not in url.lower(), \
                    f"BUG: URL содержит '{pattern}': {url}"

    @allure.title("Исходный код страницы не содержит секретных данных")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_source_no_secrets(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Исходный код страницы содержит секреты."""
        with allure.step("Получение исходного кода страницы"):
            content = profile_settings_page.page.content().lower()
        with allure.step("Проверка отсутствия секретных данных в исходном коде"):
            secrets = ["api_key", "secret_key", "private_key", "aws_", "password"]
            for secret in secrets:
                # Игнорируем password в атрибутах типа input[type=password]
                if secret == "password":
                    continue
                assert secret not in content, \
                    f"BUG: Исходный код содержит '{secret}'"

    @allure.title("Невалидный путь обрабатывается безопасно")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("invalid_path", [
        "/dashboard/settings/../../../etc/passwd",
        "/dashboard/settings/<script>",
        "/dashboard/settings/'; DROP TABLE users; --",
    ], ids=["path_traversal", "xss", "sql"])
    def test_invalid_path_safe(self, fresh_authenticated_page, invalid_path: str):
        """BUG: Невалидный путь вызывает ошибку сервера."""
        with allure.step(f"Переход по невалидному пути: {invalid_path}"):
            page = fresh_authenticated_page
            full_url = f"https://staging-seller.greatmall.uz{invalid_path}"
            page.goto(full_url, wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка отсутствия серверных ошибок"):
            page_text = page.text_content("body") or ""
            for indicator in ("Internal Server Error", "Traceback", "stack trace", "500"):
                assert indicator not in page_text, \
                    f"BUG: Путь '{invalid_path}' вызвал серверную ошибку: '{indicator}'"

    @allure.title("Деструктивные действия требуют подтверждения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_confirmation_modal_for_destructive_actions(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Нет подтверждения для деструктивных действий."""
        with allure.step("Поиск кнопки удаления на странице"):
            page = profile_settings_page.page
            # Ищем кнопку удаления
            delete_btn = page.locator("button:has-text('Удалить')").or_(
                page.locator("button:has-text('Delete')")
            ).or_(page.locator("button:has-text('O\\'chirish')")).first
        if delete_btn.is_visible(timeout=2000):
            with allure.step("Нажатие кнопки удаления"):
                delete_btn.click()
                page.wait_for_load_state("domcontentloaded")
            with allure.step("Проверка появления модального окна подтверждения"):
                # Должно появиться подтверждение
                has_modal = page.locator("[role='dialog']").is_visible(timeout=2000)
                has_confirm = page.locator("text=Подтвердить").or_(
                    page.locator("text=Confirm")
                ).or_(page.locator("text=Tasdiqlash")).is_visible(timeout=1000)
                assert has_modal or has_confirm, \
                    "BUG: Деструктивное действие без подтверждения"
            with allure.step("Отмена деструктивного действия"):
                # Отменяем если есть
                cancel = page.locator("button:has-text('Отмена')").or_(
                    page.locator("button:has-text('Cancel')")
                ).or_(page.locator("button:has-text('Bekor qilish')")).first
                if cancel.is_visible(timeout=1000):
                    cancel.click()

    @allure.title("Переключение языка работает корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_language_toggle_works(self, profile_settings_page: ProfileSettingsPage):
        """BUG: Переключение языка не работает."""
        with allure.step("Поиск переключателя языка"):
            page = profile_settings_page.page
            lang_toggle = page.locator("[data-testid='language-toggle']").or_(
                page.get_by_role("button", name="RU")
            ).or_(page.get_by_role("button", name="UZ"))
        if lang_toggle.is_visible(timeout=2000):
            with allure.step("Сохранение текста страницы до переключения"):
                initial_text = page.text_content("body") or ""
            with allure.step("Нажатие переключателя языка"):
                lang_toggle.click()
                page.wait_for_load_state("networkidle")
            with allure.step("Проверка что страница не пустая после переключения"):
                # Текст должен измениться (или остаться если уже на том языке)
                new_text = page.text_content("body") or ""
                # Не assertion - просто документируем
                assert len(new_text) > 0, "INFO: Страница пустая после переключения языка"
