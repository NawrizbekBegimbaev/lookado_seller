# Implementation Tasks: Comprehensive Code Review and Refactoring

**Feature Branch**: `001-code-review`
**Created**: 2025-12-10
**Status**: Ready for Implementation
**Plan**: [plan.md](plan.md) | **Spec**: [spec.md](spec.md)

---

## Overview

This task breakdown implements comprehensive refactoring of the Playwright + Python automation framework to resolve 11 major architectural issues. Tasks are organized by user story priority to enable independent, incremental delivery.

**Key Metrics**:
- Total Tasks: 58
- P1 (Blocker/Critical): 7 user stories → 35 tasks
- P2 (Medium): 2 user stories → 16 tasks
- Setup & Polish: 7 tasks
- Parallel Opportunities: 28 tasks marked [P]

**Strategy**: MVP-first approach focusing on P1 blockers (test isolation, locators, page objects, utils) to enable parallel execution and reduce maintenance burden by 80%.

---

## Phase 1: Setup & Prerequisites

**Goal**: Initialize project structure and verify existing components.

**Duration**: ~30 minutes

### Tasks

- [ ] T001 Verify existing utils/ directory structure (waits.py, test_data_loader.py, logger.py, browser_helpers.py, validators.py exist)
- [ ] T002 Verify existing config/ directory structure (settings.py exists with Settings dataclass)
- [ ] T003 [P] Install missing dependencies: pytest-xdist, mypy, black, flake8, jsonschema in requirements.txt
- [ ] T004 Create mypy.ini configuration file in project root with strict mode settings
- [ ] T005 [P] Create .pre-commit-config.yaml in project root with black, flake8, mypy hooks
- [ ] T006 Create test_data/schemas/ directory for JSON schema validation files
- [ ] T007 Create fixtures/ directory structure (browser_fixtures.py, auth_fixtures.py, data_fixtures.py placeholders)

**Completion Criteria**:
- All directories exist with correct structure
- requirements.txt updated with new dependencies
- Configuration files (mypy.ini, .pre-commit-config.yaml) created
- Project ready for refactoring tasks

---

## Phase 1.5: Product Creation Prerequisites (BLOCKING)

**Goal**: Fix product creation test by implementing shop selection logic.

**Duration**: ~30 minutes

**Why Blocking**: Product creation requires a "registered" shop to be selected. "Добавить товары" button is only visible when a registered shop is active.

### Tasks

- [ ] T075 [PRODUCT] Add `select_registered_shop(shop_name: str)` method to DashboardPage (pages/dashboard_page.py) - selects a specific shop from the dropdown menu
- [ ] T076 [PRODUCT] Add `ensure_registered_shop_selected()` method to ProductCreatePage (pages/productcreate_page.py) - checks if "Добавить товары" is visible, if not - opens shop dropdown and selects registered shop
- [ ] T077 [PRODUCT] Update `product_page` fixture in tests/test_productcreate.py to call `ensure_registered_shop_selected()` before clicking "Add Product"
- [ ] T078 [PRODUCT] Add shop selection data to test_data/productcreate_test_data.json (registered_shop_name field)

**Completion Criteria**:
- Product creation test passes with registered shop auto-selection
- "Добавить товары" button becomes visible after shop selection
- Test handles both registered and unregistered initial shop states

---

## Phase 2: Foundational Changes (Blocking Prerequisites)

**Goal**: Fix session-scoped fixtures to enable test isolation and parallel execution.

**Duration**: ~1-2 hours

**Why Blocking**: User Stories 1-7 all depend on test isolation. Must complete before any other refactoring.

### Tasks

- [ ] T008 [FOUNDATIONAL] Verify conftest.py fixtures: confirm context and page are already function-scoped (conftest.py:124, 154)
- [ ] T009 [FOUNDATIONAL] Verify authenticated_page fixture is function-scoped (conftest.py:260)
- [ ] T010 [FOUNDATIONAL] Run pytest -n 4 to verify parallel execution works without errors
- [ ] T011 [FOUNDATIONAL] Run pytest --random-order to verify test independence

