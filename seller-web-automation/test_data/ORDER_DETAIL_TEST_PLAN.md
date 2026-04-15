# Order Detail Page - План Тестирования

**Цель:** ~40 тестов для полного покрытия Order Detail страницы
**Файл:** `tests/test_order_detail.py`
**Page Object:** `pages/order_detail_page.py`
**Test Data:** `test_data/order_detail_test_data.json`

---

## Классы Тестов (40 тестов total)

### 1. TestOrderDetailUI (7 тестов)
**Фокус:** Видимость UI элементов, структура страницы

- [x] test_page_title_visible - Заголовок страницы виден
- [x] test_order_id_displayed - Order ID отображается
- [x] test_status_badge_visible - Status badge виден
- [x] test_back_button_visible - Кнопка Back видна
- [x] test_products_table_visible - Таблица товаров видна
- [x] test_customer_info_section_visible - Секция Customer Info видна
- [x] test_action_buttons_visible - Кнопки действий видны

---

### 2. TestOrderDetailNavigation (6 тестов)
**Фокус:** Навигация между страницами

- [x] test_navigate_from_orders_list - Переход из Orders List
- [x] test_direct_url_navigation - Прямой переход по URL
- [x] test_back_button_navigation - Кнопка Back возвращает на Orders List
- [x] test_browser_back_button - Браузер Back работает
- [x] test_browser_forward_button - Браузер Forward работает
- [x] test_refresh_page_preserves_data - Refresh сохраняет данные

---

### 3. TestOrderDetailURLManipulation (5 тестов)
**Фокус:** Безопасность URL параметров

- [x] test_invalid_order_id - Невалидный Order ID
- [x] test_nonexistent_order - Несуществующий заказ
- [x] test_xss_in_url - XSS payload в URL
- [x] test_sql_injection_in_url - SQL injection в URL
- [x] test_path_traversal_in_url - Path traversal в URL

---

### 4. TestOrderDetailSecurity (4 теста)
**Фокус:** Безопасность и авторизация

- [x] test_unauthorized_access - Доступ без авторизации
- [x] test_other_seller_order - Доступ к заказу другого продавца
- [x] test_session_expired - Истекшая сессия
- [x] test_csrf_protection - CSRF protection

---

### 5. TestOrderDetailTabs (4 теста)
**Фокус:** Вкладки (если есть Details, History, Products)

- [x] test_all_tabs_present - Все вкладки присутствуют
- [x] test_default_tab_active - Default вкладка активна
- [x] test_tab_switching - Переключение между вкладками
- [x] test_tab_url_update - URL обновляется при смене вкладки

---

### 6. TestOrderDetailProducts (3 теста)
**Фокус:** Таблица товаров в заказе

- [x] test_products_table_has_data - Таблица содержит товары
- [x] test_product_columns_visible - Все колонки видны (Name, Qty, Price)
- [x] test_empty_products_state - Пустое состояние (нет товаров)

---

### 7. TestOrderDetailActions (4 теста)
**Фокус:** Действия с заказом

- [x] test_update_status_button_click - Клик Update Status
- [x] test_cancel_order_button_click - Клик Cancel Order
- [x] test_print_button_click - Клик Print
- [x] test_refund_button_click - Клик Refund (если есть)

---

### 8. TestOrderDetailRobustness (4 теста)
**Фокус:** Устойчивость к нестандартным сценариям

- [x] test_slow_network_simulation - Медленная сеть
- [x] test_rapid_tab_switching - Быстрое переключение табов
- [x] test_page_after_long_idle - Страница после долгого idle
- [x] test_multiple_refresh - Множественные refresh

---

### 9. TestOrderDetailConcurrent (3 теста)
**Фокус:** Concurrent доступ

- [x] test_multiple_tabs_same_order - Один заказ в нескольких вкладках
- [x] test_state_after_network_error - Состояние после network error
- [x] test_order_update_in_another_tab - Обновление в другой вкладке

---

## ИТОГО: 40 тестов

```
TestOrderDetailUI:             7 тестов
TestOrderDetailNavigation:     6 тестов
TestOrderDetailURLManipulation: 5 тестов
TestOrderDetailSecurity:       4 теста
TestOrderDetailTabs:           4 теста
TestOrderDetailProducts:       3 теста
TestOrderDetailActions:        4 теста
TestOrderDetailRobustness:     4 теста
TestOrderDetailConcurrent:     3 теста
─────────────────────────────────────
TOTAL:                        40 тестов
```

---

## Приоритеты тестирования

**P0 (Critical):**
- UI elements visible
- Navigation works
- Security (unauthorized access, other seller order)
- Valid order ID loads correctly

**P1 (High):**
- URL manipulation protection
- Tabs switching
- Products table display
- Action buttons work

**P2 (Medium):**
- Robustness scenarios
- Concurrent access
- Empty states
- Browser back/forward

---

## Правила написания

1. **Fixture:** `order_detail_session` (session-scoped, логин один раз)
2. **Markers:** `@pytest.mark.smoke`, `@pytest.mark.functional`, `@pytest.mark.security`
3. **Assertions:** ЖЕСТКИЕ - `assert condition, "BUG: описание"`
4. **NO SKIPPED:** `pytest.fail()` вместо `pytest.skip()`
5. **Allure:** `@allure.title()`, `@allure.description()`, `@allure.severity()`

---

## После исследования страницы

После запуска `test_inspect_order_detail.py` и получения:
- `/tmp/order_detail_inspect.png` - скриншот
- `/tmp/order_detail_structure.json` - структура элементов
- `/tmp/order_detail_page.html` - HTML

Нужно:
1. Обновить `order_detail_page.py` - исправить локаторы
2. Обновить `order_detail_test_data.json` - реальные значения
3. Написать тесты на основе этого плана
4. Запустить тесты

---

## Ожидаемый результат

```bash
pytest tests/test_order_detail.py -v

tests/test_order_detail.py::TestOrderDetailUI::test_page_title_visible PASSED
tests/test_order_detail.py::TestOrderDetailUI::test_order_id_displayed PASSED
...
tests/test_order_detail.py::TestOrderDetailConcurrent::test_order_update_in_another_tab PASSED

======================== 40 passed in 3m 20s =========================
```

---

**Создано:** 2026-01-24
**Батыр (Session B):** Фаза 3 - Order Detail
