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
@allure.suite("Детали заказа — Товары")
@allure.feature("Таблица товаров")
@pytest.mark.functional
class TestOrderDetailProducts:
    """Тесты таблицы товаров в деталях заказа."""

    @allure.title("Таблица товаров содержит данные")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_products_table_has_data(self, order_detail_page: OrderDetailPage):
        """BUG: Таблица товаров пустая."""
        with allure.step("Проверка видимости таблицы товаров"):
            assert order_detail_page.is_products_table_visible(), \
                "BUG: Таблица товаров не видна"

        with allure.step("Проверка что таблица товаров содержит данные"):
            products_count = order_detail_page.get_products_count()
            assert products_count > 0, \
                f"BUG: Таблица товаров пустая (count: {products_count})"

    @allure.title("Колонки таблицы товаров присутствуют")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_columns_exist(self, order_detail_page: OrderDetailPage):
        """BUG: Колонки таблицы товаров отсутствуют."""
        with allure.step("Проверка видимости таблицы товаров"):
            page = order_detail_page.page
            table = order_detail_page.products_table
            assert table.is_visible(timeout=3000), "BUG: Таблица товаров не видна"

        with allure.step("Получение заголовков колонок таблицы"):
            headers = page.locator("table th, [role='columnheader']")
            assert headers.count() > 0, "BUG: Заголовки таблицы отсутствуют"
            header_texts = [h.inner_text().lower() for h in headers.all() if h.is_visible()]

        with allure.step("Проверка наличия обязательных колонок (Price, Qty, Total)"):
            has_price = any("price" in h or "цена" in h for h in header_texts)
            has_qty = any("qty" in h or "quantity" in h or "кол" in h for h in header_texts)
            has_total = any("total" in h or "sum" in h or "итог" in h for h in header_texts)

            assert has_price, f"BUG: Колонка Price не найдена. Заголовки: {header_texts}"
            assert has_qty, f"BUG: Колонка Qty не найдена. Заголовки: {header_texts}"
            assert has_total, f"BUG: Колонка Total не найдена. Заголовки: {header_texts}"



@allure.epic("Заказы")
@allure.suite("Детали заказа — Действия")
@allure.feature("Кнопки действий")
@pytest.mark.functional
class TestOrderDetailActions:
    """Тесты кнопок действий на странице деталей заказа."""

    @allure.title("Кнопка печати кликабельна")
    @allure.severity(allure.severity_level.NORMAL)
    def test_print_button_clickable(self, order_detail_page: OrderDetailPage):
        """BUG: Кнопка печати не кликабельна."""
        with allure.step("Проверка видимости и доступности кнопки печати"):
            assert order_detail_page.print_button.is_visible(timeout=3000), \
                "BUG: Кнопка печати не видна"
            assert order_detail_page.print_button.is_enabled(timeout=2000), \
                "BUG: Кнопка печати отключена"

        with allure.step("Нажатие на кнопку печати"):
            order_detail_page.click_print()
            order_detail_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка что остались на странице заказа после печати"):
            current_url = order_detail_page.get_current_url()
            assert "/orders/" in current_url, \
                "BUG: Клик на печать увёл со страницы заказа"

    @allure.title("Кнопка отмены заказа в правильном состоянии")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_order_button_state(self, order_detail_page: OrderDetailPage):
        """BUG: Кнопка отмены заказа в неправильном состоянии."""
        with allure.step("Проверка состояния кнопки отмены заказа"):
            cancel_btn = order_detail_page.cancel_order_button
            if cancel_btn.count() > 0 and cancel_btn.is_visible(timeout=2000):
                with allure.step("Проверка что кнопка отмены активна"):
                    assert cancel_btn.is_enabled(timeout=2000), \
                        "BUG: Кнопка отмены видна но отключена"

    @allure.title("Кнопка возврата в правильном состоянии")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refund_button_state(self, order_detail_page: OrderDetailPage):
        """BUG: Кнопка возврата в неправильном состоянии."""
        with allure.step("Проверка состояния кнопки возврата"):
            refund_btn = order_detail_page.refund_button
            if refund_btn.count() > 0 and refund_btn.is_visible(timeout=2000):
                with allure.step("Проверка что кнопка возврата активна"):
                    assert refund_btn.is_enabled(timeout=2000), \
                        "BUG: Кнопка возврата видна но отключена"

    @allure.title("Кнопка обновления статуса в правильном состоянии")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_status_button_state(self, order_detail_page: OrderDetailPage):
        """BUG: Кнопка обновления статуса в неправильном состоянии."""
        with allure.step("Проверка состояния кнопки обновления статуса"):
            update_btn = order_detail_page.update_status_button
            if update_btn.count() > 0 and update_btn.is_visible(timeout=2000):
                with allure.step("Проверка что кнопка обновления статуса активна"):
                    assert update_btn.is_enabled(timeout=2000), \
                        "BUG: Кнопка обновления статуса видна но отключена"



