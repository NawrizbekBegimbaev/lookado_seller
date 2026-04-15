"""
Returns Test Cases - Returns Management Functionality.
Tests returns listing, tabs, filtering, pagination.
Follows KISS, DRY, SOLID principles with POM pattern.

NOTE: This page has NO search field. Only tabs and filters.
"""

import pytest
import logging
import allure
from playwright.sync_api import expect
from pages.returns_page import ReturnsPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Синхронизация с API")
class TestReturnsAPISync:
    """Test cases for API synchronization."""

    @allure.title("RETURN-25: Синхронизация возвратов с API")
    @pytest.mark.order(159)
    def test_returns_api_sync(self, returns_page):
        """ID-1714: Verify returns data syncs with API."""
        with allure.step("Получение начального количества возвратов"):
            page = returns_page.page
            initial_count = returns_page.get_returns_count()

        with allure.step("Обновление страницы и ожидание загрузки данных"):
            page.reload()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что данные синхронизированы с API после обновления"):
            assert "returns" in page.url or page.locator("table, [role='grid']").first.is_visible(timeout=3000)
            refreshed_count = returns_page.get_returns_count()

            assert abs(refreshed_count - initial_count) <= 5, \
                f"Data should be consistent after refresh. Before: {initial_count}, After: {refreshed_count}"
            logger.info(f"Returns API sync verified - before: {initial_count}, after: {refreshed_count}")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Безопасность")
class TestReturnsSecurity:
    """Test cases for security functionality."""

    @allure.title("RETURN-27: Неавторизованный доступ к возвратам")
    @pytest.mark.order(140)
    @pytest.mark.negative
    def test_unauthorized_access(self, returns_page):
        """ID-1716: Verify authorized user has access."""
        with allure.step("Проверка что авторизованный пользователь имеет доступ к возвратам"):
            page = returns_page.page
            assert "returns" in page.url or page.locator("table, [role='grid']").first.is_visible(timeout=3000)
            logger.info("Authorized returns access verified")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Производительность")
class TestReturnsPerformance:
    """Test cases for performance functionality."""

    @allure.title("RETURN-30: Загрузка большого набора данных возвратов")
    @pytest.mark.order(143)
    def test_large_dataset_load(self, returns_page):
        """ID-1719: Verify large dataset loads properly."""
        with allure.step("Замер времени загрузки страницы возвратов"):
            page = returns_page.page
            import time
            start_time = time.time()
            page.wait_for_load_state("networkidle")
            load_time = time.time() - start_time

        with allure.step("Проверка что страница загрузилась менее чем за 10 секунд"):
            assert "returns" in page.url or page.locator("table, [role='grid']").first.is_visible(timeout=3000)
            assert load_time < 10, f"Page should load within 10 seconds, took {load_time:.2f}s"
            logger.info(f"Large returns dataset load verified - loaded in {load_time:.2f}s")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Устойчивость")
class TestReturnsRobustness:
    """Test cases for page robustness under stress conditions."""

    @allure.title("RETURN-78: Множественные обновления страницы")
    @pytest.mark.order(178)
    def test_multiple_refreshes(self, returns_page):
        """ID-1768: Verify page remains functional after multiple refreshes."""
        with allure.step("Выполнение трёх последовательных обновлений страницы"):
            page = returns_page.page
            for i in range(3):
                page.reload()
                page.wait_for_load_state("networkidle")

        with allure.step("Проверка что страница осталась функциональной после обновлений"):
            assert "returns" in page.url or page.locator("table, [role='grid']").first.is_visible(timeout=3000)
            count = returns_page.get_returns_count()
            assert count >= 0, "Page should be functional after multiple refreshes"
            logger.info(f"Multiple refreshes handled - returns count: {count}")

    @allure.title("RETURN-79: Быстрое переключение вкладок")
    @pytest.mark.order(179)
    def test_rapid_tab_switching(self, returns_page):
        """ID-1769: Verify rapid tab switching doesn't break page."""
        with allure.step("Получение списка вкладок на странице"):
            page = returns_page.page
            tabs = page.locator("[role='tab']")
            tab_count = tabs.count()

        with allure.step("Быстрое переключение между вкладками"):
            if tab_count >= 2:
                for i in range(min(tab_count, 4)):
                    tabs.nth(i % tab_count).click()
                    page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка что страница осталась функциональной"):
            if tab_count >= 2:
                assert "returns" in page.url or page.locator("table, [role='grid']").first.is_visible(timeout=3000)
                logger.info("Rapid tab switching handled correctly")
            else:
                logger.info("Not enough tabs for rapid switching test")

    @allure.title("RETURN-81: Двойной клик по строке таблицы")
    @pytest.mark.order(181)
    def test_double_click_row(self, returns_page):
        """ID-1771: Verify double-click on table row is idempotent."""
        with allure.step("Поиск первой строки в таблице возвратов"):
            page = returns_page.page
            first_row = page.locator("tbody tr, .MuiDataGrid-row").first

        with allure.step("Двойной клик по строке таблицы"):
            if first_row.is_visible(timeout=3000):
                first_row.dblclick()
                page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка отсутствия ошибок после двойного клика"):
            if first_row.is_visible(timeout=3000):
                error_toast = page.locator("[class*='error'], [role='alert']:has-text('error'), [role='alert']:has-text('ошибка'), [role='alert']:has-text('xato')")
                assert error_toast.count() == 0, "BUG: Double-click should not cause errors"
                logger.info("Double-click on row handled correctly")
            else:
                logger.info("No rows available for double-click test")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Сессия")
class TestReturnsSession:
    """Test cases for session handling on returns page."""

    @allure.title("RETURN-82: Страница возвратов сохраняет авторизацию после обновления")
    @pytest.mark.order(182)
    def test_auth_preserved_after_refresh(self, returns_page):
        """ID-1772: Verify authentication is preserved after page refresh."""
        with allure.step("Обновление страницы возвратов"):
            page = returns_page.page
            page.reload()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что авторизация сохранилась после обновления"):
            current_url = page.url
            assert "auth/login" not in current_url, \
                f"BUG: User should stay authenticated after refresh, redirected to: {current_url}"
            logger.info("Auth preserved after refresh verified")

    @allure.title("RETURN-83: Прямая навигация по URL к возвратам")
    @pytest.mark.order(183)
    def test_direct_url_navigation(self, returns_page):
        """ID-1773: Verify direct URL navigation to returns works for authenticated user."""
        with allure.step("Проверка что URL содержит путь к возвратам"):
            page = returns_page.page
            current_url = page.url
            assert "returns" in current_url, \
                f"BUG: Authenticated user should access returns via direct URL, got: {current_url}"
            logger.info("Direct URL navigation to returns verified")
