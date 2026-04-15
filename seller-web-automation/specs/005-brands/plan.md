# Implementation Plan: Brands Management

**Feature**: 005-brands
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
│   └── brands_page.py         # BrandsPage class (16.1 KB)
└── tests/
    └── test_brands.py         # Tests in multiple classes (10.7 KB)
```

## Page Object: BrandsPage

### Key Locators
- Brands list grid: Grid table
- Pagination: nav with pagination
- Search input: Search field
- Add button: `get_by_role("button", name="Добавить")`

### Key Methods
- `navigate_from_dashboard()` - Navigate to brands
- `is_on_brands_page()` - Check current page
- `scroll_to_pagination()` - Scroll to pagination
- `go_to_page(number)` - Navigate to page
- `get_current_page()` - Get current page number
- `get_last_page_number()` - Get last page
- `select_page_size(size)` - Change page size
- `search_brand(query)` - Search brands
- `clear_search()` - Clear search
- `click_add_button()` - Open create form
- `fill_brand_form()` - Fill brand data
- `upload_logo()` - Upload brand logo

## Test Approach

### Pagination Journey
Single test covers complete pagination flow:
- Start at page 1
- Jump to pages 10, 40, 80, last
- Return to page 1
- Change page sizes

### Search Flow
Single test covers complete search:
- Search by ID
- Search by name
- Clear and verify

## Implementation Notes

### Page Size Options
```python
PAGE_SIZES = [10, 30, 50, 100]
```

### Pagination Pattern
```python
# Jump directly to pages, don't iterate
self.brands_page.go_to_page(10)
assert self.brands_page.get_current_page() == 10
```