**Completion Criteria**:
- conftest.py verified with function-scoped context/page fixtures
- Tests pass with `pytest -n 4` (parallel mode)
- Tests pass with `pytest --random-order` (random order)
- Test isolation confirmed (no state pollution)

**Independent Test**:
```bash
pytest tests/ -n 4 -v  # Should pass
pytest tests/ --random-order -v  # Should pass
```

---

## Phase 3: User Story 1 - Fix Session-Scoped Fixtures (P1 - BLOCKER)

**Story**: As a QA automation engineer, I need each test to run in isolation with its own browser context so that tests can run in parallel, state doesn't leak between tests, and debugging is straightforward.

**Status**: ✅ ALREADY COMPLETE (conftest.py already refactored in Phase 1)

**Acceptance Criteria**:
1. ✅ Tests running in parallel mode (pytest -n 4) pass with isolated browser context
2. ✅ test_login failure doesn't affect test_registration
3. ✅ Authenticated test completion leaves no cookies/localStorage for next test

### Tasks

- [ ] T012 [US1] Document fixture scoping in conftest.py with detailed docstrings explaining why function scope is critical
- [ ] T013 [US1] Add validation comment in conftest.py warning against changing context/page to session scope
- [ ] T014 [US1] Create test_fixtures.py to test fixture isolation (verify fresh context per test)

**Completion Criteria**:
- conftest.py documented with fixture scoping rationale
- Warning comments prevent future regressions
- test_fixtures.py validates isolation

**Independent Test**:
```bash
# Already passing from Phase 2
pytest tests/ -n 4 -v
```

---

## Phase 4: User Story 2 - Implement Robust Locator Strategy (P1 - CRITICAL)

**Story**: As a QA automation engineer, I need locators based on semantic attributes (ARIA roles, labels) instead of CSS classes so that tests remain stable when UI styling changes.

**Acceptance Criteria**:
1. Registration form error messages use `page.get_by_role("alert")` (stable after Material-UI updates)
2. Buttons use `page.get_by_role("button", name="...")` (stable after CSS changes)
3. 90%+ of locators use ARIA roles/labels, <10% use CSS as last resort

### Tasks

#### BasePage Refactoring
- [ ] T015 [P] [US2] Add type hints to all methods in pages/base_page.py
- [ ] T016 [P] [US2] Add comprehensive docstrings to all methods in pages/base_page.py
- [ ] T017 [P] [US2] Add automatic retry logic for stale elements in base_page.py fill_input method
- [ ] T018 [P] [US2] Add error context (element, action, expected vs actual) to all base_page.py error messages

#### RegistrationPage Refactoring
- [ ] T019 [US2] Replace CSS locator `.MuiFormHelperText-root.Mui-error` with `get_by_role("alert")` in pages/registration_page.py
- [ ] T020 [US2] Replace hardcoded Russian text locators with ARIA role + English accessible name in pages/registration_page.py
- [ ] T021 [US2] Convert all string locators to @property methods returning Locator objects in pages/registration_page.py
- [ ] T022 [US2] Add type hints to all methods in pages/registration_page.py
- [ ] T023 [US2] Add docstrings to all public methods in pages/registration_page.py

#### BecomeSellerPage Refactoring
- [ ] T024 [P] [US2] Replace brittle CSS locators with ARIA roles/labels in pages/becomeseller_page.py
- [ ] T025 [P] [US2] Convert all string locators to @property methods in pages/becomeseller_page.py
- [ ] T026 [P] [US2] Add type hints to all methods in pages/becomeseller_page.py
- [ ] T027 [P] [US2] Add docstrings to all public methods in pages/becomeseller_page.py

