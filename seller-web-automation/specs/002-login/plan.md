# Implementation Plan: Login & Authentication

**Feature**: 002-login
**Created**: 2025-12-21
**Status**: Implemented

## Technical Context

| Aspect | Details |
|--------|---------|
| Framework | Playwright for Python + pytest |
| Architecture | Page Object Model (POM) |
| Environment | DEV (https://dev-admin.greatmall.uz/) |
| Test Approach | Negative cases first, positive case last |

## File Structure

```
Greatmall_Adminpanel/
├── pages/
│   └── login_page.py          # LoginPage class (5.4 KB)
├── tests/
│   └── test_login.py          # 8 tests in 3 classes (10.3 KB)
└── utils/
    └── constants.py           # TEST_USER_LOGIN, TEST_USER_PASSWORD
```

## Page Object: LoginPage

### Locators
- Username field: `get_by_role("textbox", name="Логин")`
- Password field: `get_by_role("textbox", name="Пароль")`
- Login button: `get_by_role("button", name="Войти")`
- Remember checkbox: `get_by_role("checkbox", name="Запомнить меня")`
- Forgot link: `get_by_role("link", name="Забыли пароль?")`

### Key Methods
- `navigate()` - Go to login page
- `login(username, password)` - Complete login flow
- `fill_username(value)` - Fill username field
- `fill_password(value)` - Fill password field
- `click_login_button()` - Submit form
- `is_logged_in()` - Check if on dashboard
- `is_on_login_page()` - Check if still on login
- `get_username_validation_error()` - Get username error
- `get_password_validation_error()` - Get password error
- `toggle_password_visibility()` - Toggle password view
- `set_remember_me(checked)` - Set remember checkbox

## Test Classes

### 1. TestLoginNegativeCases
**Purpose**: Verify error handling (runs FIRST)
- `test_01_empty_fields` - Empty form submission
- `test_02_invalid_username_format` - Invalid phone format
- `test_03_invalid_password_length` - Short password
- `test_04_wrong_credentials` - Incorrect password

### 2. TestLoginUIElements
**Purpose**: Verify UI interactions
- `test_05_login_page_elements` - All elements visible
- `test_06_password_visibility_toggle` - Toggle works
- `test_07_remember_me_checkbox` - Checkbox toggles

### 3. TestLoginPositive
**Purpose**: Verify successful login (runs LAST)
- `test_08_valid_login_admin` - Admin login success

## Implementation Notes

### Test Execution Order
Tests are ordered to run negative cases first:
1. Validation tests (empty, format, length)
2. Authentication tests (wrong credentials)
3. UI interaction tests
4. Positive test (successful login)

### Fixtures Used
- `page` - Fresh browser page per test (for negative cases)
- Each test navigates to login page in setup

### Validation Messages (Russian)
- Phone: "Введите корректный номер телефона в формате 998XXXXXXXXX"
- Password: "Пароль должен содержать не менее 8 символов"
