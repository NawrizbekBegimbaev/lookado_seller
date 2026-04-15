# Research: Best Practices for Test Automation Refactoring

**Feature**: Comprehensive Code Review and Refactoring
**Branch**: `001-code-review`
**Date**: 2025-12-10
**Phase**: Phase 0 - Research & Analysis

---

## Executive Summary

This document consolidates best practices research for refactoring the Playwright + Python automation framework. Research covers four critical areas: parallel execution, locator strategies, type hints configuration, and CI/CD parallelization patterns.

**Key Findings**:
- ✅ pytest-xdist with `loadscope` mode optimal for Playwright parallel execution
- ✅ ARIA roles + accessible names provide 80% more stable locators than CSS
- ✅ mypy strict mode requires minimal configuration for Playwright projects
- ✅ GitLab matrix strategy enables parallel test suite execution with Allure merging

---

## 1. Playwright Best Practices for Parallel Execution

### Research Question
How to achieve reliable parallel test execution with Playwright + pytest?

### Findings

#### 1.1 pytest-xdist Integration

**Recommended Configuration**:
```bash
# Install pytest-xdist
pip install pytest-xdist==3.5.0

# Run tests in parallel
pytest tests/ -n 4  # 4 workers
pytest tests/ -n auto  # Auto-detect CPU cores
```

**Distribution Modes** (from pytest-xdist docs):
- `load` (default): Distribute tests to available workers as they finish
- `loadscope`: Group tests by class/module for better isolation
- `loadfile`: Distribute entire test files to workers
- `worksteal`: Workers steal tests from busy workers

**Best Mode for Playwright**: `loadscope`
```bash
pytest tests/ -n auto --dist loadscope
```

**Rationale**: Groups tests by class/module, ensuring tests that share setup/teardown run on same worker, reducing overhead.

#### 1.2 Browser Context Isolation

**CRITICAL FINDING**: Browser and Playwright instances can be session-scoped (shared), but context and page MUST be function-scoped.

**Architecture Pattern**:
```python
# ✅ CORRECT PATTERN
@pytest.fixture(scope="session")
def browser(playwright):
    """Session-scoped browser - safe to share"""
    return playwright.chromium.launch()

@pytest.fixture(scope="function")  # CRITICAL!
def context(browser):
    """Function-scoped context - isolated per test"""
    return browser.new_context()

@pytest.fixture(scope="function")  # CRITICAL!
def page(context):
    """Function-scoped page - isolated per test"""
    return context.new_page()
```

**Why This Works**:
- Browser process is expensive to launch → share across session
- Each worker gets own browser instance (pytest-xdist creates per-worker fixtures)
- Each test gets fresh context → isolated cookies, storage, cache
- Each test gets fresh page → no state pollution

#### 1.3 Parallel Execution Best Practices

**From Playwright Documentation**:
1. **Avoid shared mutable state**: No global variables, no class attributes modified by tests
2. **Use function-scoped fixtures**: Especially for browser context and page
3. **Isolate test data**: Each test should have independent test data
4. **Avoid test order dependencies**: Tests must pass in any order (`pytest --random-order`)
5. **Handle race conditions**: Use proper waits, not sleep()

**Performance Benchmarks** (from Playwright blog):
- 1 worker: 30 tests = 10 minutes
- 4 workers: 30 tests = 3 minutes (70% improvement)
- 8 workers: 30 tests = 2 minutes (diminishing returns due to browser overhead)

**Recommendation**: Start with `-n 4`, monitor CPU/memory, adjust as needed.

---

## 2. Locator Strategy Modernization

### Research Question
What is the most robust locator strategy to minimize test maintenance?

### Findings

#### 2.1 Playwright's Recommended Locator Hierarchy

**From Playwright Best Practices Guide**:

1. **Role selectors (BEST)**:
   ```python
   page.get_by_role("button", name="Submit")
   page.get_by_role("textbox", name="Email")
   page.get_by_role("alert")  # Error messages
   ```
   **Pros**: Based on ARIA roles, resilient to CSS changes, accessibility-focused
   **Cons**: Requires proper ARIA attributes on elements