#### LoginPage Refactoring
- [ ] T028 [P] [US2] Review and refactor locators in pages/login_page.py (replace CSS with ARIA if needed)
- [ ] T029 [P] [US2] Add type hints to all methods in pages/login_page.py
- [ ] T030 [P] [US2] Add docstrings to all public methods in pages/login_page.py

**Completion Criteria**:
- All page objects use ARIA roles as primary locator strategy
- 90%+ locators are semantic (ARIA roles, labels, test IDs)
- All locators are @property methods returning Locator objects
- CSS locators only used as last resort with documented justification
- All methods have type hints and docstrings

**Independent Test**:
```bash
# Count CSS class selectors (should be <10%)
grep -r "\.Mui" pages/
grep -r "locator(\"\\." pages/

# Count ARIA role selectors (should be >90%)
grep -r "get_by_role" pages/ | wc -l

# Run tests after refactoring
pytest tests/test_registration.py -v
```

---

## Phase 5: User Story 3 - Remove Test Logic from Page Objects (P1 - HIGH)

**Story**: As a developer, I need page objects to only describe UI interactions, not contain test assertions, so that page objects are reusable and tests are clear.

**Acceptance Criteria**:
1. registration_page.py has 0 methods starting with "test_"
2. registration_page.py has 0 assert statements
3. test_registration.py contains all test logic with clear Allure steps

### Tasks

- [ ] T031 [US3] Remove test_empty_fields() method from pages/registration_page.py (move logic to tests/test_registration.py)
- [ ] T032 [US3] Remove test_invalid_phone_formats() method from pages/registration_page.py (move logic to tests/test_registration.py)
- [ ] T033 [US3] Remove all assert statements from pages/registration_page.py (convert to return bool verifications)
- [ ] T034 [US3] Refactor registration_page.py methods to return values instead of asserting (e.g., has_validation_error() -> bool)
- [ ] T035 [US3] Update tests/test_registration.py to use refactored page object methods with assertions in test methods
- [ ] T036 [US3] Add @allure.step() decorators to all test steps in tests/test_registration.py
- [ ] T037 [P] [US3] Review pages/becomeseller_page.py and remove any test methods or assertions
- [ ] T038 [P] [US3] Review all other page objects (login_page.py, etc.) and ensure no test logic exists

**Completion Criteria**:
- All page objects have 0 methods starting with "test_"
- All page objects have 0 assert statements
- Page objects only contain: locators (properties), actions (methods), verifications (return bool)
- All test logic moved to test files with clear Allure steps
- Tests still pass after refactoring

**Independent Test**:
```bash
# Verify no test methods in page objects
grep -r "def test_" pages/  # Should return 0 results

# Verify no assertions in page objects
grep -r "assert " pages/  # Should return 0 results

# Run tests
pytest tests/test_registration.py -v --alluredir=allure-results
```

---

## Phase 6: User Story 4 - Create Utils Directory Structure (P1 - HIGH)

**Story**: As a QA automation engineer, I need centralized utility modules (waits, locators, test data loading, logging) so that common operations are DRY and changes propagate automatically.

**Status**: ✅ PARTIALLY COMPLETE (utils/ already exists with modules)

**Acceptance Criteria**:
1. utils/ directory exists with: waits.py, test_data_loader.py, logger.py, browser_helpers.py, validators.py
2. Test data loading uses TestDataLoader with caching (not custom JSON loading)
3. Wait operations use SmartWaits utility (not duplicated logic)

### Tasks

