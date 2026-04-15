# Data Model: Test Automation Framework

**Feature**: Comprehensive Code Review and Refactoring
**Branch**: `001-code-review`
**Date**: 2025-12-10
**Phase**: Phase 1 - Design & Architecture

---

## Overview

This document defines the core entities and their relationships for the refactored Playwright + Python test automation framework. The data model supports test isolation, parallel execution, code reusability, and maintainability.

**Design Principles**:
- **Single Responsibility**: Each entity has one clear purpose
- **Immutability**: Test data and configuration are immutable after loading
- **Isolation**: Test fixtures provide isolated state per test
- **Composability**: Entities can be combined without tight coupling

---

## Entity Diagram

```
┌─────────────────┐
│  Configuration  │◄────────────────────┐
│  (Singleton)    │                     │
└─────────────────┘                     │
                                        │
┌─────────────────┐      ┌──────────────┴──────┐
│   TestFixture   │─────►│    PageObject       │
│  (pytest)       │      │   (Base/Derived)    │
└────────┬────────┘      └──────────┬──────────┘
         │                          │
         │ provides                 │ uses
         │                          │
         ▼                          ▼
┌─────────────────┐      ┌─────────────────────┐
│   TestData      │      │      Utility        │
│   (JSON)        │      │   (SmartWaits,      │
└─────────────────┘      │   BrowserHelpers)   │
                         └─────────────────────┘
                                    │
                                    │ generates
                                    ▼
                         ┌─────────────────────┐
                         │       Report        │
                         │   (Allure TestOps)  │
                         └─────────────────────┘
```

---

## Entity 1: PageObject

### Purpose
Represents a UI page or component with locators (as properties), actions (as methods), and verifications (as methods). PageObjects abstract the UI structure from test logic, enabling reusability and maintainability.

### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | `Page` | Yes | Playwright page instance (injected via fixture) |
| `url` | `str` | No | Page URL for navigation (optional) |
| `_locators` | `Dict[str, Locator]` | No | Internal cache for locators (implementation detail) |

### Behavior

#### Locator Properties
Locators are defined as `@property` methods returning `Locator` objects. This ensures lazy evaluation and built-in waiting.

**Pattern**:
```python
@property
def email_field(self) -> Locator:
    """Email input field"""
    return self.page.get_by_label("Email")
```

**Rules**:
1. Use ARIA roles first: `get_by_role("button", name="Submit")`
2. Use labels second: `get_by_label("Email")`
3. Use test IDs as fallback: `get_by_test_id("submit-btn")`
4. Avoid CSS/XPath: Use only as last resort

#### Action Methods
Methods that perform user interactions (click, fill, select, navigate).

**Pattern**:
```python
def fill_email(self, email: str) -> None:
    """Fill email field"""
    self.email_field.fill(email)

def submit_form(self) -> None:
    """Submit the form"""
    self.submit_button.click()
```

**Rules**:
1. Descriptive names: `select_business_type()`, not `click_button_3()`
2. Parameters for dynamic values: `select_category(name: str)`
3. No test assertions: Actions only, no `assert` statements
4. Return `None` for void actions, return data for getters

#### Verification Methods
Methods that check page state (visibility, text content, element presence).

**Pattern**:
```python
def has_validation_error(self) -> bool:
    """Check if validation error is visible"""
    return self.page.get_by_role("alert").is_visible()

def get_error_message(self) -> str:
    """Get error message text"""
    return self.page.get_by_role("alert").text_content()
```

**Rules**:
1. Return `bool` for existence checks: `has_validation_error()`
2. Return data for content checks: `get_error_message() -> str`
3. Raise exceptions for unexpected states (optional)
4. No assertions: Return values, let tests assert

### Relationships

**Extends**: `BasePage` (provides common methods: `navigate_to`, `wait_for_url`, `capture_screenshot`)

**Uses**:
- `Page` (Playwright page instance)
- `Utility` modules (SmartWaits for complex waits, BrowserHelpers for screenshots)

