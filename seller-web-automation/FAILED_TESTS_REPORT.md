# BUG REPORT: FAILED Tests (178 tests)

**Environment:** staging-seller.greatmall.uz
**Browser:** Chromium (headless)
**Date:** 2026-02-16
**Runner:** pytest -n 6 (parallel)
**Total FAILED:** 178

---

## Summary by Page

| Page | Count | Severity |
|------|-------|----------|
| Dashboard | 13 | High |
| Employee/Staff | 15 | Medium |
| Login | 1 | Medium |
| Multi-Product | 2 | Medium |
| Order Detail | 3 | Medium |
| Orders | 26 | Critical |
| Product Create | 30 | Critical |
| Products List | 27 | Critical |
| Profile Settings | 7 | Critical |
| Returns | 2 | Medium |
| Reviews | 6 | Medium |
| Shop Create | 14 | Critical |
| Shop Settings | 32 | Critical |

---

## Dashboard (13 failures)

### BUG-F001: test_sidebar_navigation[invoices]

- **ID:** BUG-F001
- **Test:** `TestDashboardNavigation.test_sidebar_navigation[invoices]`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Счет-фактура' not found in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:119: in test_sidebar_navigation
    assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Счет-фактура' not found in sidebar
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/auth/login'> selector="a:has-text('Счет-фактура') >> nth=0">.is_visible
```
</details>

---

### BUG-F002: test_sidebar_navigation[finance]

- **ID:** BUG-F002
- **Test:** `TestDashboardNavigation.test_sidebar_navigation[finance]`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Финансы' not found in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:119: in test_sidebar_navigation
    assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Финансы' not found in sidebar
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/auth/login'> selector="a:has-text('Финансы') >> nth=0">.is_visible
```
</details>

---

### BUG-F003: test_sidebar_navigation[analytics]

- **ID:** BUG-F003
- **Test:** `TestDashboardNavigation.test_sidebar_navigation[analytics]`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Аналитика' not found in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:119: in test_sidebar_navigation
    assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Аналитика' not found in sidebar
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/auth/login'> selector="a:has-text('Аналитика') >> nth=0">.is_visible
```
</details>

---

### BUG-F004: test_sidebar_navigation[settings]

- **ID:** BUG-F004
- **Test:** `TestDashboardNavigation.test_sidebar_navigation[settings]`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Настройки' not found in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:119: in test_sidebar_navigation
    assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Настройки' not found in sidebar
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/auth/login'> selector="a:has-text('Настройки') >> nth=0">.is_visible
```
</details>

---

### BUG-F005: test_session_persists_after_refresh

- **ID:** BUG-F005
- **Test:** `TestDashboardNavigation.test_session_persists_after_refresh`
- **File:** `tests/test_dashboard.py`
- **Severity:** High
- **Category:** Session
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert "dashboard" in page.url.lower()
E   AssertionError: assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:133: in test_session_persists_after_refresh
    assert "dashboard" in page.url.lower()
E   AssertionError: assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x1088851b0>()
E    +    where <built-in method lower of str object at 0x1088851b0> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
```
</details>

---

### BUG-F006: test_shop_dropdown_opens

- **ID:** BUG-F006
- **Test:** `TestDashboardShopDropdown.test_shop_dropdown_opens`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
E   AssertionError: Locator expected to be visible
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:158: in test_shop_dropdown_opens
    expect(shop_btn).to_be_visible(timeout=5000)
E   AssertionError: Locator expected to be visible
E   Actual value: None
E   Error: element(s) not found
E   Call log:
E     - Expect "to_be_visible" with timeout 5000ms
E     - waiting for locator("button:has-text('Active')").first
```
</details>

---

### BUG-F007: test_dashboard_loads_with_core_elements

- **ID:** BUG-F007
- **Test:** `TestDashboardSmoke.test_dashboard_loads_with_core_elements`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
E   AssertionError: Locator expected to be visible
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:63: in test_dashboard_loads_with_core_elements
    expect(shop_btn).to_be_visible(timeout=10000)
E   AssertionError: Locator expected to be visible
E   Actual value: None
E   Error: element(s) not found
E   Call log:
E     - Expect "to_be_visible" with timeout 10000ms
E     - waiting for locator("button:has-text('Active')").first
```
</details>

---

### BUG-F008: test_sidebar_navigation[products]

- **ID:** BUG-F008
- **Test:** `TestDashboardNavigation.test_sidebar_navigation[products]`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Товары' not found in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:119: in test_sidebar_navigation
    assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Товары' not found in sidebar
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard'> selector="a:has-text('Товары') >> nth=0">.is_visible
```
</details>

---

### BUG-F009: test_sidebar_navigation[orders]

- **ID:** BUG-F009
- **Test:** `TestDashboardNavigation.test_sidebar_navigation[orders]`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Заказы' not found in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:119: in test_sidebar_navigation
    assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Заказы' not found in sidebar
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard'> selector="a:has-text('Заказы') >> nth=0">.is_visible
```
</details>

---

### BUG-F010: test_sidebar_navigation[returns]

- **ID:** BUG-F010
- **Test:** `TestDashboardNavigation.test_sidebar_navigation[returns]`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Возвраты' not found in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:119: in test_sidebar_navigation
    assert nav_item.is_visible(timeout=5000), \
E   AssertionError: BUG: Navigation item 'Возвраты' not found in sidebar
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard'> selector="a:has-text('Возвраты') >> nth=0">.is_visible
```
</details>

---

### BUG-F011: test_dropdown_has_add_shop_button

- **ID:** BUG-F011
- **Test:** `TestDashboardShopDropdown.test_dropdown_has_add_shop_button`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Active')").first
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:172: in test_dropdown_has_add_shop_button
    page.locator("button:has-text('Active')").first.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Active')").first
```
</details>

---

### BUG-F012: test_dropdown_closes_on_escape

- **ID:** BUG-F012
- **Test:** `TestDashboardShopDropdown.test_dropdown_closes_on_escape`
- **File:** `tests/test_dashboard.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Active')").first
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:186: in test_dropdown_closes_on_escape
    page.locator("button:has-text('Active')").first.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Active')").first
```
</details>

---

### BUG-F013: test_logout_accessible

- **ID:** BUG-F013
- **Test:** `TestDashboardSession.test_logout_accessible`
- **File:** `tests/test_dashboard.py`
- **Severity:** High
- **Category:** Session
- **Page:** Dashboard

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
pytest.fail("BUG: Logout button not accessible from dashboard")
E   Failed: BUG: Logout button not accessible from dashboard
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_dashboard.py:234: in test_logout_accessible
    pytest.fail("BUG: Logout button not accessible from dashboard")
E   Failed: BUG: Logout button not accessible from dashboard
```
</details>

---

## Employee/Staff (15 failures)

### BUG-F014: test_create_staff_with_valid_data

- **ID:** BUG-F014
- **Test:** `TestEmployeeCreation.test_create_staff_with_valid_data`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff
3. Fill form with valid data and submit

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:202: in test_create_staff_with_valid_data
    employee = test_data["employee_data"]
