# Quickstart: Returns Test Automation

**Feature**: 001-returns-tests
**Date**: 2025-12-20

## Overview

This guide explains how to implement and run the Returns test automation feature.

## Prerequisites

1. Python 3.11+ installed
2. Project dependencies installed: `pip install -r requirements.txt`
3. Playwright browsers installed: `playwright install chromium`
4. Access to dev environment: https://dev-admin.greatmall.uz/

## Files to Create

### 1. Page Objects

**pages/returns_page.py**
```python
"""Returns list page object."""
from pages.base_page import BasePage
from utils.constants import BASE_URL

RETURN_STATUS_TABS = [
    "Все", "На рассмотрении", "Одобрено продавцом", ...
]

class ReturnsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._returns_url = f"{BASE_URL}dashboard/order-management/returns"
        # Define locators...

    def navigate(self):
        self.page.goto(self._returns_url)

    # Implement methods per plan.md...
```

**pages/return_detail_page.py**
```python
"""Return detail page object."""
from pages.base_page import BasePage

class ReturnDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Define locators...

    def get_return_number(self):
        # Extract from title...

    # Implement methods per plan.md...
```

### 2. Test File

**tests/test_returns.py**
```python
"""Returns feature tests."""
import pytest
from playwright.sync_api import Page
from pages.returns_page import ReturnsPage
from pages.return_detail_page import ReturnDetailPage

class TestReturnsBase:
    @pytest.fixture(autouse=True)
    def setup(self, logged_in_page: Page):
        self.page = logged_in_page
        self.returns_page = ReturnsPage(logged_in_page)
        self.detail_page = ReturnDetailPage(logged_in_page)

class TestReturnsNavigation(TestReturnsBase):
    @pytest.mark.returns
    def test_01_return_list_loads(self):
        self.returns_page.navigate()
        assert self.returns_page.is_on_returns_list_page()

# Continue with other test classes...
```

## Running Tests

### Run all returns tests
```bash
pytest tests/test_returns.py -v
```

### Run with specific marker
```bash
pytest -m returns -v
```

### Run with HTML report
```bash
pytest tests/test_returns.py --html=reports/returns_report.html
```

### Run in headed mode (see browser)
```bash
HEADLESS=false pytest tests/test_returns.py -v
```

## Key Patterns

### 1. Session-Scoped Login
Tests use `logged_in_page` fixture from conftest.py. Login happens once per session.

### 2. Playwright Auto-Waiting
Never use `page.wait_for_timeout()`. Use:
- `expect(element).to_be_visible()`
- `page.wait_for_url("**/pattern")`

### 3. Class-Based Organization
Group related tests in classes:
- `TestReturnsNavigation` - Page load, URL checks
- `TestReturnsPagination` - Page navigation
- `TestReturnsSearch` - Search by ID
- `TestReturnsFilter` - Status tab filtering
- `TestReturnsDetails` - Detail page content
- `TestReturnsActions` - Approve/Reject/Refund
- `TestReturnsHistory` - History section
- `TestReturnsImages` - Image management

## Qase.io Mapping

| Test Method | Qase ID | Description |
|-------------|---------|-------------|
| test_01_return_list_loads | 1623 | Return list loads correctly |
| test_02_pagination_works | 1624 | Pagination navigation |
| test_03_empty_state | 1625 | Empty state display |
| ... | ... | ... |
| test_35_no_duplicate_refund | 1657 | Prevent double refund |

See plan.md for complete mapping.

## Troubleshooting

### Test fails with "element not found"
- Check if page has loaded (add explicit wait for URL)
- Verify locator matches current UI

### Login fails
- Verify credentials in utils/constants.py
- Check if dev environment is accessible

### Flaky tests
- Avoid timing-based assertions
- Use Playwright's auto-waiting assertions
- Ensure proper page state before actions