- [ ] T039 [P] [US4] Add type hints to all functions in utils/waits.py
- [ ] T040 [P] [US4] Add docstrings to all functions in utils/waits.py
- [ ] T041 [P] [US4] Add type hints to all functions in utils/test_data_loader.py
- [ ] T042 [P] [US4] Add docstrings to all functions in utils/test_data_loader.py
- [ ] T043 [P] [US4] Add type hints to all functions in utils/browser_helpers.py
- [ ] T044 [P] [US4] Add docstrings to all functions in utils/browser_helpers.py
- [ ] T045 [P] [US4] Implement JSON schema validation in utils/validators.py using jsonschema library
- [ ] T046 [US4] Replace hardcoded time.sleep() with SmartWaits in pages/becomeseller_page.py
- [ ] T047 [US4] Replace hardcoded time.sleep() with SmartWaits in pages/registration_page.py
- [ ] T048 [US4] Update all page objects to use SmartWaits from utils/waits.py instead of duplicated wait logic

**Completion Criteria**:
- All utils/ modules have type hints and docstrings
- utils/validators.py implements JSON schema validation
- All page objects use centralized SmartWaits (no time.sleep())
- Code duplication reduced by 60%

**Independent Test**:
```bash
# Count time.sleep() usage (should be 0 in pages/)
grep -r "time.sleep" pages/  # Should return 0 results

# Count SmartWaits usage (should be >10 in pages/)
grep -r "SmartWaits" pages/ | wc -l

# Run mypy to verify type hints
mypy utils/
```

---

## Phase 7: User Story 5 - Standardize on Allure Reporting (P2 - MEDIUM)

**Story**: As a QA team lead, I need consistent test reporting in ONE system (Allure) so that results are clear, not split across two tools (Qase + Allure).

**Acceptance Criteria**:
1. test_registration.py uses @allure decorators (not @qase decorators)
2. requirements.txt has qase-pytest removed, only allure-pytest remains
3. CI/CD pipeline generates only Allure reports, uploads to Allure TestOps

### Tasks

- [ ] T049 [P] [US5] Remove qase-pytest from requirements.txt
- [ ] T050 [P] [US5] Remove all `from qase.pytest import qase` imports from test files
- [ ] T051 [P] [US5] Replace @qase.id decorators with @allure.id in tests/test_login.py
- [ ] T052 [P] [US5] Replace @qase.title decorators with @allure.title in tests/test_login.py
- [ ] T053 [P] [US5] Add missing Allure decorators (@allure.epic, @allure.feature, @allure.story) to all tests
- [ ] T054 [US5] Update .gitlab-ci.yml to remove Qase TestOps upload commands
- [ ] T055 [US5] Verify .gitlab-ci.yml only generates/uploads Allure reports to Allure TestOps

**Completion Criteria**:
- qase-pytest removed from requirements.txt
- All tests use @allure decorators exclusively
- No @qase decorators remain in codebase
- CI/CD pipeline only generates Allure reports

**Independent Test**:
```bash
# Verify no Qase imports
grep -r "from qase" tests/  # Should return 0 results

# Verify no Qase decorators
grep -r "@qase" tests/  # Should return 0 results

# Run tests and generate Allure report
pytest tests/ --alluredir=allure-results
allure generate allure-results -o allure-report
```

---

## Phase 8: User Story 6 - Add Type Hints and Docstrings (P2 - MEDIUM)

**Story**: As a developer joining the team, I need type hints on all methods and comprehensive docstrings so that IDE autocomplete works and I understand code without asking teammates.

**Acceptance Criteria**:
1. base_page.py methods have all parameters and return types with type hints
2. Fixture functions show parameter types and docstrings in IDE
3. Docstring coverage > 90%

### Tasks

- [ ] T056 [P] [US6] Add type hints to all fixture functions in conftest.py
- [ ] T057 [P] [US6] Add comprehensive docstrings to all fixtures in conftest.py explaining purpose and scope
- [ ] T058 [P] [US6] Add type hints to all test methods in tests/test_registration.py
- [ ] T059 [P] [US6] Add type hints to all test methods in tests/test_becomeseller.py
- [ ] T060 [P] [US6] Add type hints to all test methods in tests/test_login.py
- [ ] T061 [US6] Run mypy --strict on entire codebase and fix all type errors
- [ ] T062 [US6] Install pre-commit hooks (pre-commit install) to enforce black, flake8, mypy on commits