E   KeyError: 'employee_data'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:48 - conftest - INFO - playwright:74 - Starting Playwright session
2026-02-16 09:30:48 - conftest - INFO - browser:99 - Launching chromium browser (headless=True)
2026-02-16 09:30:49 - conftest - INFO - seller_auth_state:260 - Loaded cached auth state from disk
2026-02-16 09:30:49 - conftest - INFO - seller_authenticated_session:322 - Creating SELLER session from cached auth state
2026-02-16 09:30:51 - conftest - INFO - seller_authenticated_session:353 - SELLER SESSION ready (URL: https://staging-seller.greatmall.uz/dashboard)
2026-02-16 09:30:51 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:51 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:52 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:52 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:52 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:30:52 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:30:53 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
2026-02-16 09:30:53 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:30:53 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:74 Starting Playwright session
INFO     conftest:conftest.py:99 Launching chromium browser (headless=True)
INFO     conftest:conftest.py:260 Loaded cached auth state from disk
INFO     conftest:conftest.py:322 Creating SELLER session from cached auth state
INFO     conftest:conftest.py:353 SELLER SESSION ready (URL: https://staging-seller.greatmall.uz/dashboard)
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```
</details>

---

### BUG-F015: test_create_staff_different_roles[manager]

- **ID:** BUG-F015
- **Test:** `TestEmployeeCreation.test_create_staff_different_roles[manager]`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Manager' не доступна в списке ролей
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:233: in test_create_staff_different_roles
    assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Manager' не доступна в списке ролей
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/staff/create'> selector='internal:role=option[name="Manager"s]'>.is_visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:53 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:53 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:53 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:53 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:53 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:30:53 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:30:53 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:30:53 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:30:54 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
```
</details>

---

### BUG-F016: test_create_staff_different_roles[finance_manager]

- **ID:** BUG-F016
- **Test:** `TestEmployeeCreation.test_create_staff_different_roles[finance_manager]`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Finance Manager' не доступна в списке ролей
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:233: in test_create_staff_different_roles
    assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Finance Manager' не доступна в списке ролей
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/staff/create'> selector='internal:role=option[name="Finance Manager"s]'>.is_visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:54 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:54 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:54 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:54 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:54 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:30:55 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:30:55 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:30:55 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:30:55 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
```
</details>

---

### BUG-F017: test_create_staff_different_roles[content_manager]

- **ID:** BUG-F017
- **Test:** `TestEmployeeCreation.test_create_staff_different_roles[content_manager]`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Content Manager' не доступна в списке ролей
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:233: in test_create_staff_different_roles
    assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Content Manager' не доступна в списке ролей
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/staff/create'> selector='internal:role=option[name="Content Manager"s]'>.is_visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:55 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:55 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:55 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:55 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:55 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:30:56 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:30:56 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:30:56 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:30:56 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
```
</details>

---

### BUG-F018: test_create_staff_different_roles[marketer]

- **ID:** BUG-F018
- **Test:** `TestEmployeeCreation.test_create_staff_different_roles[marketer]`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Marketer' не доступна в списке ролей
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:233: in test_create_staff_different_roles
    assert role_option.is_visible(timeout=3000), \
E   AssertionError: BUG: Роль 'Marketer' не доступна в списке ролей
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/staff/create'> selector='internal:role=option[name="Marketer"s]'>.is_visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:56 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:56 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:56 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:56 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:56 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:30:57 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:30:57 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:30:57 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:30:57 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
```
</details>

---

### BUG-F019: test_form_shows_response_after_submit

- **ID:** BUG-F019
- **Test:** `TestEmployeeCreation.test_form_shows_response_after_submit`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:241: in test_form_shows_response_after_submit
    employee = test_data["employee_data"]
E   KeyError: 'employee_data'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:57 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:57 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:57 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:57 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:57 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:30:57 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:30:58 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
2026-02-16 09:30:58 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:30:58 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```
</details>

---

### BUG-F020: test_success_redirects_to_list

- **ID:** BUG-F020
- **Test:** `TestEmployeeCreation.test_success_redirects_to_list`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:260: in test_success_redirects_to_list
    employee = test_data["employee_data"]
E   KeyError: 'employee_data'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:58 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:58 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:58 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:58 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:58 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:30:58 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:30:59 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
2026-02-16 09:30:59 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:30:59 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```
</details>

---

### BUG-F021: test_delete_shows_confirmation

- **ID:** BUG-F021
- **Test:** `TestEmployeeDelete.test_delete_shows_confirmation`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert employee_page.is_delete_confirmation_visible(), \
E   AssertionError: BUG: Диалог подтверждения удаления не появился
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:289: in test_delete_shows_confirmation
    assert employee_page.is_delete_confirmation_visible(), \
E   AssertionError: BUG: Диалог подтверждения удаления не появился
E   assert False
E    +  where False = is_delete_confirmation_visible()
E    +    where is_delete_confirmation_visible = <pages.employee_page.EmployeePage object at 0x10c6daeb0>.is_delete_confirmation_visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:59 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:30:59 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:59 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:30:59 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:30:59 - pages.base_page - INFO - navigate:100 - Staff page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:31:00 - pages.base_page - INFO - get_employee_count:140 - Staff count: 3
2026-02-16 09:31:00 - pages.base_page - INFO - click_delete_staff:276 - Clicking delete button for staff at index 0...
2026-02-16 09:31:00 - pages.base_page - WARNING - click_delete_staff:288 - Delete button not found for row 0
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:employee_page.py:140 Staff count: 3
INFO     pages.base_page:employee_page.py:276 Clicking delete button for staff at index 0...
WARNING  pages.base_page:employee_page.py:288 Delete button not found for row 0
```
</details>

---

### BUG-F022: test_confirm_delete_removes_staff

- **ID:** BUG-F022
- **Test:** `TestEmployeeDelete.test_confirm_delete_removes_staff`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:276 Clicking delete button for staff at index 0...
WARNING  pages.base_page:employee_page.py:288 Delete button not found for row 0
INFO     pages.base_page:employee_page.py:292 Confirming staff deletion...
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:311: in test_confirm_delete_removes_staff
    employee_page.delete_staff_member(index=0, confirm=True)
pages/employee_page.py:323: in delete_staff_member
    self.confirm_delete()
pages/employee_page.py:296: in confirm_delete
    if confirm_btn.is_visible(timeout=settings.MEDIUM_TIMEOUT):
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:17297: in is_visible
    self._sync(self._impl_obj.is_visible(timeout=timeout))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:531: in is_visible
    return await self._frame.is_visible(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:408: in is_visible
    return await self._channel.send(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.Error: Locator.is_visible: Error: strict mode violation: get_by_role("button", name="Delete").or_(get_by_role("button", name="Удалить")).or_(get_by_role("button", name="O'
E       1) <button tabindex="0" type="button" aria-label="Xodimni o'chirish" class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorError MuiIconButton-sizeSmall css-1a1kalm">…</button> aka g
E       2) <button tabindex="0" type="button" aria-label="Xodimni o'chirish" class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorError MuiIconButton-sizeSmall css-1a1kalm">…</button> aka g
E       3) <button tabindex="0" type="button" aria-label="Xodimni o'chirish" class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorError MuiIconButton-sizeSmall css-1a1kalm">…</button> aka g
E
E   Call log:
E       - checking visibility of get_by_role("button", name="Delete").or_(get_by_role("button", name="Удалить")).or_(get_by_role("button", name="O'chirish"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:01 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:31:01 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:01 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:01 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:01 - pages.base_page - INFO - navigate:100 - Staff page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:31:02 - pages.base_page - INFO - get_employee_count:140 - Staff count: 3
2026-02-16 09:31:02 - pages.base_page - INFO - delete_staff_member:320 - Deleting staff member at index 0, confirm=True
2026-02-16 09:31:02 - pages.base_page - INFO - click_delete_staff:276 - Clicking delete button for staff at index 0...
... (8 more lines)
```
</details>

---

### BUG-F023: test_search_with_valid_query

- **ID:** BUG-F023
- **Test:** `TestEmployeeSearch.test_search_with_valid_query`
- **File:** `tests/employee/test_employee_ui.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_ui
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_ui.py:103: in test_search_with_valid_query
    query = test_data["search"]["valid_query"]
E   KeyError: 'search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:11 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:31:11 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:12 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:12 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:12 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:31:12 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
2026-02-16 09:31:12 - conftest - WARNING - test_data:498 - No test data found for module: employee_ui
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_ui
```
</details>

---

### BUG-F024: test_search_no_results

- **ID:** BUG-F024
- **Test:** `TestEmployeeSearch.test_search_no_results`
- **File:** `tests/employee/test_employee_ui.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_ui
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_ui.py:114: in test_search_no_results
    query = test_data["search"]["no_results_query"]
E   KeyError: 'search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:13 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:31:13 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:13 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:13 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:13 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:31:13 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
2026-02-16 09:31:13 - conftest - WARNING - test_data:498 - No test data found for module: employee_ui
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_ui
```
</details>

---

### BUG-F025: test_search_clear_restores_data

- **ID:** BUG-F025
- **Test:** `TestEmployeeSearch.test_search_clear_restores_data`
- **File:** `tests/employee/test_employee_ui.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_ui
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_ui.py:125: in test_search_clear_restores_data
    query = test_data["search"]["no_results_query"]
E   KeyError: 'search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:13 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:31:13 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:14 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:14 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:14 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:31:14 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
2026-02-16 09:31:14 - conftest - WARNING - test_data:498 - No test data found for module: employee_ui
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_ui
```
</details>

---

### BUG-F026: test_expected_columns_exist

- **ID:** BUG-F026
- **Test:** `TestEmployeeTable.test_expected_columns_exist`
- **File:** `tests/employee/test_employee_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert has_name or has_phone or has_role, \
E   AssertionError: BUG: Нет ожидаемых колонок (name/phone/role) в: ["To'liq ism", 'Email', 'Telefon', 'Rol', "Do'konlar", 'Yaratilgan sana', 'Harakatlar']
E   assert (False or False or False)
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_ui.py:198: in test_expected_columns_exist
    assert has_name or has_phone or has_role, \
E   AssertionError: BUG: Нет ожидаемых колонок (name/phone/role) в: ["To'liq ism", 'Email', 'Telefon', 'Rol', "Do'konlar", 'Yaratilgan sana', 'Harakatlar']
E   assert (False or False or False)
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:21 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:31:21 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:21 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:31:21 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:21 - pages.base_page - INFO - navigate:100 - Staff page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
```
</details>

---

### BUG-F027: test_phone_only_without_role_blocked

- **ID:** BUG-F027
- **Test:** `TestEmployeeFormValidation.test_phone_only_without_role_blocked`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:117: in test_phone_only_without_role_blocked
    phone = test_data["employee_data"]["phone"]
E   KeyError: 'employee_data'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:12 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:32:12 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:32:12 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:32:12 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:12 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:32:12 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:32:13 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
2026-02-16 09:32:13 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:32:13 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```
</details>

---

### BUG-F028: test_double_click_submit_no_duplicate

- **ID:** BUG-F028
- **Test:** `TestEmployeeFormValidation.test_double_click_submit_no_duplicate`
- **File:** `tests/employee/test_employee_functional.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Employee/Staff

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/staff
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/employee/test_employee_functional.py:130: in test_double_click_submit_no_duplicate
    phone = test_data["employee_data"]["phone"]
E   KeyError: 'employee_data'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:13 - pages.base_page - INFO - navigate:97 - Navigating to staff page...
2026-02-16 09:32:13 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:32:13 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
2026-02-16 09:32:13 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:13 - pages.base_page - INFO - navigate:100 - Staff page loaded
2026-02-16 09:32:13 - pages.base_page - INFO - click_add_employee:166 - Clicking Add Staff Member link...
2026-02-16 09:32:14 - pages.base_page - INFO - click_add_employee:172 - Add Staff Member form opened
2026-02-16 09:32:14 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.
2026-02-16 09:32:14 - conftest - WARNING - test_data:498 - No test data found for module: employee_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:employee_page.py:97 Navigating to staff page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/staff
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:employee_page.py:100 Staff page loaded
INFO     pages.base_page:employee_page.py:166 Clicking Add Staff Member link...
INFO     pages.base_page:employee_page.py:172 Add Staff Member form opened
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/employee_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: employee_functional
```
</details>

---

## Login (1 failures)

### BUG-F029: test_complete_login_logout_flow

- **ID:** BUG-F029
- **Test:** `TestLoginSmoke.test_complete_login_logout_flow`
- **File:** `tests/test_login.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Login

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /auth/login

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert logout_found, "Sign Out button not found in profile sidebar"
E   AssertionError: Sign Out button not found in profile sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw4] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_login.py:146: in test_complete_login_logout_flow
    assert logout_found, "Sign Out button not found in profile sidebar"
E   AssertionError: Sign Out button not found in profile sidebar
E   assert False
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:56 - conftest - INFO - context:385 - Creating SESSION-SCOPED browser context
2026-02-16 09:43:56 - conftest - INFO - page:420 - Creating SESSION-SCOPED page
2026-02-16 09:43:57 - pages.login_page - INFO - open_login_page:58 - Opening login page...
2026-02-16 09:43:57 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/auth/login
2026-02-16 09:43:57 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/auth/login
2026-02-16 09:43:57 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:43:57 - utils.test_data_loader - INFO - load:63 - Loaded test data from login_test_data.json
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:385 Creating SESSION-SCOPED browser context
INFO     conftest:conftest.py:420 Creating SESSION-SCOPED page
INFO     pages.login_page:login_page.py:58 Opening login page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/auth/login
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/auth/login
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     utils.test_data_loader:test_data_loader.py:63 Loaded test data from login_test_data.json
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:43:57 - pages.login_page - INFO - enter_email:71 - Entering email: 998001112233
2026-02-16 09:43:57 - pages.login_page - INFO - enter_password:78 - Entering password
2026-02-16 09:43:57 - pages.login_page - INFO - click_login:85 - Clicking login button
------------------------------ Captured log call -------------------------------
INFO     pages.login_page:login_page.py:71 Entering email: 998001112233
INFO     pages.login_page:login_page.py:78 Entering password
INFO     pages.login_page:login_page.py:85 Clicking login button
--------------------------- Captured stdout teardown ---------------------------
2026-02-16 09:43:59 - conftest - INFO - screenshot_on_failure:645 - Test failed: test_complete_login_logout_flow, capturing screenshot
2026-02-16 09:43:59 - utils.browser_helpers - INFO - capture_screenshot:53 - Screenshot saved: failure_test_complete_login_logout_flow_20260216_094359.png
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:645 Test failed: test_complete_login_logout_flow, capturing screenshot
INFO     utils.browser_helpers:browser_helpers.py:53 Screenshot saved: failure_test_complete_login_logout_flow_20260216_094359.png
```
</details>

---

## Multi-Product (2 failures)

### BUG-F030: test_create_multi_product_complete

- **ID:** BUG-F030
- **Test:** `TestMultiProductE2E.test_create_multi_product_complete`
- **File:** `tests/multiproduct/test_multiproduct_functional.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Multi-Product

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to multi-product creation

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:multiproduct_page.py:169 Selecting combobox[2]: Xitoy
INFO     pages.base_page:multiproduct_page.py:169 Selecting combobox[3]: Samsung
INFO     pages.base_page:multiproduct_page.py:169 Selecting combobox[4]: Samsung Model A
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/multiproduct/test_multiproduct_functional.py:273: in test_create_multi_product_complete
    multi_page.fill_step1_product_info(data)
pages/multiproduct_page.py:204: in fill_step1_product_info
    self.select_from_combobox_by_index(4, data["model"])
pages/multiproduct_page.py:176: in select_from_combobox_by_index
    self.page.get_by_role("option").first.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("option").first
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:30:48 - conftest - INFO - playwright:74 - Starting Playwright session
2026-02-16 09:30:48 - conftest - INFO - browser:99 - Launching chromium browser (headless=True)
2026-02-16 09:30:49 - conftest - INFO - seller_auth_state:260 - Loaded cached auth state from disk
2026-02-16 09:30:49 - conftest - INFO - seller_authenticated_session:322 - Creating SELLER session from cached auth state
2026-02-16 09:30:51 - conftest - INFO - seller_authenticated_session:353 - SELLER SESSION ready (URL: https://staging-seller.greatmall.uz/dashboard)
2026-02-16 09:30:51 - utils.test_data_loader - INFO - load:63 - Loaded test data from multiproduct_test_data.json
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:74 Starting Playwright session
INFO     conftest:conftest.py:99 Launching chromium browser (headless=True)
INFO     conftest:conftest.py:260 Loaded cached auth state from disk
INFO     conftest:conftest.py:322 Creating SELLER session from cached auth state
INFO     conftest:conftest.py:353 SELLER SESSION ready (URL: https://staging-seller.greatmall.uz/dashboard)
INFO     utils.test_data_loader:test_data_loader.py:63 Loaded test data from multiproduct_test_data.json
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:30:51 - pages.base_page - INFO - select_shop_universal:41 - Selecting shop: Zara
2026-02-16 09:30:52 - pages.base_page - INFO - select_shop_universal:52 - Shop 'Zara' selected
2026-02-16 09:30:52 - pages.base_page - INFO - click_add_products_link:61 - Clicking Add Products link
2026-02-16 09:30:52 - pages.base_page - INFO - click_multi_product_option:68 - Selecting multi-product option
2026-02-16 09:30:54 - pages.base_page - INFO - fill_step1_product_info:188 - === STEP 1: Product Information ===
... (16 more lines)
```
</details>

---

### BUG-F031: test_create_multi_product_minimal

- **ID:** BUG-F031
- **Test:** `TestMultiProductE2E.test_create_multi_product_minimal`
- **File:** `tests/multiproduct/test_multiproduct_functional.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Multi-Product

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to multi-product creation

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:multiproduct_page.py:41 Selecting shop: Zara
INFO     pages.base_page:multiproduct_page.py:52 Shop 'Zara' selected
INFO     pages.base_page:multiproduct_page.py:61 Clicking Add Products link
```

<details>
<summary>Full Traceback</summary>

```python
[gw2] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/multiproduct/test_multiproduct_functional.py:294: in test_create_multi_product_minimal
    multi_page.click_add_products_link()
pages/multiproduct_page.py:63: in click_add_products_link
    link.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("a[href*='/dashboard/products/add']").first
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:37:07 - pages.base_page - INFO - select_shop_universal:41 - Selecting shop: Zara
2026-02-16 09:37:07 - pages.base_page - INFO - select_shop_universal:52 - Shop 'Zara' selected
2026-02-16 09:37:07 - pages.base_page - INFO - click_add_products_link:61 - Clicking Add Products link
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:multiproduct_page.py:41 Selecting shop: Zara
INFO     pages.base_page:multiproduct_page.py:52 Shop 'Zara' selected
INFO     pages.base_page:multiproduct_page.py:61 Clicking Add Products link
```
</details>

---

## Order Detail (3 failures)

### BUG-F032: test_product_columns_exist

- **ID:** BUG-F032
- **Test:** `TestOrderDetailProducts.test_product_columns_exist`
- **File:** `tests/order_detail/test_order_detail_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Order Detail

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
4. Click on first order

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert has_price, f"BUG: Колонка Price не найдена. Заголовки: {header_texts}"
E   AssertionError: BUG: Колонка Price не найдена. Заголовки: ['', 'narx', 'miqdor', "jami (so'm)"]
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw4] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/order_detail/test_order_detail_functional.py:54: in test_product_columns_exist
    assert has_price, f"BUG: Колонка Price не найдена. Заголовки: {header_texts}"
E   AssertionError: BUG: Колонка Price не найдена. Заголовки: ['', 'narx', 'miqdor', "jami (so'm)"]
E   assert False
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:46 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:42:46 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:42:46 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:42:46 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:42:46 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:42:48 - pages.base_page - INFO - navigate_to_order_detail:141 - Navigating to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:42:48 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:42:48 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:42:49 - pages.base_page - INFO - navigate_to_order_detail:145 - Navigated to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
INFO     pages.base_page:order_detail_page.py:141 Navigating to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:order_detail_page.py:145 Navigated to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
```
</details>

---

### BUG-F033: test_print_button_clickable

- **ID:** BUG-F033
- **Test:** `TestOrderDetailActions.test_print_button_clickable`
- **File:** `tests/order_detail/test_order_detail_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Order Detail

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
4. Click on first order
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert order_detail_page.print_button.is_visible(timeout=3000), \
E   AssertionError: BUG: Кнопка печати не видна
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw4] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/order_detail/test_order_detail_functional.py:70: in test_print_button_clickable
    assert order_detail_page.print_button.is_visible(timeout=3000), \
E   AssertionError: BUG: Кнопка печати не видна
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3'> selector="button:has-text('P
E    +      where <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3'> selector="button:has-text('Print'), but
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:50 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:42:50 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:42:50 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:42:50 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:42:50 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:42:51 - pages.base_page - INFO - navigate_to_order_detail:141 - Navigating to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:42:52 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:42:52 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:42:53 - pages.base_page - INFO - navigate_to_order_detail:145 - Navigated to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
INFO     pages.base_page:order_detail_page.py:141 Navigating to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:order_detail_page.py:145 Navigated to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
```
</details>

---

### BUG-F034: test_print_button_visible

- **ID:** BUG-F034
- **Test:** `TestOrderDetailUI.test_print_button_visible`
- **File:** `tests/order_detail/test_order_detail_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Order Detail

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
4. Click on first order
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert order_detail_page.print_button.is_visible(timeout=5000), \
E   AssertionError: BUG: Кнопка печати не видна
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw4] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/order_detail/test_order_detail_ui.py:51: in test_print_button_visible
    assert order_detail_page.print_button.is_visible(timeout=5000), \
E   AssertionError: BUG: Кнопка печати не видна
E   assert False
E    +  where False = is_visible(timeout=5000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3'> selector="button:has-text('P
E    +      where <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3'> selector="button:has-text('Print'), but
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:46 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:43:46 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:43:46 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:43:46 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:43:46 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:43:47 - pages.base_page - INFO - navigate_to_order_detail:141 - Navigating to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:43:47 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:43:47 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
2026-02-16 09:43:48 - pages.base_page - INFO - navigate_to_order_detail:145 - Navigated to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
INFO     pages.base_page:order_detail_page.py:141 Navigating to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders/24b52350-645e-4daf-83a8-19f16ef853c3
INFO     pages.base_page:order_detail_page.py:145 Navigated to order detail: 24b52350-645e-4daf-83a8-19f16ef853c3
```
</details>

---

## Orders (26 failures)

### BUG-F035: test_negative_page_param

- **ID:** BUG-F035
- **Test:** `TestOrdersURLManipulation.test_negative_page_param`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:82: in test_negative_page_param
    url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['negative_page']}"
E   KeyError: 'url_manipulation'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:43 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:31:43 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F036: test_huge_page_param

- **ID:** BUG-F036
- **Test:** `TestOrdersURLManipulation.test_huge_page_param`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:92: in test_huge_page_param
    url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['huge_page']}"
E   KeyError: 'url_manipulation'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:43 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:31:43 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F037: test_string_page_params

- **ID:** BUG-F037
- **Test:** `TestOrdersURLManipulation.test_string_page_params`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:102: in test_string_page_params
    url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['string_params']}"
E   KeyError: 'url_manipulation'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:43 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:31:43 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F038: test_xss_in_url_param

- **ID:** BUG-F038
- **Test:** `TestOrdersURLManipulation.test_xss_in_url_param`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:111: in test_xss_in_url_param
    url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['xss_in_url']}"
E   KeyError: 'url_manipulation'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:43 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:31:43 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F039: test_sql_in_url_param

- **ID:** BUG-F039
- **Test:** `TestOrdersURLManipulation.test_sql_in_url_param`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Medium
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:121: in test_sql_in_url_param
    url = f"https://staging-seller.greatmall.uz/dashboard/orders-management/orders{test_data['url_manipulation']['sql_in_url']}"
E   KeyError: 'url_manipulation'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:43 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:31:43 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F040: test_search_xss_script_tag

- **ID:** BUG-F040
- **Test:** `TestOrdersSearchSecurity.test_search_xss_script_tag`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:71: in test_search_xss_script_tag
    xss = test_data["invalid_search"]["xss_payload"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:42 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:42 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:42 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:42 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:42 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:43 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:43 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F041: test_search_xss_event_handler

- **ID:** BUG-F041
- **Test:** `TestOrdersSearchSecurity.test_search_xss_event_handler`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:79: in test_search_xss_event_handler
    xss = test_data["invalid_search"]["xss_event"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:43 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:43 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:44 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:44 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:44 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:45 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:45 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F042: test_search_sql_injection

- **ID:** BUG-F042
- **Test:** `TestOrdersSearchSecurity.test_search_sql_injection`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:87: in test_search_sql_injection
    sql = test_data["invalid_search"]["sql_injection"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:45 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:45 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:45 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:45 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:45 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:46 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:46 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F043: test_search_null_bytes

- **ID:** BUG-F043
- **Test:** `TestOrdersSearchSecurity.test_search_null_bytes`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:94: in test_search_null_bytes
    null_input = test_data["invalid_search"]["null_bytes"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:46 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:46 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:46 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:46 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:46 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:47 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:47 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F044: test_search_command_injection

- **ID:** BUG-F044
- **Test:** `TestOrdersSearchSecurity.test_search_command_injection`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:101: in test_search_command_injection
    cmd = test_data["invalid_search"]["command_injection"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:47 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:47 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:47 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:47 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:47 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:49 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:49 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F045: test_search_very_long_input

- **ID:** BUG-F045
- **Test:** `TestOrdersSearchSecurity.test_search_very_long_input`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:108: in test_search_very_long_input
    long_str = test_data["invalid_search"]["very_long"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:49 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:49 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:49 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:49 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:49 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:50 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:50 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F046: test_search_only_spaces

- **ID:** BUG-F046
- **Test:** `TestOrdersSearchWhitespace.test_search_only_spaces`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:123: in test_search_only_spaces
    orders_page.search_order(test_data["whitespace_inputs"]["only_spaces"])
E   KeyError: 'whitespace_inputs'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:50 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:50 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:50 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:50 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:50 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:51 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:51 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F047: test_search_with_tabs

- **ID:** BUG-F047
- **Test:** `TestOrdersSearchWhitespace.test_search_with_tabs`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:129: in test_search_with_tabs
    orders_page.search_order(test_data["whitespace_inputs"]["tabs"])
E   KeyError: 'whitespace_inputs'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:51 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:51 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:52 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:52 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:52 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:53 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:53 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F048: test_search_leading_trailing_spaces

- **ID:** BUG-F048
- **Test:** `TestOrdersSearchWhitespace.test_search_leading_trailing_spaces`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:135: in test_search_leading_trailing_spaces
    orders_page.search_order(test_data["whitespace_inputs"]["leading_trailing"])
E   KeyError: 'whitespace_inputs'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:53 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:53 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:53 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:53 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:53 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:54 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:54 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F049: test_search_multiple_spaces

- **ID:** BUG-F049
- **Test:** `TestOrdersSearchWhitespace.test_search_multiple_spaces`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:141: in test_search_multiple_spaces
    orders_page.search_order(test_data["whitespace_inputs"]["multiple_spaces"])
E   KeyError: 'whitespace_inputs'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:54 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:54 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:54 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:54 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:54 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:55 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:55 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F050: test_date_from_accepts_input

- **ID:** BUG-F050
- **Test:** `TestOrdersDateFilter.test_date_from_accepts_input`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:155: in test_date_from_accepts_input
    date = test_data["date_filter"]["valid_from"]
E   KeyError: 'date_filter'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:55 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:55 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:56 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:56 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:56 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:57 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:57 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F051: test_html_injection_search

- **ID:** BUG-F051
- **Test:** `TestOrdersAdvancedSecurity.test_html_injection_search`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:257: in test_html_injection_search
    html = test_data["invalid_search"]["html_tags"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:57 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:57 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:57 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:57 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:57 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:58 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:31:58 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F052: test_date_to_accepts_input

- **ID:** BUG-F052
- **Test:** `TestOrdersDateFilter.test_date_to_accepts_input`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:162: in test_date_to_accepts_input
    date = test_data["date_filter"]["valid_to"]
E   KeyError: 'date_filter'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:57 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:57 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:57 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:57 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:57 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:31:58 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:31:58 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F053: test_ldap_injection_search

- **ID:** BUG-F053
- **Test:** `TestOrdersAdvancedSecurity.test_ldap_injection_search`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:265: in test_ldap_injection_search
    ldap = test_data["invalid_search"]["ldap_injection"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:58 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:58 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:58 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:58 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:58 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:00 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:32:00 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F054: test_date_range_filter

- **ID:** BUG-F054
- **Test:** `TestOrdersDateFilter.test_date_range_filter`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:170: in test_date_range_filter
    test_data["date_filter"]["valid_from"],
E   KeyError: 'date_filter'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:58 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:31:58 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:58 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:31:59 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:31:59 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:00 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:32:00 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F055: test_path_traversal_search

- **ID:** BUG-F055
- **Test:** `TestOrdersAdvancedSecurity.test_path_traversal_search`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:272: in test_path_traversal_search
    path = test_data["invalid_search"]["path_traversal"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:00 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:32:00 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:00 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:00 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:00 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:01 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:32:01 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F056: test_invalid_date_format

- **ID:** BUG-F056
- **Test:** `TestOrdersDateFilter.test_invalid_date_format`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Fill form with valid data and submit

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:178: in test_invalid_date_format
    orders_page.set_date_from(test_data["date_filter"]["invalid_date"])
E   KeyError: 'date_filter'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:00 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:32:00 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:00 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:00 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:00 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:01 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:32:01 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F057: test_unicode_emoji_search

- **ID:** BUG-F057
- **Test:** `TestOrdersAdvancedSecurity.test_unicode_emoji_search`
- **File:** `tests/orders/test_orders_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_functional.py:279: in test_unicode_emoji_search
    emoji = test_data["invalid_search"]["unicode_emoji"]
E   KeyError: 'invalid_search'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:01 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:32:01 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:01 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:01 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:01 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:02 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.js
2026-02-16 09:32:02 - conftest - WARNING - test_data:498 - No test data found for module: orders_functional
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_functional
```
</details>

---

### BUG-F058: test_future_date

- **ID:** BUG-F058
- **Test:** `TestOrdersDateFilter.test_future_date`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:184: in test_future_date
    orders_page.set_date_from(test_data["date_filter"]["future_date"])
E   KeyError: 'date_filter'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:01 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:32:01 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:01 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:01 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:01 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:02 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:32:02 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F059: test_reversed_date_range

- **ID:** BUG-F059
- **Test:** `TestOrdersDateFilter.test_reversed_date_range`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:190: in test_reversed_date_range
    reversed_range = test_data["date_filter"]["reversed_range"]
E   KeyError: 'date_filter'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:02 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:32:02 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:02 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:03 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:03 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:04 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:32:04 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

### BUG-F060: test_search_invalid_order_id

- **ID:** BUG-F060
- **Test:** `TestOrdersSearch.test_search_invalid_order_id`
- **File:** `tests/orders/test_orders_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Orders

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/orders-management/orders
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/orders/test_orders_search.py:26: in test_search_invalid_order_id
    invalid_id = test_data["search_scenarios"]["invalid_order_id"]
E   KeyError: 'search_scenarios'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:07 - pages.base_page - INFO - navigate:186 - Navigating to orders page...
2026-02-16 09:32:07 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:07 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
2026-02-16 09:32:07 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:32:07 - pages.base_page - INFO - navigate:189 - Orders page loaded
2026-02-16 09:32:08 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
2026-02-16 09:32:08 - conftest - WARNING - test_data:498 - No test data found for module: orders_search
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:orders_page.py:186 Navigating to orders page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:orders_page.py:189 Orders page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/orders_search_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: orders_search
```
</details>

---

## Product Create (30 failures)

### BUG-F061: test_command_injection

- **ID:** BUG-F061
- **Test:** `TestProductCreateAdvancedSecurity.test_command_injection`
- **File:** `tests/product_create/test_product_create_security.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_security.py:160: in test_command_injection
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:19 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_d
2026-02-16 09:32:19 - conftest - WARNING - test_data:498 - No test data found for module: product_create_security
2026-02-16 09:32:19 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:19 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:19 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:19 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:32:20 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:32:21 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:32:21 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:32:21 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:32:21 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:21 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:21 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:21 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:32:21 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:32:21 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
... (2 more lines)
```
</details>

---

### BUG-F062: test_path_traversal

- **ID:** BUG-F062
- **Test:** `TestProductCreateAdvancedSecurity.test_path_traversal`
- **File:** `tests/product_create/test_product_create_security.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_security.py:172: in test_path_traversal
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:21 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_d
2026-02-16 09:32:21 - conftest - WARNING - test_data:498 - No test data found for module: product_create_security
2026-02-16 09:32:21 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:21 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:21 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:22 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:32:23 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:32:23 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:32:23 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:32:23 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:32:23 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:24 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:32:24 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:32:24 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:32:24 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F063: test_xss_uz_description

- **ID:** BUG-F063
- **Test:** `TestProductCreateDescriptionInjection.test_xss_uz_description`
- **File:** `tests/product_create/test_product_create_security.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_security.py:208: in test_xss_uz_description
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:27 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_d
2026-02-16 09:32:27 - conftest - WARNING - test_data:498 - No test data found for module: product_create_security
2026-02-16 09:32:27 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:28 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:28 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:28 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:32:29 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:32:30 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:32:30 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:32:30 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:32:30 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:30 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:30 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:30 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:32:30 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:32:30 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
... (2 more lines)
```
</details>

---

### BUG-F064: test_xss_ru_description

- **ID:** BUG-F064
- **Test:** `TestProductCreateDescriptionInjection.test_xss_ru_description`
- **File:** `tests/product_create/test_product_create_security.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_security.py:223: in test_xss_ru_description
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:30 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_d
2026-02-16 09:32:30 - conftest - WARNING - test_data:498 - No test data found for module: product_create_security
2026-02-16 09:32:30 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:30 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:30 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:30 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:32:31 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:32:32 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:32:32 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:32:32 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:32:32 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:32 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:32:32 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:32:32 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:32:32 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F065: test_sql_injection_description

- **ID:** BUG-F065
- **Test:** `TestProductCreateDescriptionInjection.test_sql_injection_description`
- **File:** `tests/product_create/test_product_create_security.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_security.py:238: in test_sql_injection_description
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:32 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_d
2026-02-16 09:32:32 - conftest - WARNING - test_data:498 - No test data found for module: product_create_security
2026-02-16 09:32:32 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:33 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:33 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:33 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:32:34 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:32:34 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:32:34 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:32:35 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:32:35 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:35 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:35 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:32:35 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:32:35 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```
</details>

---

### BUG-F066: test_html_injection_description

- **ID:** BUG-F066
- **Test:** `TestProductCreateDescriptionInjection.test_html_injection_description`
- **File:** `tests/product_create/test_product_create_security.py`
- **Severity:** Critical
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_security.py:253: in test_html_injection_description
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:35 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_d
2026-02-16 09:32:35 - conftest - WARNING - test_data:498 - No test data found for module: product_create_security
2026-02-16 09:32:35 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:35 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:35 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:36 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:32:37 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:32:37 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:32:37 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:32:37 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:32:37 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:38 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:32:38 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:32:38 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:32:38 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F067: test_emoji_in_name

- **ID:** BUG-F067
- **Test:** `TestProductCreateInvalidFormat.test_emoji_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:311: in test_emoji_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:04 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:04 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:04 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:04 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:04 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:04 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:05 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:06 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:33:07 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:07 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:07 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:07 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:07 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:07 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:07 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```
</details>

---

### BUG-F068: test_html_tags_in_name

- **ID:** BUG-F068
- **Test:** `TestProductCreateInvalidFormat.test_html_tags_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:324: in test_html_tags_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:07 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:07 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:07 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:07 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:07 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:07 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:08 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:09 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:33:09 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:09 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:09 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:09 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:09 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:09 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:33:09 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F069: test_mixed_scripts_in_name

- **ID:** BUG-F069
- **Test:** `TestProductCreateInvalidFormat.test_mixed_scripts_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:339: in test_mixed_scripts_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:09 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:09 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:09 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:09 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:09 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:10 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:10 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:11 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:33:11 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:11 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:11 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:11 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:12 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:12 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:12 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```
</details>

---

### BUG-F070: test_only_digits_in_name

- **ID:** BUG-F070
- **Test:** `TestProductCreateInvalidFormat.test_only_digits_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:353: in test_only_digits_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:12 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:12 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:12 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:12 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:12 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:12 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:13 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:15 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:33:15 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:15 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:15 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:15 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:15 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:15 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:33:15 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F071: test_special_chars_in_name

- **ID:** BUG-F071
- **Test:** `TestProductCreateInvalidFormat.test_special_chars_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:366: in test_special_chars_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:15 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:15 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:15 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:15 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:15 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:15 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:16 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:17 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:33:17 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:17 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:17 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:17 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:17 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:17 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:17 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```
</details>

---

### BUG-F072: test_decimal_price

- **ID:** BUG-F072
- **Test:** `TestProductCreateInvalidFormat.test_decimal_price`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:314 Clicking 'Next' button
WARNING  pages.base_page:productcreate_page.py:330 URL unchanged - checking for validation errors
INFO     pages.base_page:productcreate_page.py:335 ✓ Clicked 'Next' button
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:386: in test_decimal_price
    product_on_step2.fill_single_field("Regular price (UZS)", "1000.50")
pages/productcreate_page.py:662: in fill_single_field
    field.first.wait_for(state="visible", timeout=5000)
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:18074: in wait_for
    self._sync(self._impl_obj.wait_for(timeout=timeout, state=state))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:710: in wait_for
    await self._frame.wait_for_selector(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:369: in wait_for_selector
    await self._channel.send(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 5000ms exceeded.
E   Call log:
E     - waiting for locator("input[name='price'], textarea[name='price']").or_(get_by_role("textbox", name="Regular price (UZS)")).or_(get_by_role("textbox", name="Oddiy narx (UZS)")).first to be visi
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:19 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:19 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:19 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:20 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:20 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:20 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:21 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:22 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:33:22 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:22 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:22 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:22 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:23 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:23 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:23 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:33:23 - pages.base_page - INFO - select_category_from_combobox:164 - ✓ Selected 'Ustki kiyim'
2026-02-16 09:33:23 - pages.base_page - INFO - select_category_from_combobox:176 - ✓ Category selection complete
2026-02-16 09:33:23 - pages.base_page - INFO - select_ikpu_from_combobox:189 - Selecting IKPU: kurtkalar
2026-02-16 09:33:23 - pages.base_page - INFO - select_ikpu_from_combobox:199 - ✓ IKPU selected: kurtkalar
2026-02-16 09:33:23 - pages.base_page - INFO - select_country_from_combobox:212 - Selecting country: Turkiya
2026-02-16 09:33:23 - pages.base_page - INFO - select_country_from_combobox:221 - ✓ Country selected: Turkiya
... (44 more lines)
```
</details>

---

### BUG-F073: test_discount_greater_than_price

- **ID:** BUG-F073
- **Test:** `TestProductCreatePriceDiscount.test_discount_greater_than_price`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:314 Clicking 'Next' button
WARNING  pages.base_page:productcreate_page.py:330 URL unchanged - checking for validation errors
INFO     pages.base_page:productcreate_page.py:335 ✓ Clicked 'Next' button
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:419: in test_discount_greater_than_price
    self._get_price_field(product_on_step2).fill("1000000")
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15983: in fill
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:215: in fill
    return await self._frame.fill(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:607: in fill
    await self._fill(**locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:619: in _fill
    await self._channel.send("fill", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.fill: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("input[name='price']").or_(get_by_role("textbox", name="Regular price (UZS)")).or_(get_by_role("textbox", name="Oddiy narx (UZS)")).first
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:29 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:29 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:29 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:29 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:29 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:30 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:30 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:31 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:33:31 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:31 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:31 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:31 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:31 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:32 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:32 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:32 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:33:32 - pages.base_page - INFO - select_category_from_combobox:164 - ✓ Selected 'Ustki kiyim'
2026-02-16 09:33:32 - pages.base_page - INFO - select_category_from_combobox:176 - ✓ Category selection complete
2026-02-16 09:33:32 - pages.base_page - INFO - select_ikpu_from_combobox:189 - Selecting IKPU: kurtkalar
2026-02-16 09:33:32 - pages.base_page - INFO - select_ikpu_from_combobox:199 - ✓ IKPU selected: kurtkalar
2026-02-16 09:33:32 - pages.base_page - INFO - select_country_from_combobox:212 - Selecting country: Turkiya
... (46 more lines)
```
</details>

---

### BUG-F074: test_empty_product_names_error

- **ID:** BUG-F074
- **Test:** `TestProductCreateEmptyFields.test_empty_product_names_error`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page
3. Submit form with empty fields

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:45: in test_empty_product_names_error
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:03 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:03 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:03 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:03 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:03 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:03 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:04 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:05 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:05 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:05 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:05 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:05 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:05 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:05 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:05 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F075: test_description_49_chars

- **ID:** BUG-F075
- **Test:** `TestProductCreateBoundary.test_description_49_chars`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:102: in test_description_49_chars
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:11 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:11 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:11 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:11 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:11 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:11 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:12 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:13 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:13 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:13 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:13 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:13 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:13 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:13 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:13 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```
</details>

---

### BUG-F076: test_complete_product_creation

- **ID:** BUG-F076
- **Test:** `TestProductCreateE2E.test_complete_product_creation`
- **File:** `tests/product_create/test_product_create_functional.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
- waiting for get_by_role("menuitem", name="Zara")
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_functional.py:287: in test_complete_product_creation
    product_page.select_shop(data["shop_name"])
pages/productcreate_page.py:52: in select_shop
    shop_item.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("menuitem", name="Zara")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:44 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test
2026-02-16 09:33:44 - conftest - WARNING - test_data:498 - No test data found for module: product_create_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:33:44 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:44 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:44 - pages.base_page - INFO - select_shop:41 - Selecting shop: Zara
2026-02-16 09:34:14 - pages.base_page - ERROR - select_shop:57 - Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")

------------------------------ Captured log call -------------------------------
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:41 Selecting shop: Zara
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")
```
</details>

---

### BUG-F077: test_description_50_chars

- **ID:** BUG-F077
- **Test:** `TestProductCreateBoundary.test_description_50_chars`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:125: in test_description_50_chars
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:14 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:14 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:14 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:14 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:14 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:14 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:15 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:16 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:16 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F078: test_description_exact_min_length

- **ID:** BUG-F078
- **Test:** `TestProductCreateDescriptionLength.test_description_exact_min_length`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:480: in test_description_exact_min_length
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:13 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:13 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:13 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:13 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:13 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:13 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:14 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:16 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:16 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:16 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
... (4 more lines)
```
</details>

---

### BUG-F079: test_product_name_500_chars

- **ID:** BUG-F079
- **Test:** `TestProductCreateBoundary.test_product_name_500_chars`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:160: in test_product_name_500_chars
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:20 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:20 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:20 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:20 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:20 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:20 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:21 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:23 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:23 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:23 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:23 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:23 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:23 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:23 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:23 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:23 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
... (2 more lines)
```
</details>

---

### BUG-F080: test_price_zero

- **ID:** BUG-F080
- **Test:** `TestProductCreateBoundary.test_price_zero`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:314 Clicking 'Next' button
WARNING  pages.base_page:productcreate_page.py:330 URL unchanged - checking for validation errors
INFO     pages.base_page:productcreate_page.py:335 ✓ Clicked 'Next' button
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:185: in test_price_zero
    product_on_step2.fill_single_field("SKU", data["sku"])
pages/productcreate_page.py:662: in fill_single_field
    field.first.wait_for(state="visible", timeout=5000)
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:18074: in wait_for
    self._sync(self._impl_obj.wait_for(timeout=timeout, state=state))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:710: in wait_for
    await self._frame.wait_for_selector(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:369: in wait_for_selector
    await self._channel.send(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 5000ms exceeded.
E   Call log:
E     - waiting for locator("input[name='sku'], textarea[name='sku']").or_(get_by_role("textbox", name="SKU")).or_(get_by_role("textbox", name="SKU")).first to be visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:25 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:25 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:25 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:25 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:25 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:26 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:26 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:27 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:34:27 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:27 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:27 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:27 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:27 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:27 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:164 - ✓ Selected 'Ustki kiyim'
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:176 - ✓ Category selection complete
2026-02-16 09:34:28 - pages.base_page - INFO - select_ikpu_from_combobox:189 - Selecting IKPU: kurtkalar
2026-02-16 09:34:28 - pages.base_page - INFO - select_ikpu_from_combobox:199 - ✓ IKPU selected: kurtkalar
2026-02-16 09:34:28 - pages.base_page - INFO - select_country_from_combobox:212 - Selecting country: Turkiya
2026-02-16 09:34:28 - pages.base_page - INFO - select_country_from_combobox:221 - ✓ Country selected: Turkiya
... (44 more lines)
```
</details>

---

### BUG-F081: test_only_spaces_in_name

- **ID:** BUG-F081
- **Test:** `TestProductCreateWhitespace.test_only_spaces_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:224: in test_only_spaces_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:37 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:37 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:37 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:37 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:37 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:38 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:38 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:39 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:39 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:39 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:39 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:39 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:39 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:39 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:40 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F082: test_leading_trailing_spaces

- **ID:** BUG-F082
- **Test:** `TestProductCreateWhitespace.test_leading_trailing_spaces`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:246: in test_leading_trailing_spaces
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:40 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:40 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:40 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:40 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:40 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:40 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:41 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:42 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:42 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:42 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:42 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:42 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:42 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:42 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:42 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```
</details>

---

### BUG-F083: test_tabs_in_name

- **ID:** BUG-F083
- **Test:** `TestProductCreateWhitespace.test_tabs_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:261: in test_tabs_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:42 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:42 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:42 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:42 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:42 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:42 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:43 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:44 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:44 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:44 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:44 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:44 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:44 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:44 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:44 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F084: test_create_with_minimum_data

- **ID:** BUG-F084
- **Test:** `TestProductCreateE2E.test_create_with_minimum_data`
- **File:** `tests/product_create/test_product_create_functional.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
- waiting for get_by_role("menuitem", name="Zara")
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_functional.py:348: in test_create_with_minimum_data
    product_page.select_shop(data["shop_name"])
pages/productcreate_page.py:52: in select_shop
    shop_item.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("menuitem", name="Zara")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:14 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test
2026-02-16 09:34:14 - conftest - WARNING - test_data:498 - No test data found for module: product_create_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:14 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:15 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:15 - pages.base_page - INFO - select_shop:41 - Selecting shop: Zara
2026-02-16 09:34:45 - pages.base_page - ERROR - select_shop:57 - Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")

------------------------------ Captured log call -------------------------------
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:41 Selecting shop: Zara
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")
```
</details>

---

### BUG-F085: test_nbsp_in_name

- **ID:** BUG-F085
- **Test:** `TestProductCreateWhitespace.test_nbsp_in_name`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:274: in test_nbsp_in_name
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:44 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:44 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:44 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:44 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:44 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:45 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:45 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:46 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:46 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:46 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:46 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:46 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:47 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:47 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:47 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```
</details>

---

### BUG-F086: test_multiple_spaces

- **ID:** BUG-F086
- **Test:** `TestProductCreateWhitespace.test_multiple_spaces`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:287: in test_multiple_spaces
    product_create_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:47 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:47 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:47 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:47 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:47 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:47 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:48 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:49 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:49 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:49 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:49 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:49 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:49 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:49 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:49 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```
</details>

---

### BUG-F087: test_zero_width

- **ID:** BUG-F087
- **Test:** `TestProductCreateDimensions.test_zero_width`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:515 Scrolling page by 300px
INFO     pages.base_page:productcreate_page.py:518 ✓ Page scrolled by 300px
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:600: in test_zero_width
    width_field.fill("0")
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15983: in fill
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:215: in fill
    return await self._frame.fill(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:607: in fill
    await self._fill(**locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:619: in _fill
    await self._channel.send("fill", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.fill: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("textbox", name="Eni")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:26 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:34:26 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:34:26 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:26 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:26 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:34:26 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:34:27 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:34:28 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:164 - ✓ Selected 'Ustki kiyim'
2026-02-16 09:34:28 - pages.base_page - INFO - select_category_from_combobox:176 - ✓ Category selection complete
2026-02-16 09:34:28 - pages.base_page - INFO - select_ikpu_from_combobox:189 - Selecting IKPU: kurtkalar
2026-02-16 09:34:28 - pages.base_page - INFO - select_ikpu_from_combobox:199 - ✓ IKPU selected: kurtkalar
2026-02-16 09:34:28 - pages.base_page - INFO - select_country_from_combobox:212 - Selecting country: Turkiya
2026-02-16 09:34:28 - pages.base_page - INFO - select_country_from_combobox:221 - ✓ Country selected: Turkiya
... (50 more lines)
```
</details>

---

### BUG-F088: test_abort_creation_midway

- **ID:** BUG-F088
- **Test:** `TestProductCreateE2E.test_abort_creation_midway`
- **File:** `tests/product_create/test_product_create_functional.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
- waiting for get_by_role("menuitem", name="Zara")
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_functional.py:410: in test_abort_creation_midway
    product_page.select_shop(data["shop_name"])
pages/productcreate_page.py:52: in select_shop
    shop_item.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("menuitem", name="Zara")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:46 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test
2026-02-16 09:34:46 - conftest - WARNING - test_data:498 - No test data found for module: product_create_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:34:46 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:46 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:34:46 - pages.base_page - INFO - select_shop:41 - Selecting shop: Zara
2026-02-16 09:35:17 - pages.base_page - ERROR - select_shop:57 - Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")

------------------------------ Captured log call -------------------------------
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:41 Selecting shop: Zara
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")
```
</details>

---

### BUG-F089: test_negative_weight

- **ID:** BUG-F089
- **Test:** `TestProductCreateDimensions.test_negative_weight`
- **File:** `tests/product_create/test_product_create_validation.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:productcreate_page.py:515 Scrolling page by 300px
INFO     pages.base_page:productcreate_page.py:518 ✓ Page scrolled by 300px
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_validation.py:654: in test_negative_weight
    weight_field.fill("-5")
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15983: in fill
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:215: in fill
    return await self._frame.fill(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:607: in fill
    await self._fill(**locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:619: in _fill
    await self._channel.send("fill", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.fill: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("textbox", name="Og'irligi")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:35:10 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:35:10 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:35:10 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:35:10 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:35:10 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:35:10 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:35:11 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:35:12 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:164 - ✓ Selected 'Ustki kiyim'
2026-02-16 09:35:12 - pages.base_page - INFO - select_category_from_combobox:176 - ✓ Category selection complete
2026-02-16 09:35:12 - pages.base_page - INFO - select_ikpu_from_combobox:189 - Selecting IKPU: kurtkalar
2026-02-16 09:35:12 - pages.base_page - INFO - select_ikpu_from_combobox:199 - ✓ IKPU selected: kurtkalar
2026-02-16 09:35:12 - pages.base_page - INFO - select_country_from_combobox:212 - Selecting country: Turkiya
2026-02-16 09:35:12 - pages.base_page - INFO - select_country_from_combobox:221 - ✓ Country selected: Turkiya
... (50 more lines)
```
</details>

---

### BUG-F090: test_multi_tab_independence

- **ID:** BUG-F090
- **Test:** `TestProductCreateConcurrent.test_multi_tab_independence`
- **File:** `tests/product_create/test_product_create_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Product Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to product create page

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
- waiting for get_by_role("menuitem", name="Zara")
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/test_product_create_functional.py:619: in test_multi_tab_independence
    product_page.select_shop(staging_data.get("shop_name", "Zara"))
pages/productcreate_page.py:52: in select_shop
    shop_item.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("menuitem", name="Zara")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:36:34 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test
2026-02-16 09:36:34 - conftest - WARNING - test_data:498 - No test data found for module: product_create_functional
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_functional
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:36:34 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:36:34 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:36:34 - pages.base_page - INFO - select_shop:41 - Selecting shop: Zara
2026-02-16 09:37:05 - pages.base_page - ERROR - select_shop:57 - Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")

------------------------------ Captured log call -------------------------------
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:41 Selecting shop: Zara
ERROR    pages.base_page:productcreate_page.py:57 Failed to select shop: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for get_by_role("menuitem", name="Zara")
```
</details>

---

## Products List (27 failures)

### BUG-F091: test_sidebar_navigation_workflow

- **ID:** BUG-F091
- **Test:** `TestProductsListE2E.test_sidebar_navigation_workflow`
- **File:** `tests/products_list/test_products_list_e2e.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:555 Clicking products navigation link...
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_e2e.py:147: in test_sidebar_navigation_workflow
    products_page.click_products_nav_link()
pages/products_list_page.py:556: in click_products_nav_link
    self.products_nav_link.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.Error: Locator.click: Error: strict mode violation: get_by_role("link", name="Products").or_(get_by_role("link", name="Mahsulotlar")) resolved to 2 elements:
E       1) <a tabindex="0" href="/dashboard" aria-current="page" data-status="active" aria-label="items.products" class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineHover Mu
E       2) <a tabindex="0" href="/dashboard/products/add" class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineHover MuiButtonBase-root MuiButton-root MuiButton-contained MuiB
E
E   Call log:
E     - waiting for get_by_role("link", name="Products").or_(get_by_role("link", name="Mahsulotlar"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:36:05 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:36:05 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:05 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:05 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:36:05 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:36:05 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:36:05 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:36:05 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:36:05 - pages.base_page - INFO - click_products_nav_link:555 - Clicking products navigation link...
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
... (3 more lines)
```
</details>

---

### BUG-F092: test_rows_per_page_10

- **ID:** BUG-F092
- **Test:** `TestProductsListPagination.test_rows_per_page_10`
- **File:** `tests/products_list/test_products_list_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:36:28 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 10
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 10
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_functional.py:80: in test_rows_per_page_10
    products_page.set_rows_per_page(10)
pages/products_list_page.py:857: in set_rows_per_page
    self.rows_per_page_select.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator(".MuiTablePagination-select").or_(get_by_label("Rows per page"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:36:28 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:36:28 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:28 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:28 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:36:28 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:36:28 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 10
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 10
```
</details>

---

### BUG-F093: test_double_click_navigation

- **ID:** BUG-F093
- **Test:** `TestProductsListRobustness.test_double_click_navigation`
- **File:** `tests/products_list/test_products_list_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_functional.py:392: in test_double_click_navigation
    products_page.products_nav_link.dblclick()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15712: in dblclick
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:177: in dblclick
    return await self._frame.dblclick(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:581: in dblclick
    await self._channel.send(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.dblclick: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("link", name="Products").or_(get_by_role("link", name="Mahsulotlar"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:36:43 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:36:43 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:44 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:44 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:36:44 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F094: test_rows_per_page_25

- **ID:** BUG-F094
- **Test:** `TestProductsListPagination.test_rows_per_page_25`
- **File:** `tests/products_list/test_products_list_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:36:58 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 25
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 25
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_functional.py:87: in test_rows_per_page_25
    products_page.set_rows_per_page(25)
pages/products_list_page.py:857: in set_rows_per_page
    self.rows_per_page_select.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator(".MuiTablePagination-select").or_(get_by_label("Rows per page"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:36:58 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:36:58 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:58 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:36:58 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:36:58 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:36:58 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 25
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 25
```
</details>

---

### BUG-F095: test_rows_per_page_50

- **ID:** BUG-F095
- **Test:** `TestProductsListPagination.test_rows_per_page_50`
- **File:** `tests/products_list/test_products_list_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:37:29 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 50
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 50
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_functional.py:94: in test_rows_per_page_50
    products_page.set_rows_per_page(50)
pages/products_list_page.py:857: in set_rows_per_page
    self.rows_per_page_select.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator(".MuiTablePagination-select").or_(get_by_label("Rows per page"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:37:29 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:37:29 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:37:29 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:37:29 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:37:29 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:37:29 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 50
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 50
```
</details>

---

### BUG-F096: test_handles_large_dataset

- **ID:** BUG-F096
- **Test:** `TestProductsListPerformance.test_handles_large_dataset`
- **File:** `tests/products_list/test_products_list_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:37:32 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 100
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 100
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_functional.py:505: in test_handles_large_dataset
    products_page.set_rows_per_page(100)
pages/products_list_page.py:857: in set_rows_per_page
    self.rows_per_page_select.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator(".MuiTablePagination-select").or_(get_by_label("Rows per page"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:37:32 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:37:32 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:37:32 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:37:32 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:37:32 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:37:32 - pages.base_page - INFO - set_rows_per_page:856 - Setting rows per page to: 100
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:856 Setting rows per page to: 100
```
</details>

---

### BUG-F097: test_sidebar_navigation

- **ID:** BUG-F097
- **Test:** `TestProductsListNavigation.test_sidebar_navigation`
- **File:** `tests/products_list/test_products_list_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:38:17 - pages.base_page - INFO - click_products_nav_link:555 - Clicking products navigation link...
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:555 Clicking products navigation link...
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_functional.py:224: in test_sidebar_navigation
    products_page.click_products_nav_link()
pages/products_list_page.py:556: in click_products_nav_link
    self.products_nav_link.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_role("link", name="Products").or_(get_by_role("link", name="Mahsulotlar"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:38:17 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:38:17 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:38:17 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:38:17 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:38:17 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:38:17 - pages.base_page - INFO - click_products_nav_link:555 - Clicking products navigation link...
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:555 Clicking products navigation link...
```
</details>

---

### BUG-F098: test_search_html_injection

- **ID:** BUG-F098
- **Test:** `TestProductsListSearchSecurity.test_search_html_injection`
- **File:** `tests/products_list/test_products_list_search.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert "onerror=alert" not in page_content, \
E   AssertionError: BUG: HTML injection not sanitized - SECURITY VULNERABILITY!
E   assert 'onerror=alert' not in '<!DOCTYPE h...body></html>'
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_search.py:163: in test_search_html_injection
    assert "onerror=alert" not in page_content, \
E   AssertionError: BUG: HTML injection not sanitized - SECURITY VULNERABILITY!
E   assert 'onerror=alert' not in '<!DOCTYPE h...body></html>'
E
E     'onerror=alert' is contained here:
E       img src=x onerror=alert(1)&gt;"><div class="MuiInputAdornment-root MuiInputAdornment-positionEnd MuiInputAdornment-outlined MuiInputAdornment-sizeMedium css-19y70k0"><button class="MuiButtonBa
E
E     ...Full output truncated (5 lines hidden), use '-vv' to show
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:38:51 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:38:51 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:38:51 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:38:51 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:38:51 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:38:51 - pages.base_page - INFO - search:649 - Searching for: <b>bold</b><img src=x onerror=alert(1)>
2026-02-16 09:38:53 - pages.base_page - INFO - search:653 - Search completed for: <b>bold</b><img src=x onerror=alert(1)>
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:649 Searching for: <b>bold</b><img src=x onerror=alert(1)>
INFO     pages.base_page:products_list_page.py:653 Search completed for: <b>bold</b><img src=x onerror=alert(1)>
```
</details>

---

### BUG-F099: test_page_title_visible

- **ID:** BUG-F099
- **Test:** `TestProductsListUI.test_page_title_visible`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert title.is_visible(timeout=3000), \
E   AssertionError: BUG: Page title not visible
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:52: in test_page_title_visible
    assert title.is_visible(timeout=3000), \
E   AssertionError: BUG: Page title not visible
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/products?page=1&size=10'> selector='h6:...ternal:or="h6:has-text(\'Mahsulotlar\')" >> intern
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:39:54 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:39:54 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:39:54 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:39:54 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:39:54 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F100: test_add_product_button_visible

- **ID:** BUG-F100
- **Test:** `TestProductsListUI.test_add_product_button_visible`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert btn.is_visible(timeout=3000), \
E   AssertionError: BUG: Add Products button not visible
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:58: in test_add_product_button_visible
    assert btn.is_visible(timeout=3000), \
E   AssertionError: BUG: Add Products button not visible
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/products?page=1&size=10'> selector='int...f*=\'/products/add\']" >> internal:or="button:has-
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:39:56 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:39:56 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:39:56 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:39:56 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:39:56 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F101: test_status_filter_approved

- **ID:** BUG-F101
- **Test:** `TestProductsListFilters.test_status_filter_approved`
- **File:** `tests/products_list/test_products_list_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:681 Applying status filter: Approved
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_search.py:226: in test_status_filter_approved
    products_page.apply_status_filter("Approved")
pages/products_list_page.py:682: in apply_status_filter
    self.status_filter.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_label("Status").or_(get_by_label("Holat")).or_(locator("[data-testid='status-filter']"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:39:32 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:39:32 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:39:32 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:39:32 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:39:32 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:39:32 - pages.base_page - INFO - open_filters:673 - Opening filters panel...
2026-02-16 09:39:32 - pages.base_page - INFO - open_filters:677 - Filters panel opened
2026-02-16 09:39:32 - pages.base_page - INFO - apply_status_filter:681 - Applying status filter: Approved
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:681 Applying status filter: Approved
```
</details>

---

### BUG-F102: test_search_input_visible

- **ID:** BUG-F102
- **Test:** `TestProductsListUI.test_search_input_visible`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products
3. Perform search action

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert search.is_visible(timeout=3000), \
E   AssertionError: BUG: Search input not visible
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:64: in test_search_input_visible
    assert search.is_visible(timeout=3000), \
E   AssertionError: BUG: Search input not visible
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/products?page=1&size=10'> selector='inp...l:or="internal:role=searchbox" >> internal:or="inp
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:03 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:03 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:03 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:03 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:03 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F103: test_products_visible_or_empty_state

- **ID:** BUG-F103
- **Test:** `TestProductsListUI.test_products_visible_or_empty_state`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products
3. Submit form with empty fields

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert products_count > 0 or empty_visible or table_visible, \
E   AssertionError: BUG: Neither products nor empty state visible
E   assert (0 > 0 or False or False)
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:73: in test_products_visible_or_empty_state
    assert products_count > 0 or empty_visible or table_visible, \
E   AssertionError: BUG: Neither products nor empty state visible
E   assert (0 > 0 or False or False)
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:03 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:03 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:04 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:04 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:04 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:40:04 - pages.base_page - INFO - get_products_count:723 - Products count (table view): 0
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:723 Products count (table view): 0
```
</details>

---

### BUG-F104: test_status_tabs_visible

- **ID:** BUG-F104
- **Test:** `TestProductsListUI.test_status_tabs_visible`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert tabs.first.is_visible(timeout=3000), \
E   AssertionError: BUG: Status tabs not visible
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:87: in test_status_tabs_visible
    assert tabs.first.is_visible(timeout=3000), \
E   AssertionError: BUG: Status tabs not visible
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/auth/login'> selector='[role=\'tab\'] >> internal:or=".MuiTab-root" >> nth=0'>.is_visible
E    +      where <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/auth/login'> selector='[role=\'tab\'] >> internal:or=".MuiTab-root" >> nth=0'> = <Locator frame=<Frame name= url=
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:05 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:05 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:05 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:05 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:05 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F105: test_view_toggle_visible

- **ID:** BUG-F105
- **Test:** `TestProductsListUI.test_view_toggle_visible`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert grid_toggle.is_visible(timeout=2000) or table_toggle.is_visible(timeout=2000), \
E   AssertionError: BUG: View toggle buttons not visible
E   assert (False or False)
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:96: in test_view_toggle_visible
    assert grid_toggle.is_visible(timeout=2000) or table_toggle.is_visible(timeout=2000), \
E   AssertionError: BUG: View toggle buttons not visible
E   assert (False or False)
E    +  where False = is_visible(timeout=2000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/products?page=1&size=10'> selector='button[aria-label=\'grid view\'] >> internal:or=".MuiTog
E    +  and   False = is_visible(timeout=2000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/products?page=1&size=10'> selector='button[aria-label=\'table view\'] >> internal:or=".MuiTo
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:06 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:06 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:06 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:06 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:06 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F106: test_sidebar_products_link_active

- **ID:** BUG-F106
- **Test:** `TestProductsListUI.test_sidebar_products_link_active`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert link.is_visible(timeout=3000), \
E   AssertionError: BUG: Products nav link not visible in sidebar
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:115: in test_sidebar_products_link_active
    assert link.is_visible(timeout=3000), \
E   AssertionError: BUG: Products nav link not visible in sidebar
E   assert False
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/products?page=1&size=10'> selector='internal:role=link[name="Products"i] >> internal:or="int
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:09 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:09 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:09 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:09 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:09 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F107: test_table_empty_state

- **ID:** BUG-F107
- **Test:** `TestProductsListTable.test_table_empty_state`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products
3. Submit form with empty fields

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert products_page.is_page_loaded(), \
E   AssertionError: BUG: Page not handling empty state
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:194: in test_table_empty_state
    assert products_page.is_page_loaded(), \
E   AssertionError: BUG: Page not handling empty state
E   assert False
E    +  where False = is_page_loaded()
E    +    where is_page_loaded = <pages.products_list_page.ProductsListPage object at 0x1080a0490>.is_page_loaded
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:17 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:17 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:17 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:17 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:17 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:40:17 - pages.base_page - INFO - search:649 - Searching for: NONEXISTENT_PRODUCT_XYZ_999
2026-02-16 09:40:18 - pages.base_page - INFO - search:653 - Search completed for: NONEXISTENT_PRODUCT_XYZ_999
2026-02-16 09:40:18 - pages.base_page - INFO - get_products_count:723 - Products count (table view): 0
2026-02-16 09:40:18 - pages.base_page - INFO - is_page_loaded:1018 - Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
2026-02-16 09:40:18 - pages.base_page - WARNING - is_page_loaded:1022 - Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:649 Searching for: NONEXISTENT_PRODUCT_XYZ_999
INFO     pages.base_page:products_list_page.py:653 Search completed for: NONEXISTENT_PRODUCT_XYZ_999
INFO     pages.base_page:products_list_page.py:723 Products count (table view): 0
INFO     pages.base_page:products_list_page.py:1018 Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
WARNING  pages.base_page:products_list_page.py:1022 Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
```
</details>

---

### BUG-F108: test_keyboard_navigation_works

- **ID:** BUG-F108
- **Test:** `TestProductsListAccessibility.test_keyboard_navigation_works`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert products_page.is_page_loaded(), \
E   AssertionError: BUG: Keyboard navigation failed
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:235: in test_keyboard_navigation_works
    assert products_page.is_page_loaded(), \
E   AssertionError: BUG: Keyboard navigation failed
E   assert False
E    +  where False = is_page_loaded()
E    +    where is_page_loaded = <pages.products_list_page.ProductsListPage object at 0x10889f340>.is_page_loaded
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:21 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:21 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:21 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:21 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:21 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:40:21 - pages.base_page - INFO - is_page_loaded:1018 - Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
2026-02-16 09:40:21 - pages.base_page - WARNING - is_page_loaded:1022 - Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:1018 Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
WARNING  pages.base_page:products_list_page.py:1022 Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
```
</details>

---

### BUG-F109: test_enter_activates_focused

- **ID:** BUG-F109
- **Test:** `TestProductsListKeyboardShortcuts.test_enter_activates_focused`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert products_page.is_page_loaded()
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:293: in test_enter_activates_focused
    assert products_page.is_page_loaded()
E   assert False
E    +  where False = is_page_loaded()
E    +    where is_page_loaded = <pages.products_list_page.ProductsListPage object at 0x1080b4880>.is_page_loaded
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:27 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:27 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:27 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:27 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:27 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:40:28 - pages.base_page - INFO - is_page_loaded:1018 - Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
2026-02-16 09:40:28 - pages.base_page - WARNING - is_page_loaded:1022 - Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:1018 Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
WARNING  pages.base_page:products_list_page.py:1022 Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
```
</details>

---

### BUG-F110: test_status_filter_rejected

- **ID:** BUG-F110
- **Test:** `TestProductsListFilters.test_status_filter_rejected`
- **File:** `tests/products_list/test_products_list_search.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:681 Applying status filter: Rejected
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_search.py:234: in test_status_filter_rejected
    products_page.apply_status_filter("Rejected")
pages/products_list_page.py:682: in apply_status_filter
    self.status_filter.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_label("Status").or_(get_by_label("Holat")).or_(locator("[data-testid='status-filter']"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:03 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:03 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:03 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:03 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:03 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:40:03 - pages.base_page - INFO - open_filters:673 - Opening filters panel...
2026-02-16 09:40:03 - pages.base_page - INFO - open_filters:677 - Filters panel opened
2026-02-16 09:40:03 - pages.base_page - INFO - apply_status_filter:681 - Applying status filter: Rejected
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:681 Applying status filter: Rejected
```
</details>

---

### BUG-F111: test_filter_by_status_updates_list

- **ID:** BUG-F111
- **Test:** `TestProductsListStatusIndicators.test_filter_by_status_updates_list`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:681 Applying status filter: Pending
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:356: in test_filter_by_status_updates_list
    products_page.apply_status_filter("Pending")
pages/products_list_page.py:682: in apply_status_filter
    self.status_filter.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_label("Status").or_(get_by_label("Holat")).or_(locator("[data-testid='status-filter']"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:07 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:07 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:07 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:07 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:07 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:40:07 - pages.base_page - INFO - open_filters:673 - Opening filters panel...
2026-02-16 09:40:07 - pages.base_page - INFO - open_filters:677 - Filters panel opened
2026-02-16 09:40:07 - pages.base_page - INFO - apply_status_filter:681 - Applying status filter: Pending
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:681 Applying status filter: Pending
```
</details>

---

### BUG-F112: test_arrow_keys_in_dropdown

- **ID:** BUG-F112
- **Test:** `TestProductsListKeyboardShortcuts.test_arrow_keys_in_dropdown`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:298: in test_arrow_keys_in_dropdown
    products_page.rows_per_page_select.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator(".MuiTablePagination-select").or_(get_by_label("Rows per page"))
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:28 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:28 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:28 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:28 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:28 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F113: test_no_flash_of_content

- **ID:** BUG-F113
- **Test:** `TestProductsListLoading.test_no_flash_of_content`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert products_page.is_page_loaded()
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:513: in test_no_flash_of_content
    assert products_page.is_page_loaded()
E   assert False
E    +  where False = is_page_loaded()
E    +    where is_page_loaded = <pages.products_list_page.ProductsListPage object at 0x1081e9460>.is_page_loaded
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:40:59 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:59 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:59 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:59 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:59 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:40:59 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:40:59 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:59 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:40:59 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:40:59 - pages.base_page - INFO - navigate:551 - Products list page loaded
2026-02-16 09:41:00 - pages.base_page - INFO - is_page_loaded:1018 - Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
2026-02-16 09:41:00 - pages.base_page - WARNING - is_page_loaded:1022 - Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
INFO     pages.base_page:products_list_page.py:1018 Checking if page loaded, current URL: https://staging-seller.greatmall.uz/auth/login
WARNING  pages.base_page:products_list_page.py:1022 Not on products page, URL: https://staging-seller.greatmall.uz/auth/login
```
</details>

---

### BUG-F114: test_tablet_layout

- **ID:** BUG-F114
- **Test:** `TestProductsListResponsive.test_tablet_layout`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** UI
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
ERROR    pages.base_page:base_page.py:89 Navigation failed to https://staging-seller.greatmall.uz/dashboard/products: Page.goto: net::ERR_ABORTED at https://staging-seller.greatmall.uz/dashboard/produ
Call log:
- navigating to "https://staging-seller.greatmall.uz/dashboard/products", waiting until "load"
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
pages/base_page.py:85: in navigate_to
    self.page.goto(full_url, wait_until=PageConstants.NETWORK_IDLE,
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:9054: in goto
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_page.py:552: in goto
    return await self._main_frame.goto(**locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:153: in goto
    await self._channel.send(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.Error: Page.goto: net::ERR_ABORTED at https://staging-seller.greatmall.uz/dashboard/products
E   Call log:
E     - navigating to "https://staging-seller.greatmall.uz/dashboard/products", waiting until "load"

During handling of the above exception, another exception occurred:
tests/products_list/test_products_list_ui.py:540: in test_tablet_layout
    products_page.navigate()
pages/products_list_page.py:549: in navigate
    self.navigate_to(self.PRODUCTS_PATH)
pages/base_page.py:90: in navigate_to
    raise NavigationError(f"Navigation failed to {full_url}: {str(e)}")
E   pages.base_page.NavigationError: Navigation failed to https://staging-seller.greatmall.uz/dashboard/products: Page.goto: net::ERR_ABORTED at https://staging-seller.greatmall.uz/dashboard/products
E   Call log:
E     - navigating to "https://staging-seller.greatmall.uz/dashboard/products", waiting until "load"
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:03 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:41:03 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:03 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:03 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:03 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
... (12 more lines)
```
</details>

---

### BUG-F115: test_default_view_mode

- **ID:** BUG-F115
- **Test:** `TestProductsListViewModes.test_default_view_mode`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert table.is_visible(timeout=3000) or products_page.is_empty_state_visible(), \
E   AssertionError: BUG: No view displayed
E   assert (False or False)
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:648: in test_default_view_mode
    assert table.is_visible(timeout=3000) or products_page.is_empty_state_visible(), \
E   AssertionError: BUG: No view displayed
E   assert (False or False)
E    +  where False = is_visible(timeout=3000)
E    +    where is_visible = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard/products?page=1&size=10'> selector='table >> internal:or="[role=\'grid\']" >> internal:or=".
E    +  and   False = is_empty_state_visible()
E    +    where is_empty_state_visible = <pages.products_list_page.ProductsListPage object at 0x10849b880>.is_empty_state_visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:19 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:41:19 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:19 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:19 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:19 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
```
</details>

---

### BUG-F116: test_view_mode_persists

- **ID:** BUG-F116
- **Test:** `TestProductsListViewModes.test_view_mode_persists`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
ERROR    pages.base_page:base_page.py:89 Navigation failed to https://staging-seller.greatmall.uz/dashboard/products: Page.goto: net::ERR_ABORTED at https://staging-seller.greatmall.uz/dashboard/produ
Call log:
- navigating to "https://staging-seller.greatmall.uz/dashboard/products", waiting until "load"
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
pages/base_page.py:85: in navigate_to
    self.page.goto(full_url, wait_until=PageConstants.NETWORK_IDLE,
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:9054: in goto
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_page.py:552: in goto
    return await self._main_frame.goto(**locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:153: in goto
    await self._channel.send(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.Error: Page.goto: net::ERR_ABORTED at https://staging-seller.greatmall.uz/dashboard/products
E   Call log:
E     - navigating to "https://staging-seller.greatmall.uz/dashboard/products", waiting until "load"

During handling of the above exception, another exception occurred:
tests/products_list/test_products_list_ui.py:674: in test_view_mode_persists
    products_page.navigate()
pages/products_list_page.py:549: in navigate
    self.navigate_to(self.PRODUCTS_PATH)
pages/base_page.py:90: in navigate_to
    raise NavigationError(f"Navigation failed to {full_url}: {str(e)}")
E   pages.base_page.NavigationError: Navigation failed to https://staging-seller.greatmall.uz/dashboard/products: Page.goto: net::ERR_ABORTED at https://staging-seller.greatmall.uz/dashboard/products
E   Call log:
E     - navigating to "https://staging-seller.greatmall.uz/dashboard/products", waiting until "load"
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:22 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:41:22 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:22 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:22 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:22 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
... (12 more lines)
```
</details>

---

### BUG-F117: test_subcategory_filter

- **ID:** BUG-F117
- **Test:** `TestProductsListCategoryDisplay.test_subcategory_filter`
- **File:** `tests/products_list/test_products_list_ui.py`
- **Severity:** Medium
- **Category:** Search/Filter
- **Page:** Products List

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Select Zara shop
3. Navigate to /dashboard/products

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:692 Applying category filter: Electronics
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/products_list/test_products_list_ui.py:705: in test_subcategory_filter
    products_page.apply_category_filter("Electronics")
pages/products_list_page.py:693: in apply_category_filter
    self.category_filter.click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for get_by_label("Category").or_(get_by_label("Kategoriya")).or_(locator("[data-testid='category-filter']"))
E       - waiting for" https://staging-seller.greatmall.uz/auth/login" navigation to finish...
E       - navigated to "https://staging-seller.greatmall.uz/auth/login"
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:26 - pages.base_page - INFO - navigate:548 - Navigating to products list page...
2026-02-16 09:41:26 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:26 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
2026-02-16 09:41:26 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:26 - pages.base_page - INFO - navigate:551 - Products list page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:products_list_page.py:548 Navigating to products list page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/products
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:products_list_page.py:551 Products list page loaded
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:41:26 - pages.base_page - INFO - open_filters:673 - Opening filters panel...
2026-02-16 09:41:26 - pages.base_page - INFO - open_filters:677 - Filters panel opened
2026-02-16 09:41:26 - pages.base_page - INFO - apply_category_filter:692 - Applying category filter: Electronics
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:products_list_page.py:673 Opening filters panel...
INFO     pages.base_page:products_list_page.py:677 Filters panel opened
INFO     pages.base_page:products_list_page.py:692 Applying category filter: Electronics
```
</details>

---

## Profile Settings (7 failures)

### BUG-F118: test_settings_nav_link_exists

- **ID:** BUG-F118
- **Test:** `TestProfileSettingsNavigation.test_settings_nav_link_exists`
- **File:** `tests/profile_settings/test_profile_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Profile Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert settings_link.count() > 0, \
E   AssertionError: BUG: Ссылка на настройки отсутствует в навигации
E   assert 0 > 0
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/profile_settings/test_profile_settings_functional.py:62: in test_settings_nav_link_exists
    assert settings_link.count() > 0, \
E   AssertionError: BUG: Ссылка на настройки отсутствует в навигации
E   assert 0 > 0
E    +  where 0 = count()
E    +    where count = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/dashboard'> selector='a:has-text(\'Настройки\') >> internal:or="a:has-text(\'Settings\')" >> internal:or="[
```
</details>

---

### BUG-F119: test_empty_bank_account_rejected

- **ID:** BUG-F119
- **Test:** `TestBankAccountValidation.test_empty_bank_account_rejected`
- **File:** `tests/profile_settings/test_profile_settings_ui.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Profile Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/settings
3. Submit form with empty fields

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/profile_settings_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: profile_settings_ui
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/profile_settings/test_profile_settings_ui.py:156: in test_empty_bank_account_rejected
    pytest.fail("Секция банковских счетов недоступна")
E   Failed: Секция банковских счетов недоступна
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:17 - pages.base_page - INFO - navigate_to_settings:106 - Navigating to settings page...
2026-02-16 09:41:17 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:17 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:17 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:17 - pages.base_page - INFO - navigate_to_settings:109 - Settings page loaded
2026-02-16 09:41:18 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/profile_settings_ui_test_data.
2026-02-16 09:41:18 - conftest - WARNING - test_data:498 - No test data found for module: profile_settings_ui
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:profile_settings_page.py:106 Navigating to settings page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/profile_settings_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: profile_settings_ui
```
</details>

---

### BUG-F120: test_short_bank_account_rejected

- **ID:** BUG-F120
- **Test:** `TestBankAccountValidation.test_short_bank_account_rejected`
- **File:** `tests/profile_settings/test_profile_settings_ui.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Profile Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/profile_settings_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: profile_settings_ui
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/profile_settings/test_profile_settings_ui.py:173: in test_short_bank_account_rejected
    pytest.fail("Секция банковских счетов недоступна")
E   Failed: Секция банковских счетов недоступна
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:18 - pages.base_page - INFO - navigate_to_settings:106 - Navigating to settings page...
2026-02-16 09:41:18 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:18 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:18 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:18 - pages.base_page - INFO - navigate_to_settings:109 - Settings page loaded
2026-02-16 09:41:19 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/profile_settings_ui_test_data.
2026-02-16 09:41:19 - conftest - WARNING - test_data:498 - No test data found for module: profile_settings_ui
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:profile_settings_page.py:106 Navigating to settings page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/profile_settings_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: profile_settings_ui
```
</details>

---

### BUG-F121: test_bank_account_injection_safe[xss]

- **ID:** BUG-F121
- **Test:** `TestBankAccountValidation.test_bank_account_injection_safe[xss]`
- **File:** `tests/profile_settings/test_profile_settings_ui.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Profile Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/profile_settings/test_profile_settings_ui.py:195: in test_bank_account_injection_safe
    pytest.fail("Секция банковских счетов недоступна")
E   Failed: Секция банковских счетов недоступна
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:19 - pages.base_page - INFO - navigate_to_settings:106 - Navigating to settings page...
2026-02-16 09:41:19 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:19 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:19 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:19 - pages.base_page - INFO - navigate_to_settings:109 - Settings page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:profile_settings_page.py:106 Navigating to settings page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```
</details>

---

### BUG-F122: test_bank_account_injection_safe[sql]

- **ID:** BUG-F122
- **Test:** `TestBankAccountValidation.test_bank_account_injection_safe[sql]`
- **File:** `tests/profile_settings/test_profile_settings_ui.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Profile Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/profile_settings/test_profile_settings_ui.py:195: in test_bank_account_injection_safe
    pytest.fail("Секция банковских счетов недоступна")
E   Failed: Секция банковских счетов недоступна
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:20 - pages.base_page - INFO - navigate_to_settings:106 - Navigating to settings page...
2026-02-16 09:41:20 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:20 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:20 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:20 - pages.base_page - INFO - navigate_to_settings:109 - Settings page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:profile_settings_page.py:106 Navigating to settings page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```
</details>

---

### BUG-F123: test_document_section_or_alternative_exists

- **ID:** BUG-F123
- **Test:** `TestDocumentSection.test_document_section_or_alternative_exists`
- **File:** `tests/profile_settings/test_profile_settings_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Profile Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/profile_settings/test_profile_settings_ui.py:230: in test_document_section_or_alternative_exists
    pytest.fail("Секция документов не найдена на странице")
E   Failed: Секция документов не найдена на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:21 - pages.base_page - INFO - navigate_to_settings:106 - Navigating to settings page...
2026-02-16 09:41:21 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:21 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:21 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:21 - pages.base_page - INFO - navigate_to_settings:109 - Settings page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:profile_settings_page.py:106 Navigating to settings page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```
</details>

---

### BUG-F124: test_moderation_section_or_alternative_exists

- **ID:** BUG-F124
- **Test:** `TestModerationSection.test_moderation_section_or_alternative_exists`
- **File:** `tests/profile_settings/test_profile_settings_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Profile Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/profile_settings/test_profile_settings_ui.py:301: in test_moderation_section_or_alternative_exists
    pytest.fail("Секция модерации не найдена на странице")
E   Failed: Секция модерации не найдена на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:26 - pages.base_page - INFO - navigate_to_settings:106 - Navigating to settings page...
2026-02-16 09:41:26 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:26 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
2026-02-16 09:41:26 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:41:26 - pages.base_page - INFO - navigate_to_settings:109 - Settings page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:profile_settings_page.py:106 Navigating to settings page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/profile/settings
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:profile_settings_page.py:109 Settings page loaded
```
</details>

---

## Returns (2 failures)

### BUG-F125: test_switch_status_tab

- **ID:** BUG-F125
- **Test:** `TestReturnsStatusTabs.test_switch_status_tab`
- **File:** `tests/returns/test_returns_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Returns

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/returns

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert new_active != initial_active, f"Tab should change after click. Before: {initial_active}, After: {new_active}"
E   AssertionError: Tab should change after click. Before: Hammasi, After: Hammasi
E   assert 'Hammasi' != 'Hammasi'
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/returns/test_returns_ui.py:90: in test_switch_status_tab
    assert new_active != initial_active, f"Tab should change after click. Before: {initial_active}, After: {new_active}"
E   AssertionError: Tab should change after click. Before: Hammasi, After: Hammasi
E   assert 'Hammasi' != 'Hammasi'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:32 - pages.base_page - INFO - navigate:196 - Navigating to returns page...
2026-02-16 09:31:32 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
2026-02-16 09:31:32 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
2026-02-16 09:31:33 - pages.base_page - INFO - navigate:199 - Returns page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:returns_page.py:196 Navigating to returns page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
INFO     pages.base_page:returns_page.py:199 Returns page loaded
```
</details>

---

### BUG-F126: test_all_tab_names_russian

- **ID:** BUG-F126
- **Test:** `TestReturnsStatusTabs.test_all_tab_names_russian`
- **File:** `tests/returns/test_returns_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Returns

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/returns

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert any(expected in t for t in found_tabs), \
E   AssertionError: BUG: Expected tab 'Все' not found in ['Hammasi', "Ko'rib chiqilmoqda", 'Sotuvchi tomonidan tasdiqlandi', 'Sotuvchi tomonidan rad etildi', 'Marketpleys yordami', 'Marketpleys tomoni
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/returns/test_returns_ui.py:131: in test_all_tab_names_russian
    assert any(expected in t for t in found_tabs), \
E   AssertionError: BUG: Expected tab 'Все' not found in ['Hammasi', "Ko'rib chiqilmoqda", 'Sotuvchi tomonidan tasdiqlandi', 'Sotuvchi tomonidan rad etildi', 'Marketpleys yordami', 'Marketpleys tomoni
E   assert False
E    +  where False = any(<generator object TestReturnsStatusTabs.test_all_tab_names_russian.<locals>.<genexpr> at 0x10a2db5f0>)
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:31:59 - pages.base_page - INFO - navigate:196 - Navigating to returns page...
2026-02-16 09:31:59 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
2026-02-16 09:31:59 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
2026-02-16 09:32:00 - pages.base_page - INFO - navigate:199 - Returns page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:returns_page.py:196 Navigating to returns page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/orders-management/returns?page=1&size=10
INFO     pages.base_page:returns_page.py:199 Returns page loaded
```
</details>

---

## Reviews (6 failures)

### BUG-F127: test_page_url_contains_reviews

- **ID:** BUG-F127
- **Test:** `TestReviewsPageUI.test_page_url_contains_reviews`
- **File:** `tests/test_reviews.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Reviews

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/reviews

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert "/reviews" in reviews_page.page.url, \
E   AssertionError: BUG: URL не содержит /reviews: https://staging-seller.greatmall.uz/auth/login
E   assert '/reviews' in 'https://staging-seller.greatmall.uz/auth/login'
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_reviews.py:48: in test_page_url_contains_reviews
    assert "/reviews" in reviews_page.page.url, \
E   AssertionError: BUG: URL не содержит /reviews: https://staging-seller.greatmall.uz/auth/login
E   assert '/reviews' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
E    +    where <Page url='https://staging-seller.greatmall.uz/auth/login'> = <pages.reviews_page.ReviewsPage object at 0x107f6db50>.page
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:44:51 - pages.base_page - INFO - navigate:142 - Navigating to reviews page...
2026-02-16 09:44:51 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:51 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:51 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:44:51 - pages.base_page - INFO - navigate:145 - Reviews page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:reviews_page.py:142 Navigating to reviews page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:reviews_page.py:145 Reviews page loaded
```
</details>

---

### BUG-F128: test_tabs_visible

- **ID:** BUG-F128
- **Test:** `TestReviewsTabs.test_tabs_visible`
- **File:** `tests/test_reviews.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Reviews

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/reviews

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert len(tabs) >= 1, \
E   AssertionError: BUG: Ожидалось хотя бы 1 таб, найдено 0
E   assert 0 >= 1
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_reviews.py:89: in test_tabs_visible
    assert len(tabs) >= 1, \
E   AssertionError: BUG: Ожидалось хотя бы 1 таб, найдено 0
E   assert 0 >= 1
E    +  where 0 = len([])
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:44:52 - pages.base_page - INFO - navigate:142 - Navigating to reviews page...
2026-02-16 09:44:52 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:52 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:52 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:44:52 - pages.base_page - INFO - navigate:145 - Reviews page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:reviews_page.py:142 Navigating to reviews page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:reviews_page.py:145 Reviews page loaded
```
</details>

---

### BUG-F129: test_one_tab_active_by_default

- **ID:** BUG-F129
- **Test:** `TestReviewsTabs.test_one_tab_active_by_default`
- **File:** `tests/test_reviews.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Reviews

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/reviews

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert len(active) > 0, \
E   AssertionError: BUG: Нет активного таба по умолчанию
E   assert 0 > 0
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_reviews.py:96: in test_one_tab_active_by_default
    assert len(active) > 0, \
E   AssertionError: BUG: Нет активного таба по умолчанию
E   assert 0 > 0
E    +  where 0 = len('')
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:44:53 - pages.base_page - INFO - navigate:142 - Navigating to reviews page...
2026-02-16 09:44:53 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:53 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:53 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:44:53 - pages.base_page - INFO - navigate:145 - Reviews page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:reviews_page.py:142 Navigating to reviews page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:reviews_page.py:145 Reviews page loaded
```
</details>

---

### BUG-F130: test_tab_click_changes_active

- **ID:** BUG-F130
- **Test:** `TestReviewsTabs.test_tab_click_changes_active`
- **File:** `tests/test_reviews.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Reviews

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/reviews
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert new_active != initial_active, \
E   AssertionError: BUG: После клика на второй таб активный таб не изменился: 'Hammasi'
E   assert 'Hammasi' != 'Hammasi'
```

<details>
<summary>Full Traceback</summary>

```python
[gw4] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_reviews.py:108: in test_tab_click_changes_active
    assert new_active != initial_active, \
E   AssertionError: BUG: После клика на второй таб активный таб не изменился: 'Hammasi'
E   assert 'Hammasi' != 'Hammasi'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:44:54 - pages.base_page - INFO - navigate:142 - Navigating to reviews page...
2026-02-16 09:44:54 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:54 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:54 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:44:54 - pages.base_page - INFO - navigate:145 - Reviews page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:reviews_page.py:142 Navigating to reviews page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:reviews_page.py:145 Reviews page loaded
```
</details>

---

### BUG-F131: test_empty_state_or_rows_visible

- **ID:** BUG-F131
- **Test:** `TestReviewsGrid.test_empty_state_or_rows_visible`
- **File:** `tests/test_reviews.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Reviews

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/reviews
3. Submit form with empty fields

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert rows > 0 or empty, \
E   AssertionError: BUG: DataGrid не показывает ни строк ни empty state
E   assert (0 > 0 or False)
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_reviews.py:158: in test_empty_state_or_rows_visible
    assert rows > 0 or empty, \
E   AssertionError: BUG: DataGrid не показывает ни строк ни empty state
E   assert (0 > 0 or False)
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:44:55 - pages.base_page - INFO - navigate:142 - Navigating to reviews page...
2026-02-16 09:44:55 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:55 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:55 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:44:55 - pages.base_page - INFO - navigate:145 - Reviews page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:reviews_page.py:142 Navigating to reviews page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:reviews_page.py:145 Reviews page loaded
```
</details>

---

### BUG-F132: test_page_size_in_url

- **ID:** BUG-F132
- **Test:** `TestReviewsGrid.test_page_size_in_url`
- **File:** `tests/test_reviews.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Reviews

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/reviews

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert "page=" in url and "size=" in url, \
E   AssertionError: BUG: URL не содержит page/size параметры: https://staging-seller.greatmall.uz/auth/login
E   assert ('page=' in 'https://staging-seller.greatmall.uz/auth/login')
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/test_reviews.py:172: in test_page_size_in_url
    assert "page=" in url and "size=" in url, \
E   AssertionError: BUG: URL не содержит page/size параметры: https://staging-seller.greatmall.uz/auth/login
E   assert ('page=' in 'https://staging-seller.greatmall.uz/auth/login')
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:44:56 - pages.base_page - INFO - navigate:142 - Navigating to reviews page...
2026-02-16 09:44:56 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:56 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
2026-02-16 09:44:56 - pages.base_page - INFO - wait_for_page_load:103 - Page loaded successfully
2026-02-16 09:44:56 - pages.base_page - INFO - navigate:145 - Reviews page loaded
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:reviews_page.py:142 Navigating to reviews page...
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/reviews?page=1&size=10
INFO     pages.base_page:base_page.py:103 Page loaded successfully
INFO     pages.base_page:reviews_page.py:145 Reviews page loaded
```
</details>

---

## Shop Create (14 failures)

### BUG-F133: test_shop_name_min_length

- **ID:** BUG-F133
- **Test:** `TestShopCreateBoundary.test_shop_name_min_length`
- **File:** `tests/shop_create/test_shop_create_boundary.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:41:52 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_boundary.py:65: in test_shop_name_min_length
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:20 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data
2026-02-16 09:41:20 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_boundary
2026-02-16 09:41:20 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:41:21 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:41:21 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:41:21 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:41:21 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:41:22 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_boundary
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:41:22 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: AB
2026-02-16 09:41:22 - pages.base_page - INFO - click_save:257 - Clicking save button
------------------------------ Captured log call -------------------------------
... (6 more lines)
```
</details>

---

### BUG-F134: test_shop_name_max_length

- **ID:** BUG-F134
- **Test:** `TestShopCreateBoundary.test_shop_name_max_length`
- **File:** `tests/shop_create/test_shop_create_boundary.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:42:00 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_boundary.py:44: in test_shop_name_max_length
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:29 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data
2026-02-16 09:41:29 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_boundary
2026-02-16 09:41:29 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:41:29 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:41:30 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:41:30 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:41:30 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:41:30 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_boundary
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:41:30 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
2026-02-16 09:41:30 - pages.base_page - INFO - click_save:257 - Clicking save button
------------------------------ Captured log call -------------------------------
... (6 more lines)
```
</details>

---

### BUG-F135: test_description_whitespace_only

- **ID:** BUG-F135
- **Test:** `TestShopCreateBoundary.test_description_whitespace_only`
- **File:** `tests/shop_create/test_shop_create_boundary.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:42:24 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_boundary.py:94: in test_description_whitespace_only
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:52 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data
2026-02-16 09:41:52 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_boundary
2026-02-16 09:41:52 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:41:52 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:41:53 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:41:53 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:41:53 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:41:53 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_boundary
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:41:54 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Test Shop 1771216914
2026-02-16 09:41:54 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description:      ...
2026-02-16 09:41:54 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description:      ...
... (10 more lines)
```
</details>

---

### BUG-F136: test_slug_conflict

- **ID:** BUG-F136
- **Test:** `TestShopCreateFunctional.test_slug_conflict`
- **File:** `tests/shop_create/test_shop_create_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:42:41 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_functional.py:291: in test_slug_conflict
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:09 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_functional_test_da
2026-02-16 09:42:09 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_functional
2026-02-16 09:42:09 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:09 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:10 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:42:10 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:42:10 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:42:10 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_functional
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:42:10 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Unique Name 1771216930
2026-02-16 09:42:10 - pages.base_page - INFO - fill_slug:115 - Filling slug: zara
2026-02-16 09:42:10 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: Тест...
... (12 more lines)
```
</details>

---

### BUG-F137: test_shop_name_with_tabs

- **ID:** BUG-F137
- **Test:** `TestShopCreateWhitespace.test_shop_name_with_tabs`
- **File:** `tests/shop_create/test_shop_create_boundary.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:42:57 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_boundary.py:174: in test_shop_name_with_tabs
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:25 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data
2026-02-16 09:42:25 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_boundary
2026-02-16 09:42:25 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:26 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:26 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:42:27 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:42:27 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:42:27 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_boundary
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:42:27 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Test	Shop	With	Tabs
2026-02-16 09:42:27 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: Тест с табами...
2026-02-16 09:42:27 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: Test with tabs...
... (10 more lines)
```
</details>

---

### BUG-F138: test_sql_injection_in_shop_name

- **ID:** BUG-F138
- **Test:** `TestShopCreateSecurity.test_sql_injection_in_shop_name`
- **File:** `tests/shop_create/test_shop_create_security.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:43:30 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_security.py:64: in test_sql_injection_in_shop_name
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:59 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data
2026-02-16 09:42:59 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_security
2026-02-16 09:42:59 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:59 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:43:00 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:43:00 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:43:00 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:43:00 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:43:00 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: '; DROP TABLE shops; --
2026-02-16 09:43:00 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: Test UZ...
2026-02-16 09:43:00 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: Test RU...
... (10 more lines)
```
</details>

---

### BUG-F139: test_description_with_nbsp

- **ID:** BUG-F139
- **Test:** `TestShopCreateWhitespace.test_description_with_nbsp`
- **File:** `tests/shop_create/test_shop_create_boundary.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:43:31 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_boundary.py:239: in test_description_with_nbsp
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:59 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data
2026-02-16 09:42:59 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_boundary
2026-02-16 09:42:59 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:59 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:43:00 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:43:00 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:43:00 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:43:00 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_boundary_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_boundary
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:43:00 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: NBSP Test 1771216980
2026-02-16 09:43:00 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: Test description with NBSP...
2026-02-16 09:43:00 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: Normal description...
... (10 more lines)
```
</details>

---

### BUG-F140: test_javascript_uri_in_description

- **ID:** BUG-F140
- **Test:** `TestShopCreateSecurity.test_javascript_uri_in_description`
- **File:** `tests/shop_create/test_shop_create_security.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:44:02 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_security.py:93: in test_javascript_uri_in_description
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:30 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data
2026-02-16 09:43:30 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_security
2026-02-16 09:43:30 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:43:30 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:43:31 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:43:31 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:43:31 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:43:32 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:43:32 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Test Shop 1771217012
2026-02-16 09:43:32 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: javascript:alert('XSS')...
2026-02-16 09:43:32 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: Normal description...
... (10 more lines)
```
</details>

---

### BUG-F141: test_complete_shop_creation

- **ID:** BUG-F141
- **Test:** `TestShopCreateE2E.test_complete_shop_creation`
- **File:** `tests/shop_create/test_shop_create_e2e.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:dashboard_page.py:139 Filling Uzbek description: E2E test tavsifi...
INFO     pages.base_page:dashboard_page.py:154 Filling Russian description: E2E тестовое описание...
INFO     pages.base_page:dashboard_page.py:257 Clicking save button
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_e2e.py:61: in test_complete_shop_creation
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:40 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
2026-02-16 09:43:40 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_e2e
2026-02-16 09:43:40 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:43:40 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_e2e
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:43:41 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:43:41 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:43:41 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:43:41 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
2026-02-16 09:43:41 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: E2E Test Shop 1771217021
2026-02-16 09:43:41 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: E2E test tavsifi...
2026-02-16 09:43:41 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: E2E тестовое описание...
2026-02-16 09:43:41 - pages.base_page - INFO - click_save:257 - Clicking save button
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
... (6 more lines)
```
</details>

---

### BUG-F142: test_shop_appears_in_dropdown

- **ID:** BUG-F142
- **Test:** `TestShopCreateE2E.test_shop_appears_in_dropdown`
- **File:** `tests/shop_create/test_shop_create_e2e.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:dashboard_page.py:139 Filling Uzbek description: Test...
INFO     pages.base_page:dashboard_page.py:154 Filling Russian description: Тест...
INFO     pages.base_page:dashboard_page.py:257 Clicking save button
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_e2e.py:109: in test_shop_appears_in_dropdown
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:44:12 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
2026-02-16 09:44:12 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_e2e
2026-02-16 09:44:12 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:44:12 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_e2e
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:44:13 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:44:13 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:44:13 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:44:13 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
2026-02-16 09:44:13 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Dropdown Test 1771217053
2026-02-16 09:44:13 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: Test...
2026-02-16 09:44:14 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: Тест...
2026-02-16 09:44:14 - pages.base_page - INFO - click_save:257 - Clicking save button
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
... (6 more lines)
```
</details>

---

### BUG-F143: test_full_cancel_reopen_workflow

- **ID:** BUG-F143
- **Test:** `TestShopCreateE2E.test_full_cancel_reopen_workflow`
- **File:** `tests/shop_create/test_shop_create_e2e.py`
- **Severity:** Medium
- **Category:** E2E
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert not shop_modal.is_modal_visible(timeout=2000), \
E   AssertionError: FAILED: Modal did not close
E   assert not True
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_e2e.py:257: in test_full_cancel_reopen_workflow
    assert not shop_modal.is_modal_visible(timeout=2000), \
E   AssertionError: FAILED: Modal did not close
E   assert not True
E    +  where True = is_modal_visible(timeout=2000)
E    +    where is_modal_visible = <pages.dashboard_page.ShopCreateModal object at 0x10d628c40>.is_modal_visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:45:48 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
2026-02-16 09:45:48 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_e2e
2026-02-16 09:45:48 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:45:48 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_e2e
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:45:49 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:45:49 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:45:49 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:45:49 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
2026-02-16 09:45:49 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Workflow Test 1771217149
2026-02-16 09:45:49 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: First attempt UZ...
2026-02-16 09:45:49 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: First attempt RU...
2026-02-16 09:45:49 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
INFO     pages.base_page:dashboard_page.py:88 Filling shop name: Workflow Test 1771217149
INFO     pages.base_page:dashboard_page.py:139 Filling Uzbek description: First attempt UZ...
INFO     pages.base_page:dashboard_page.py:154 Filling Russian description: First attempt RU...
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```
</details>

---

### BUG-F144: test_double_click_save

- **ID:** BUG-F144
- **Test:** `TestShopCreateRobustness.test_double_click_save`
- **File:** `tests/shop_create/test_shop_create_e2e.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:46:20 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_e2e.py:308: in test_double_click_save
    save_button.dblclick()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15712: in dblclick
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:177: in dblclick
    return await self._frame.dblclick(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:581: in dblclick
    await self._channel.send(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.dblclick: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("[role='dialog'] button:has-text('Сохранить'), [role='dialog'] button:has-text('Save')").first
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:45:49 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
2026-02-16 09:45:49 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_e2e
2026-02-16 09:45:49 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:45:49 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:45:50 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:45:50 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:45:50 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:45:50 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_e2e
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:45:50 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Double Click Test 1771217150
2026-02-16 09:45:50 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: Test...
2026-02-16 09:45:50 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: Тест...
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:dashboard_page.py:88 Filling shop name: Double Click Test 1771217150
... (6 more lines)
```
</details>

---

### BUG-F145: test_slow_network

- **ID:** BUG-F145
- **Test:** `TestShopCreateRobustness.test_slow_network`
- **File:** `tests/shop_create/test_shop_create_e2e.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
2026-02-16 09:46:52 - pages.base_page - INFO - close_modal:70 - Closing shop create modal
---------------------------- Captured log teardown -----------------------------
INFO     pages.base_page:dashboard_page.py:70 Closing shop create modal
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_e2e.py:359: in test_slow_network
    shop_modal.click_save()
pages/dashboard_page.py:258: in click_save
    self.page.locator(self.SAVE_BTN).click()
../../../Library/Python/3.9/lib/python/site-packages/playwright/sync_api/_generated.py:15631: in click
    self._sync(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_locator.py:162: in click
    return await self._frame._click(self._selector, strict=True, **params)
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_frame.py:566: in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
../../../Library/Python/3.9/lib/python/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("button:has-text('Save and Submit for Moderation')")
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:46:20 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
2026-02-16 09:46:20 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_e2e
2026-02-16 09:46:20 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:46:20 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:46:21 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:46:21 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:46:21 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:46:22 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_e2e
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:46:22 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Slow Network Test 1771217182
2026-02-16 09:46:22 - pages.base_page - INFO - fill_description_uz:139 - Filling Uzbek description: Test...
2026-02-16 09:46:22 - pages.base_page - INFO - fill_description_ru:154 - Filling Russian description: Тест...
... (10 more lines)
```
</details>

---

### BUG-F146: test_rapid_form_changes

- **ID:** BUG-F146
- **Test:** `TestShopCreateRobustness.test_rapid_form_changes`
- **File:** `tests/shop_create/test_shop_create_e2e.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Create

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shops/create

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert len(slug) > 0, \
E   AssertionError: BUG: Slug NOT generated after rapid changes and 2s debounce! Name: Rapid Test 9 - 1771217216
E   assert 0 > 0
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/test_shop_create_e2e.py:415: in test_rapid_form_changes
    assert len(slug) > 0, \
E   AssertionError: BUG: Slug NOT generated after rapid changes and 2s debounce! Name: Rapid Test 9 - 1771217216
E   assert 0 > 0
E    +  where 0 = len('')
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:46:52 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
2026-02-16 09:46:52 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_e2e
2026-02-16 09:46:52 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:46:52 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:46:55 - pages.base_page - INFO - open_shop_dropdown:503 - Opening shop dropdown
2026-02-16 09:46:55 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
2026-02-16 09:46:55 - pages.base_page - INFO - click_add_shop:547 - Clicking 'Add Shop' button
2026-02-16 09:46:56 - pages.base_page - INFO - click_element:203 - Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_e2e
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:dashboard_page.py:503 Opening shop dropdown
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Active'), button:has-text('Faol'), button:has-text('Активный')
INFO     pages.base_page:dashboard_page.py:547 Clicking 'Add Shop' button
INFO     pages.base_page:base_page.py:203 Clicked element: button:has-text('Add Shop'), button:has-text('Do\'kon qo\'shish'), button:has-text('Добавить магазин')
----------------------------- Captured stdout call -----------------------------
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 0 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 1 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 2 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 3 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 4 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 5 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 6 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 7 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 8 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - fill_shop_name:88 - Filling shop name: Rapid Test 9 - 1771217216
2026-02-16 09:46:56 - pages.base_page - INFO - get_slug_value:104 - Retrieved slug value:
------------------------------ Captured log call -------------------------------
INFO     pages.base_page:dashboard_page.py:88 Filling shop name: Rapid Test 0 - 1771217216
INFO     pages.base_page:dashboard_page.py:88 Filling shop name: Rapid Test 1 - 1771217216
INFO     pages.base_page:dashboard_page.py:88 Filling shop name: Rapid Test 2 - 1771217216
... (18 more lines)
```
</details>

---

## Shop Settings (32 failures)

### BUG-F147: test_shop_name_has_value

- **ID:** BUG-F147
- **Test:** `TestShopNameField.test_shop_name_has_value`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:26: in test_shop_name_has_value
    pytest.fail("Поле названия магазина не найдено")
E   Failed: Поле названия магазина не найдено
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:50 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:50 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:50 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F148: test_shop_name_editable

- **ID:** BUG-F148
- **Test:** `TestShopNameField.test_shop_name_editable`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:35: in test_shop_name_editable
    pytest.fail("Поле названия магазина не найдено")
E   Failed: Поле названия магазина не найдено
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:51 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:51 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:51 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F149: test_shop_name_empty_rejected

- **ID:** BUG-F149
- **Test:** `TestShopNameField.test_shop_name_empty_rejected`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Validation
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Submit form with empty fields

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:46: in test_shop_name_empty_rejected
    pytest.fail("Поле названия магазина недоступно")
E   Failed: Поле названия магазина недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:52 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:52 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:52 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F150: test_shop_name_injection_safe[xss]

- **ID:** BUG-F150
- **Test:** `TestShopNameField.test_shop_name_injection_safe[xss]`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:68: in test_shop_name_injection_safe
    pytest.fail("Поле названия магазина недоступно")
E   Failed: Поле названия магазина недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:53 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:53 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:53 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F151: test_shop_name_injection_safe[sql]

- **ID:** BUG-F151
- **Test:** `TestShopNameField.test_shop_name_injection_safe[sql]`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:68: in test_shop_name_injection_safe
    pytest.fail("Поле названия магазина недоступно")
E   Failed: Поле названия магазина недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:54 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:54 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:55 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F152: test_description_uz_field_exists

- **ID:** BUG-F152
- **Test:** `TestShopDescriptionFields.test_description_uz_field_exists`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:95: in test_description_uz_field_exists
    pytest.fail("Поле описания UZ не найдено на странице")
E   Failed: Поле описания UZ не найдено на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:56 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:56 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:56 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F153: test_description_ru_field_exists

- **ID:** BUG-F153
- **Test:** `TestShopDescriptionFields.test_description_ru_field_exists`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:103: in test_description_ru_field_exists
    pytest.fail("Поле описания RU не найдено на странице")
E   Failed: Поле описания RU не найдено на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:57 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:57 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:57 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F154: test_description_editable

- **ID:** BUG-F154
- **Test:** `TestShopDescriptionFields.test_description_editable`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:110: in test_description_editable
    pytest.fail("Поле описания UZ не найдено")
E   Failed: Поле описания UZ не найдено
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:58 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:58 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:58 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F155: test_description_xss_safe[xss_script]

- **ID:** BUG-F155
- **Test:** `TestShopDescriptionFields.test_description_xss_safe[xss_script]`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:124: in test_description_xss_safe
    pytest.fail("Поле описания UZ недоступно")
E   Failed: Поле описания UZ недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:59 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:42:59 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:42:59 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F156: test_description_xss_safe[xss_img]

- **ID:** BUG-F156
- **Test:** `TestShopDescriptionFields.test_description_xss_safe[xss_img]`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:124: in test_description_xss_safe
    pytest.fail("Поле описания UZ недоступно")
E   Failed: Поле описания UZ недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:00 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:00 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:00 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F157: test_description_accepts_valid_text

- **ID:** BUG-F157
- **Test:** `TestShopDescriptionFields.test_description_accepts_valid_text`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Fill form with valid data and submit

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:136: in test_description_accepts_valid_text
    pytest.fail("Поле описания UZ недоступно")
E   Failed: Поле описания UZ недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:01 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:01 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:01 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F158: test_slug_field_exists

- **ID:** BUG-F158
- **Test:** `TestShopSlugSku.test_slug_field_exists`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:157: in test_slug_field_exists
    pytest.fail("Поле slug не найдено на странице")
E   Failed: Поле slug не найдено на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:02 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:02 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:02 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F159: test_sku_field_exists

- **ID:** BUG-F159
- **Test:** `TestShopSlugSku.test_sku_field_exists`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:165: in test_sku_field_exists
    pytest.fail("Поле SKU не найдено на странице")
E   Failed: Поле SKU не найдено на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:03 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:03 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:03 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F160: test_slug_has_value

- **ID:** BUG-F160
- **Test:** `TestShopSlugSku.test_slug_has_value`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:172: in test_slug_has_value
    pytest.fail("Поле slug не найдено")
E   Failed: Поле slug не найдено
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:04 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:04 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:04 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F161: test_sku_has_value

- **ID:** BUG-F161
- **Test:** `TestShopSlugSku.test_sku_has_value`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:181: in test_sku_has_value
    pytest.fail("Поле SKU не найдено")
E   Failed: Поле SKU не найдено
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:05 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:05 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:05 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F162: test_slug_format_valid

- **ID:** BUG-F162
- **Test:** `TestShopSlugSku.test_slug_format_valid`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Fill form with valid data and submit

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:190: in test_slug_format_valid
    pytest.fail("Поле slug не найдено")
E   Failed: Поле slug не найдено
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:06 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:06 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:06 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F163: test_logo_upload_field_exists

- **ID:** BUG-F163
- **Test:** `TestShopImageUpload.test_logo_upload_field_exists`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:217: in test_logo_upload_field_exists
    pytest.fail("Поле загрузки логотипа не найдено на странице")
E   Failed: Поле загрузки логотипа не найдено на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:07 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:07 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:07 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F164: test_banner_upload_field_exists

- **ID:** BUG-F164
- **Test:** `TestShopImageUpload.test_banner_upload_field_exists`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:229: in test_banner_upload_field_exists
    pytest.fail("Поле загрузки баннера не найдено на странице")
E   Failed: Поле загрузки баннера не найдено на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:08 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:08 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:08 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F165: test_save_button_enabled

- **ID:** BUG-F165
- **Test:** `TestShopSettingsSaveCancel.test_save_button_enabled`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:253: in test_save_button_enabled
    pytest.fail("Кнопка сохранения не найдена")
E   Failed: Кнопка сохранения не найдена
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:09 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:09 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:10 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F166: test_save_button_clickable

- **ID:** BUG-F166
- **Test:** `TestShopSettingsSaveCancel.test_save_button_clickable`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:262: in test_save_button_clickable
    pytest.fail("Кнопка сохранения не найдена")
E   Failed: Кнопка сохранения не найдена
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:11 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:11 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:11 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F167: test_cancel_button_clickable

- **ID:** BUG-F167
- **Test:** `TestShopSettingsSaveCancel.test_cancel_button_clickable`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:275: in test_cancel_button_clickable
    pytest.fail("Кнопка отмены не найдена")
E   Failed: Кнопка отмены не найдена
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:12 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:12 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:12 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F168: test_description_injection_safe[command]

- **ID:** BUG-F168
- **Test:** `TestShopSettingsSecurity.test_description_injection_safe[command]`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:357: in test_description_injection_safe
    pytest.fail("Поле описания UZ недоступно")
E   Failed: Поле описания UZ недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:20 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:20 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:20 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F169: test_description_injection_safe[ldap]

- **ID:** BUG-F169
- **Test:** `TestShopSettingsSecurity.test_description_injection_safe[ldap]`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:357: in test_description_injection_safe
    pytest.fail("Поле описания UZ недоступно")
E   Failed: Поле описания UZ недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:21 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:21 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:21 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F170: test_description_injection_safe[path_traversal]

- **ID:** BUG-F170
- **Test:** `TestShopSettingsSecurity.test_description_injection_safe[path_traversal]`
- **File:** `tests/shop_settings/test_shop_settings_functional.py`
- **Severity:** Critical
- **Category:** Security
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Enter malicious payload into form field

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_functional.py:357: in test_description_injection_safe
    pytest.fail("Поле описания UZ недоступно")
E   Failed: Поле описания UZ недоступно
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:22 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:22 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:23 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F171: test_shop_settings_page_loads

- **ID:** BUG-F171
- **Test:** `TestShopSettingsUI.test_shop_settings_page_loads`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert is_loaded, \
E   AssertionError: BUG: Страница настроек магазина не загрузилась. URL: https://staging-seller.greatmall.uz/auth/login
E   assert False
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:26: in test_shop_settings_page_loads
    assert is_loaded, \
E   AssertionError: BUG: Страница настроек магазина не загрузилась. URL: https://staging-seller.greatmall.uz/auth/login
E   assert False
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:23 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:23 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:24 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F172: test_page_url_contains_shop_or_settings

- **ID:** BUG-F172
- **Test:** `TestShopSettingsUI.test_page_url_contains_shop_or_settings`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert has_shop or has_settings, \
E   AssertionError: BUG: URL не содержит shop/settings: https://staging-seller.greatmall.uz/auth/login
E   assert (False or False)
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:35: in test_page_url_contains_shop_or_settings
    assert has_shop or has_settings, \
E   AssertionError: BUG: URL не содержит shop/settings: https://staging-seller.greatmall.uz/auth/login
E   assert (False or False)
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:24 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:24 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:25 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F173: test_shop_name_input_visible

- **ID:** BUG-F173
- **Test:** `TestShopSettingsUI.test_shop_name_input_visible`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:57: in test_shop_name_input_visible
    pytest.fail("Поле названия магазина не найдено на странице")
E   Failed: Поле названия магазина не найдено на странице
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:28 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:28 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:28 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F174: test_cancel_button_visible

- **ID:** BUG-F174
- **Test:** `TestShopSettingsUI.test_cancel_button_visible`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Low
- **Category:** UI
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings
3. Click relevant button/element

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:93: in test_cancel_button_visible
    pytest.fail("Кнопка отмены не найдена (не все формы её имеют)")
E   Failed: Кнопка отмены не найдена (не все формы её имеют)
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:30 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:30 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:31 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F175: test_direct_url_loads_page

- **ID:** BUG-F175
- **Test:** `TestShopSettingsNavigation.test_direct_url_loads_page`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert "/auth/login" not in page.url, \
E   AssertionError: BUG: Редирект на логин вместо настроек: https://staging-seller.greatmall.uz/auth/login
E   assert '/auth/login' not in 'https://sta...z/auth/login'
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:112: in test_direct_url_loads_page
    assert "/auth/login" not in page.url, \
E   AssertionError: BUG: Редирект на логин вместо настроек: https://staging-seller.greatmall.uz/auth/login
E   assert '/auth/login' not in 'https://sta...z/auth/login'
E
E     '/auth/login' is contained here:
E       https://staging-seller.greatmall.uz/auth/login
E     ?                                    +++++++++++
```
</details>

---

### BUG-F176: test_refresh_preserves_page

- **ID:** BUG-F176
- **Test:** `TestShopSettingsNavigation.test_refresh_preserves_page`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert "/dashboard" in url, \
E   AssertionError: BUG: После refresh URL изменился: https://staging-seller.greatmall.uz/auth/login
E   assert '/dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:121: in test_refresh_preserves_page
    assert "/dashboard" in url, \
E   AssertionError: BUG: После refresh URL изменился: https://staging-seller.greatmall.uz/auth/login
E   assert '/dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:32 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:32 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:33 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F177: test_browser_back_from_settings

- **ID:** BUG-F177
- **Test:** `TestShopSettingsNavigation.test_browser_back_from_settings`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert "/dashboard" in shop_settings_page.page.url, \
E   AssertionError: BUG: Кнопка назад не сработала: https://staging-seller.greatmall.uz/auth/login
E   assert '/dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:129: in test_browser_back_from_settings
    assert "/dashboard" in shop_settings_page.page.url, \
E   AssertionError: BUG: Кнопка назад не сработала: https://staging-seller.greatmall.uz/auth/login
E   assert '/dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
E    +    where <Page url='https://staging-seller.greatmall.uz/auth/login'> = <pages.shop_settings_page.ShopSettingsPage object at 0x10860d760>.page
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:43:34 - pages.base_page - INFO - navigate_to_shop_settings:67 - Navigating to shop settings
2026-02-16 09:43:34 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
2026-02-16 09:43:35 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:shop_settings_page.py:67 Navigating to shop settings
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard/settings
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard/settings
```
</details>

---

### BUG-F178: test_settings_link_in_sidebar

- **ID:** BUG-F178
- **Test:** `TestShopSettingsNavigation.test_settings_link_in_sidebar`
- **File:** `tests/shop_settings/test_shop_settings_ui.py`
- **Severity:** Medium
- **Category:** Functional
- **Page:** Shop Settings

**Steps to Reproduce:**
1. Login to staging-seller.greatmall.uz (998001112233 / 76543217)
2. Navigate to /dashboard/shop/settings

**Expected Result:**
Test should PASS - system should handle the scenario correctly.

**Actual Result:**
```
assert settings_link.count() > 0, \
E   AssertionError: BUG: Ссылка на настройки отсутствует в сайдбаре
E   assert 0 > 0
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_settings/test_shop_settings_ui.py:142: in test_settings_link_in_sidebar
    assert settings_link.count() > 0, \
E   AssertionError: BUG: Ссылка на настройки отсутствует в сайдбаре
E   assert 0 > 0
E    +  where 0 = count()
E    +    where count = <Locator frame=<Frame name= url='https://staging-seller.greatmall.uz/auth/login'> selector='a:has-text(\'Настройки\') >> internal:or="a:has-text(\'Settings\')" >> internal:or="
```
</details>

---
