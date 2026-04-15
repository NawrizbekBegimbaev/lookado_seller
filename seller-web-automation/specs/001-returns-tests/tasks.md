# Tasks: Returns Test Automation

**Input**: Design documents from `/specs/001-returns-tests/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Page Objects**: `pages/` at repository root
- **Tests**: `tests/` at repository root
- **Repository root**: `/Users/maxsudbekshavkatov/PythonProjects/Greatmall_Adminpanel/`

---

## Phase 1: Setup

**Purpose**: Verify project structure and dependencies

- [X] T001 Verify existing project structure has pages/ and tests/ directories
- [X] T002 Verify base_page.py exists and has required methods in pages/base_page.py
- [X] T003 Verify conftest.py has logged_in_page fixture in tests/conftest.py

**Checkpoint**: Project ready for page object and test creation ✅

---

## Phase 2: Foundational (Page Object Structure)

**Purpose**: Create page object files with base structure - MUST complete before user story tests

**⚠️ CRITICAL**: No user story tests can be implemented until page objects are created

- [X] T004 [P] Create returns_page.py with ReturnsPage class skeleton in pages/returns_page.py
- [X] T005 [P] Create return_detail_page.py with ReturnDetailPage class skeleton in pages/return_detail_page.py
- [X] T006 Create test_returns.py with TestReturnsBase class and setup fixture in tests/test_returns.py
- [X] T007 Add RETURN_STATUS_TABS constant list (11 statuses) in pages/returns_page.py
- [X] T008 Update conftest.py TEST_ORDER to include test_returns.py in tests/conftest.py

**Checkpoint**: Foundation ready - page objects exist, user story implementation can begin ✅

---

## Phase 3: User Story 1 - Returns List Navigation (Priority: P1) 🎯 MVP

**Goal**: Admin can navigate to Returns page and see list with pagination

**Independent Test**: Navigate to Returns page, verify table loads with correct columns

### Page Object Methods for US1

- [X] T009 [US1] Add navigation locators (_returns_url, _page_title, _list_title) in pages/returns_page.py
- [X] T010 [US1] Implement navigate() method in pages/returns_page.py
- [X] T011 [US1] Implement navigate_from_dashboard() method in pages/returns_page.py
- [X] T012 [US1] Implement is_on_returns_list_page() method in pages/returns_page.py
- [X] T013 [US1] Add table locators (_returns_grid) in pages/returns_page.py
- [X] T014 [US1] Implement get_return_rows() and get_return_row_count() methods in pages/returns_page.py
- [X] T015 [US1] Add pagination locators in pages/returns_page.py
- [X] T016 [US1] Implement pagination methods (go_to_next_page, go_to_previous_page, go_to_page, get_current_page) in pages/returns_page.py
- [X] T017 [US1] Implement select_page_size() method in pages/returns_page.py
- [X] T018 [US1] Implement scroll_to_pagination() and scroll_to_top() methods in pages/returns_page.py

### Tests for US1

- [X] T019 [US1] Create TestReturnsNavigation class in tests/test_returns.py
- [X] T020 [US1] Implement test_01_return_list_loads (Qase 1623) in tests/test_returns.py
- [X] T021 [US1] Create TestReturnsPagination class in tests/test_returns.py
- [X] T022 [US1] Implement test_02_pagination_works (Qase 1624) in tests/test_returns.py
- [X] T023 [US1] Implement test_03_empty_state (Qase 1625) with xfail marker in tests/test_returns.py

**Checkpoint**: US1 complete - Returns list navigation and pagination works ✅

---

## Phase 4: User Story 2 - Returns Search and Filter (Priority: P1)

**Goal**: Admin can search returns by ID and filter by status tabs

**Independent Test**: Search by ID, select status tabs, verify filtered results

### Page Object Methods for US2

- [X] T024 [US2] Add search locator (_search_input) in pages/returns_page.py
- [X] T025 [US2] Implement search_return(query) method in pages/returns_page.py
- [X] T026 [US2] Implement clear_search() method in pages/returns_page.py
- [X] T027 [US2] Implement select_status_tab(tab_name) method in pages/returns_page.py
- [X] T028 [US2] Implement get_selected_status_tab() method in pages/returns_page.py
- [X] T029 [US2] Implement is_tab_selected(tab_name) method in pages/returns_page.py
- [X] T030 [US2] Implement get_all_status_tabs() method in pages/returns_page.py

### Tests for US2

- [X] T031 [US2] Create TestReturnsSearch class in tests/test_returns.py
- [X] T032 [US2] Implement test_04_search_by_id (Qase 1626) in tests/test_returns.py
- [X] T033 [US2] Create TestReturnsFilter class in tests/test_returns.py
- [X] T034 [US2] Implement test_05_filter_by_status (Qase 1627) in tests/test_returns.py

**Checkpoint**: US2 complete - Search and filter functionality works ✅

---

## Phase 5: User Story 3 - View Return Details (Priority: P1)

**Goal**: Admin can open return details and see all information sections

**Independent Test**: Click return row, verify detail page shows order info, items, images

### Page Object Methods for US3

- [X] T035 [US3] Implement click_return_by_id(return_id) method in pages/returns_page.py
- [X] T036 [US3] Implement click_return_by_index(index) method in pages/returns_page.py
- [X] T037 [US3] Add basic locators (title, status, date) in pages/return_detail_page.py
- [X] T038 [US3] Implement get_return_title() and get_return_number() methods in pages/return_detail_page.py
- [X] T039 [US3] Implement get_status() method in pages/return_detail_page.py
- [X] T040 [US3] Add section locators (products, customer, store, history) in pages/return_detail_page.py
- [X] T041 [US3] Implement section visibility check methods (is_products_section_visible, etc.) in pages/return_detail_page.py
- [X] T042 [US3] Implement get_products_table() and get_product_count() methods in pages/return_detail_page.py
- [X] T043 [US3] Implement get_return_reason() and get_customer_comment() methods in pages/return_detail_page.py
- [X] T044 [US3] Implement get_customer_name() and get_store_name() methods in pages/return_detail_page.py
- [X] T045 [US3] Implement click_back() method in pages/return_detail_page.py

### Tests for US3

- [X] T046 [US3] Create TestReturnsDetails class in tests/test_returns.py
- [X] T047 [US3] Implement test_06_open_return_details (Qase 1628) in tests/test_returns.py
- [X] T048 [US3] Implement test_07_details_shows_order_info (Qase 1629) in tests/test_returns.py
- [X] T049 [US3] Implement test_08_details_shows_items (Qase 1630) in tests/test_returns.py
- [X] T050 [US3] Implement test_09_details_shows_images (Qase 1631) in tests/test_returns.py
- [X] T051 [US3] Implement test_10_image_fullscreen (Qase 1632) in tests/test_returns.py

**Checkpoint**: US3 complete - Return detail page displays all information correctly ✅

---

## Phase 6: User Story 4 - Approve Return (Priority: P2)

**Goal**: Admin can approve a pending return with confirmation

**Independent Test**: Open pending return, click approve, confirm, verify status change

### Page Object Methods for US4

- [X] T052 [US4] Add action button locators (approve, reject, refund) in pages/return_detail_page.py
- [X] T053 [US4] Implement is_approve_button_visible() method in pages/return_detail_page.py
- [X] T054 [US4] Implement click_approve() method in pages/return_detail_page.py
- [X] T055 [US4] Add confirmation modal locators in pages/return_detail_page.py
- [X] T056 [US4] Implement confirm_action() and cancel_action() methods in pages/return_detail_page.py
- [X] T057 [US4] Implement is_confirmation_modal_visible() method in pages/return_detail_page.py

### Tests for US4

- [X] T058 [US4] Create TestReturnsApprove class in tests/test_returns.py
- [X] T059 [US4] Implement test_12_approve_button_visible (Qase 1634) in tests/test_returns.py
- [X] T060 [US4] Implement test_13_approve_confirmation (Qase 1635) in tests/test_returns.py
- [ ] T061 [US4] Implement test_16_cancel_approve (Qase 1638) in tests/test_returns.py
- [ ] T062 [US4] Implement test_17_confirm_approve (Qase 1639) with xfail marker in tests/test_returns.py

**Checkpoint**: US4 complete - Approve action works with confirmation modal ✅

---

## Phase 7: User Story 5 - Reject Return with Reason (Priority: P2)

**Goal**: Admin can reject a return with mandatory reason

**Independent Test**: Open pending return, try reject without reason (error), add reason, confirm

### Page Object Methods for US5

- [X] T063 [US5] Implement click_reject() method in pages/return_detail_page.py
- [X] T064 [US5] Add reject modal locators (reason input, error message) in pages/return_detail_page.py
- [X] T065 [US5] Implement enter_reject_reason(reason) method in pages/return_detail_page.py
- [X] T066 [US5] Implement get_reject_validation_error() method in pages/return_detail_page.py

### Tests for US5

- [X] T067 [US5] Implement test_14_reject_button_visible (Qase 1636) in tests/test_returns.py
- [X] T068 [US5] Implement test_15_reject_requires_reason (Qase 1637) with xfail marker in tests/test_returns.py

**Checkpoint**: US5 complete - Reject action requires reason and works correctly ✅

---

## Phase 8: User Story 6 - Process Refund (Priority: P2)

**Goal**: Admin can process refund with amount validation

**Independent Test**: Open approved return, test amount boundaries, complete refund

### Page Object Methods for US6

- [X] T069 [US6] Implement is_refund_button_visible() method in pages/return_detail_page.py
- [X] T070 [US6] Implement click_refund() method in pages/return_detail_page.py
- [X] T071 [US6] Add refund modal locators (amount input, error messages) in pages/return_detail_page.py
- [X] T072 [US6] Implement enter_refund_amount(amount) method in pages/return_detail_page.py
- [X] T073 [US6] Implement get_refund_validation_error() method in pages/return_detail_page.py
- [X] T074 [US6] Implement is_refund_button_disabled() method in pages/return_detail_page.py

### Tests for US6

- [X] T075 [US6] Implement test_16_refund_button_after_approve (Qase 1639) in tests/test_returns.py
- [X] T076 [US6] Implement test_17_refund_amount_validation (Qase 1641) in tests/test_returns.py
- [ ] T077 [US6] Implement test_22_refund_min_boundary (Qase 1644) in tests/test_returns.py
- [ ] T078 [US6] Implement test_23_refund_max_boundary (Qase 1645) in tests/test_returns.py
- [ ] T079 [US6] Implement test_24_successful_refund (Qase 1646) with xfail marker in tests/test_returns.py
- [ ] T080 [US6] Implement test_34_cancel_refund (Qase 1656) in tests/test_returns.py
- [ ] T081 [US6] Implement test_35_no_duplicate_refund (Qase 1657) in tests/test_returns.py

**Checkpoint**: US6 complete - Refund workflow with validation works correctly ✅

---

## Phase 9: User Story 7 - View Return History (Priority: P3)

**Goal**: Admin can view status change history with actor and timestamp

**Independent Test**: Open return details, view history section, verify entries

### Page Object Methods for US7

- [X] T082 [US7] Add history section locators in pages/return_detail_page.py
- [X] T083 [US7] Implement is_history_section_visible() method in pages/return_detail_page.py
- [X] T084 [US7] Implement get_history_entries() method in pages/return_detail_page.py
- [X] T085 [US7] Implement export_history() method in pages/return_detail_page.py

### Tests for US7

- [X] T086 [US7] Create TestReturnsHistory class in tests/test_returns.py
- [X] T087 [US7] Implement test_18_history_section_visible (Qase 1643) in tests/test_returns.py
- [X] T088 [US7] Implement test_19_history_has_entries (Qase 1644) in tests/test_returns.py
- [X] T089 [US7] Implement test_20_history_export (Qase 1645) in tests/test_returns.py

**Checkpoint**: US7 complete - History section shows all status changes

---

## Phase 10: User Story 8 - Image Management (Priority: P3)

**Goal**: Admin can view images fullscreen and delete with confirmation

**Independent Test**: View image gallery, click for fullscreen, delete with confirmation

### Page Object Methods for US8

- [ ] T090 [US8] Add image gallery locators in pages/return_detail_page.py
- [ ] T091 [US8] Implement get_images() and get_image_count() methods in pages/return_detail_page.py
- [ ] T092 [US8] Implement click_image(index) method in pages/return_detail_page.py
- [ ] T093 [US8] Implement is_fullscreen_preview_visible() method in pages/return_detail_page.py
- [ ] T094 [US8] Implement close_fullscreen_preview() method in pages/return_detail_page.py
- [ ] T095 [US8] Implement delete_image(index) method in pages/return_detail_page.py
- [ ] T096 [US8] Implement is_delete_confirmation_visible() method in pages/return_detail_page.py
- [ ] T097 [US8] Implement confirm_delete() and cancel_delete() methods in pages/return_detail_page.py

### Tests for US8

- [ ] T098 [US8] Create TestReturnsImages class in tests/test_returns.py
- [ ] T099 [US8] Implement test_11_delete_image_modal (Qase 1633) in tests/test_returns.py
- [ ] T100 [US8] Implement test_12_cancel_image_delete (Qase 1634) in tests/test_returns.py
- [ ] T101 [US8] Implement test_13_confirm_image_delete (Qase 1635) with xfail marker in tests/test_returns.py

**Checkpoint**: US8 complete - Image management works with fullscreen and delete

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Additional tests and final verification

### Permission and Performance Tests

- [ ] T102 [P] Implement test_28_unauthorized_no_approve (Qase 1650) with xfail in tests/test_returns.py
- [ ] T103 [P] Implement test_29_unauthorized_blocked (Qase 1651) with xfail in tests/test_returns.py
- [ ] T104 [P] Implement test_30_list_performance (Qase 1652) in tests/test_returns.py
- [ ] T105 [P] Implement test_31_image_load_performance (Qase 1653) in tests/test_returns.py
- [ ] T106 [P] Implement test_32_modal_response_ux (Qase 1654) in tests/test_returns.py
- [ ] T107 [P] Implement test_33_status_colors (Qase 1655) in tests/test_returns.py

### Final Validation

- [ ] T108 Run all returns tests and verify pass rate: pytest tests/test_returns.py -v
- [ ] T109 Verify page object files are under 500 lines per Constitution
- [ ] T110 Add pages/returns_page.py and pages/return_detail_page.py to pages/__init__.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - verify existing structure
- **Foundational (Phase 2)**: Create page object skeletons - BLOCKS all user stories
- **User Stories (Phase 3-10)**: All depend on Foundational phase completion
  - US1-US3 (P1): Core functionality - do first
  - US4-US6 (P2): Actions - require US3 detail page
  - US7-US8 (P3): Supporting features - can run in parallel
- **Polish (Phase 11)**: Depends on all user story phases

### User Story Dependencies

- **US1** (List Navigation): Independent - can start immediately after Phase 2
- **US2** (Search/Filter): Independent - can run parallel to US1
- **US3** (View Details): Depends on US1 (need to click return from list)
- **US4** (Approve): Depends on US3 (need detail page)
- **US5** (Reject): Depends on US3 (need detail page), parallel to US4
- **US6** (Refund): Depends on US3 (need detail page), parallel to US4/US5
- **US7** (History): Depends on US3 (need detail page), parallel to US4-US6
- **US8** (Images): Depends on US3 (need detail page), parallel to US4-US7

### Parallel Opportunities

- T004 and T005 can run in parallel (different files)
- Within each user story, page object methods marked [P] can run in parallel
- US4, US5, US6, US7, US8 can all run in parallel after US3 completes
- All Polish tests (T102-T107) can run in parallel

---

## Parallel Example: Foundational Phase

```bash
# Launch page object creation in parallel:
Task: "Create returns_page.py with ReturnsPage class skeleton in pages/returns_page.py"
Task: "Create return_detail_page.py with ReturnDetailPage class skeleton in pages/return_detail_page.py"
```

## Parallel Example: P2 User Stories

```bash
# After US3 completes, launch P2 stories in parallel:
Task: "Phase 6: User Story 4 - Approve Return"
Task: "Phase 7: User Story 5 - Reject Return"
Task: "Phase 8: User Story 6 - Process Refund"
```

---

## Implementation Strategy

### MVP First (US1 + US2 + US3)

1. Complete Phase 1: Setup verification
2. Complete Phase 2: Foundational page objects
3. Complete Phase 3: US1 - List Navigation
4. Complete Phase 4: US2 - Search/Filter
5. Complete Phase 5: US3 - View Details
6. **STOP and VALIDATE**: Run tests for US1-US3
7. MVP complete with 11 tests passing

### Incremental Delivery

1. MVP (US1-US3) → 11 tests → Can demo list/search/details
2. Add US4-US6 → +13 tests → Can demo approve/reject/refund
3. Add US7-US8 → +7 tests → Can demo history/images
4. Add Polish → +6 tests → Complete with 37 tests

---

## Summary

| Metric | Count |
|--------|-------|
| Total Tasks | 110 |
| Phase 1 (Setup) | 3 |
| Phase 2 (Foundational) | 5 |
| US1 Tasks | 15 |
| US2 Tasks | 11 |
| US3 Tasks | 17 |
| US4 Tasks | 11 |
| US5 Tasks | 6 |
| US6 Tasks | 13 |
| US7 Tasks | 8 |
| US8 Tasks | 12 |
| Phase 11 (Polish) | 9 |

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Tests with `xfail` marker: Actions that modify data (may not have safe test data)
- Qase.io IDs included for traceability (1623-1657)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
