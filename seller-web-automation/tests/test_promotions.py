"""
Tests for Promotions page.
6 classes, ~27 methods, ~35+ test cases.

URL: /dashboard/promotions?filter=AVAILABLE&page=1&size=10
"""

import pytest
import allure
from pages.promotions_page import PromotionsPage


# ================================================================================
# Fixtures
# ================================================================================

@pytest.fixture
def promotions_page(fresh_authenticated_page) -> PromotionsPage:
    """Navigate to promotions page."""
    page = fresh_authenticated_page
    pp = PromotionsPage(page)
    pp.navigate()
    page.wait_for_load_state("networkidle")
    return pp


# ================================================================================
# 1. TestPromotionsPageUI
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Промоакции — Интерфейс")
@allure.feature("Элементы интерфейса")
@pytest.mark.smoke
class TestPromotionsPageUI:
    """Тесты UI элементов страницы промоакций."""

    @allure.title("Загрузка страницы промоакций")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_promotions_page_loads(self, promotions_page: PromotionsPage):
        """BUG: Страница промоакций не загружается."""
        with allure.step("Проверка загрузки страницы промоакций"):
            assert promotions_page.is_page_loaded(), \
                f"BUG: Страница промоакций не загрузилась. URL: {promotions_page.page.url}"

    @allure.title("URL содержит /promotions")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_url_contains_promotions(self, promotions_page: PromotionsPage):
        """BUG: URL не содержит /promotions."""
        with allure.step("Проверка что URL содержит /promotions"):
            assert "/promotions" in promotions_page.page.url, \
                f"BUG: URL не содержит /promotions: {promotions_page.page.url}"

    @allure.title("URL содержит параметр filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_url_has_filter_parameter(self, promotions_page: PromotionsPage):
        """BUG: URL не содержит filter параметр."""
        with allure.step("Проверка наличия параметра filter в URL"):
            assert "filter=" in promotions_page.page.url, \
                f"BUG: URL не содержит filter=: {promotions_page.page.url}"

    @allure.title("Все табы промоакций отображаются")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_tabs_visible(self, promotions_page: PromotionsPage, test_data):
        """BUG: Не все табы промоакций отображаются."""
        with allure.step("Получение списка ожидаемых и видимых табов"):
            expected_tabs = test_data["tabs"]["names"]
            visible_tabs = promotions_page.get_all_visible_tabs()
        with allure.step("Проверка видимости всех табов"):
            for tab in expected_tabs:
                assert tab in visible_tabs, \
                    f"BUG: Таб '{tab}' не найден. Видимые: {visible_tabs}"

    @allure.title("Проверка HTTPS соединения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_https_connection(self, promotions_page: PromotionsPage):
        """BUG: Страница не использует HTTPS."""
        with allure.step("Проверка что страница загружена по HTTPS"):
            assert promotions_page.page.url.startswith("https://"), \
                f"BUG: Не HTTPS: {promotions_page.page.url}"

    @allure.title("Отсутствие чувствительных данных в URL")
    @allure.severity(allure.severity_level.NORMAL)
    def test_no_sensitive_data_in_url(self, promotions_page: PromotionsPage):
        """BUG: URL содержит чувствительные данные."""
        with allure.step("Проверка отсутствия чувствительных данных в URL"):
            url = promotions_page.page.url.lower()
            for sensitive in ["token", "password", "secret", "api_key"]:
                assert sensitive not in url, \
                    f"BUG: URL содержит '{sensitive}': {url}"


# ================================================================================
# 2. TestPromotionsTabs
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Промоакции — Табы")
@allure.feature("Навигация по табам")
@pytest.mark.functional
class TestPromotionsTabs:
    """Тесты табов промоакций."""

    @allure.title("Таб промоакции отображается")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("tab_name", [
        "Available", "Upcoming", "Participated", "Not Participated", "Completed"
    ], ids=["available", "upcoming", "participated", "not_participated", "completed"])
    def test_tab_visible(self, promotions_page: PromotionsPage, tab_name: str):
        """BUG: Таб не отображается."""
        with allure.step(f"Проверка видимости таба '{tab_name}'"):
            assert promotions_page.is_tab_visible(tab_name), \
                f"BUG: Таб '{tab_name}' не видим"

    @allure.title("Таб Available активен по умолчанию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_available_tab_active_by_default(self, promotions_page: PromotionsPage):
        """BUG: Таб 'Available' не активен по умолчанию."""
        with allure.step("Проверка что таб Available активен по умолчанию"):
            filter_val = promotions_page.get_active_tab_filter()
            assert filter_val == "AVAILABLE", \
                f"BUG: Фильтр по умолчанию не 'AVAILABLE': '{filter_val}'"

    @allure.title("Клик на таб меняет параметр filter в URL")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("tab_name,expected_filter", [
        ("Upcoming", "UPCOMING"),
        ("Participated", "PARTICIPATED"),
        ("Completed", "COMPLETED"),
    ], ids=["upcoming", "participated", "completed"])
    def test_tab_click_changes_url_filter(self, promotions_page: PromotionsPage,
                                          tab_name: str, expected_filter: str):
        """BUG: Клик на таб не меняет filter в URL."""
        with allure.step(f"Нажатие на таб '{tab_name}'"):
            promotions_page.click_tab(tab_name)
        with allure.step(f"Проверка что фильтр изменился на '{expected_filter}'"):
            actual_filter = promotions_page.get_active_tab_filter()
            assert actual_filter == expected_filter, \
                f"BUG: После клика на '{tab_name}' filter='{actual_filter}', " \
                f"ожидалось '{expected_filter}'"

    @allure.title("Фильтр таба Not Participated установлен корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_not_participated_tab_filter(self, promotions_page: PromotionsPage):
        """BUG: Таб 'Not Participated' не устанавливает правильный фильтр."""
        with allure.step("Нажатие на таб 'Not Participated'"):
            promotions_page.click_tab("Not Participated")
        with allure.step("Проверка значения фильтра"):
            filter_val = promotions_page.get_active_tab_filter()
            assert "NOT" in filter_val or "not" in filter_val.lower(), \
                f"BUG: 'Not Participated' filter неправильный: '{filter_val}'"

    @allure.title("Возврат на таб Available после переключения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tab_switch_back_to_available(self, promotions_page: PromotionsPage):
        """BUG: Возврат на таб Available не работает."""
        with allure.step("Переключение на таб Completed"):
            promotions_page.click_tab("Completed")
        with allure.step("Возврат на таб Available"):
            promotions_page.click_tab("Available")
        with allure.step("Проверка что фильтр вернулся на AVAILABLE"):
            filter_val = promotions_page.get_active_tab_filter()
            assert filter_val == "AVAILABLE", \
                f"BUG: Возврат на Available не сработал: '{filter_val}'"

    @allure.title("Быстрое переключение между табами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_rapid_tab_switching(self, promotions_page: PromotionsPage):
        """BUG: Быстрое переключение табов ломает страницу."""
        with allure.step("Быстрое переключение между 4 табами"):
            for tab in ["Upcoming", "Completed", "Available", "Participated"]:
                promotions_page.click_tab(tab)
                promotions_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что страница не сломалась"):
            assert "/promotions" in promotions_page.page.url, \
                f"BUG: Быстрое переключение сломало страницу: {promotions_page.page.url}"


# ================================================================================
# 3. TestPromotionsEmptyState
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Промоакции — Пустые состояния")
@allure.feature("Пустые состояния")
@pytest.mark.functional
class TestPromotionsEmptyState:
    """Тесты пустых состояний промоакций."""

    @allure.title("Пустое состояние на табе Available")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_state_visible_on_available(self, promotions_page: PromotionsPage):
        """BUG: Нет empty state для пустого Available."""
        with allure.step("Проверка наличия карточек или пустого состояния"):
            has_items = promotions_page.get_promotion_count() > 0
            has_empty = promotions_page.is_empty_state_visible()
            assert has_items or has_empty, \
                "BUG: Нет ни карточек промо ни empty state на Available"

    @allure.title("Пустое состояние на каждом табе")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("tab_name", [
        "Upcoming", "Participated", "Not Participated", "Completed"
    ], ids=["upcoming", "participated", "not_participated", "completed"])
    def test_empty_state_on_each_tab(self, promotions_page: PromotionsPage, tab_name: str):
        """BUG: Нет empty state на пустом табе."""
        with allure.step(f"Переключение на таб '{tab_name}'"):
            promotions_page.click_tab(tab_name)
        with allure.step("Проверка наличия данных или пустого состояния"):
            has_items = promotions_page.get_promotion_count() > 0
            has_empty = promotions_page.is_empty_state_visible()
            assert has_items or has_empty, \
                f"BUG: Нет ни данных ни empty state на табе '{tab_name}'"

    @allure.title("Корректный текст пустого состояния")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_state_text_correct(self, promotions_page: PromotionsPage):
        """BUG: Текст empty state неправильный."""
        with allure.step("Проверка текста пустого состояния"):
            if promotions_page.is_empty_state_visible():
                text = promotions_page.empty_state.text_content().strip()
                assert "Данные отсутствуют" in text or "No data" in text, \
                    f"BUG: Неверный текст empty state: '{text}'"


# ================================================================================
# 4. TestPromotionsNavigation
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Промоакции — Навигация")
@allure.feature("Навигация")
@pytest.mark.regression
class TestPromotionsNavigation:
    """Тесты навигации страницы промоакций."""

    @allure.title("Прямой переход по URL загружает страницу промоакций")
    @allure.severity(allure.severity_level.NORMAL)
    def test_direct_url_loads_page(self, fresh_authenticated_page):
        """BUG: Прямой переход на /promotions не работает."""
        with allure.step("Прямой переход по URL на страницу промоакций"):
            page = fresh_authenticated_page
            page.goto("https://staging-seller.greatmall.uz/dashboard/promotions",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что URL содержит /promotions"):
            assert "/promotions" in page.url, \
                f"BUG: Прямой URL не сработал: {page.url}"

    @allure.title("Обновление страницы сохраняет промоакции")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refresh_preserves_page(self, promotions_page: PromotionsPage):
        """BUG: Обновление страницы ломает промоакции."""
        with allure.step("Обновление страницы"):
            promotions_page.page.reload(wait_until="networkidle", timeout=15000)
            promotions_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница сохранилась после обновления"):
            assert "/promotions" in promotions_page.page.url, \
                f"BUG: После refresh URL изменился: {promotions_page.page.url}"

    @allure.title("Обновление страницы сохраняет выбранный таб")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refresh_preserves_tab_filter(self, promotions_page: PromotionsPage):
        """BUG: Обновление страницы сбрасывает выбранный таб."""
        with allure.step("Переключение на таб Completed"):
            promotions_page.click_tab("Completed")
        with allure.step("Обновление страницы"):
            promotions_page.page.reload(wait_until="networkidle", timeout=15000)
            promotions_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что фильтр сохранился"):
            filter_val = promotions_page.get_active_tab_filter()
            assert filter_val == "COMPLETED", \
                f"BUG: После refresh фильтр сбросился: '{filter_val}'"

    @allure.title("Кнопка назад из страницы промоакций")
    @allure.severity(allure.severity_level.NORMAL)
    def test_browser_back_from_promotions(self, promotions_page: PromotionsPage):
        """Кнопка назад из промоакций возвращает на предыдущую страницу."""
        page = promotions_page.page
        with allure.step("Переход на dashboard чтобы создать историю навигации"):
            page.goto("https://staging-seller.greatmall.uz/dashboard",
                      wait_until="networkidle", timeout=15000)
        with allure.step("Переход обратно на промоакции"):
            page.goto("https://staging-seller.greatmall.uz/dashboard/promotions?filter=AVAILABLE&page=1&size=10",
                      wait_until="networkidle", timeout=15000)
        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            page.go_back(wait_until="networkidle", timeout=10000)
        with allure.step("Проверка перехода на предыдущую страницу"):
            assert "/dashboard" in page.url, \
                f"BUG: Кнопка назад не сработала: {page.url}"


# ================================================================================
# 5. TestPromotionsAuthGuard
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Промоакции — Защита авторизации")
@allure.feature("Авторизация")
@pytest.mark.security
class TestPromotionsAuthGuard:
    """Тесты авторизации страницы промоакций."""

    @allure.title("Неавторизованный пользователь перенаправляется на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_redirects_to_login(self, browser):
        """BUG: Неавторизованный доступ к /promotions не редиректит."""
        with allure.step("Создание неавторизованного контекста"):
            context = browser.new_context()
            page = context.new_page()
        with allure.step("Переход на страницу промоакций без авторизации"):
            page.goto("https://staging-seller.greatmall.uz/dashboard/promotions",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка перенаправления на страницу входа"):
            assert "/auth/login" in page.url or "/login" in page.url, \
                f"BUG: Неавторизованный доступ не редиректит: {page.url}"
            context.close()

    @allure.title("Данные промоакций не доступны без авторизации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_no_data_exposed(self, browser):
        """BUG: Данные промоакций доступны без авторизации."""
        with allure.step("Создание неавторизованного контекста"):
            context = browser.new_context()
            page = context.new_page()
        with allure.step("Переход на страницу промоакций без авторизации"):
            page.goto("https://staging-seller.greatmall.uz/dashboard/promotions",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что данные промоакций не отображаются"):
            body_text = page.text_content("body") or ""
            assert "Promotion" not in body_text or "/auth" in page.url, \
                "BUG: Данные промоакций доступны без авторизации"
            context.close()


# ================================================================================
# 6. TestPromotionsSecurity
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Промоакции — Безопасность")
@allure.feature("Безопасность")
@pytest.mark.security
class TestPromotionsSecurity:
    """Тесты безопасности страницы промоакций."""

    @allure.title("Отсутствие токена авторизации в URL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_token_in_url(self, promotions_page: PromotionsPage):
        """BUG: Токен авторизации виден в URL."""
        with allure.step("Проверка отсутствия токенов в URL"):
            url = promotions_page.page.url
            for pattern in ["token=", "jwt=", "session=", "auth="]:
                assert pattern not in url.lower(), \
                    f"BUG: URL содержит '{pattern}': {url}"

    @allure.title("Безопасная обработка невалидного параметра filter")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("invalid_filter", [
        pytest.param("<script>alert(1)</script>", id="xss"),
        pytest.param("'; DROP TABLE promotions; --", id="sql"),
        pytest.param("../../../etc/passwd", id="path_traversal"),
    ])
    def test_invalid_filter_param_safe(self, fresh_authenticated_page, invalid_filter: str):
        """BUG: Невалидный filter параметр вызывает ошибку."""
        with allure.step(f"Переход по URL с невалидным filter: {invalid_filter[:30]}"):
            page = fresh_authenticated_page
            url = f"https://staging-seller.greatmall.uz/dashboard/promotions?filter={invalid_filter}"
            page.goto(url, wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка отсутствия серверной ошибки"):
            page_text = page.text_content("body") or ""
            for indicator in ("Internal Server Error", "Traceback", "stack trace"):
                assert indicator not in page_text, \
                    f"BUG: Невалидный filter '{invalid_filter}' вызвал: '{indicator}'"

    @allure.title("Отсутствие секретов в исходном коде страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_source_no_secrets(self, promotions_page: PromotionsPage):
        """BUG: Исходный код страницы содержит секреты."""
        with allure.step("Проверка отсутствия секретов в исходном коде"):
            content = promotions_page.page.content()
            for secret in ["api_key", "secret_key", "private_key", "AWS_"]:
                assert secret.lower() not in content.lower(), \
                    f"BUG: Исходный код содержит '{secret}'"

    @allure.title("XSS через параметр filter не исполняется")
    @allure.severity(allure.severity_level.NORMAL)
    def test_xss_in_filter_not_executed(self, fresh_authenticated_page):
        """BUG: XSS через filter параметр исполняется."""
        with allure.step("Переход по URL с XSS payload в параметре filter"):
            page = fresh_authenticated_page
            url = "https://staging-seller.greatmall.uz/dashboard/promotions?filter=<script>alert(1)</script>"
            page.goto(url, wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что XSS скрипт не был внедрён"):
            script_count = page.locator("body script:not([src])").count()
            assert script_count == 0, \
                "BUG: XSS через filter параметр создал script элемент"