**Completion Criteria**:
- All Python files pass mypy --strict with 0 errors
- All public methods have docstrings
- Docstring coverage > 90%
- Pre-commit hooks installed and enforced

**Independent Test**:
```bash
# Run mypy strict mode
mypy . --strict

# Count docstring coverage
pydocstyle pages/ utils/ config/ tests/

# Test pre-commit hooks
pre-commit run --all-files
```

---

## Phase 9: User Story 7 - Implement CI/CD Parallel Execution (P2 - MEDIUM)

**Story**: As a DevOps engineer, I need CI/CD pipeline to run tests in parallel so that pipeline completes in 15 minutes instead of 45 minutes.

**Acceptance Criteria**:
1. .gitlab-ci.yml runs test_login, test_registration, test_becomeseller in parallel
2. Test stage uses pytest-xdist with -n 4 for each test suite
3. Pipeline execution completes in <15 minutes (50%+ reduction from 30-45min)

### Tasks

- [ ] T063 [US7] Update .gitlab-ci.yml to use GitLab parallel matrix strategy for test suites
- [ ] T064 [US7] Add pytest-xdist -n 4 --dist loadscope to each test suite execution in .gitlab-ci.yml
- [ ] T065 [US7] Add Allure result merging stage in .gitlab-ci.yml to combine results from parallel jobs
- [ ] T066 [US7] Add pytest-rerunfailures with max 2 retries for flaky test handling in .gitlab-ci.yml
- [ ] T067 [US7] Test CI/CD pipeline execution time (should be <15 minutes)

**Completion Criteria**:
- .gitlab-ci.yml runs test suites in parallel (matrix strategy)
- Each test suite uses pytest-xdist -n 4
- Allure reports merged correctly from parallel jobs
- Pipeline completes in <15 minutes

**Independent Test**:
```bash
# Locally test parallel execution
pytest tests/ -n 4 --dist loadscope --alluredir=allure-results

# Measure execution time
time pytest tests/ -n 4

# Trigger GitLab CI/CD pipeline and measure duration
```

---

## Phase 10: Polish & Cross-Cutting Concerns

**Goal**: Final improvements for documentation, validation, and maintenance.

**Duration**: ~2-3 hours

### Tasks

- [ ] T068 [P] Create JSON schemas for all test data files in test_data/schemas/ (login_schema.json, registration_schema.json, becomeseller_schema.json)
- [ ] T069 [P] Update TestDataLoader to validate data against schemas before returning
- [ ] T070 [P] Add error handling for missing/malformed JSON files in TestDataLoader
- [ ] T071 [P] Create docs/architecture.md documenting refactored framework architecture
- [ ] T072 Update README.md with new locator strategy guidelines and parallel execution instructions
- [ ] T073 Run full test suite with all refactorings (pytest tests/ -n 4 -v --alluredir=allure-results)
- [ ] T074 Generate final Allure report and verify all improvements (allure generate allure-results -o allure-report)

**Completion Criteria**:
- All test data has JSON schemas
- TestDataLoader validates data on load
- Documentation updated (architecture.md, README.md)
- Full test suite passes with all refactorings
- Allure report shows clear test structure

---

## Task Dependencies & Execution Order

### Critical Path (Must Complete in Order)

```
Phase 1: Setup (T001-T007)
    ↓
Phase 2: Foundational (T008-T011) ← BLOCKING for all user stories
    ↓
Phase 3-9: User Stories (Can execute in parallel by story)
    ├── US1: T012-T014 (Already complete, documentation only)
    ├── US2: T015-T030 (Locators - CRITICAL)
    ├── US3: T031-T038 (Page Objects - depends on US2 completion)
    ├── US4: T039-T048 (Utils - can parallel with US2/US3)
    ├── US5: T049-T055 (Allure - independent, can parallel)
    ├── US6: T056-T062 (Type Hints - can parallel, conflicts with US2-US5 on same files)
    └── US7: T063-T067 (CI/CD - independent, can parallel)
    ↓
Phase 10: Polish (T068-T074)
```