**Used By**:
- Test methods (tests import and instantiate page objects via fixtures)

### State Transitions

PageObjects are **stateless** (functional scope). Each test gets a fresh page object instance with a fresh page/context.

```
┌─────────────┐
│ Test Start  │
└──────┬──────┘
       │ fixture injection
       ▼
┌─────────────┐
│ PageObject  │
│ Created     │
└──────┬──────┘
       │ test interactions
       ▼
┌─────────────┐
│ PageObject  │
│ Used        │
└──────┬──────┘
       │ test end
       ▼
┌─────────────┐
│ PageObject  │
│ Destroyed   │
└─────────────┘
```

### Validation Rules

1. ❌ **MUST NOT** contain test methods (methods starting with `test_`)
2. ❌ **MUST NOT** contain assertions (`assert` statements)
3. ❌ **MUST NOT** use CSS classes like `.MuiButton-root-123abc`
4. ❌ **MUST NOT** use hardcoded non-English text in locators
5. ✅ **MUST** use `@property` for all locators
6. ✅ **MUST** have type hints on all methods
7. ✅ **MUST** have docstrings on all public methods

### Example

```python
from typing import Optional
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    """Registration page for new user accounts"""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "https://seller.greatmall.uz/register"

    # Locators (properties)
    @property
    def first_name_field(self) -> Locator:
        """First name input"""
        return self.page.get_by_label("First Name")

    @property
    def email_field(self) -> Locator:
        """Email input"""
        return self.page.get_by_label("Email")

    @property
    def submit_button(self) -> Locator:
        """Submit button"""
        return self.page.get_by_role("button", name="Create Account")

    @property
    def validation_errors(self) -> Locator:
        """Validation error messages"""
        return self.page.get_by_role("alert")

    # Actions
    def fill_registration_form(
        self,
        first_name: str,
        email: str,
        password: str
    ) -> None:
        """Fill registration form with provided data"""
        self.first_name_field.fill(first_name)
        self.email_field.fill(email)
        self.page.get_by_label("Password").fill(password)

    def submit_registration(self) -> None:
        """Submit registration form"""
        self.submit_button.click()

    # Verifications
    def has_validation_errors(self) -> bool:
        """Check if validation errors are displayed"""
        return self.validation_errors.count() > 0

    def get_error_messages(self) -> list[str]:
        """Get all error messages"""
        return [elem.text_content() for elem in self.validation_errors.all()]
```

---

## Entity 2: TestFixture

### Purpose
Provides setup and teardown for test dependencies (browser, context, page, authentication, test data). Fixtures enable test isolation and parallel execution.

### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `scope` | `str` | Yes | pytest fixture scope: "session", "module", "class", "function" |
| `dependencies` | `List[str]` | No | Other fixtures required (implicit via parameters) |
| `teardown` | `Callable` | No | Cleanup function (implicit via `yield`) |
| `autouse` | `bool` | No | Auto-apply to all tests (default: False) |

### Types

#### Browser Fixtures (Session Scope)
Shared across all tests for performance.

**Fixtures**:
- `playwright`: Playwright instance (launches once per session)
- `browser`: Browser instance (chromium/firefox/webkit)

**Rationale**: Browser launch is expensive (~1-2 seconds), sharing saves time.

**Implementation** (conftest.py:62-115):
```python
@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    """Session-level Playwright instance"""
    pw = sync_playwright().start()
    yield pw
    pw.stop()

@pytest.fixture(scope="session")
def browser(playwright: Playwright, request) -> Generator[Browser, None, None]:
    """Session-level browser instance"""
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    browser_instance = playwright.chromium.launch(headless=headless)
    yield browser_instance
    browser_instance.close()
```

#### Page Fixtures (Function Scope)
Isolated per test for parallel execution.

**Fixtures**:
- `context`: BrowserContext (isolated cookies, storage, cache)
- `page`: Page (isolated page instance)

