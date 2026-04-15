# Implementation Plan: Comprehensive Code Review and Refactoring

**Branch**: `001-code-review` | **Date**: 2025-12-10 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-code-review/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan addresses comprehensive refactoring of the Playwright + Python automation framework to resolve 11 major architectural issues including session-scoped fixtures preventing parallel execution, brittle CSS locators causing 80% maintenance burden, test logic in page objects violating SRP, and 60% code duplication from missing utility modules. The refactoring will enable parallel test execution (50% speed improvement), reduce locator brittleness by 80%, eliminate code duplication through centralized utils/, standardize on Allure reporting, add type hints for IDE support, and implement CI/CD parallelization for sub-15-minute pipeline completion.

## Technical Context

**Language/Version**: Python 3.13
**Primary Dependencies**: Playwright 1.51.0, pytest 8.4.2, allure-pytest 2.13.5
**Storage**: JSON files for test data (test_data/), filesystem for logs/reports
**Testing**: pytest (unit/integration tests for page objects, utils), Playwright (E2E tests)
**Target Platform**: macOS/Linux/Windows (cross-platform test execution), GitLab CI/CD runners
**Project Type**: Single automation project with web application target
**Performance Goals**: Test suite completion < 15 minutes (50% improvement from current 30-45min), parallel execution with pytest-xdist -n 4
**Constraints**: Must maintain backward compatibility with existing test files during migration, no breaking changes to test data format, preserve Allure TestOps integration
**Scale/Scope**: 212 total test cases planned (13 currently automated), 10 page objects, 4-5 test suites, 3-environment deployment (dev/staging/prod)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Status**: ✅ PASS (Constitution template not yet populated - no violations possible)

**Analysis**: The project constitution file (`.specify/memory/constitution.md`) contains only template placeholders and no enforced principles. Therefore, no constitution violations exist. Once the constitution is ratified with actual principles (e.g., TDD mandatory, library-first architecture, CLI interfaces), this section must be re-evaluated.