### Story Dependencies

- **US1 (Fixtures)**: ✅ Already complete, no dependencies
- **US2 (Locators)**: No dependencies, can start after Foundational phase
- **US3 (Page Objects)**: Depends on US2 (easier to refactor after locators fixed)
- **US4 (Utils)**: No dependencies, can parallel with US2/US3
- **US5 (Allure)**: No dependencies, can parallel with all
- **US6 (Type Hints)**: Conflicts with US2-US5 (file modifications), run after or coordinate carefully
- **US7 (CI/CD)**: Depends on US1 (test isolation required for parallel execution)

---

## Parallel Execution Strategies

### Strategy 1: By User Story (Recommended for Team)

Assign different user stories to different developers:

```bash
# Developer 1: Locators (US2)
Tasks: T015-T030

# Developer 2: Page Objects (US3) - starts after US2 completes
Tasks: T031-T038

# Developer 3: Utils (US4)
Tasks: T039-T048

# Developer 4: Allure (US5)
Tasks: T049-T055

# Developer 5: CI/CD (US7)
Tasks: T063-T067
```

### Strategy 2: By File (For Solo Developer)

Complete all changes for one page object at a time:

```bash
# registration_page.py (all changes)
T019-T023 (locators), T031-T035 (test logic removal), T047 (waits)

# becomeseller_page.py (all changes)
T024-T027 (locators), T037 (test logic removal), T046 (waits)

# Etc.
```

### Strategy 3: MVP First (Fastest to Production)

Minimum viable product focusing on P1 blockers:

```bash
# MVP Scope (US1-US4 only)
Phase 1: Setup (T001-T007)
Phase 2: Foundational (T008-T011)
US1: Already complete (T012-T014 optional)
US2: Locators (T015-T030)
US3: Page Objects (T031-T038)
US4: Utils (T039-T048)

# Result: Test isolation + stable locators + clean architecture
# Defer US5-US7 (Allure, Type Hints, CI/CD) to post-MVP
```

---

## Validation & Testing

### Per-Story Validation

**US1 (Fixtures)**:
```bash
pytest tests/ -n 4 -v  # Parallel execution
pytest tests/ --random-order -v  # Random order
```

**US2 (Locators)**:
```bash
grep -r "\.Mui" pages/  # Should be minimal
grep -r "get_by_role" pages/ | wc -l  # Should be high
pytest tests/test_registration.py -v
```

**US3 (Page Objects)**:
```bash
grep -r "def test_" pages/  # Should be 0
grep -r "assert " pages/  # Should be 0
pytest tests/test_registration.py -v
```

**US4 (Utils)**:
```bash
grep -r "time.sleep" pages/  # Should be 0
mypy utils/  # Should pass
```

**US5 (Allure)**:
```bash
grep -r "@qase" tests/  # Should be 0
pytest tests/ --alluredir=allure-results
allure generate allure-results
```

**US6 (Type Hints)**:
```bash
mypy . --strict  # Should pass with 0 errors
pydocstyle pages/ utils/  # Check docstrings
```

**US7 (CI/CD)**:
```bash
time pytest tests/ -n 4  # Measure local time
# Trigger GitLab pipeline, measure duration
```

### Final Validation (All Stories Complete)

```bash
# All tests pass in parallel
pytest tests/ -n 4 -v --alluredir=allure-results

# All tests pass in random order
pytest tests/ --random-order -v

# Type checking passes
mypy . --strict

# Code quality gates pass
black pages/ tests/ utils/ --check
flake8 pages/ tests/ utils/
pylint pages/ tests/ utils/

# Pre-commit hooks pass
pre-commit run --all-files

# Generate final Allure report
allure generate allure-results -o allure-report
allure open allure-report
```

