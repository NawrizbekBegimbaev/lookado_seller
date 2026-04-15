# Research: Returns Test Automation

**Feature**: 001-returns-tests
**Date**: 2025-12-20

## Research Summary

This document consolidates research findings for the Returns test automation feature.

## UI Structure Research

### Returns List Page

**Decision**: Use `/dashboard/order-management/returns` as base URL

**Findings from Playwright MCP exploration**:
- Page URL: `https://dev-admin.greatmall.uz/dashboard/order-management/returns?page=1&size=10`
- Title heading: "Список возвратов" (level 6)
- Main heading: "Возвраты" (level 4)
- Search placeholder: "Поиск по ID..."

**Status Tabs (11 total)**:
1. Все (All) - default selected
2. На рассмотрении (Under Review)
3. Одобрено продавцом (Approved by Seller)
4. Отклонено продавцом (Rejected by Seller)
5. Помощь маркетплейса (Marketplace Help)
6. Одобрено маркетплейсом (Approved by Marketplace)
7. Отклонено маркетплейсом (Rejected by Marketplace)
8. Получено складом (Received by Warehouse)
9. Отклонено складом (Rejected by Warehouse)
10. Возвращено (Returned/Refunded)
11. Отменено (Cancelled)

**Table Columns**:
- ID (format: RMA + number, e.g., RMA39)
- Тип возврата (Return Type)
- Статус (Status)
- Дата (Date)
- Покупатель (Customer)
- Магазин (Store)
- Кол-во (Quantity)
- Сумма (сум) (Amount)

**Pagination**:
- Page size options via combobox
- Previous/Next buttons
- Page number buttons
- Total count display: "Всего: {n}"

### Return Detail Page

**Decision**: Use `/dashboard/order-management/returns/{id}` pattern

**Findings**:
- URL pattern: `/returns/{numeric_id}` (e.g., /returns/39)
- Title format: "Возврат №{id}"
- Date format: "19 дек. 2025, 11:50"
- Status displayed as badge

**Sections identified**:
1. Products table with columns: (product info), Цена, Кол-во, Сумма
2. Product info: name, SKU, Barcode
3. Return info: Причина возврата, Комментарий покупателя
4. Summary: Сумма, Комиссия, Итого к возврату
5. History section with export
6. Customer info
7. Store info with review time indicator

## Existing Patterns Research

### Decision: Follow existing page object patterns

**Rationale**: Project already has established patterns in orders_list_page.py and brands_page.py

**Patterns to reuse**:
- BasePage inheritance
- Private locators with underscore prefix
- Public methods for actions
- Type hints on all methods
- Docstrings following Google style
- `navigate()` and `navigate_from_dashboard()` pattern
- `is_on_*_page()` verification pattern
- Pagination helper methods

### Decision: Follow existing test patterns

**Rationale**: test_brands.py provides clear class-based structure

**Patterns to reuse**:
- TestBase class with autouse fixture
- Test classes by category (Navigation, Pagination, Search, etc.)
- pytest.mark decorators for filtering
- Numbered test methods for ordering
- Session-scoped logged_in_page fixture

## Technology Decisions

### Decision: Single test file with multiple classes

**Rationale**: 35 tests organized into 8-9 logical categories fits within 500 line limit

**Alternatives considered**:
- Multiple test files: Rejected (unnecessary complexity for 35 tests)
- Single monolithic class: Rejected (violates single responsibility)

### Decision: Two page object files

**Rationale**: List and Detail pages have distinct responsibilities

**Files**:
- `returns_page.py`: List page operations
- `return_detail_page.py`: Detail page operations

## Locator Strategy Research

### Decision: Use role-based locators where possible

**Rationale**: Playwright best practice, more resilient to UI changes

**Primary strategies**:
1. `get_by_role()` for buttons, tabs, headings, textboxes
2. `get_by_placeholder()` for search input
3. `get_by_text()` for labels and static text
4. `filter()` for refining selections

### Decision: Avoid CSS/XPath selectors

**Rationale**: Role-based locators are more maintainable and align with accessibility

## Test Data Considerations

### Decision: Use existing test returns in dev environment

**Rationale**: Dev environment has sample data (RMA30-RMA39 observed)

**Considerations**:
- Actions that modify state (approve/reject/refund) may need careful handling
- Some tests may need xfail markers if data not available
- Permission tests may need separate user or skip

## No Clarifications Needed

All technical decisions have been made based on:
1. Playwright MCP exploration of actual UI
2. Analysis of existing codebase patterns
3. Constitution requirements
4. Qase.io test case specifications