**Post-Design Re-Check Required**: After Phase 1 design completion, verify that:
- Test-first principles are followed (if mandated)
- Code quality gates (mypy, black, flake8) align with constitution requirements
- Documentation standards meet constitutional minimums
- CI/CD requirements comply with constitution

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
seller_web1/                          # Project root
├── pages/                            # Page Object Models (POM)
│   ├── __init__.py
│   ├── base_page.py                 # Base page with common methods
│   ├── login_page.py                # Login page object
│   ├── registration_page.py         # Registration page object
│   ├── becomeseller_page.py        # Become seller page object
│   └── dashboard_page.py           # Dashboard page object
│
├── tests/                           # Test suites
│   ├── __init__.py
│   ├── test_login.py               # Login test cases (7 tests)
│   ├── test_registration.py        # Registration tests (3 tests)
│   ├── test_becomeseller.py       # Become seller tests (3 tests)
│   └── test_shopcreate.py         # Shop creation tests (planned)
│
├── utils/                           # ✅ Already created (Phase 1)
│   ├── __init__.py                 # Exports: TestDataLoader, setup_logger, etc.
│   ├── waits.py                    # Smart wait strategies (SmartWaits class)
│   ├── test_data_loader.py        # JSON loading with caching
│   ├── logger.py                   # Logging configuration
│   ├── browser_helpers.py         # Browser utilities (screenshots, etc.)
│   └── validators.py              # JSON schema validation
│
├── config/                         # ✅ Already created (Phase 1)
│   ├── __init__.py                # Exports: settings
│   └── settings.py               # Centralized configuration (Settings dataclass)
│
├── fixtures/                      # Fixture modules (planned refactoring)
│   ├── __init__.py
│   ├── browser_fixtures.py       # Browser, context, page fixtures
│   ├── auth_fixtures.py          # Authentication fixtures
│   └── data_fixtures.py          # Test data fixtures
│
├── test_data/                    # Test data (JSON)
│   ├── login_test_data.json
│   ├── registration_test_data.json
│   ├── becomeseller_test_data.json
│   └── schemas/                  # JSON schemas for validation
│       ├── login_schema.json
│       └── registration_schema.json
│
├── reports/                      # Test execution reports
│   └── (HTML reports generated here)
│
├── logs/                         # Application logs
│   └── (Log files with rotation)
│
├── allure-results/              # Allure test results
│   └── (Allure JSON results)
│
├── docs/                        # Documentation
│   ├── test_mapping.csv        # Test coverage mapping
│   └── architecture.md         # Architecture documentation (planned)
│
├── specs/                       # Feature specifications (SpecKit)
│   └── 001-code-review/        # This feature
│       ├── spec.md
│       ├── plan.md             # This file
│       ├── research.md         # Phase 0 output (to be generated)
│       ├── data-model.md       # Phase 1 output (to be generated)
│       ├── quickstart.md       # Phase 1 output (to be generated)
│       ├── contracts/          # API contracts (if applicable)
│       └── tasks.md            # Phase 2 output (via /speckit.tasks)
│
├── conftest.py                 # ✅ Already refactored (Phase 1)
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
├── .gitlab-ci.yml             # CI/CD pipeline configuration
├── .gitignore                 # Git ignore rules
├── mypy.ini                   # Mypy configuration (to be created)
├── .pre-commit-config.yaml   # Pre-commit hooks (to be created)
├── CLAUDE.md                  # Development guidelines
└── README.md                  # Project documentation
```

**Structure Decision**: Single automation project structure (Option 1) with Page Object Model architecture. The project follows a flat, organized structure with clear separation of concerns:

1. **pages/** - Page Object Models following SRP
2. **tests/** - Test suites organized by feature
3. **utils/** - Reusable utility modules (DRY principle)
4. **config/** - Centralized configuration
5. **fixtures/** - Modular fixture organization (planned)
6. **test_data/** - JSON test data with schema validation

This structure supports the refactoring goals: test isolation, code reusability, maintainability, and scalability to 212 planned test cases.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

**Status**: N/A - No constitution violations detected (constitution not yet ratified with enforced principles).

---

## Phase 0: Research & Analysis

**Goal**: Resolve all technical unknowns and validate refactoring approach.

### Research Tasks

Since the technical context is fully specified (Python 3.13, Playwright, pytest, existing codebase), no technical unknowns require research. However, the following best practices research will inform implementation:

1. **Playwright Best Practices for Parallel Execution**
   - Research pytest-xdist integration with Playwright
   - Investigate browser context isolation patterns
   - Review fixture scope best practices for parallel tests

2. **Locator Strategy Modernization**
   - Review ARIA role best practices for test automation
   - Research Material-UI testing patterns (avoiding CSS classes)
   - Investigate Playwright's recommended locator hierarchy

3. **Type Hints & Mypy Configuration**
   - Research mypy strict mode requirements for Playwright projects
   - Investigate type stub packages needed (playwright types)
   - Review Python 3.13 type hint best practices

4. **CI/CD Parallelization Patterns**
   - Research GitLab CI matrix strategy for test splitting
   - Investigate pytest-xdist modes (load, loadscope, loadfile)
   - Review Allure report merging from parallel jobs

**Deliverable**: `research.md` with findings and recommendations (to be generated)

---

## Phase 1: Design & Architecture

**Goal**: Define data models, refactored architecture patterns, and contracts.

### 1. Data Model Design (`data-model.md`)

**Entities** (derived from spec.md Key Entities section):

#### PageObject
- **Purpose**: Represents UI page/component with locators, actions, verifications
- **Attributes**:
  - `page: Page` - Playwright page instance
  - `url: str` - Page URL (optional)
  - `locators: Dict[str, Locator]` - Named locators (as properties)
- **Behavior**:
  - Locator properties using `@property` decorator
  - Action methods (click, fill, select, navigate)
  - Verification methods (is_visible, has_text, get_text)
  - NO test assertions, NO test methods
- **Relationships**: Extends `BasePage`
- **State Transitions**: Stateless (functional scope)

#### TestFixture
- **Purpose**: Provides setup/teardown for browser, context, page, auth, data
- **Attributes**:
  - `scope: str` - pytest fixture scope (session/function)
  - `dependencies: List[str]` - Other fixtures required
  - `teardown: Callable` - Cleanup function
- **Types**:
  - Browser fixtures: `playwright`, `browser` (session scope)
  - Page fixtures: `context`, `page` (function scope)
  - Auth fixtures: `authenticated_page` (function scope)
  - Data fixtures: `test_data` (function scope)
- **Validation Rules**:
  - Function scope for context/page (test isolation)
  - Session scope only for browser/playwright (performance)

#### TestData
- **Purpose**: JSON-based input data with schema validation
- **Attributes**:
  - `source: Path` - JSON file path
  - `schema: Dict` - JSON schema for validation
  - `data: Dict` - Loaded test data
  - `environment_overrides: Dict` - Env-specific overrides
- **Behavior**:
  - Load from JSON with caching (`@lru_cache`)
  - Validate against JSON schema
  - Merge environment overrides
  - Per-test isolation (no shared mutable data)
- **Validation Rules**:
  - Must pass JSON schema validation
  - Sensitive data from env vars, not committed
  - Immutable after loading

#### Configuration
- **Purpose**: Centralized settings (URLs, timeouts, browser options, credentials)
- **Attributes** (from `config/settings.py`):
  - `BASE_URL: str`
  - `BROWSER: str` (chromium/firefox/webkit)
  - `HEADLESS: bool`
  - `DEFAULT_TIMEOUT: int`
  - `SCREENSHOTS_DIR: Path`
  - `ALLURE_ENDPOINT: str`
  - `ALLURE_TOKEN: str`
- **Behavior**:
  - Load from environment variables
  - Provide browser launch options
  - Provide context options (viewport, locale)
- **Validation**: Required vars must be set, paths must be writable

#### Utility
- **Purpose**: Reusable helper functions (waits, locators, logging, data)
- **Modules**:
  - `SmartWaits`: wait strategies (element visible, URL, network idle)
  - `TestDataLoader`: JSON loading with caching
  - `BrowserHelpers`: screenshots, console logs, HAR capture
  - `setup_logger`: logging configuration with rotation
  - `Validators`: JSON schema validation
- **Behavior**: Stateless functions/classes, no side effects

#### Report
- **Purpose**: Allure test report with steps, attachments, metadata
- **Attributes**:
  - `@allure.epic`, `@allure.feature`, `@allure.story`
  - `@allure.title`, `@allure.severity`
  - `@allure.step()` for test steps
  - Auto-attachments: screenshot, HTML, console logs, network
- **Integration**: Allure TestOps for centralized reporting

**Deliverable**: `data-model.md` documenting all entities (to be generated)

### 2. Refactoring Contracts

**Contract 1: PageObject Interface** (`contracts/page_object_contract.py`)

```python
from abc import ABC, abstractmethod
from typing import Optional
from playwright.sync_api import Page, Locator