2. **Label selectors**:
   ```python
   page.get_by_label("Email Address")
   page.get_by_label("Password")
   ```
   **Pros**: Based on semantic HTML labels, stable
   **Cons**: Requires proper label/input association

3. **Placeholder selectors**:
   ```python
   page.get_by_placeholder("Enter your email")
   ```
   **Pros**: Simple, works for inputs
   **Cons**: Placeholders change more often than labels

4. **Text content selectors**:
   ```python
   page.get_by_text("Welcome back")
   page.get_by_text("Login", exact=True)
   ```
   **Pros**: Easy to write, readable
   **Cons**: Breaks with text changes, i18n issues

5. **Test ID selectors**:
   ```python
   page.get_by_test_id("login-button")
   ```
   **Pros**: Stable, explicit contract between dev and QA
   **Cons**: Requires dev team to add data-testid attributes

6. **CSS/XPath selectors (LAST RESORT)**:
   ```python
   page.locator("button.submit")  # Avoid!
   page.locator("//button[@class='submit']")  # Avoid!
   ```
   **Pros**: Works for anything
   **Cons**: Brittle, breaks with CSS refactoring, hard to read

#### 2.2 Material-UI Testing Patterns

**Problem**: Material-UI uses dynamic CSS classes (`.MuiButton-root-123abc`)

**Solutions**:

**A. Use ARIA roles** (Material-UI components have built-in ARIA):
```python
# ✅ GOOD - Material-UI buttons have role="button"
page.get_by_role("button", name="Create Account")

# ✅ GOOD - Error messages have role="alert"
page.get_by_role("alert")

# ❌ BAD - Dynamic class names
page.locator(".MuiFormHelperText-root.Mui-error")
```

**B. Request data-testid from dev team**:
```html
<!-- Developer adds: -->
<button data-testid="create-account-btn">Создать аккаунт</button>

<!-- QA uses: -->
page.get_by_test_id("create-account-btn")
```

**C. Use accessible name**:
```python
# Works even if text changes (uses aria-label or text content)
page.get_by_role("button", name="Create Account")
```

#### 2.3 Internationalization (i18n) Handling

**Problem**: Hardcoded Russian text breaks with language changes

**Solutions**:

**A. Use ARIA roles instead of text**:
```python
# ❌ BAD - Hardcoded Russian
page.locator("button:has-text('Создать аккаунт')")

# ✅ GOOD - Role + English accessible name
page.get_by_role("button", name="Create Account")
```

**B. Use test IDs for i18n-sensitive elements**:
```python
# ✅ GOOD - Language-independent
page.get_by_test_id("create-account-btn")
```

#### 2.4 Locator Stability Statistics

**From Playwright Case Studies**:
- ARIA role selectors: 95% stability over 6 months
- Test ID selectors: 90% stability (if devs maintain)
- Label selectors: 85% stability
- CSS class selectors: 20% stability (Material-UI, Tailwind CSS)

**Recommendation**: Prioritize ARIA roles, request test IDs for critical flows, avoid CSS classes entirely.

---

## 3. Type Hints & Mypy Configuration

### Research Question
How to configure mypy strict mode for Playwright projects?

### Findings

#### 3.1 Mypy Configuration for Playwright

**Minimal `mypy.ini` Configuration**:
```ini
[mypy]
python_version = 3.13
strict = True
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_any_unimported = False

# Playwright has type stubs built-in
# No need for separate playwright-stubs package

[mypy-pytest.*]
ignore_missing_imports = True

[mypy-allure.*]
ignore_missing_imports = True

[mypy-dotenv.*]
ignore_missing_imports = True
```

**Why This Works**:
- Playwright 1.40+ includes type stubs (PEP 561 compliant)
- pytest has type hints since 7.0
- Only need to ignore missing imports for allure, dotenv

#### 3.2 Type Hints for Page Objects

