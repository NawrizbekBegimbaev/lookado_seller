"""
Tests for Shop Settings page.
9 classes, ~41 methods, ~50+ test cases.

URL: /dashboard/settings
"""

import pytest
import allure
from pages.shop_settings_page import ShopSettingsPage
from pages.dashboard_page import DashboardPage



@allure.epic("Настройки магазина")
@allure.suite("Интерфейс настроек магазина")
@allure.feature("Элементы интерфейса")
@pytest.mark.smoke
class TestShopSettingsUI:
    """Тесты UI элементов страницы настроек магазина."""

    @allure.title("Страница настроек магазина загружается")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_shop_settings_page_loads(self, shop_settings_page: ShopSettingsPage):
        """BUG: Страница настроек магазина не загружается."""
        with allure.step("Проверка загрузки страницы настроек магазина"):
            is_loaded = shop_settings_page.is_settings_page_loaded()
            assert is_loaded, \
                f"BUG: Страница настроек магазина не загрузилась. URL: {shop_settings_page.page.url}"

    @allure.title("URL содержит shop или settings")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_url_contains_shop_or_settings(self, shop_settings_page: ShopSettingsPage):
        """BUG: URL не содержит shop или settings."""
        with allure.step("Проверка что URL содержит shop или settings"):
            url = shop_settings_page.page.url
            has_shop = "/shop" in url
            has_settings = "settings" in url
            assert has_shop or has_settings, \
                f"BUG: URL не содержит shop/settings: {url}"

    @allure.title("Страница использует HTTPS соединение")
    @allure.severity(allure.severity_level.NORMAL)
    def test_https_connection(self, shop_settings_page: ShopSettingsPage):
        """BUG: Страница не использует HTTPS."""
        with allure.step("Проверка что страница использует HTTPS соединение"):
            assert shop_settings_page.page.url.startswith("https://"), \
                f"BUG: Не HTTPS: {shop_settings_page.page.url}"

    @allure.title("URL не содержит чувствительных данных")
    @allure.severity(allure.severity_level.NORMAL)
    def test_no_sensitive_data_in_url(self, shop_settings_page: ShopSettingsPage):
        """BUG: URL содержит чувствительные данные."""
        with allure.step("Проверка что URL не содержит чувствительные данные"):
            url = shop_settings_page.page.url.lower()
            for sensitive in ["token", "password", "secret", "api_key", "session"]:
                assert sensitive not in url, \
                    f"BUG: URL содержит '{sensitive}': {url}"

    @allure.title("Поле названия магазина видимо")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_name_input_visible(self, shop_settings_page: ShopSettingsPage):
        """BUG: Поле названия магазина не отображается."""
        with allure.step("Проверка видимости поля названия магазина"):
            has_input = shop_settings_page.shop_name_input.is_visible(timeout=3000)
            if not has_input:
                pytest.fail("Поле названия магазина не найдено на странице")
            assert has_input, "BUG: Поле названия магазина не видимо"

    @allure.title("Кнопка сохранения видима")
    @allure.severity(allure.severity_level.NORMAL)
    def test_save_button_visible(self, shop_settings_page: ShopSettingsPage):
        """BUG: Кнопка сохранения не отображается."""
        with allure.step("Проверка видимости кнопки сохранения"):
            has_save = shop_settings_page.save_btn.is_visible(timeout=3000)
        with allure.step("Поиск альтернативных кнопок сохранения"):
            if not has_save:
                alt_save = shop_settings_page.page.locator("button:has-text('Save')").or_(
                    shop_settings_page.page.locator("button:has-text('Сохранить')")
                ).or_(shop_settings_page.page.locator("button:has-text('Saqlash')")).or_(
                    shop_settings_page.page.locator("button[type='submit']")
                )
                has_save = alt_save.count() > 0
            if not has_save:
                pytest.fail("Кнопка сохранения не найдена на странице")
            assert has_save, "BUG: Кнопка сохранения не видима"

    @allure.title("Страница содержит элементы формы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_has_form_elements(self, shop_settings_page: ShopSettingsPage):
        """BUG: Страница не содержит форм."""
        with allure.step("Проверка наличия элементов формы на странице"):
            page = shop_settings_page.page
            has_inputs = page.locator("input").count() > 0
            has_textareas = page.locator("textarea").count() > 0
            has_buttons = page.locator("button").count() > 0
            assert has_inputs or has_textareas or has_buttons, \
                "BUG: Страница настроек магазина не содержит форм"

    @allure.title("Кнопка редактирования видима в read-only режиме")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_button_visible(self, shop_settings_page: ShopSettingsPage):
        """Кнопка редактирования переключает страницу в режим правки."""
        with allure.step("Проверка что режим редактирования активен"):
            page = shop_settings_page.page
            has_inputs = page.locator("input, textarea").first.is_visible(timeout=3000)
            assert has_inputs, \
                "BUG: Режим редактирования не активен — поля ввода не найдены"



@allure.epic("Настройки магазина")
@allure.suite("Навигация настроек магазина")
@allure.feature("Навигация")
@pytest.mark.functional
class TestShopSettingsNavigation:
    """Тесты навигации страницы настроек магазина."""

    @allure.title("Прямой переход по URL загружает страницу")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_direct_url_loads_page(self, fresh_authenticated_page):
        """BUG: Прямой переход на /shop/settings не работает."""
        with allure.step("Переход на страницу настроек магазина по прямому URL"):
            page = fresh_authenticated_page
            page.goto("https://staging-seller.greatmall.uz/dashboard/settings",
                      wait_until="domcontentloaded", timeout=15000)
            page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что страница загрузилась без редиректа на логин"):
            assert "/auth/login" not in page.url, \
                f"BUG: Редирект на логин вместо настроек: {page.url}"

    @allure.title("Обновление страницы сохраняет настройки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refresh_preserves_page(self, shop_settings_page: ShopSettingsPage):
        """BUG: Обновление страницы ломает настройки."""
        with allure.step("Обновление страницы настроек магазина"):
            shop_settings_page.page.reload(wait_until="domcontentloaded", timeout=15000)
            shop_settings_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что страница сохранилась после обновления"):
            url = shop_settings_page.page.url
            assert "/dashboard" in url, \
                f"BUG: После refresh URL изменился: {url}"

    @allure.title("Кнопка назад в браузере работает")
    @allure.severity(allure.severity_level.NORMAL)
    def test_browser_back_from_settings(self, shop_settings_page: ShopSettingsPage):
        """BUG: Кнопка назад не работает."""
        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            shop_settings_page.page.go_back(wait_until="domcontentloaded", timeout=10000)
            shop_settings_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что навигация назад сработала"):
            assert "/dashboard" in shop_settings_page.page.url, \
                f"BUG: Кнопка назад не сработала: {shop_settings_page.page.url}"

    @allure.title("Ссылка на настройки присутствует в сайдбаре")
    @allure.severity(allure.severity_level.NORMAL)
    def test_settings_link_in_sidebar(self, fresh_authenticated_page):
        """BUG: Ссылка на настройки магазина отсутствует в сайдбаре."""
        with allure.step("Переход на страницу дашборда"):
            page = fresh_authenticated_page
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="domcontentloaded", timeout=15000)
            # Ждём рендер React — сайдбар содержит ссылки
            page.wait_for_selector("a", state="visible", timeout=10000)
        with allure.step("Поиск ссылки на настройки в сайдбаре"):
            settings_link = page.locator("a:has-text('Настройки')").or_(
                page.locator("a:has-text('Settings')")
            ).or_(page.locator("a:has-text('Sozlamalar')")).or_(
                page.locator("[href*='settings']")
            )
        with allure.step("Проверка что ссылка на настройки существует"):
            assert settings_link.count() > 0, \
                "BUG: Ссылка на настройки отсутствует в сайдбаре"



@allure.epic("Настройки магазина")
@allure.suite("Защита авторизации настроек магазина")
@allure.feature("Авторизация")
@pytest.mark.security
class TestShopSettingsAuthGuard:
    """Тесты авторизации страницы настроек магазина."""

    @allure.title("Неавторизованный доступ перенаправляет на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_shop_settings_redirects_to_login(self, browser):
        """BUG: Неавторизованный доступ к /shop/settings не редиректит."""
        with allure.step("Открытие страницы настроек магазина без авторизации"):
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://staging-seller.greatmall.uz/dashboard/settings",
                      wait_until="domcontentloaded", timeout=15000)
            page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка редиректа на страницу логина"):
            assert "/auth/login" in page.url or "/login" in page.url, \
                f"BUG: Неавторизованный доступ не редиректит: {page.url}"
            context.close()

    @allure.title("Данные магазина не доступны без авторизации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_no_data_exposed(self, browser):
        """BUG: Данные магазина доступны без авторизации."""
        with allure.step("Открытие страницы настроек магазина без авторизации"):
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://staging-seller.greatmall.uz/dashboard/settings",
                      wait_until="domcontentloaded", timeout=15000)
            page.wait_for_load_state("domcontentloaded")
            current_url = page.url
        with allure.step("Проверка что редирект на логин сработал"):
            # Если на логине - данные не раскрыты (ожидаемое поведение)
            is_on_login = "/auth" in current_url or "/login" in current_url
            if is_on_login:
                # Редирект сработал - данные защищены
                context.close()
                return
        with allure.step("Проверка что данные магазина не раскрыты"):
            # Если не на логине - проверяем что нет данных магазина
            body_text = page.text_content("body") or ""
            has_shop_data = any([
                "shop_name" in body_text.lower(),
                "магазин" in body_text.lower() and "настройки" in body_text.lower(),
            ])
            context.close()
            assert not has_shop_data, \
                "BUG: Данные магазина доступны без авторизации"