class IPageObject(ABC):
    """Contract for all Page Objects"""

    @property
    @abstractmethod
    def page(self) -> Page:
        """Playwright page instance"""
        pass

    @property
    def url(self) -> Optional[str]:
        """Page URL (optional)"""
        return None

    @abstractmethod
    def navigate_to(self, url: Optional[str] = None) -> None:
        """Navigate to page"""
        pass

    # Locators MUST be @property methods returning Locator
    # Actions MUST be descriptive methods (select_category, fill_form)
    # Verifications MUST return bool or raise exception
    # NO test methods (test_*), NO assertions
```

**Contract 2: TestDataLoader Interface** (`contracts/data_loader_contract.py`)

```python
from abc import ABC, abstractmethod
from typing import Dict, Any

class ITestDataLoader(ABC):
    """Contract for test data loading"""

    @classmethod
    @abstractmethod
    def load(cls, module_name: str) -> Dict[str, Any]:
        """Load test data for module with caching"""
        pass

    @classmethod
    @abstractmethod
    def validate(cls, data: Dict, schema: Dict) -> bool:
        """Validate data against JSON schema"""
        pass
```

**Contract 3: Fixture Scopes** (`contracts/fixture_contract.md`)

```markdown
# Fixture Scope Contract

## Session Scope (Shared)
- playwright (Playwright instance)
- browser (Browser instance)

