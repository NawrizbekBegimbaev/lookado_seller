# Implementation Plan: Returns Test Automation

**Branch**: `001-returns-tests` | **Date**: 2025-12-20 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-returns-tests/spec.md`

## Summary

Implement end-to-end test automation for Returns management feature in Greatmall Admin Panel. This includes creating Page Object classes for Returns list and detail pages, and comprehensive test coverage for 35 Qase.io test cases (1623-1657). Tests cover navigation, search/filter, CRUD operations (approve, reject, refund), history, and image management.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Playwright for Python, pytest, pytest-playwright
**Storage**: N/A (UI test automation, no database)
**Testing**: pytest with Playwright assertions
**Target Platform**: Web (Chromium browser)
**Project Type**: Single project - Test automation suite
**Performance Goals**: Tests complete within 30 minutes for full suite
**Constraints**: No hard-coded waits (Playwright auto-waiting), session-scoped browser
**Scale/Scope**: 35 test cases organized into ~8 test classes

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| P1: KISS | ✅ PASS | Simple page objects, explicit test methods |
| P2: SOLID | ✅ PASS | Single responsibility per page object class |
| P3: Page Object Model | ✅ PASS | ReturnsPage + ReturnDetailPage classes |
| P4: DRY | ✅ PASS | Shared base class, reusable fixtures |
| P5: Code Size (<500 lines) | ✅ PASS | Split into returns_page.py + test_returns.py |
| P6: Playwright Python | ✅ PASS | Using Playwright for Python |
| P7: Iterative Development | ✅ PASS | Following speckit workflow |
| P8: Session Management | ✅ PASS | Using logged_in_page fixture |
| P9: Class-Based Tests | ✅ PASS | Test classes per feature category |
| P10: Explicit Refactoring | ✅ PASS | New files, no refactoring needed |

## Project Structure

### Documentation (this feature)

```text
specs/001-returns-tests/
├── spec.md              # Feature specification (done)
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── checklists/
│   └── requirements.md  # Spec quality checklist (done)
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
Greatmall_Adminpanel/
├── pages/
│   ├── base_page.py              # Existing base class
│   ├── returns_page.py           # NEW: Returns list page object
│   └── return_detail_page.py     # NEW: Return detail page object
├── tests/
│   ├── conftest.py               # Existing fixtures
│   └── test_returns.py           # NEW: Returns test suite
└── utils/
    └── constants.py              # Existing constants
