# Implementation Plan: Categories Management

**Feature**: 004-categories
**Created**: 2025-12-21
**Status**: Implemented

## Technical Context

| Aspect | Details |
|--------|---------|
| Framework | Playwright for Python + pytest |
| Architecture | Page Object Model (POM) |
| Environment | STAGING (https://staging-admin.greatmall.uz/) |
| Fixture | `staging_logged_in_page` (session-scoped) |

## File Structure

```
Greatmall_Adminpanel/
├── pages/
│   └── categories_page.py     # CategoriesPage class (17.4 KB)
└── tests/
    └── test_categories.py     # Tests in multiple classes (14.6 KB)
```

## Page Object: CategoriesPage

### Key Locators
- Page heading: `get_by_role("heading", name="Категории")`
- Add button: `get_by_role("button", name="Добавить")`
- Category tree: Tree item locators
- Form tabs: Tab navigation

### Key Methods
- `navigate_from_dashboard()` - Navigate to categories
- `is_on_categories_page()` - Check current page
- `get_all_root_categories()` - Get tree roots
- `expand_category(name)` - Expand tree node
- `select_category(name)` - Select category
- `click_add_button()` - Open create form
- `get_form_heading()` - Get form title
- `fill_category_form()` - Fill form fields
- `select_tab(name)` - Switch form tabs

## Test Approach

### Environment Note
Categories tests run on **STAGING** environment, not DEV.
Uses `staging_logged_in_page` fixture.

### Test Design Techniques
- Equivalence Partitioning: Empty vs valid input
- Boundary Value Analysis: SEO field limits
- Error Guessing: Tab validation indicators

## Implementation Notes

### Staging vs DEV
```python
# Uses staging fixture instead of logged_in_page
@pytest.fixture(autouse=True)
def setup(self, staging_logged_in_page: Page):
    self.page = staging_logged_in_page
    self.categories_page = CategoriesPage(staging_logged_in_page)
```

### Tree Navigation Pattern
```python
# Expand parent, then select child
self.categories_page.expand_category("Электроника")
self.categories_page.select_category("Смартфоны")
```