**Rationale**: Function scope ensures each test has fresh state, enabling parallel execution.

**Implementation** (conftest.py:124-183):
```python
@pytest.fixture(scope="function")  # ✅ CRITICAL for test isolation
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Function-level browser context"""
    context_instance = browser.new_context()
    yield context_instance
    context_instance.close()

@pytest.fixture(scope="function")  # ✅ CRITICAL for test isolation
def page(context: BrowserContext, request) -> Generator[Page, None, None]:
    """Function-level page"""
    page_instance = context.new_page()
    base_url = request.config.getoption("url_name")
    page_instance.goto(base_url)
    yield page_instance
    page_instance.close()
```

#### Authentication Fixtures (Function Scope)
Provide pre-authenticated page instances.

**Fixture**:
- `authenticated_page`: Page instance after login

**Implementation** (conftest.py:260-304):
```python
@pytest.fixture(scope="function")
def authenticated_page(page: Page, test_data: Dict[str, Any]) -> Page:
    """Pre-authenticated page"""
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

#### Data Fixtures (Function Scope)
Load test data from JSON files.

**Fixture**:
- `test_data`: Dictionary of test data for current test module

**Implementation** (conftest.py:222-253):
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

### Validation Rules

1. ✅ **MUST** use function scope for `context` and `page` (test isolation)
2. ✅ **MUST** use session scope only for `playwright` and `browser` (performance)
3. ❌ **MUST NOT** use session/class scope for `context` or `page` (blocks parallel execution)
4. ✅ **MUST** clean up resources in teardown (via `yield`)
5. ✅ **MUST** have type hints on fixture return types

---

## Entity 3: TestData

### Purpose
JSON-based test data with schema validation, environment overrides, and per-test isolation.

### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | `Path` | Yes | Path to JSON file (e.g., `test_data/login_test_data.json`) |
| `schema` | `Dict` | No | JSON schema for validation (e.g., `test_data/schemas/login_schema.json`) |
| `data` | `Dict[str, Any]` | Yes | Loaded test data |
| `environment_overrides` | `Dict` | No | Environment-specific overrides (dev/staging/prod) |

### Behavior

#### Loading with Caching
Uses `@lru_cache` to avoid re-reading JSON files for each test.

**Implementation** (utils/test_data_loader.py:13-25):
```python
from functools import lru_cache
import json
from pathlib import Path

class TestDataLoader:
    BASE_DIR = Path(__file__).parent.parent / "test_data"

    @classmethod
    @lru_cache(maxsize=32)
    def load(cls, module_name: str) -> Dict[str, Any]:
        """Load test data with caching"""
        json_file = cls.BASE_DIR / f"{module_name}_test_data.json"
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)
```

#### Schema Validation
Validates test data against JSON schema before use.

**Implementation** (utils/validators.py):
```python
import jsonschema

def validate_test_data(data: Dict, schema: Dict) -> bool:
    """Validate test data against JSON schema"""
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.ValidationError as e:
        raise ValueError(f"Test data validation failed: {e.message}")
```

#### Environment Overrides
Merges environment-specific values (URLs, credentials) into test data.

**Pattern**:
```json
{
  "base_url": "${BASE_URL}",
  "credentials": {
    "email": "${TEST_EMAIL}",
    "password": "${TEST_PASSWORD}"
  }
}
```

### Validation Rules

1. ✅ **MUST** pass JSON schema validation (if schema provided)
2. ❌ **MUST NOT** contain hardcoded credentials (use env vars)
3. ✅ **MUST** be immutable after loading (no in-place modifications)
4. ✅ **MUST** provide per-test isolation (no shared mutable data)

### Example

**Test Data File** (`test_data/login_test_data.json`):
```json
{
  "valid_credentials": {
    "email": "test@example.com",
    "password": "SecurePassword123"
  },
  "invalid_credentials": {
    "email": "invalid@example.com",
    "password": "WrongPassword"
  },
  "empty_email": {
    "email": "",
    "password": "SecurePassword123"
  }
}
```

**Schema File** (`test_data/schemas/login_schema.json`):
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "valid_credentials": {
      "type": "object",
      "properties": {
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string", "minLength": 8}
      },
      "required": ["email", "password"]
    }
  },
  "required": ["valid_credentials"]
}
```

