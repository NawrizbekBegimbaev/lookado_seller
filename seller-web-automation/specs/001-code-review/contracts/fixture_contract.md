# Fixture Scope Contract

**Purpose**: Define the correct fixture scopes for test isolation and parallel execution.

**Critical Rule**: NEVER use session/class scope for `context` or `page` fixtures. This blocks parallel execution and causes state pollution between tests.

---

## Session Scope (Shared Across All Tests)

**Use When**: Resource is expensive to create and can be safely shared.

### ✅ Allowed Session-Scoped Fixtures

#### 1. `playwright` Fixture
```python
@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    """Session-level Playwright instance"""
    pw = sync_playwright().start()
    yield pw
    pw.stop()
```

**Rationale**:
- Playwright initialization is expensive (~500ms)
- Playwright instance is stateless (no per-test state)
- Safe to share across all tests

#### 2. `browser` Fixture
```python
@pytest.fixture(scope="session")
def browser(playwright: Playwright, request) -> Generator[Browser, None, None]:
    """Session-level browser instance"""
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    browser_instance = playwright.chromium.launch(headless=headless)
    yield browser_instance
    browser_instance.close()
```

**Rationale**:
- Browser launch is expensive (~1-2 seconds)
- Browser instance is stateless (contexts provide isolation)
- Each pytest-xdist worker gets its own browser instance
- Safe to share across all tests **within a worker**

---

## Function Scope (Isolated Per Test)

**Use When**: Resource contains per-test state (cookies, storage, DOM).

### ✅ Required Function-Scoped Fixtures

#### 1. `context` Fixture ⚠️ **CRITICAL**
```python
@pytest.fixture(scope="function")  # ✅ MUST BE FUNCTION SCOPE
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Function-level browser context - CRITICAL for test isolation"""
    context_instance = browser.new_context()
    yield context_instance
    context_instance.close()
```

**Rationale**:
- Context contains per-test state:
  - Cookies
  - localStorage
  - sessionStorage
  - Cache
  - Service workers
- Sharing context across tests causes state pollution
- Function scope enables parallel execution (each test gets fresh context)

**Impact of Wrong Scope**:
```python
# ❌ WRONG - Session scope
@pytest.fixture(scope="session")
def context(browser: Browser):
    # All tests share ONE context
    # Test 1 logs in → Test 2 sees logged-in state
    # Test 3 modifies cookie → Test 4 affected
    # PARALLEL EXECUTION: IMPOSSIBLE (context conflicts)
```

#### 2. `page` Fixture ⚠️ **CRITICAL**
```python
@pytest.fixture(scope="function")  # ✅ MUST BE FUNCTION SCOPE
def page(context: BrowserContext, request) -> Generator[Page, None, None]:
    """Function-level page - CRITICAL for test isolation"""
    page_instance = context.new_page()
    base_url = request.config.getoption("url_name")
    page_instance.goto(base_url)
    yield page_instance
    page_instance.close()
```

**Rationale**:
- Page contains per-test state:
  - Current URL
  - DOM state
  - JavaScript execution context
  - Event listeners
- Sharing page across tests causes state pollution
- Function scope enables parallel execution

**Impact of Wrong Scope**:
```python
# ❌ WRONG - Session scope
@pytest.fixture(scope="session")
def page(context: BrowserContext):
    # All tests share ONE page
    # Test 1 navigates to /login → Test 2 starts at /login (unexpected!)
    # Test 3 fills form → Test 4 sees filled form (state pollution)
    # PARALLEL EXECUTION: IMPOSSIBLE (page conflicts)
```

#### 3. `authenticated_page` Fixture
```python
@pytest.fixture(scope="function")  # ✅ MUST BE FUNCTION SCOPE
def authenticated_page(page: Page, test_data: Dict[str, Any]) -> Page:
    """Pre-authenticated page for tests requiring login"""
    from pages.login_page import LoginPage

    credentials = test_data.get("login_credentials")
    login_page = LoginPage(page)
    login_page.navigate_to(login_page.url)
    login_page.perform_login(
        email=credentials["email"],
        password=credentials["password"]
    )
    page.wait_for_url("**/dashboard/**", timeout=15000)
    return page
```

**Rationale**:
- Authentication state (cookies/tokens) is per-test
- Each test needs fresh authentication
- Function scope prevents shared auth state

#### 4. `test_data` Fixture
```python
@pytest.fixture
def test_data(request) -> Dict[str, Any]:
    """Load test data based on test module name"""
    test_module = request.module.__name__
    if "test_" in test_module:
        module_name = test_module.split("test_")[-1]
        return TestDataLoader.load(module_name)
    return {}
```

**Rationale**:
- Test data should be immutable per test
- Function scope (default) ensures fresh data load
- Caching handled by TestDataLoader, not fixture scope

---

## Module Scope (Rarely Used)

**Use When**: Resource is expensive but can be shared within a module.

### ⚠️ Use With Caution

Module scope can be used for fixtures that:
1. Are expensive to create
2. Are truly stateless
3. Are only used by tests in one module

**Example** (rare case):
```python
@pytest.fixture(scope="module")
def database_connection():
    """Database connection shared within module"""
    conn = create_connection()
    yield conn
    conn.close()
```