```

**Structure Decision**: Following existing project structure with Page Object Model. Creating two page objects (returns_page.py for list, return_detail_page.py for details) and one test file (test_returns.py) with multiple test classes organized by feature category.

## File Specifications

### pages/returns_page.py (~300 lines)

**Purpose**: Page object for Returns list page

**Locators**:
- Page title: "Список возвратов"
- Search input: placeholder "Поиск по ID..."
- Status tabs: 11 tabs (Все, На рассмотрении, etc.)
- Date filters: "Диапазон от", "Диапазон до"
- Export button
- Filters button
- Returns grid/table
- Pagination controls

**Methods**:
- `navigate()` - Direct navigation to returns URL
- `navigate_from_dashboard()` - Navigate via sidebar
- `is_on_returns_list_page()` - URL verification
- `search_return(query)` - Search by ID
- `clear_search()` - Clear search field
- `select_status_tab(tab_name)` - Select filter tab
- `get_selected_status_tab()` - Get current tab
- `is_tab_selected(tab_name)` - Check tab selection
- `set_date_from(day, month, year)` - Set date filter
- `set_date_to(day, month, year)` - Set date filter
- `click_export()` - Export functionality
- `open_filters()` - Open filter panel
- `get_total_returns_count()` - Get count from pagination
- `get_return_rows()` - Get table rows
- `get_return_row_count()` - Count visible rows
- `click_return_by_id(return_id)` - Open detail by ID
- `click_return_by_index(index)` - Open detail by row index
- `get_return_status_by_index(index)` - Get status from row
- `get_return_id_by_index(index)` - Get ID from row
- `sort_by_column(column_name)` - Sort by column
- Pagination methods: `go_to_next_page()`, `go_to_previous_page()`, `go_to_page(n)`, `select_page_size(size)`

### pages/return_detail_page.py (~250 lines)

**Purpose**: Page object for Return detail page

**Locators**:
- Back button
- Return title: "Возврат №{id}"
- Status badge
- Products section: "Товары"
- Product info section: reason, comment
- Summary section: amount, commission, total
- History section with export
- Customer section
- Store section
- Action buttons: Approve, Reject, Refund
- Confirmation modals
- Image gallery

**Methods**:
- `get_return_title()` - Get title text
- `get_return_number()` - Extract number from title
- `get_status()` - Get current status
- `get_return_date()` - Get date
- `get_return_reason()` - Get reason text
- `get_customer_comment()` - Get comment
- `get_total_to_return()` - Get refund amount
- `get_customer_name()` - Get customer info
- `get_store_name()` - Get store info
- `click_back()` - Navigate back to list
- Section visibility checks
- `get_products_table()` - Get products
- `get_product_count()` - Count products
- Action methods: `click_approve()`, `click_reject()`, `click_refund()`
- Modal methods: `confirm_action()`, `cancel_action()`, `enter_reject_reason()`
- Image methods: `get_images()`, `click_image(index)`, `delete_image(index)`
- History methods: `get_history_entries()`, `export_history()`

### tests/test_returns.py (~400 lines)

**Purpose**: Comprehensive test suite for Returns feature

**Test Classes**:

1. `TestReturnsBase` - Base class with setup fixture
2. `TestReturnsNavigation` - Navigation and page load tests
3. `TestReturnsPagination` - Pagination journey tests
4. `TestReturnsSearch` - Search functionality tests
5. `TestReturnsFilter` - Status tab filter tests
6. `TestReturnsDetails` - Detail page tests
7. `TestReturnsActions` - Approve/Reject/Refund tests
8. `TestReturnsHistory` - History section tests
9. `TestReturnsImages` - Image management tests

**Test Methods** (mapped to Qase.io):
- test_01_return_list_loads (1623)
- test_02_pagination_works (1624)
- test_03_empty_state (1625)
- test_04_search_by_id (1626)
- test_05_filter_by_status (1627)
- test_06_open_return_details (1628)
- test_07_details_shows_order_info (1629)
- test_08_details_shows_items (1630)
- test_09_details_shows_images (1631)
- test_10_image_fullscreen (1632)
- test_11_delete_image_modal (1633)
- test_12_cancel_image_delete (1634)
- test_13_confirm_image_delete (1635)
- test_14_approve_button_visible (1636)
- test_15_approve_modal (1637)
- test_16_cancel_approve (1638)
- test_17_confirm_approve (1639)
- test_18_reject_requires_reason (1640)
- test_19_reject_with_reason (1641)
- test_20_refund_button_visible (1642)
- test_21_refund_modal (1643)
- test_22_refund_min_boundary (1644)
- test_23_refund_max_boundary (1645)
- test_24_successful_refund (1646)
- test_25_history_tab_visible (1647)
- test_26_history_logs_changes (1648)
- test_27_history_shows_actor (1649)
- test_28_unauthorized_no_approve (1650)
- test_29_unauthorized_blocked (1651)
- test_30_list_performance (1652)
- test_31_image_load_performance (1653)
- test_32_modal_response_ux (1654)
- test_33_status_colors (1655)
- test_34_cancel_refund (1656)
- test_35_no_duplicate_refund (1657)

## Complexity Tracking

> No violations - all principles satisfied

## Dependencies

- Existing `base_page.py` for inheritance
- Existing `conftest.py` for `logged_in_page` fixture
- Existing `utils/constants.py` for BASE_URL

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Actions may change return data | Use test returns that can be safely modified or mock data |
| Permission tests need different user | May need separate fixture or skip if not testable |
| Image upload not in scope | Test existing images only |