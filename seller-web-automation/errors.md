# Errors Report - 356 Setup/Fixture Errors

Generated: 2026-01-22

## Summary
- **Total Errors**: 356
- **Root Causes**: KeyError in page objects, network issues (ERR_ABORTED), missing fixtures

---

## By Test File

| File | Errors | Cause |
|------|--------|-------|
| test_products_list.py | 239 | KeyError - missing page object config |
| test_shopcreate.py | 91 | Fixture setup failure |
| test_profile_settings.py | 16 | KeyError - missing settings config |
| test_shop_settings.py | 10 | KeyError - missing settings config |

---

## test_products_list.py (239 errors)

### Root Cause
`KeyError` in page object - likely missing locator configuration in `pages/products_list_page.py`

### Affected Test Classes
- TestProductsListUI (12 tests)
- TestProductsListSearch (10 tests)
- TestProductsListSearchSecurity (8 tests)
- TestProductsListFilters (8 tests)
- TestProductsListPagination (10 tests)
- TestProductsListSorting (6 tests)
- TestProductsListTable (8 tests)
- TestProductsListBulkActions (8 tests)
- TestProductsListEmptyState (5 tests)
- TestProductsListNavigation (6 tests)
- TestProductsListURL (5 tests)
- TestProductsListLoading (5 tests)
- TestProductsListToasts (5 tests)
- TestProductsListModals (5 tests)
- TestProductsListRobustness (8 tests)
- TestProductsListAccessibility (8 tests)
- TestProductsListLocalization (5 tests)
- TestProductsListE2E (11 tests)
- TestProductsListKeyboardShortcuts (6 tests)
- TestProductsListImageHandling (5 tests)
- TestProductsListStatusIndicators (6 tests)
- TestProductsListStockIndicators (5 tests)
- TestProductsListPriceDisplay (5 tests)
- TestProductsListWhitespace (5 tests)
- TestProductsListAdvancedSecurity (6 tests)
- TestProductsListPerformance (5 tests)
- TestProductsListConsole (3 tests)
- TestProductsListResponsive (5 tests)
- TestProductsListDataIntegrity (5 tests)
- TestProductsListViewModes (4 tests)
- TestProductsListQuickActions (5 tests)
- TestProductsListCategoryDisplay (5 tests)
- TestProductsListDateFilters (5 tests)
- TestProductsListColumnCustomization (5 tests)
- TestProductsListSavedFilters (5 tests)
- TestProductsListMultiLanguage (5 tests)
- TestProductsListSession (4 tests)
- TestProductsListErrorHandling (5 tests)
- TestProductsListAnalytics (4 tests)
- TestProductsListExport (3 tests)

---

## test_shopcreate.py (91 errors)

### Root Cause
Fixture setup failure - `pages.base_page` error during setup

### Affected Test Classes
- TestShopCreateUI (11 tests)
- TestShopCreateEmptyFields (5 tests)
- TestShopCreateInvalidFormat (8 tests)
- TestShopCreateFileUpload (5 tests)
- TestShopCreateBoundary (4 tests)
- TestShopCreateSecurity (4 tests)
- TestShopCreateFunctional (9 tests)
- TestShopCreateSession (2 tests)
- TestShopCreateE2E (5 tests)
- TestShopCreateWhitespace (5 tests)
- TestShopCreateAdvancedSecurity (5 tests)
- TestShopCreateAdvancedInput (3 tests)
- TestShopCreateRobustness (4 tests)
- TestShopCreateAccessibility (3 tests)
- TestShopCreateSlugSku (5 tests)
- TestShopCreateDescriptionInjection (3 tests)
- TestShopCreateAdvancedFileUpload (4 tests)
- TestShopCreateConcurrent (3 tests)
- TestShopCreateValidationUX (3 tests)

---

## test_profile_settings.py (16 errors)

### Root Cause
`KeyError` - missing configuration in profile settings page object

### Affected Test Classes
- TestBankAccountValidation (3 tests)
  - test_bank_account_format
  - test_bank_account_validation
  - test_duplicate_bank_account
- TestDocumentValidation (3 tests)
  - test_invalid_document_upload
  - test_max_file_size_validation
  - test_required_document_validation
- TestModeration (3 tests)
  - test_moderation_rejection_flow
  - test_send_for_moderation
  - test_approved_profile_state
- TestBankAccount (2 tests)
  - test_delete_bank_account
  - test_add_bank_account
- TestDocument (2 tests)
  - test_delete_document
  - test_valid_document_upload
- TestSettings (3 tests)
  - test_language_toggle
  - test_vat_toggle
  - test_confirmation_modal

---

## test_shop_settings.py (10 errors)

### Root Cause
`KeyError` - missing configuration in shop settings page object

### Affected Test Classes
- TestShopSettingsNavigation (2 tests)
  - test_navigate_to_shop_settings
  - test_shop_settings_page_loads
- TestShopInformation (3 tests)
  - test_shop_name_displayed
  - test_shop_slug_displayed
  - test_shop_sku_displayed
- TestEditShopSettings (3 tests)
  - test_edit_shop_description
  - test_save_shop_settings
  - test_cancel_shop_settings
- TestShopStatus (2 tests)
  - test_view_shop_status
  - test_shop_settings_ui_elements

---

## How to Fix

### 1. Products List Page
Check `pages/products_list_page.py` for missing locators or configuration keys.

### 2. Shop Create
Check fixture `seller_authenticated_session` in `conftest.py` - likely network/auth issue.

### 3. Profile Settings
Check `pages/profile_settings_page.py` for missing configuration.

### 4. Shop Settings
Check `pages/shop_settings_page.py` for missing configuration.

---

## Network Errors (Intermittent)
Some errors are caused by `net::ERR_ABORTED` when navigating to staging server:
- `https://staging-seller.greatmall.uz/`

This indicates staging server instability or network issues during test run.
