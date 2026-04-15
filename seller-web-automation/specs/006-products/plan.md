# Implementation Plan: Products Management

**Feature**: 006-products
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
│   ├── products_list_page.py  # ProductsListPage class (7.8 KB)
│   └── product_detail_page.py # ProductDetailPage class (9.4 KB)
└── tests/
    └── test_products.py       # Tests in multiple classes (8.5 KB)
```

## Page Objects

### ProductsListPage
**Key Methods**:
- `navigate_from_dashboard()` - Navigate to products
- `is_on_products_list_page()` - Check current page
- `select_status_tab(name)` - Select status filter
- `get_all_status_tabs()` - Get tab names
- `search_product(query)` - Search products
- `scroll_to_products()` - Scroll product list
- `click_product_by_index(index)` - Open product
- `scroll_to_pagination()` - Show pagination
- `go_to_next_page()` - Next page
- `select_page_size(size)` - Change size

### ProductDetailPage
**Key Methods**:
- `is_on_product_detail_page()` - Check detail page
- `select_tab(name)` - Switch tabs
- `get_product_title()` - Get product name
- `is_media_section_visible()` - Check media
- `is_moderation_section_visible()` - Check moderation
- `click_back_button()` - Return to list

## Status Tabs

```python
PRODUCT_STATUS_TABS = [
    "Все",
    "Опубликован",
    "Черновик",
    "В архиве",
    "На модерации",
    "Прошел модерацию"
]
```

## Implementation Notes

### User Journey Pattern
Single test covers complete product detail journey:
1. Navigate to products
2. Click first product
3. View all tabs
4. Check media section
5. Check moderation section
6. Return to list

### Known Bug
Search functionality documented as xfail:
```python
@pytest.mark.xfail(reason="Search filtering bug - dev team notified 2025-12-18")
def test_02_search_product(self):
    ...
```
