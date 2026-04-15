# Feature Specification: Orders Management

**Feature ID**: 007-orders
**Created**: 2025-12-21
**Status**: Implemented

## Overview

Comprehensive order management with list view, filtering, search, and detail pages. Based on Qase.io test cases 1269-1298.

## User Stories

### US1: Orders List (P1)
**As an** admin user
**I want to** view orders list
**So that I** can manage customer orders

**Acceptance Criteria**:
- Orders list loads with all columns
- Statistics cards visible (New, Paid, Delivered, Returns, Cancelled)
- Table shows ID, Status, Date, Customer, Qty, Amount, Payment, Delivery

### US2: Search & Filter (P1)
**As an** admin user
**I want to** search and filter orders
**So that I** can find specific orders

**Acceptance Criteria**:
- Search by order ID works
- Search by customer name works
- Status tabs filter orders (13 statuses)
- Payment method filter works
- Delivery type filter works
- Date range filter works

### US3: Pagination (P1)
**As an** admin user
**I want to** navigate order pages
**So that I** can view all orders

**Acceptance Criteria**:
- Pagination visible at bottom
- Can navigate next/previous
- Can change page size

### US4: Order Details (P1)
**As an** admin user
**I want to** view order details
**So that I** can see complete order information

**Acceptance Criteria**:
- Click order opens detail page
- Shows products section
- Shows customer info
- Shows payment details
- Shows delivery info
- Print button available

### US5: Order History (P2)
**As an** admin user
**I want to** view order history
**So that I** can track status changes

**Acceptance Criteria**:
- History section visible
- Export button available

## Functional Requirements

| ID | Requirement | Priority | Qase ID |
|----|-------------|----------|---------|
| FR-001 | System shall display orders list | P1 | 1269 |
| FR-002 | System shall search by ID | P1 | 1270 |
| FR-003 | System shall search by customer | P1 | 1271 |
| FR-004 | System shall filter by status | P1 | 1272 |
| FR-005 | System shall filter by payment | P1 | 1273 |
| FR-006 | System shall filter by delivery | P1 | 1274 |
| FR-007 | System shall filter by date | P1 | 1275 |
| FR-008 | System shall paginate orders | P1 | 1276 |
| FR-009 | System shall sort by date | P1 | 1277 |
| FR-010 | System shall show order details | P1 | 1278 |

## Test Coverage

| Test Class | Tests | Qase IDs |
|------------|-------|----------|
| TestOrdersListLoads | 2 | 1269 |
| TestOrdersSearch | 2 | 1270-1271 |
| TestOrdersStatusFilter | 2 | 1272 |
| TestOrdersPaymentFilter | 1 | 1273 |
| TestOrdersDeliveryFilter | 1 | 1274 |
| TestOrdersDateFilter | 1 | 1275 |
| TestOrdersPagination | 2 | 1276 |
| TestOrdersSorting | 1 | 1277 |
| TestOrderDetailView | 7 | 1278-1285 |
| TestOrderHistory | 1 | - |
| TestOrderExport | 1 | 1298 |
| TestOrderStatusDisplay | 4 | 1283-1293 |
| TestOrdersListAdditional | 5 | - |

**Total Tests**: 30
**Page Objects**: `pages/orders_list_page.py`, `pages/order_detail_page.py`
**Test File**: `tests/test_orders.py`

## Status Tabs

13 order statuses:
1. Все
2. Черновик
3. В обработке
4. Сборка
5. Упаковка
6. Упакован
7. Отправка
8. Отправлен
9. В пути
10. Доставлен
11. Отменен
12. Не удалось
13. Возврат