@allure.epic("Заказы")
@allure.suite("Детали заказа — Устойчивость")
@allure.feature("Устойчивость")
@pytest.mark.regression
class TestOrderDetailRobustness:
    """Тесты устойчивости страницы деталей заказа."""

    @allure.title("Множественные обновления не ломают страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_multiple_refresh(self, order_detail_page: OrderDetailPage):
        """BUG: Множественные refresh ломают страницу."""
        with allure.step("Выполнение 3 последовательных обновлений страницы"):
            page = order_detail_page.page
            for _ in range(3):
                page.reload()
                page.wait_for_load_state("networkidle")

        with allure.step("Проверка что страница работает после множественных обновлений"):
            assert order_detail_page.is_on_order_detail_page(), \
                "BUG: Страница сломалась после множественных refresh"
            assert order_detail_page.is_page_loaded(), \
                "BUG: Страница не загрузилась после refresh"

    @allure.title("Двойной клик на печать не ломает страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_double_click_print(self, order_detail_page: OrderDetailPage):
        """BUG: Двойной клик на печать ломает страницу."""
        page = order_detail_page.page

        with allure.step("Проверка видимости кнопки печати"):
            if order_detail_page.print_button.is_visible(timeout=3000):
                with allure.step("Двойной клик на кнопку печати"):
                    order_detail_page.print_button.dblclick()
                    page.wait_for_load_state("networkidle")

                with allure.step("Проверка что страница не сломалась после двойного клика"):
                    assert order_detail_page.is_on_order_detail_page(), \
                        "BUG: Двойной клик сломал страницу"

    @allure.title("Страница работает после простоя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_after_idle(self, order_detail_page: OrderDetailPage):
        """BUG: Страница не работает после простоя."""
        with allure.step("Ожидание простоя страницы"):
            page = order_detail_page.page
            page.wait_for_load_state("networkidle", timeout=10000)

        with allure.step("Попытка взаимодействия с кнопкой печати после простоя"):
            if order_detail_page.print_button.is_visible(timeout=3000):
                order_detail_page.print_button.click()
                page.wait_for_load_state("networkidle")

        with allure.step("Проверка что страница работает после простоя"):
            assert order_detail_page.is_on_order_detail_page(), \
                "BUG: Страница не работает после простоя"



@allure.epic("Заказы")
@allure.suite("Детали заказа — Параллелизм")
@allure.feature("Параллельный доступ")
@pytest.mark.regression
class TestOrderDetailConcurrent:
    """Тесты параллельного доступа к странице деталей заказа."""

    @allure.title("Несколько вкладок с одним заказом работают независимо")
    @allure.severity(allure.severity_level.NORMAL)
    def test_multiple_tabs_same_order(self, order_detail_page: OrderDetailPage):
        """BUG: Несколько вкладок с одним заказом ломают друг друга."""
        with allure.step("Получение ID заказа из текущей вкладки"):
            page = order_detail_page.page
            order_id = order_detail_page.get_current_order_id_from_url()

        with allure.step("Открытие второй вкладки с тем же заказом"):
            page2 = page.context.new_page()
            order_detail2 = OrderDetailPage(page2)
            order_detail2.navigate_to_order_detail(order_id)

        with allure.step("Проверка что обе вкладки работают независимо"):
            assert order_detail_page.is_on_order_detail_page(), \
                "BUG: Первая вкладка сломалась"
            assert order_detail2.is_on_order_detail_page(), \
                "BUG: Вторая вкладка не загрузилась"
            page2.close()

    @allure.title("Страница восстанавливается после сетевой ошибки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_state_after_network_error(self, order_detail_page: OrderDetailPage):
        """BUG: Страница не восстанавливается после сетевой ошибки."""
        with allure.step("Блокировка сетевых запросов"):
            page = order_detail_page.page
            page.route("**/*", lambda route: route.abort())
            page.wait_for_load_state("networkidle")

        with allure.step("Разблокировка сетевых запросов"):
            page.unroute("**/*")
            page.wait_for_load_state("networkidle")

        with allure.step("Перезагрузка страницы после восстановления сети"):
            page.reload()
            page.wait_for_load_state("networkidle")
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что страница восстановилась"):
            assert order_detail_page.is_on_order_detail_page(), \
                "BUG: Страница не восстановилась после сетевой ошибки"
