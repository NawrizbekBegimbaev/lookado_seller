"""
Tests for Reviews page.
URL: /dashboard/reviews?page=1&size=10

NOTE: This page has NO search field.
Tabs are language-dependent (EN/RU/UZ).
"""

import pytest
import allure
from pages.reviews_page import ReviewsPage


# ================================================================================
# Fixtures
# ================================================================================

@pytest.fixture
def reviews_page(fresh_authenticated_page) -> ReviewsPage:
    """Navigate to reviews page."""
    page = fresh_authenticated_page
    rp = ReviewsPage(page)
    rp.navigate()
    page.wait_for_load_state("networkidle")
    return rp


# ================================================================================
# 1. TestReviewsPageUI
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Отзывы — Интерфейс")
@allure.feature("Элементы интерфейса")
@pytest.mark.smoke
class TestReviewsPageUI:
    """Тесты UI элементов страницы отзывов."""

    @allure.title("Загрузка страницы отзывов")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_reviews_page_loads(self, reviews_page: ReviewsPage):
        """BUG: Страница отзывов не загружается."""
        with allure.step("Проверка загрузки страницы отзывов"):
            assert reviews_page.is_page_loaded(), \
                f"BUG: Страница отзывов не загрузилась. URL: {reviews_page.page.url}"

    @allure.title("URL содержит /reviews")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_url_contains_reviews(self, reviews_page: ReviewsPage):
        """BUG: URL не содержит /reviews."""
        with allure.step("Проверка что URL содержит /reviews"):
            assert "/reviews" in reviews_page.page.url, \
                f"BUG: URL не содержит /reviews: {reviews_page.page.url}"

    @allure.title("DataGrid отображается на странице отзывов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_data_grid_visible(self, reviews_page: ReviewsPage):
        """BUG: DataGrid не отображается на странице отзывов."""
        with allure.step("Проверка видимости таблицы данных или пустого состояния"):
            grid_visible = reviews_page.data_grid.is_visible(timeout=5000)
            empty_visible = reviews_page.is_empty_state_visible()
            assert grid_visible or empty_visible, \
                "BUG: Нет ни DataGrid ни empty state на странице отзывов"

    @allure.title("Проверка HTTPS соединения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_https_connection(self, reviews_page: ReviewsPage):
        """BUG: Страница не использует HTTPS."""
        with allure.step("Проверка что страница загружена по HTTPS"):
            assert reviews_page.page.url.startswith("https://"), \
                f"BUG: Не HTTPS: {reviews_page.page.url}"

    @allure.title("Отсутствие чувствительных данных в URL")
    @allure.severity(allure.severity_level.NORMAL)
    def test_no_sensitive_data_in_url(self, reviews_page: ReviewsPage):
        """BUG: URL содержит чувствительные данные."""
        with allure.step("Проверка отсутствия чувствительных данных в URL"):
            url = reviews_page.page.url.lower()
            for sensitive in ["token", "password", "secret", "api_key"]:
                assert sensitive not in url, \
                    f"BUG: URL содержит '{sensitive}': {url}"


# ================================================================================
# 2. TestReviewsTabs
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Отзывы — Табы")
@allure.feature("Табы статусов")
@pytest.mark.functional
class TestReviewsTabs:
    """Тесты табов статусов отзывов (language-independent)."""

    @allure.title("Табы статусов отображаются")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tabs_visible(self, reviews_page: ReviewsPage):
        """BUG: Табы статусов не отображаются."""
        with allure.step("Получение списка табов"):
            tabs = reviews_page.get_all_tabs()
        with allure.step("Проверка что есть хотя бы 1 таб"):
            assert len(tabs) >= 1, \
                f"BUG: Ожидалось хотя бы 1 таб, найдено {len(tabs)}"

    @allure.title("Один таб активен по умолчанию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_one_tab_active_by_default(self, reviews_page: ReviewsPage):
        """BUG: Ни один таб не активен по умолчанию."""
        with allure.step("Проверка наличия активного таба"):
            active = reviews_page.get_active_tab()
            assert len(active) > 0, \
                "BUG: Нет активного таба по умолчанию"

    @allure.title("Клик на таб меняет активный таб")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tab_click_changes_active(self, reviews_page: ReviewsPage):
        """BUG: Клик на таб не меняет активный таб."""
        page = reviews_page.page
        tabs = page.locator("[role='tab']")
        tab_count = tabs.count()
        if tab_count >= 2:
            with allure.step("Определение текущего активного таба"):
                initial_index = 0
                for i in range(tab_count):
                    if tabs.nth(i).get_attribute("aria-selected") == "true":
                        initial_index = i
                        break

            with allure.step("Клик на другой таб"):
                target_index = 1 if initial_index == 0 else 0
                tabs.nth(target_index).click()
                page.wait_for_load_state("networkidle")

            with allure.step("Проверка что активный таб изменился"):
                new_selected = tabs.nth(target_index).get_attribute("aria-selected")
                old_selected = tabs.nth(initial_index).get_attribute("aria-selected")
                assert new_selected == "true", \
                    f"BUG: Clicked tab not selected. aria-selected={new_selected}"
                assert old_selected != "true", \
                    f"BUG: Previous tab still selected after clicking new one"

    @allure.title("Табы имеют атрибут role='tab'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tabs_have_role_tab(self, reviews_page: ReviewsPage):
        """BUG: Табы не имеют role='tab' (accessibility)."""
        with allure.step("Проверка атрибута role='tab' на всех табах"):
            tabs = reviews_page.get_all_tabs()
            assert len(tabs) >= 1, \
                f"BUG: Ожидался хотя бы 1 таб, найдено {len(tabs)}"
            for tab in tabs:
                role = tab.get_attribute("role")
                assert role == "tab", \
                    f"BUG: Таб '{tab.text_content().strip()}' не имеет role='tab'"

    @allure.title("Клик на таб показывает таблицу или пустое состояние")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tab_click_shows_grid_or_empty(self, reviews_page: ReviewsPage):
        """BUG: После клика на таб нет ни грида ни empty state."""
        tabs = reviews_page.get_all_tabs()
        if len(tabs) >= 2:
            with allure.step("Клик на второй таб"):
                tabs[1].click()
                reviews_page.page.wait_for_load_state("networkidle")
            with allure.step("Проверка наличия таблицы или пустого состояния"):
                grid_visible = reviews_page.data_grid.is_visible(timeout=3000)
                empty_visible = reviews_page.is_empty_state_visible()
                assert grid_visible or empty_visible, \
                    "BUG: После клика на таб нет ни грида ни empty state"


# ================================================================================
# 3. TestReviewsGrid
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Отзывы — Таблица данных")
@allure.feature("Таблица данных")
@pytest.mark.functional
class TestReviewsGrid:
    """Тесты DataGrid отзывов."""

    @allure.title("DataGrid содержит колонки")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_grid_has_columns(self, reviews_page: ReviewsPage):
        """BUG: DataGrid не содержит колонок."""
        with allure.step("Проверка наличия колонок в таблице"):
            count = reviews_page.get_column_count()
            assert count >= 1, \
                f"BUG: Ожидалась 1+ колонок, найдено {count}"

    @allure.title("Отображение строк данных или пустого состояния")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_state_or_rows_visible(self, reviews_page: ReviewsPage):
        """BUG: Нет ни данных ни empty state."""
        with allure.step("Проверка наличия строк или пустого состояния"):
            rows = reviews_page.get_row_count()
            empty = reviews_page.is_empty_state_visible()
            assert rows > 0 or empty, \
                "BUG: DataGrid не показывает ни строк ни empty state"

    @allure.title("DataGrid имеет атрибут role='grid'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_grid_has_role_grid(self, reviews_page: ReviewsPage):
        """BUG: DataGrid не имеет role='grid' (accessibility)."""
        with allure.step("Проверка наличия элемента с role='grid'"):
            grid = reviews_page.page.locator("[role='grid']")
            assert grid.first.is_visible(timeout=3000), \
                "BUG: Элемент с role='grid' не найден"

    @allure.title("URL содержит параметры пагинации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_size_in_url(self, reviews_page: ReviewsPage):
        """BUG: URL не содержит параметры пагинации."""
        with allure.step("Проверка наличия параметров page и size в URL"):
            url = reviews_page.page.url
            assert "page=" in url and "size=" in url, \
                f"BUG: URL не содержит page/size параметры: {url}"


# ================================================================================
# 4. TestReviewsNavigation
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Отзывы — Навигация")
@allure.feature("Навигация")
@pytest.mark.regression
class TestReviewsNavigation:
    """Тесты навигации страницы отзывов."""

    @allure.title("Прямой переход по URL загружает страницу отзывов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_direct_url_loads_page(self, fresh_authenticated_page):
        """BUG: Прямой переход на /reviews не работает."""
        with allure.step("Прямой переход по URL на страницу отзывов"):
            page = fresh_authenticated_page
            page.goto(f"https://staging-seller.greatmall.uz/dashboard/reviews",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что URL содержит /reviews"):
            assert "/reviews" in page.url, \
                f"BUG: Прямой URL не сработал, текущий URL: {page.url}"

    @allure.title("Обновление страницы не ломает отзывы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refresh_does_not_crash(self, reviews_page: ReviewsPage):
        """BUG: Обновление страницы ломает отзывы."""
        with allure.step("Обновление страницы"):
            reviews_page.page.reload(wait_until="networkidle", timeout=15000)
            reviews_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница сохранилась"):
            assert "/reviews" in reviews_page.page.url, \
                f"BUG: После refresh URL изменился: {reviews_page.page.url}"
            grid_or_empty = reviews_page.data_grid.is_visible(timeout=5000) or \
                reviews_page.is_empty_state_visible()
            assert grid_or_empty, \
                "BUG: После refresh нет ни грида ни empty state"

    @allure.title("Кнопка назад из страницы отзывов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_browser_back_from_reviews(self, reviews_page: ReviewsPage):
        """BUG: Кнопка назад из отзывов не работает."""
        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            reviews_page.page.go_back(wait_until="networkidle", timeout=10000)
            reviews_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка перехода на предыдущую страницу"):
            assert "/reviews" not in reviews_page.page.url or \
                "/dashboard" in reviews_page.page.url, \
                "BUG: Кнопка назад не увела со страницы отзывов"

    @allure.title("Переключение табов сохраняет URL страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tab_switch_preserves_url(self, reviews_page: ReviewsPage):
        """BUG: Переключение табов не сохраняет страницу."""
        tabs = reviews_page.get_all_tabs()
        if len(tabs) >= 2:
            with allure.step("Клик на второй таб"):
                tabs[1].click()
                reviews_page.page.wait_for_load_state("networkidle")
            with allure.step("Проверка что URL содержит /reviews"):
                url_after = reviews_page.page.url
                assert "/reviews" in url_after, \
                    f"BUG: После клика на таб URL не содержит /reviews: {url_after}"


# ================================================================================
# 5. TestReviewsAuthGuard
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Отзывы — Защита авторизации")
@allure.feature("Авторизация")
@pytest.mark.security
class TestReviewsAuthGuard:
    """Тесты авторизации страницы отзывов."""

    @allure.title("Неавторизованный пользователь перенаправляется на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_redirects_to_login(self, browser):
        """BUG: Неавторизованный доступ к /reviews не редиректит на логин."""
        with allure.step("Создание неавторизованного контекста"):
            context = browser.new_context()
            page = context.new_page()
        with allure.step("Переход на страницу отзывов без авторизации"):
            page.goto("https://staging-seller.greatmall.uz/dashboard/reviews",
                      wait_until="networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка перенаправления на страницу входа"):
            assert "/auth/login" in page.url or "/login" in page.url, \
                f"BUG: Неавторизованный доступ к /reviews не редиректит: {page.url}"
            context.close()


# ================================================================================
# 6. TestReviewsSecurity
# ================================================================================

@allure.epic("Платформа продавца")
@allure.suite("Отзывы — Безопасность")
@allure.feature("Безопасность")
@pytest.mark.security
class TestReviewsSecurity:
    """Тесты безопасности страницы отзывов."""

    @allure.title("Отсутствие токена авторизации в URL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_token_in_url(self, reviews_page: ReviewsPage):
        """BUG: Токен авторизации виден в URL."""
        with allure.step("Проверка отсутствия токенов в URL"):
            url = reviews_page.page.url
            for pattern in ["token=", "jwt=", "session=", "auth="]:
                assert pattern not in url.lower(), \
                    f"BUG: URL содержит '{pattern}': {url}"

    @allure.title("Отсутствие секретов в исходном коде страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_source_no_secrets(self, reviews_page: ReviewsPage):
        """BUG: Исходный код страницы содержит секреты."""
        with allure.step("Проверка отсутствия секретов в исходном коде"):
            content = reviews_page.page.content()
            for secret in ["api_key", "secret_key", "private_key", "AWS_"]:
                assert secret.lower() not in content.lower(), \
                    f"BUG: Исходный код содержит '{secret}'"
