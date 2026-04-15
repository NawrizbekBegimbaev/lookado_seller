# Implementation Plan: Orders Management

**Feature**: 007-orders
**Created**: 2025-12-21
**Status**: Implemented

## Technical Context

| Aspect | Details |
|--------|---------|
| Framework | Playwright for Python + pytest |
| Architecture | Page Object Model (POM) |
| Environment | DEV (https://dev-admin.greatmall.uz/) |
| Fixture | `logged_in_page` (session-scoped) |
| Test Cases | Qase.io 1269-1298 |

## File Structure

```
Greatmall_Adminpanel/
├── pages/
│   ├── orders_list_page.py    # OrdersListPage class (15.0 KB)
│   └── order_detail_page.py   # OrderDetailPage class (12.2 KB)
└── tests/
    └── test_orders.py         # 30 tests in 13 classes (26.0 KB)
```

## Page Objects

### OrdersListPage
**Key Locators**:
- Page title: `get_by_role("heading", name="Список заказов")`
- Status tabs: 13 tabs
- Search input: Search field
- Filters button: Opens additional filters
- Grid: Order rows

**Key Methods**:
- `navigate()` / `navigate_from_dashboard()`
- `is_on_orders_list_page()`
- `search_order(query)`
- `select_status_tab(name)`
- `open_filters()`
- `select_payment_method(name)`
- `select_delivery_type(name)`
- `set_date_from(d, m, y)` / `set_date_to(d, m, y)`
- Pagination methods

### OrderDetailPage
**Key Methods**:
- `is_on_order_detail_page()`
- `get_order_title()`
- `click_back_button()`
- Section visibility checks

## Status Tabs

```python
ORDER_STATUS_TABS = [
    "Все", "Черновик", "В обработке", "Сборка", "Упаковка",
    "Упакован", "Отправка", "Отправлен", "В пути", "Доставлен",
    "Отменен", "Не удалось", "Возврат"
]
```

## Test Organization

### By Qase.io Test Cases
- **1269-1277**: Orders List Tests
- **1278-1285**: Order Detail Tests
- **1283-1284**: Status Display Tests
- **1290-1293**: Special Tab Tests
- **1298**: Export Tests

### Test Classes (13 total)
1. TestOrdersListLoads
2. TestOrdersSearch
3. TestOrdersStatusFilter
4. TestOrdersPaymentFilter
5. TestOrdersDeliveryFilter
6. TestOrdersDateFilter
7. TestOrdersPagination
8. TestOrdersSorting
9. TestOrderDetailView
10. TestOrderHistory
11. TestOrderExport
12. TestOrderStatusDisplay
13. TestOrdersListAdditional