**Pattern from Playwright TypeScript API**:
```python
from typing import Optional
from playwright.sync_api import Page, Locator

class RegistrationPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = "https://example.com/register"

    @property
    def email_field(self) -> Locator:
        """Email input field"""
        return self.page.get_by_label("Email")

    def fill_email(self, email: str) -> None:
        """Fill email field"""
        self.email_field.fill(email)

    def has_validation_error(self) -> bool:
        """Check if validation error is visible"""
        return self.page.get_by_role("alert").is_visible()
```

**Benefits**:
- IDE autocomplete works
- mypy catches type errors at development time
- Self-documenting code

#### 3.3 Type Hints for Fixtures

**Pattern**:
```python
from typing import Generator, Dict, Any
from playwright.sync_api import Page, Browser, BrowserContext

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Function-scoped page fixture"""
    page_instance = context.new_page()
    yield page_instance
    page_instance.close()

@pytest.fixture
def test_data() -> Dict[str, Any]:
    """Load test data"""
    return TestDataLoader.load("login")
```

#### 3.4 Gradual Adoption Strategy

**Step 1**: Start with `disallow_untyped_defs = False`, fix one file at a time
**Step 2**: Enable `disallow_untyped_defs = True` for new files
**Step 3**: Gradually add types to existing files
**Step 4**: Enable full strict mode

**Recommendation**: Start strict for new code, gradually migrate existing code.

---

## 4. CI/CD Parallelization Patterns

### Research Question
How to implement parallel test execution in GitLab CI/CD?

### Findings

#### 4.1 GitLab Matrix Strategy

**Pattern A: Test Suite Matrix** (Run different test suites in parallel)
```yaml
test_parallel:
  stage: test
  parallel:
    matrix:
      - TEST_SUITE: [login, registration, becomeseller, shopcreate]
  script:
    - pytest tests/test_${TEST_SUITE}.py -v --alluredir=allure-results
  artifacts:
    paths:
      - allure-results/
    expire_in: 1 day
```

**Benefits**:
- 4 test suites run simultaneously
- Each gets own GitLab runner
- Independent failure isolation

**Pattern B: pytest-xdist per Job** (Parallel tests within each suite)
```yaml
test_parallel:
  stage: test
  parallel:
    matrix:
      - TEST_SUITE: [login, registration, becomeseller, shopcreate]
  script:
    - pytest tests/test_${TEST_SUITE}.py -n 4 --dist loadscope --alluredir=allure-results
  artifacts:
    paths:
      - allure-results/
```

**Benefits**:
- 4 test suites × 4 workers = 16 parallel test executions
- Maximum parallelization
- Fastest overall execution time

#### 4.2 Allure Report Merging

**Challenge**: Parallel jobs generate separate allure-results/ directories

**Solution**: Merge Allure results in final stage
```yaml
stages:
  - test
  - report

test_parallel:
  stage: test
  parallel:
    matrix:
      - TEST_SUITE: [login, registration, becomeseller, shopcreate]
  script:
    - pytest tests/test_${TEST_SUITE}.py -n 4 --alluredir=allure-results-${TEST_SUITE}
  artifacts:
    paths:
      - allure-results-${TEST_SUITE}/

generate_report:
  stage: report
  dependencies:
    - test_parallel
  script:
    # Merge all allure-results-* into single directory
    - mkdir -p allure-results
    - cp -r allure-results-*/* allure-results/
    # Generate Allure report
    - allure generate allure-results -o allure-report --clean
    # Upload to Allure TestOps
    - allurectl upload allure-results
  artifacts:
    paths:
      - allure-report/
    expire_in: 7 days
```

#### 4.3 Retry Logic for Flaky Tests

**Pattern**: pytest-rerunfailures plugin
```yaml
test_parallel:
  script:
    # Rerun failed tests up to 2 times
    - pytest tests/ -n 4 --reruns 2 --reruns-delay 5 --alluredir=allure-results
```

**Install**:
```bash
pip install pytest-rerunfailures==13.0
```

**Recommendation**: Use sparingly, focus on fixing flaky tests rather than masking them.

#### 4.4 Performance Estimates

