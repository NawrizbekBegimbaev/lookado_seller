"""
Order Detail Page Tests.
Tests for /dashboard/orders-management/orders/[order_id] page.

8 classes, 36 methods, ~40 test cases.

Page Object: pages/order_detail_page.py
"""

import logging
import pytest
import allure
from pages.order_detail_page import OrderDetailPage
from pages.orders_page import OrdersPage

logger = logging.getLogger(__name__)



@allure.epic("Заказы")
@allure.suite("Детали заказа — Интерфейс")
@allure.feature("Элементы интерфейса")
@pytest.mark.smoke
class TestOrderDetailUI:
    """Тесты UI элементов страницы деталей заказа."""

    @allure.title("Страница деталей заказа загружается")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_order_detail_page_loads(self, order_detail_page: OrderDetailPage):
        """BUG: Страница деталей заказа не загружается."""
        with allure.step("Проверка что страница деталей заказа загрузилась"):
            assert order_detail_page.is_page_loaded(), \
                f"BUG: Страница не загрузилась. URL: {order_detail_page.page.url}"

    @allure.title("URL содержит ID заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_url_contains_order_id(self, order_detail_page: OrderDetailPage):
        """BUG: URL не содержит ID заказа."""
        with allure.step("Получение текущего URL страницы"):
            url = order_detail_page.get_current_url()
        with allure.step("Проверка что URL содержит ID заказа"):
            assert "/orders/" in url, \
                f"BUG: URL не содержит /orders/: {url}"

    @allure.title("Заголовок страницы отображается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_title_visible(self, order_detail_page: OrderDetailPage):
        """BUG: Заголовок страницы не отображается."""
        with allure.step("Проверка видимости заголовка страницы"):
            assert order_detail_page.page_title.is_visible(timeout=5000), \
                "BUG: Заголовок страницы не виден"
        with allure.step("Проверка что заголовок не пустой"):
            title_text = order_detail_page.page_title.inner_text()
            assert len(title_text) > 0, "BUG: Заголовок страницы пустой"

    @allure.title("Кнопка печати отображается")
    @allure.severity(allure.severity_level.NORMAL)
    def test_print_button_visible(self, order_detail_page: OrderDetailPage):
        """BUG: Кнопка печати не отображается."""
        with allure.step("Проверка видимости кнопки печати"):
            assert order_detail_page.print_button.is_visible(timeout=5000), \
                "BUG: Кнопка печати не видна"

    @allure.title("Бейдж статуса заказа отображается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_status_badge_visible(self, order_detail_page: OrderDetailPage):
        """BUG: Бейдж статуса заказа не отображается."""
        with allure.step("Поиск бейджа статуса заказа на странице"):
            page = order_detail_page.page
            badges = page.locator("[class*='badge'], [class*='chip'], [class*='status']")
        with allure.step("Проверка что бейдж статуса отображается"):
            assert badges.count() > 0, \
                "BUG: Статус заказа не найден на странице"

    @allure.title("Таблица товаров отображается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_products_table_visible(self, order_detail_page: OrderDetailPage):
        """BUG: Таблица товаров не отображается."""
        with allure.step("Проверка видимости таблицы товаров"):
            assert order_detail_page.is_products_table_visible(), \
                "BUG: Таблица товаров не видна"

    @allure.title("Страница использует HTTPS соединение")
    @allure.severity(allure.severity_level.NORMAL)
    def test_https_connection(self, order_detail_page: OrderDetailPage):
        """BUG: Страница не использует HTTPS."""
        with allure.step("Проверка что страница использует HTTPS"):
            assert order_detail_page.page.url.startswith("https://"), \
                f"BUG: Не HTTPS: {order_detail_page.page.url}"



@allure.epic("Заказы")
@allure.suite("Детали заказа — Навигация")
@allure.feature("Навигация")
@pytest.mark.functional
class TestOrderDetailNavigation:
    """Тесты навигации страницы деталей заказа."""

    @allure.title("Переход из списка заказов на детали")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_from_orders_list(self, fresh_authenticated_page):
        """BUG: Переход из списка заказов не работает."""
        with allure.step("Переход на страницу списка заказов"):
            page = fresh_authenticated_page
            orders_page = OrdersPage(page)
            order_detail = OrderDetailPage(page)
            orders_page.navigate()
            page.wait_for_load_state("networkidle")

        with allure.step("Получение первого заказа из списка"):
            order_rows = page.locator(".MuiDataGrid-row[data-id]").all()
            if len(order_rows) == 0:
                pytest.fail("No orders available")
            first_order = order_rows[0]
            order_id = first_order.get_attribute("data-id")

        with allure.step("Клик по первому заказу для перехода на детальную страницу"):
            first_order.click()
            page.wait_for_load_state("networkidle")
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что открылась страница деталей заказа"):
            assert order_detail.is_on_order_detail_page(), \
                "BUG: Клик по заказу не открыл детальную страницу"
            assert order_id in order_detail.get_current_url(), \
                f"BUG: URL не содержит ID заказа {order_id}"

    @allure.title("Прямой переход по URL на деталь заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_direct_url_navigation(self, fresh_authenticated_page, get_first_order_id):
        """BUG: Прямой переход по URL не работает."""
        with allure.step("Переход на страницу деталей заказа по прямому URL"):
            page = fresh_authenticated_page
            order_id = get_first_order_id
            order_detail = OrderDetailPage(page)
            order_detail.navigate_to_order_detail(order_id)

        with allure.step("Проверка что страница деталей заказа загрузилась"):
            assert order_detail.is_on_order_detail_page(), \
                "BUG: Прямой URL не открыл страницу деталей"
            assert order_detail.is_page_loaded(), \
                "BUG: Страница не загрузилась после прямого перехода"

    @allure.title("Кнопка 'Назад' возвращает к списку заказов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_back_button_returns_to_list(self, order_detail_page: OrderDetailPage):
        """BUG: Кнопка назад не возвращает к списку."""
        page = order_detail_page.page

        with allure.step("Проверка видимости кнопки 'Назад'"):
            if order_detail_page.back_button.is_visible(timeout=3000):
                with allure.step("Нажатие на кнопку 'Назад'"):
                    order_detail_page.navigate_back_to_list()
                    page.wait_for_load_state("networkidle")
                with allure.step("Проверка что вернулись к списку заказов"):
                    current_url = page.url
                    assert "/orders" in current_url, \
                        f"BUG: Кнопка назад не вернула к списку. URL: {current_url}"

    @allure.title("Кнопка 'Назад' браузера работает корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_browser_back_button(self, fresh_authenticated_page, get_first_order_id):
        """BUG: Кнопка браузера назад не работает."""
        with allure.step("Переход на страницу списка заказов"):
            page = fresh_authenticated_page
            order_id = get_first_order_id
            orders_page = OrdersPage(page)
            order_detail = OrderDetailPage(page)
            orders_page.navigate()
            page.wait_for_load_state("networkidle")

        with allure.step("Переход на страницу деталей заказа"):
            order_detail.navigate_to_order_detail(order_id)
            assert order_detail.is_on_order_detail_page()

        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            page.go_back()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что вернулись к списку заказов"):
            current_url = page.url
            assert "/orders" in current_url and f"/orders/{order_id}" not in current_url, \
                f"BUG: Browser back не сработал. URL: {current_url}"

    @allure.title("Обновление страницы сохраняет данные")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refresh_preserves_page(self, order_detail_page: OrderDetailPage):
        """BUG: Обновление страницы теряет данные."""
        with allure.step("Сохранение текущего URL перед обновлением"):
            page = order_detail_page.page
            initial_url = order_detail_page.get_current_url()

        with allure.step("Обновление страницы"):
            page.reload()
            page.wait_for_load_state("networkidle")
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что URL и данные сохранились после обновления"):
            after_url = order_detail_page.get_current_url()
            assert initial_url == after_url, \
                f"BUG: URL изменился после refresh. До: {initial_url}, После: {after_url}"
            assert order_detail_page.is_page_loaded(), \
                "BUG: Страница не загрузилась после refresh"



@allure.epic("Заказы")
@allure.suite("Детали заказа — Манипуляция URL")
@allure.feature("Безопасность URL")
@pytest.mark.security
class TestOrderDetailURLManipulation:
    """Тесты манипуляции URL и невалидных ID заказов."""

    @allure.title("Невалидный ID заказа обрабатывается корректно")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_order_id_handled(self, fresh_authenticated_page):
        """BUG: Невалидный ID заказа не обрабатывается."""
        with allure.step("Переход на страницу заказа с невалидным ID"):
            page = fresh_authenticated_page
            order_detail = OrderDetailPage(page)
            invalid_id = "invalid-uuid-12345"
            order_detail.navigate_to_order_detail(invalid_id)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что данные реального заказа не отображаются"):
            products_table = page.locator(".MuiDataGrid-root, table").first
            has_products = products_table.is_visible() and products_table.locator("tr, .MuiDataGrid-row").count() > 0

            if has_products:
                body_text = page.text_content("body") or ""
                assert "product" not in body_text.lower() or "error" in body_text.lower(), \
                    f"BUG: Невалидный ID '{invalid_id}' показывает данные заказа!"

    @allure.title("ID заказа '0' не раскрывает данные")
    @allure.severity(allure.severity_level.NORMAL)
    def test_zero_order_id_handled(self, fresh_authenticated_page):
        """BUG: ID заказа '0' раскрывает данные."""
        with allure.step("Переход на страницу заказа с ID '0'"):
            page = fresh_authenticated_page
            order_detail = OrderDetailPage(page)
            order_detail.navigate_to_order_detail("0")
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что данные реальных заказов не раскрываются"):
            body_text = page.text_content("body") or ""
            order_data_indicators = page.locator(".MuiDataGrid-row, table tr[data-id]")
            has_real_data = order_data_indicators.count() > 0
            assert not has_real_data, \
                "BUG: ID '0' показывает данные заказа (возможная IDOR)"

    @allure.title("XSS через URL блокируется")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_xss_in_url_blocked(self, fresh_authenticated_page):
        """BUG: XSS через URL не блокируется."""
        with allure.step("Переход на страницу заказа с XSS payload в URL"):
            page = fresh_authenticated_page
            order_detail = OrderDetailPage(page)
            xss_payload = "<script>alert('XSS')</script>"
            order_detail.navigate_to_order_detail(xss_payload)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что XSS скрипт не исполнился"):
            page_content = page.content()
            assert "<script>alert" not in page_content, \
                "BUG: XSS payload исполнился!"

    @allure.title("SQL injection через URL не вызывает ошибку БД")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sql_injection_in_url_safe(self, fresh_authenticated_page):
        """BUG: SQL injection через URL вызывает ошибку БД."""
        with allure.step("Переход на страницу заказа с SQL injection payload в URL"):
            page = fresh_authenticated_page
            order_detail = OrderDetailPage(page)
            sql_payload = "'; DROP TABLE orders; --"
            order_detail.navigate_to_order_detail(sql_payload)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что ошибки БД не раскрываются"):
            page_text = page.text_content("body") or ""
            db_errors = ["SQL", "database", "syntax error", "mysql", "postgres"]
            for error in db_errors:
                assert error.lower() not in page_text.lower(), \
                    f"BUG: SQL injection раскрыл ошибку БД: '{error}'"

    @allure.title("Path traversal через URL блокируется")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_path_traversal_blocked(self, fresh_authenticated_page):
        """BUG: Path traversal через URL раскрывает системные файлы."""
        with allure.step("Переход на страницу заказа с path traversal payload в URL"):
            page = fresh_authenticated_page
            order_detail = OrderDetailPage(page)
            traversal_payload = "../../../etc/passwd"
            order_detail.navigate_to_order_detail(traversal_payload)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что системный контент не раскрыт"):
            body_text = page.text_content("body") or ""
            sensitive_content = ["root:", "bin:", "daemon:", "/bin/bash", "/bin/sh"]
            for content in sensitive_content:
                assert content not in body_text, \
                    f"BUG: Path traversal раскрыл системный контент: '{content}'"



@allure.epic("Заказы")
@allure.suite("Детали заказа — Безопасность")
@allure.feature("Безопасность")
@pytest.mark.security
class TestOrderDetailSecurity:
    """Тесты безопасности страницы деталей заказа."""

    @allure.title("Неавторизованный доступ редиректит на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthorized_access_redirects(self, browser):
        """BUG: Неавторизованный доступ не редиректит на логин."""
        with allure.step("Открытие страницы деталей заказа без авторизации"):
            context = browser.new_context()
            page = context.new_page()
            fake_order_id = "24b52350-645e-4daf-83a8-19f16ef853c3"
            page.goto(
                f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders/{fake_order_id}",
                wait_until="networkidle", timeout=15000
            )
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что произошёл редирект на страницу логина"):
            current_url = page.url
            assert "/login" in current_url or "/auth" in current_url, \
                f"BUG: Неавторизованный доступ не редиректит. URL: {current_url}"

            context.close()

    @allure.title("Доступ к заказам другого продавца заблокирован")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_other_seller_order_blocked(self, fresh_authenticated_page):
        """BUG: Можно получить доступ к заказам другого продавца."""
        with allure.step("Переход на страницу заказа с несуществующим UUID"):
            page = fresh_authenticated_page
            order_detail = OrderDetailPage(page)
            fake_order_id = "00000000-0000-0000-0000-000000000000"
            order_detail.navigate_to_order_detail(fake_order_id)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что доступ к чужому заказу заблокирован"):
            current_url = order_detail.get_current_url()
            if fake_order_id in current_url:
                error_msg = page.locator("text=/not found|no access|forbidden|access denied|не найден|нет доступа|запрещено|topilmadi|ruxsat yo'q/i").first
                has_error = error_msg.is_visible(timeout=2000)
                assert has_error or not order_detail.is_page_loaded(), \
                    "BUG: Доступ к чужому заказу без ошибки!"

    @allure.title("Токен авторизации не виден в URL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_token_in_url(self, order_detail_page: OrderDetailPage):
        """BUG: Токен авторизации виден в URL."""
        with allure.step("Получение текущего URL страницы"):
            url = order_detail_page.page.url
        with allure.step("Проверка что URL не содержит токенов авторизации"):
            sensitive = ["token=", "jwt=", "session=", "auth=", "api_key="]
            for pattern in sensitive:
                assert pattern not in url.lower(), \
                    f"BUG: URL содержит '{pattern}': {url}"

    @allure.title("Истекшая сессия обрабатывается корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_session_expired_handled(self, order_detail_page: OrderDetailPage):
        """BUG: Истекшая сессия не обрабатывается."""
        with allure.step("Очистка cookies для имитации истекшей сессии"):
            page = order_detail_page.page
            page.context.clear_cookies()
            page.wait_for_load_state("networkidle")

        with allure.step("Перезагрузка страницы после очистки сессии"):
            page.reload()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что произошёл редирект на логин или показана ошибка"):
            current_url = page.url
            is_on_login = "/login" in current_url or "/auth" in current_url
            if not is_on_login:
                order_detail = OrderDetailPage(page)
                assert not order_detail.is_page_loaded(), \
                    "BUG: Истекшая сессия не редиректит и не показывает ошибку"