## Function Scope (Isolated)
- context (BrowserContext - CRITICAL for test isolation)
- page (Page - CRITICAL for test isolation)
- authenticated_page (Pre-authenticated page)
- test_data (Test data dictionary)

## RULE: Never use session/class scope for context or page
## REASON: Prevents parallel execution, causes state pollution
```

**Deliverable**: `contracts/` directory with interface definitions (to be generated)

### 3. Quickstart Guide (`quickstart.md`)

**Purpose**: 15-minute onboarding for new developers

**Sections**:
1. Setup (install, configure .env)
2. Run first test
3. Write new page object
4. Write new test
5. Run tests in parallel
6. Debug failing tests
7. View Allure reports

**Deliverable**: `quickstart.md` for rapid onboarding (to be generated)

### 4. Agent Context Update

After generating design artifacts, run:

```bash
.specify/scripts/bash/update-agent-context.sh claude
```

This will update `.claude/claude-context.json` with:
- New technology: pytest-xdist, mypy, black, flake8
- Architecture patterns: POM with function-scoped fixtures
- Locator strategy: ARIA roles first, CSS last
- CI/CD approach: GitLab matrix + pytest-xdist

**Deliverable**: Updated agent context file

---

## Phase 2: Implementation Planning

**Note**: Phase 2 (task breakdown) is handled by `/speckit.tasks` command, NOT by `/speckit.plan`.

The `/speckit.tasks` command will generate `tasks.md` with:
- Dependency-ordered tasks from spec.md requirements
- File references for each task
- Parallel execution markers [P]
- Phase grouping (aligned with spec.md Implementation Roadmap)
- Acceptance criteria per task

**Expected Task Phases** (from spec.md):
1. **Phase 1: Critical Foundations** (Week 1)
   - Fix session-scoped fixtures → function-scoped
   - Verify utils/ directory structure (already exists)
   - Remove test logic from page objects
   - **Product Creation Prerequisites**: Implement shop selection logic - product creation requires a "registered" shop to be selected. When logging in, if current shop is unregistered, must select a registered shop before "Добавить товары" button becomes visible.

2. **Phase 2: Locator Strategy** (Week 1-2)
   - Replace CSS locators with ARIA roles/labels
   - Work with devs to add test IDs where needed
   - Remove hardcoded non-English text

3. **Phase 3: Code Quality** (Week 2)
   - Add type hints to all files
   - Add docstrings (> 90% coverage)
   - Setup mypy, black, flake8, pre-commit hooks
   - Standardize on Allure, remove Qase

4. **Phase 4: Performance** (Week 2-3)
   - Replace hardcoded waits with smart waits
   - Implement CI/CD parallelization
   - Add logging and monitoring

5. **Phase 5: Polish** (Week 3)
   - Improve logging configuration
   - Add test data validation
   - Documentation and training

**Deliverable**: `tasks.md` generated by `/speckit.tasks` (separate command)

---

## Summary

This implementation plan defines:

1. **Technical Context**: Python 3.13, Playwright, pytest, Allure, GitLab CI/CD
2. **Constitution Check**: ✅ PASS (no enforced principles yet)
3. **Project Structure**: Single automation project with POM architecture
4. **Phase 0 Research**: Best practices for parallel execution, locators, types, CI/CD
5. **Phase 1 Design**: Data models (6 entities), contracts (3 interfaces), quickstart guide
6. **Phase 2 Tasks**: To be generated by `/speckit.tasks` command

**Next Steps**:
1. Generate `research.md` via research agents (Phase 0)
2. Generate `data-model.md`, `contracts/`, `quickstart.md` (Phase 1)
3. Run `update-agent-context.sh` to update Claude context
4. Execute `/speckit.tasks` to generate implementation task breakdown