---

## Entity 4: Configuration

### Purpose
Centralized settings for URLs, timeouts, browser options, and credentials. Loads from environment variables with sensible defaults.

### Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `BASE_URL` | `str` | `"https://dev-seller.greatmall.uz"` | Base URL for tests |
| `BROWSER` | `str` | `"chromium"` | Browser: chromium, firefox, webkit |
| `HEADLESS` | `bool` | `False` | Run browser in headless mode |
| `DEFAULT_TIMEOUT` | `int` | `10000` | Default timeout in milliseconds |
| `SCREENSHOTS_DIR` | `Path` | `Path("screenshots")` | Screenshot directory |
| `REPORTS_DIR` | `Path` | `Path("reports")` | Reports directory |
| `LOGS_DIR` | `Path` | `Path("logs")` | Logs directory |
| `TEST_DATA_DIR` | `Path` | `Path("test_data")` | Test data directory |
| `ALLURE_ENDPOINT` | `str` | `None` | Allure TestOps endpoint |
| `ALLURE_TOKEN` | `str` | `None` | Allure TestOps API token |
| `ALLURE_PROJECT_ID` | `str` | `None` | Allure TestOps project ID |

### Behavior

#### Loading from Environment
Uses `os.getenv()` with defaults.

**Implementation** (config/settings.py):
```python
import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Settings:
    BASE_URL: str = os.getenv('BASE_URL', 'https://dev-seller.greatmall.uz')
    BROWSER: str = os.getenv('BROWSER', 'chromium')
    HEADLESS: bool = os.getenv('HEADLESS', 'false').lower() == 'true'
    DEFAULT_TIMEOUT: int = int(os.getenv('DEFAULT_TIMEOUT', '10000'))
    SCREENSHOTS_DIR: Path = Path(os.getenv('SCREENSHOTS_DIR', 'screenshots'))
    ALLURE_ENDPOINT: str = os.getenv('ALLURE_ENDPOINT', '')
    ALLURE_TOKEN: str = os.getenv('ALLURE_TOKEN', '')

    def get_browser_launch_options(self) -> dict:
        """Get browser launch options"""
        return {
            "headless": self.HEADLESS,
            "args": ["--start-maximized"],
        }

    def get_browser_context_options(self) -> dict:
        """Get browser context options"""
        return {
            "viewport": {"width": 1920, "height": 1080},
            "locale": "en-US",
        }

settings = Settings()
```

### Validation Rules

1. ✅ **MUST** load from environment variables (not hardcoded)
2. ✅ **MUST** provide sensible defaults for local development
3. ✅ **MUST** validate required variables (raise exception if missing)
4. ✅ **MUST** create directories on startup if they don't exist

---

## Entity 5: Utility

### Purpose
Reusable helper functions for waits, logging, data manipulation, and browser operations. Utilities are stateless and side-effect-free.

### Modules

#### SmartWaits (utils/waits.py)
Intelligent wait strategies beyond Playwright's built-in waits.

**Methods**:
- `wait_for_element_visible(locator, timeout)`: Wait for element visibility
- `wait_for_url_pattern(page, pattern, timeout)`: Wait for URL to match pattern
- `wait_for_ajax_complete(page)`: Wait for network idle
- `wait_for_element_count(locator, count, timeout)`: Wait for specific element count

#### TestDataLoader (utils/test_data_loader.py)
JSON loading with caching (documented in Entity 3).

#### BrowserHelpers (utils/browser_helpers.py)
Browser operations: screenshots, console logs, HAR capture.