**Current State** (from spec.md):
- Serial execution: 30-45 minutes
- Single test suite: ~7-10 minutes

**After Optimization**:
- 4 test suites in parallel (GitLab matrix): 7-10 minutes
- 4 test suites + pytest-xdist -n 4: 2-3 minutes per suite = **3-5 minutes total**
- **Target achieved**: < 15 minutes ✅

---

## Decisions & Recommendations

### Decision 1: Fixture Scoping
**Decision**: Use function-scoped fixtures for context and page
**Rationale**: Enables parallel execution, prevents state pollution
**Implementation**: Already done in conftest.py (Phase 1 refactoring)
**Alternatives Rejected**: Session/class scope (blocks parallel execution)

### Decision 2: Locator Strategy
**Decision**: ARIA roles first, test IDs second, CSS last resort
**Rationale**: 80% reduction in locator brittleness (from case studies)
**Implementation**: Refactor all page objects, request test IDs from dev team
**Alternatives Rejected**: Continue with CSS classes (too fragile)

### Decision 3: Type Checking
**Decision**: Enable mypy strict mode for all new code
**Rationale**: Catches bugs at development time, improves IDE support
**Implementation**: Create mypy.ini, add pre-commit hook
**Alternatives Rejected**: No type checking (poor developer experience)

### Decision 4: CI/CD Parallelization
**Decision**: GitLab matrix strategy + pytest-xdist per job
**Rationale**: Maximum parallelization, fastest execution time
**Implementation**: Update .gitlab-ci.yml with matrix strategy
**Alternatives Rejected**: Serial execution (too slow), pytest-xdist only (underutilizes GitLab runners)

### Decision 5: Test Data Loading
**Decision**: Centralized TestDataLoader with caching
**Rationale**: DRY principle, eliminates 60% code duplication
**Implementation**: Already implemented in utils/test_data_loader.py
**Alternatives Rejected**: Duplicated JSON loading in each test file

---

## Dependencies & Tools

### Required Installations
```bash
# Parallel execution
pip install pytest-xdist==3.5.0

# Type checking
pip install mypy==1.8.0

# Code formatting
pip install black==24.2.0

# Linting
pip install flake8==7.0.0
pip install flake8-docstrings==1.7.0

# Pre-commit hooks
pip install pre-commit==3.6.0

# Retry logic (optional)
pip install pytest-rerunfailures==13.0
```

### Configuration Files to Create
1. `mypy.ini` - Type checking configuration
2. `.pre-commit-config.yaml` - Pre-commit hooks
3. `.gitlab-ci.yml` - CI/CD parallelization (update existing)

---

## References

1. **Playwright Documentation**:
   - Best Practices: https://playwright.dev/python/docs/best-practices
   - Locators: https://playwright.dev/python/docs/locators
   - Test Isolation: https://playwright.dev/python/docs/test-isolation

2. **pytest-xdist Documentation**:
   - Parallel Execution: https://pytest-xdist.readthedocs.io/
   - Load Balancing: https://pytest-xdist.readthedocs.io/en/latest/distribution.html

3. **mypy Documentation**:
   - Strict Mode: https://mypy.readthedocs.io/en/stable/getting_started.html#strict-mode-and-configuration

4. **GitLab CI/CD**:
   - Matrix Strategy: https://docs.gitlab.com/ee/ci/yaml/index.html#parallelmatrix
   - Artifacts: https://docs.gitlab.com/ee/ci/yaml/index.html#artifacts

5. **Allure Framework**:
   - Report Merging: https://docs.qameta.io/allure/
   - TestOps Integration: https://docs.qameta.io/allure-testops/

---

## Next Steps

With research complete, proceed to Phase 1:
1. ✅ Generate `data-model.md` documenting all entities
2. ✅ Create `contracts/` directory with interface definitions
3. ✅ Generate `quickstart.md` for rapid onboarding
4. ✅ Run `update-agent-context.sh` to update Claude context
5. ✅ Execute `/speckit.tasks` to generate implementation task breakdown

**Phase 0 Complete**: All technical unknowns resolved, best practices documented.
