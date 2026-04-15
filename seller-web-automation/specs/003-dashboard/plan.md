# Implementation Plan: Dashboard

**Feature**: 003-dashboard
**Created**: 2025-12-21
**Status**: Implemented

## Technical Context

| Aspect | Details |
|--------|---------|
| Framework | Playwright for Python + pytest |
| Architecture | Page Object Model (POM) |
| Environment | DEV (https://dev-admin.greatmall.uz/) |
| Fixture | `logged_in_page` (session-scoped) |

## File Structure

```
Greatmall_Adminpanel/
├── pages/
│   └── dashboard_page.py      # DashboardPage class (5.1 KB)
└── tests/
    └── test_dashboard.py      # 8 tests in 3 classes (5.4 KB)
```

## Page Object: DashboardPage

### Locators
- Dashboard title: `get_by_role("heading", name="Панель управления")`
- Sidebar: Main navigation container
- Product Management menu: `get_by_role("button", name="Управление товарами")`
- Products link: `get_by_role("link", name="Товары")`
- Categories link: `get_by_role("link", name="Категории")`

### Key Methods
- `navigate_to_dashboard()` - Go to dashboard
- `is_on_dashboard()` - Check if on dashboard
- `get_dashboard_title()` - Get page title
- `is_sidebar_visible()` - Check sidebar visibility
- `expand_sidebar_menu(name)` - Expand menu item
- `is_user_profile_visible()` - Check profile section

## Test Classes

### 1. TestDashboardNavigation
- `test_01_dashboard_loads_after_login`
- `test_02_dashboard_url_pattern`

### 2. TestDashboardSidebar
- `test_03_sidebar_visible`
- `test_04_sidebar_menu_items`
- `test_05_expand_product_management`
- `test_06_navigate_to_products_from_sidebar`
- `test_07_navigate_to_categories_from_sidebar`

### 3. TestDashboardUserProfile
- `test_08_user_profile_visible`

## Implementation Notes

### Session-Scoped Login
All dashboard tests use `logged_in_page` fixture which:
- Logs in once at session start
- Reuses authenticated session across all tests
- Simulates real user behavior

### Navigation Pattern
```python
# Expand menu then click submenu
self.dashboard_page.expand_sidebar_menu("Управление товарами")
self.page.get_by_role("link", name="Товары").click()
```