**Caution**: Module scope does NOT provide per-test isolation. Use only when absolutely necessary.

---

## Class Scope (Legacy, Avoid)

**Use When**: Never for new code. Only for backward compatibility with existing test classes.

### ⚠️ Deprecated Pattern

```python
# ❌ DEPRECATED - Class scope for page fixtures
@pytest.fixture(scope="class")
def authenticated_seller_session(page: Page):
    """Class-level authentication (deprecated)"""
    # All tests in class share authentication state
    # State pollution within class
    # Blocks parallel execution for class
```

**Migration Path**:
1. Refactor test class to use function-scoped fixtures
2. If performance is concern, optimize login process (API login instead of UI)
3. Remove class-scoped fixtures entirely

---

## Parallel Execution Requirements

### ✅ Correct Pattern for Parallel Execution

```python
# conftest.py
@pytest.fixture(scope="session")
def browser(playwright):
    """Session scope - shared within worker"""
    return playwright.chromium.launch()

@pytest.fixture(scope="function")
def context(browser):
    """Function scope - isolated per test"""
    return browser.new_context()

@pytest.fixture(scope="function")
def page(context):
    """Function scope - isolated per test"""
    return context.new_page()

# Run tests in parallel
# $ pytest tests/ -n 4 --dist loadscope
# ✅ Works: Each test has isolated context and page
```

### ❌ Broken Pattern (Blocks Parallel Execution)

```python
# conftest.py
@pytest.fixture(scope="session")
def context(browser):
    """❌ WRONG: Session scope for context"""
    return browser.new_context()

@pytest.fixture(scope="session")
def page(context):
    """❌ WRONG: Session scope for page"""
    return context.new_page()

# Run tests in parallel
# $ pytest tests/ -n 4 --dist loadscope
# ❌ FAILS: All workers try to use same context/page
# Result: Context conflicts, test failures, flakiness
```

---

## Verification Checklist

Use this checklist to verify correct fixture scoping:

### Session Scope
- [ ] `playwright` fixture is session-scoped ✅
- [ ] `browser` fixture is session-scoped ✅
- [ ] NO `context` fixture at session scope ❌
- [ ] NO `page` fixture at session scope ❌

### Function Scope
- [ ] `context` fixture is function-scoped ✅
- [ ] `page` fixture is function-scoped ✅
- [ ] `authenticated_page` fixture is function-scoped ✅
- [ ] `test_data` fixture is function-scoped (default) ✅

### Parallel Execution
- [ ] Tests pass with `pytest -n 4` ✅
- [ ] Tests pass with `pytest --random-order` ✅
- [ ] No shared mutable state between tests ✅
- [ ] Each test is independent ✅

---

## Common Mistakes & Solutions

### Mistake 1: Session-Scoped Page Fixture
```python
# ❌ WRONG
@pytest.fixture(scope="session")
def page(context):
    return context.new_page()

# ✅ CORRECT
@pytest.fixture(scope="function")
def page(context):
    page_instance = context.new_page()
    yield page_instance
    page_instance.close()
```

### Mistake 2: Class-Scoped Authentication
```python
# ❌ WRONG
@pytest.fixture(scope="class")
def authenticated_page(page):
    # Perform login
    return page

# ✅ CORRECT
@pytest.fixture(scope="function")
def authenticated_page(page):
    # Perform login
    return page
```

### Mistake 3: Modifying Shared State
```python
# ❌ WRONG
@pytest.fixture(scope="session")
def shared_data():
    return {"counter": 0}  # Mutable shared state

def test_1(shared_data):
    shared_data["counter"] += 1  # Affects other tests!

# ✅ CORRECT
@pytest.fixture
def isolated_data():
    return {"counter": 0}  # Fresh data per test

def test_1(isolated_data):
    isolated_data["counter"] += 1  # Only affects this test
```

---

## Performance Considerations

### Session Scope Performance
- Browser launch: ~1-2 seconds saved per test
- Playwright init: ~500ms saved per test
- **Savings**: 30 tests × 2 seconds = **60 seconds saved**

### Function Scope Performance
- Context creation: ~50ms per test
- Page creation: ~20ms per test
- **Cost**: 30 tests × 70ms = **2.1 seconds overhead**

### Net Benefit
- **Session scope benefits**: 60 seconds saved
- **Function scope cost**: 2.1 seconds overhead
- **Net benefit**: **57.9 seconds faster** + parallel execution enabled

---

## Summary

### ✅ DO
- Use session scope for `playwright` and `browser`
- Use function scope for `context` and `page`
- Use function scope for `authenticated_page`
- Use function scope for `test_data` (default)

### ❌ DON'T
- Use session/class scope for `context` (blocks parallel execution)
- Use session/class scope for `page` (causes state pollution)
- Share mutable state between tests
- Assume test order (tests must be independent)

### 🎯 Goal
- **Test isolation**: Each test has fresh state
- **Parallel execution**: Tests run in parallel without conflicts
- **Performance**: Optimize only where safe (browser/playwright)
- **Maintainability**: Clear fixture scopes make debugging easier

---

**Version**: 1.0.0
**Last Updated**: 2025-12-10
**Status**: Enforced in conftest.py (Phase 1 refactoring complete)