**Methods**:
- `capture_screenshot(page, name)`: Save screenshot to SCREENSHOTS_DIR
- `get_console_logs(page)`: Get all console messages
- `get_failed_requests(page)`: Get all failed network requests
- `save_har(context, filename)`: Save network HAR file

#### Logger (utils/logger.py)
Logging configuration with rotation.

**Implementation**:
```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str = "test_execution.log") -> logging.Logger:
    """Setup logger with rotation"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Console handler
    console = logging.StreamHandler()
    logger.addHandler(console)

    # File handler (rotating, 10MB max, 5 backups)
    file_handler = RotatingFileHandler(
        f"logs/{log_file}", maxBytes=10*1024*1024, backupCount=5
    )
    logger.addHandler(file_handler)

    return logger
```

#### Validators (utils/validators.py)
JSON schema validation (documented in Entity 3).

---

## Entity 6: Report

### Purpose
Allure test report with steps, attachments, metadata, and traceability. Integrates with Allure TestOps for centralized reporting.

### Attributes

**Decorators**:
- `@allure.epic("Seller Web Platform")`: Top-level grouping
- `@allure.feature("User Registration")`: Feature grouping
- `@allure.story("Field Validation")`: Story grouping
- `@allure.title("Verify empty fields validation")`: Test title
- `@allure.severity(allure.severity_level.CRITICAL)`: Severity level
- `@pytest.mark.negative`: Custom marker

**Steps**:
- `@allure.step("Fill registration form")`: Test step

**Attachments**:
- Screenshot (auto-attached on failure)
- Page HTML (auto-attached on failure)
- Console logs (auto-attached on failure)
- Network requests (auto-attached on failure)

### Example

```python
import allure
import pytest
from pages.registration_page import RegistrationPage

@allure.epic("Seller Web Platform")
@allure.feature("User Registration")
@allure.story("Field Validation")
@allure.title("Verify empty fields validation")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative
def test_empty_fields(page, registration_page: RegistrationPage):
    with allure.step("Navigate to registration page"):
        registration_page.navigate_to()

    with allure.step("Submit form with empty fields"):
        registration_page.fill_registration_form("", "", "", "")
        registration_page.submit_registration()

    with allure.step("Verify validation errors displayed"):
        assert registration_page.has_validation_errors()
        errors = registration_page.get_error_messages()
        assert len(errors) == 4  # 4 required fields
```

---

## Relationships Summary

```
Configuration (singleton)
    └── loaded by → TestFixture, PageObject, Utility

TestFixture
    └── provides → PageObject (via page/context)
    └── provides → TestData (via test_data fixture)

PageObject
    └── extends → BasePage
    └── uses → Page (from fixture)
    └── uses → Utility (SmartWaits, BrowserHelpers)
    └── used by → Test methods

TestData
    └── loaded by → TestDataLoader utility
    └── validated by → Validators utility
    └── injected by → test_data fixture

Utility
    └── used by → PageObject, TestFixture, Tests

Report
    └── generated by → Allure decorators + auto-attachments
    └── uploaded to → Allure TestOps
```

---

## Summary

This data model defines 6 core entities for the refactored test automation framework:

1. **PageObject**: UI abstraction with locators (properties), actions, verifications
2. **TestFixture**: Setup/teardown with proper scoping (session for browser, function for page)
3. **TestData**: JSON-based test data with schema validation and caching
4. **Configuration**: Centralized settings loaded from environment variables
5. **Utility**: Reusable helpers (waits, logging, browser operations)
6. **Report**: Allure reports with steps, attachments, TestOps integration

**Key Design Decisions**:
- Function-scoped fixtures for test isolation and parallel execution
- ARIA roles for stable locators
- Immutable test data for predictability
- Stateless utilities for composability
- Allure for comprehensive reporting

**Next Steps**:
1. ✅ Create `contracts/` directory with interface definitions
2. ✅ Generate `quickstart.md` for rapid onboarding
3. ✅ Run `update-agent-context.sh` to update Claude context
4. ✅ Execute `/speckit.tasks` to generate implementation tasks