---

## Success Metrics (from Spec.md)

Track these metrics to validate refactoring success:

- [ ] **SC-003**: Test execution time reduced by 50% (from ~30min to ~15min) via parallel execution
- [ ] **SC-004**: Locator brittleness reduced by 80% (remove 90%+ CSS class selectors)
- [ ] **SC-005**: Code duplication reduced by 60% through centralized utilities
- [ ] **SC-002**: Mypy strict mode passes with 0 errors
- [ ] **SC-006**: All tests have minimum 3 Allure steps with clear descriptions
- [ ] **SC-007**: CI/CD pipeline completes in under 15 minutes
- [ ] **SC-009**: Zero hardcoded credentials in repository (use env vars)
- [ ] **QG-006**: All tests pass when run in random order (pytest --random-order)
- [ ] **QG-007**: All tests pass when run in parallel (pytest -n 4)

---

## Implementation Notes

### Backward Compatibility

**CRITICAL**: Maintain backward compatibility during migration:
- Keep existing test files working during refactoring
- No breaking changes to test data format
- Preserve Allure TestOps integration
- Tests should continue to pass at each step

### Incremental Delivery

**Recommended Approach**:
1. Complete Phase 1-2 (Setup + Foundational) first - BLOCKING
2. Complete US1-US4 (P1 stories) for MVP
3. Validate MVP with full test suite
4. Complete US5-US7 (P2 stories) post-MVP
5. Complete Phase 10 (Polish) as final step

### Risk Mitigation

**High-Risk Tasks** (require careful testing):
- T008-T011: Fixture scope changes (ALREADY DONE, verify only)
- T019-T030: Locator refactoring (high impact, test thoroughly)
- T063-T067: CI/CD changes (test in dev environment first)

**Low-Risk Tasks** (safe to parallel):
- T039-T044: Adding type hints/docstrings to utils
- T049-T055: Removing Qase integration
- T068-T071: Documentation updates

---

## Estimated Completion Time

| Phase | Duration | Tasks |
|-------|----------|-------|
| Phase 1: Setup | 30 min | 7 tasks |
| Phase 2: Foundational | 1-2 hours | 4 tasks (verification only) |
| Phase 3: US1 (Fixtures) | 30 min | 3 tasks (documentation) |
| Phase 4: US2 (Locators) | 4-6 hours | 16 tasks |
| Phase 5: US3 (Page Objects) | 2-3 hours | 8 tasks |
| Phase 6: US4 (Utils) | 2-3 hours | 10 tasks |
| Phase 7: US5 (Allure) | 1-2 hours | 7 tasks |
| Phase 8: US6 (Type Hints) | 3-4 hours | 7 tasks |
| Phase 9: US7 (CI/CD) | 2-3 hours | 5 tasks |
| Phase 10: Polish | 2-3 hours | 7 tasks |
| **Total** | **18-30 hours** | **74 tasks** |

**MVP (Phases 1-6)**: ~11-17 hours for critical P1 stories

---

## Questions & Clarifications

Before starting implementation, clarify:

1. **Locator Strategy**: Do we have agreement from dev team to add data-testid attributes where ARIA roles are insufficient?
2. **CI/CD Access**: Do we have permissions to modify .gitlab-ci.yml and test pipeline changes?
3. **Allure TestOps**: Do we have Allure TestOps credentials configured in GitLab CI/CD variables?
4. **Breaking Changes**: Are we allowed to remove Qase integration completely, or does it need gradual deprecation?
5. **Timeline**: Is the 18-30 hour estimate acceptable, or do we need to prioritize a smaller MVP scope?

---

**Status**: Ready for implementation
**Next Step**: Execute Phase 1 (Setup) tasks T001-T007
**Review Required**: Yes - review task breakdown with team before starting Phase 2

---

*Generated by `/speckit.tasks` on 2025-12-10*
