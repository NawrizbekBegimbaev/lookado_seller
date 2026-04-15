# Feature Specification: Products Management

**Feature ID**: 006-products
**Created**: 2025-12-21
**Status**: Implemented

## Overview

Product listing and detail view functionality. Enables admins to view products by status, search, navigate details with multiple tabs, and manage product moderation.

## User Stories

### US1: Status Filtering (P1)
**As an** admin user
**I want to** filter products by status
**So that I** can view products in different states

**Acceptance Criteria**:
- 6 status tabs available: Все, Опубликован, Черновик, В архиве, На модерации, Прошел модерацию
- Clicking tab filters products
- Tab selection persists

### US2: Product Search (P1)
**As an** admin user
**I want to** search for products
**So that I** can find specific products

**Acceptance Criteria**:
- Search input accepts text
- Search filters product list
- Note: Search has known bug (marked xfail)

### US3: Product List (P1)
**As an** admin user
**I want to** scroll and view product list
**So that I** can see all products

**Acceptance Criteria**:
- Product cards display in grid
- Scrolling loads more products
- Product info visible on cards

### US4: Product Details (P1)
**As an** admin user
**I want to** view product details
**So that I** can see complete product information

**Acceptance Criteria**:
- Click product opens detail page
- Multiple tabs available (Info, Media, Moderation)
- Back button returns to list

### US5: Pagination (P2)
**As an** admin user
**I want to** navigate product pages
**So that I** can view all products

**Acceptance Criteria**:
- Pagination controls visible
- Page navigation works
- Page size can be changed

## Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-001 | System shall filter by 6 status types | P1 |
| FR-002 | System shall support product search | P1 |
| FR-003 | System shall display product cards | P1 |
| FR-004 | System shall show multi-tab details | P1 |
| FR-005 | System shall paginate product list | P2 |

## Test Coverage

| Test Class | Tests | Description |
|------------|-------|-------------|
| TestProductsStatusTabs | 1 | Status tab cycle |
| TestProductsSearch | 1 | Search (xfail) |
| TestProductsListScroll | 1 | Scroll and view |
| TestProductsDetail | 1 | Complete detail journey |
| TestProductsPagination | 2 | Page nav, size change |

**Total Tests**: ~6
**Page Objects**: `pages/products_list_page.py`, `pages/product_detail_page.py`
**Test File**: `tests/test_products.py`

## Known Issues

- Search functionality has a bug (does not filter results)
- Test marked with `@pytest.mark.xfail`
