# ERROR REPORT: Setup/Fixture Errors (284 tests)

**Environment:** staging-seller.greatmall.uz
**Browser:** Chromium (headless)
**Date:** 2026-02-16
**Runner:** pytest -n 6 (parallel)
**Total ERROR:** 284 tests (169 unique tracebacks)

> **Note:** ERROR means test setup (fixture) failed before the test body executed.
> These are NOT assertion failures — the test never ran.
> Multiple tests can share the same root cause (e.g. shared fixture failure).

---

## Summary by File

| File | Error Count |
|------|------------|
| `tests/multiproduct/test_multiproduct_functional.py` | 27 |
| `tests/multiproduct/test_multiproduct_security.py` | 13 |
| `tests/multiproduct/test_multiproduct_ui.py` | 21 |
| `tests/multiproduct/test_multiproduct_validation.py` | 34 |
| `tests/product_create/test_product_create_functional.py` | 27 |
| `tests/product_create/test_product_create_security.py` | 22 |
| `tests/product_create/test_product_create_ui.py` | 6 |
| `tests/product_create/test_product_create_validation.py` | 16 |
| `tests/product_detail/test_product_detail_functional.py` | 18 |
| `tests/product_detail/test_product_detail_ui.py` | 16 |
| `tests/product_detail/test_product_detail_validation.py` | 28 |
| `tests/shop_create/test_shop_create_e2e.py` | 4 |
| `tests/shop_create/test_shop_create_files.py` | 9 |
| `tests/shop_create/test_shop_create_functional.py` | 4 |
| `tests/shop_create/test_shop_create_security.py` | 9 |
| `tests/shop_create/test_shop_create_ui.py` | 17 |
| `tests/shop_create/test_shop_create_validation.py` | 13 |

---

## Root Cause Analysis

## Multi-Product (95 errors)

### ERR-001: `tests/multiproduct/test_multiproduct_functional.py` (27 tests)

**Affected Tests:**
- `TestMultiProductNavigation::test_back_from_step2_to_step1`
- `TestMultiProductNavigation::test_back_from_step3_to_step2`
- `TestMultiProductNavigation::test_data_preserved_after_back`
- `TestMultiProductVariants::test_single_variant_generation`
- `TestMultiProductVariants::test_two_by_two_variant_matrix`
- `TestMultiProductVariants::test_variant_option_selection`
- `TestMultiProductBulkFill::test_bulk_fill_applies_sku`
- `TestMultiProductBulkFill::test_bulk_fill_applies_price`
- `TestMultiProductSession::test_page_refresh_preserves_step`
- `TestMultiProductRobustness::test_double_click_next_button`
- `TestMultiProductRobustness::test_rapid_field_changes`
- `TestMultiProductRobustness::test_concurrent_field_edits`
- `TestMultiProductConcurrent::test_state_preserved_after_error`
- `TestMultiProductConcurrent::test_multiple_submissions_prevented`
- `TestMultiProductVariantSKU::test_sku_with_spaces`
- `TestMultiProductVariantSKU::test_sku_with_special_chars`
- `TestMultiProductVariantSKU::test_sku_xss_injection`
- `TestMultiProductVariantSKU::test_sku_duplicate_across_variants`
- `TestMultiProductVariantMatrix::test_three_by_three_matrix`
- `TestMultiProductVariantMatrix::test_single_variant_single_option`
- `TestMultiProductVariantMatrix::test_asymmetric_two_by_one`
- `TestMultiProductModel::test_model_combobox_visible`
- `TestMultiProductModel::test_model_search_functionality`
- `TestMultiProductSubmit::test_submit_without_prices`
- `TestMultiProductSubmit::test_submit_with_partial_grid`
- `TestMultiProductGridPriceDiscount::test_discount_greater_than_price`
- `TestMultiProductGridPriceDiscount::test_negative_price_in_grid`

**Root Cause:**
Fixture setup timeout or navigation failure.

---

### ERR-002: `tests/multiproduct/test_multiproduct_security.py` (13 tests)

**Affected Tests:**
- `TestMultiProductAdvancedSecurity::test_null_byte_injection`
- `TestMultiProductAdvancedSecurity::test_ldap_injection`
- `TestMultiProductAdvancedSecurity::test_command_injection`
- `TestMultiProductAdvancedSecurity::test_path_traversal`
- `TestMultiProductDescriptionInjection::test_xss_in_uz_description`
- `TestMultiProductDescriptionInjection::test_xss_in_ru_description`
- `TestMultiProductDescriptionInjection::test_sql_in_uz_description`
- `TestMultiProductDescriptionInjection::test_html_in_description`
- `TestMultiProductXSS::test_xss_in_uz_name`
- `TestMultiProductXSS::test_xss_in_ru_name`
- `TestMultiProductXSS::test_xss_in_description`
- `TestMultiProductXSS::test_javascript_uri_in_name`
- `TestMultiProductSQL::test_sql_injection_in_name`

**Root Cause:**
Fixture setup timeout or navigation failure.

---

### ERR-003: `tests/multiproduct/test_multiproduct_ui.py` (21 tests)

**Affected Tests:**
- `TestMultiProductUIStep1::test_category_combobox_visible`
- `TestMultiProductUIStep1::test_ikpu_combobox_visible`
- `TestMultiProductUIStep1::test_country_combobox_visible`
- `TestMultiProductUIStep1::test_brand_combobox_visible`
- `TestMultiProductUIStep1::test_uz_name_textbox_visible`
- `TestMultiProductUIStep1::test_uz_description_textbox_visible`
- `TestMultiProductUIStep1::test_ru_name_textbox_visible`
- `TestMultiProductUIStep1::test_ru_description_textbox_visible`
- `TestMultiProductUIStep1::test_combobox_count_step1`
- `TestMultiProductUIStep1::test_textbox_count_step1`
- `TestMultiProductUIStep2::test_on_step2`
- `TestMultiProductUIStep2::test_characteristics_section_visible`
- `TestMultiProductUIStep2::test_numeric_fields_present`
- `TestMultiProductUIStep3::test_on_step3`
- `TestMultiProductUIStep3::test_variant_comboboxes_visible`
- `TestMultiProductUIStep3::test_next_button_initially_disabled`
- `TestMultiProductAccessibility::test_keyboard_navigation_step1`
- `TestMultiProductAccessibility::test_escape_closes_dropdown`
- `TestMultiProductAccessibility::test_focus_visible_on_inputs`
- `TestMultiProductValidationUX::test_error_cleared_on_valid_input`
- `TestMultiProductValidationUX::test_inline_validation_on_blur`

**Root Cause:**
```
raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
```

<details>
<summary>Full Traceback</summary>

```python
[gw3] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/multiproduct/conftest.py:64: in multi_step1
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
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:34:59 - pages.base_page - INFO - click_add_products_link:61 - Clicking Add Products link
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:multiproduct_page.py:61 Clicking Add Products link
```
</details>

---

### ERR-004: `tests/multiproduct/test_multiproduct_validation.py` (34 tests)

**Affected Tests:**
- `TestMultiProductWhitespace::test_trailing_spaces_trimmed`
- `TestMultiProductWhitespace::test_only_spaces_rejected`
- `TestMultiProductWhitespace::test_tabs_in_name`
- `TestMultiProductWhitespace::test_newlines_in_single_line`
- `TestMultiProductInvalidFormat::test_special_chars_in_name`
- `TestMultiProductInvalidFormat::test_emoji_in_name`
- `TestMultiProductInvalidFormat::test_html_tags_in_name`
- `TestMultiProductInvalidFormat::test_mixed_cyrillic_latin`
- `TestMultiProductInvalidFormat::test_numbers_only_name`
- `TestMultiProductPriceValidation::test_discount_greater_than_price_error`
- `TestMultiProductPriceValidation::test_negative_price_rejected`
- `TestMultiProductPriceValidation::test_alpha_price_rejected`
- `TestMultiProductDescriptionLength::test_uz_description_under_50_chars`
- `TestMultiProductDescriptionLength::test_ru_description_under_50_chars`
- `TestMultiProductDescriptionLength::test_description_exactly_50_chars`
- `TestMultiProductCharacteristics::test_screen_size_zero`
- `TestMultiProductCharacteristics::test_screen_size_negative`
- `TestMultiProductCharacteristics::test_battery_extreme_value`
- `TestMultiProductCharacteristics::test_numeric_field_alpha_input`
- `TestMultiProductBarcodeValidation::test_barcode_alpha_chars`
- `TestMultiProductBarcodeValidation::test_barcode_too_short`
- `TestMultiProductBarcodeValidation::test_barcode_valid_ean13`
- `TestMultiProductEmptyCountry::test_submit_without_country`
- `TestMultiProductEmptyFields::test_empty_uz_name_shows_error`
- `TestMultiProductEmptyFields::test_empty_ru_name_shows_error`
- `TestMultiProductEmptyFields::test_empty_category_shows_error`
- `TestMultiProductEmptyFields::test_empty_ikpu_shows_error`
- `TestMultiProductBoundary::test_uz_name_min_length`
- `TestMultiProductBoundary::test_uz_name_max_length`
- `TestMultiProductBoundary::test_uz_name_over_max_length`
- `TestMultiProductBoundary::test_sku_min_length`
- `TestMultiProductBoundary::test_sku_max_length`
- `TestMultiProductBoundary::test_price_zero_value`
- `TestMultiProductBoundary::test_barcode_exact_length`

**Root Cause:**
Fixture setup timeout or navigation failure.

---

## Product Create (71 errors)

### ERR-005: `tests/product_create/test_product_create_functional.py` (27 tests)

**Affected Tests:**
- `TestProductCreateNavigation::test_browser_back_button`
- `TestProductCreateSession::test_session_persists_during_wizard`
- `TestProductCreateSession::test_data_after_refresh`
- `TestProductCreateRobustness::test_double_click_next`
- `TestProductCreateNavigation::test_back_button_from_step2`
- `TestProductCreateRobustness::test_rapid_field_changes`
- `TestProductCreateNavigation::test_data_persists_after_back`
- `TestProductCreateRobustness::test_form_state_after_error`
- `TestProductCreateAccessibility::test_focus_states`
- `TestProductCreateAccessibility::test_keyboard_navigation`
- `TestProductCreateAccessibility::test_accessible_error_messages`
- `TestProductCreateValidationUX::test_clear_error_messages`
- `TestProductCreateValidationUX::test_validation_on_blur`
- `TestProductCreateValidationUX::test_error_visual_state`
- `TestProductCreateAdvancedInput::test_copy_paste_product_name`
- `TestProductCreateAdvancedInput::test_input_methods`
- `TestProductCreateAdvancedInput::test_autocomplete_attributes`
- `TestProductCreateConcurrent::test_state_after_validation_error`
- `TestProductCreateConcurrent::test_idle_timeout_handling`
- `TestProductCreateFunctional::test_change_category`
- `TestProductCreateFunctional::test_brand_search_selection`
- `TestProductCreateFunctional::test_ikpu_partial_search`
- `TestProductCreateFunctional::test_country_list_loads`
- `TestProductCreateFunctional::test_edit_filled_fields`
- `TestProductCreateFunctional::test_description_character_counter`
- `TestProductCreateSubmit::test_submit_without_image`
- `TestProductCreateSubmit::test_full_submit_flow`

**Root Cause:**
```
E   playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 10000ms exceeded.
2026-02-16 09:32:18 - pages.base_page - ERROR - click_add_product_btn_staging:76 - Failed to click add product button: Locator.wait_for: Timeout 10000ms exceeded.
ERROR    pages.base_page:productcreate_page.py:76 Failed to click add product button: Locator.wait_for: Timeout 10000ms exceeded.
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/conftest.py:102: in product_create_page
    product_page.click_add_product_btn_staging()
pages/productcreate_page.py:72: in click_add_product_btn_staging
    add_btn.wait_for(state="visible", timeout=10000)
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
E   playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 10000ms exceeded.
E   Call log:
E     - waiting for locator("a[href*='/products/add'], a:has-text('Add Products'), a:has-text('Tovar qo\\'shish'), a:has-text('Добавить товар')").first to be visible
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:08 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test
2026-02-16 09:32:08 - conftest - WARNING - test_data:498 - No test data found for module: product_create_functional
2026-02-16 09:32:08 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:08 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:08 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:18 - pages.base_page - ERROR - click_add_product_btn_staging:76 - Failed to click add product button: Locator.wait_for: Timeout 10000ms exceeded.
Call log:
  - waiting for locator("a[href*='/products/add'], a:has-text('Add Products'), a:has-text('Tovar qo\\'shish'), a:has-text('Добавить товар')").first to be visible

------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_functional
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
ERROR    pages.base_page:productcreate_page.py:76 Failed to click add product button: Locator.wait_for: Timeout 10000ms exceeded.
Call log:
  - waiting for locator("a[href*='/products/add'], a:has-text('Add Products'), a:has-text('Tovar qo\\'shish'), a:has-text('Добавить товар')").first to be visible
```
</details>

---

### ERR-006: `tests/product_create/test_product_create_security.py` (22 tests)

**Affected Tests:**
- `TestProductCreateSlugSku::test_sku_with_spaces`
- `TestProductCreateSlugSku::test_sku_special_characters`
- `TestProductCreateSlugSku::test_sku_over_max_length`
- `TestProductCreateSlugSku::test_sku_cyrillic`
- `TestProductCreateSlugSku::test_sku_xss_injection`
- `TestProductCreateFileUpload::test_valid_image_upload`
- `TestProductCreateFileUpload::test_large_file_rejected`
- `TestProductCreateFileUpload::test_empty_file_rejected`
- `TestProductCreateFileUpload::test_wrong_format_rejected`
- `TestProductCreateFileUpload::test_renamed_extension_rejected`
- `TestProductCreateAdvancedFileUpload::test_svg_xss_upload`
- `TestProductCreateAdvancedFileUpload::test_double_extension_upload`
- `TestProductCreateAdvancedFileUpload::test_corrupted_image_upload`
- `TestProductCreateAdvancedFileUpload::test_replace_uploaded_file`
- `TestProductCreateXSS::test_xss_in_product_name`
- `TestProductCreateXSS::test_xss_in_description`
- `TestProductCreateXSS::test_svg_xss_in_name`
- `TestProductCreateXSS::test_javascript_uri`
- `TestProductCreateSQL::test_sql_in_product_name`
- `TestProductCreateSQL::test_sql_in_sku`
- `TestProductCreateSQL::test_union_select_injection`
- `TestProductCreateAdvancedSecurity::test_null_byte_injection`

**Root Cause:**
```
2026-02-16 09:32:40 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/conftest.py:116: in product_on_step2
    product_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:32:38 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_d
2026-02-16 09:32:38 - conftest - WARNING - test_data:498 - No test data found for module: product_create_security
2026-02-16 09:32:38 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:38 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:32:38 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:32:38 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:32:39 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:32:40 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:32:40 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:32:40 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:32:40 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:40 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:32:40 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:32:40 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:32:40 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Erkaklar uchun' not found. Available: ['... Назад к "Kiyim"']
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
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

### ERR-007: `tests/product_create/test_product_create_ui.py` (6 tests)

**Affected Tests:**
- `TestProductCreateUIStep2::test_sku_field_visible`
- `TestProductCreateUIStep2::test_barcode_field_visible`
- `TestProductCreateUIStep2::test_price_field_visible`
- `TestProductCreateUIStep2::test_discount_price_field_visible`
- `TestProductCreateUIStep2::test_dimension_fields_visible`
- `TestProductCreateUIStep2::test_weight_field_visible`

**Root Cause:**
```
2026-02-16 09:33:47 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
```

<details>
<summary>Full Traceback</summary>

```python
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/conftest.py:116: in product_on_step2
    product_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:45 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_ui_test_data.js
2026-02-16 09:33:45 - conftest - WARNING - test_data:498 - No test data found for module: product_create_ui
2026-02-16 09:33:45 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:45 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:45 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:45 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:46 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:47 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:33:47 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:47 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:47 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:47 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:47 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:47 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:33:47 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_ui
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
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

### ERR-008: `tests/product_create/test_product_create_validation.py` (16 tests)

**Affected Tests:**
- `TestProductCreateInvalidFormat::test_non_numeric_price`
- `TestProductCreatePriceDiscount::test_discount_equal_to_price`
- `TestProductCreatePriceDiscount::test_price_overflow`
- `TestProductCreateEmptyFields::test_empty_sku_error`
- `TestProductCreateEmptyFields::test_empty_price_error`
- `TestProductCreateBarcode::test_barcode_alpha_characters`
- `TestProductCreateBarcode::test_barcode_too_short`
- `TestProductCreateBarcode::test_barcode_too_long`
- `TestProductCreateBoundary::test_sku_special_chars`
- `TestProductCreateBarcode::test_barcode_special_chars`
- `TestProductCreateBoundary::test_price_negative`
- `TestProductCreateDimensions::test_negative_dimensions`
- `TestProductCreateDimensions::test_non_numeric_dimensions`
- `TestProductCreateDimensions::test_dimension_overflow`
- `TestProductCreateDimensions::test_zero_weight`
- `TestProductCreateDimensions::test_decimal_weight`

**Root Cause:**
```
2026-02-16 09:33:21 - pages.base_page - ERROR - fill_variant_fields_staging:448 - Failed to fill variant fields: Locator.wait_for: Timeout 10000ms exceeded.
WARNING  pages.base_page:productcreate_page.py:330 URL unchanged - checking for validation errors
ERROR    pages.base_page:productcreate_page.py:448 Failed to fill variant fields: Locator.wait_for: Timeout 10000ms exceeded.
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_create/conftest.py:116: in product_on_step2
    product_page.select_category_from_combobox(data["category_path"])
pages/productcreate_page.py:158: in select_category_from_combobox
    raise Exception(f"'{name}' not found. Available: {available}")
E   Exception: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:33:17 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test
2026-02-16 09:33:17 - conftest - WARNING - test_data:498 - No test data found for module: product_create_validation
2026-02-16 09:33:17 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:17 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:33:17 - pages.base_page - INFO - click_add_product_btn_staging:62 - Clicking 'Add Products' button (staging)
2026-02-16 09:33:17 - pages.base_page - INFO - click_add_product_btn_staging:74 - ✓ 'Add Products' button clicked
2026-02-16 09:33:18 - pages.base_page - INFO - click_single_product_option:81 - Clicking single product option
2026-02-16 09:33:19 - pages.base_page - INFO - click_single_product_option:88 - ✓ Single product option selected
2026-02-16 09:33:19 - pages.base_page - INFO - select_category_from_combobox:107 - Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
2026-02-16 09:33:19 - pages.base_page - INFO - select_category_from_combobox:123 - ✓ Dropdown opened
2026-02-16 09:33:19 - pages.base_page - INFO - select_category_from_combobox:132 - ✓ Back to parent
2026-02-16 09:33:19 - pages.base_page - INFO - select_category_from_combobox:135 - ✓ At root level
2026-02-16 09:33:19 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Kiyim'
2026-02-16 09:33:19 - pages.base_page - INFO - select_category_from_combobox:170 - ✓ Expanded 'Erkaklar uchun'
2026-02-16 09:33:19 - pages.base_page - ERROR - select_category_from_combobox:179 - Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/product_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: product_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:productcreate_page.py:62 Clicking 'Add Products' button (staging)
INFO     pages.base_page:productcreate_page.py:74 ✓ 'Add Products' button clicked
INFO     pages.base_page:productcreate_page.py:81 Clicking single product option
INFO     pages.base_page:productcreate_page.py:88 ✓ Single product option selected
INFO     pages.base_page:productcreate_page.py:107 Selecting category path: Kiyim → Erkaklar uchun → Ustki kiyim
INFO     pages.base_page:productcreate_page.py:123 ✓ Dropdown opened
INFO     pages.base_page:productcreate_page.py:132 ✓ Back to parent
INFO     pages.base_page:productcreate_page.py:135 ✓ At root level
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Kiyim'
INFO     pages.base_page:productcreate_page.py:170 ✓ Expanded 'Erkaklar uchun'
ERROR    pages.base_page:productcreate_page.py:179 Category selection failed: 'Ustki kiyim' not found. Available: ['... Назад к "Erkaklar uchun"']
_ ERROR at setup of TestProductCreateAdvancedFileUpload.test_corrupted_image_upload _
[gw0] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
... (92 more lines)
```
</details>

---

## Product Detail (62 errors)

### ERR-009: `tests/product_detail/test_product_detail_functional.py` (18 tests)

**Affected Tests:**
- `TestProductDetailEdit::test_fields_are_editable`
- `TestProductDetailEdit::test_edit_uz_name`
- `TestProductDetailEdit::test_edit_ru_name`
- `TestProductDetailEdit::test_edit_price`
- `TestProductDetailEdit::test_cancel_discards_changes`
- `TestProductDetailEdit::test_save_button_state`
- `TestProductDetailDelete::test_delete_button_visible`
- `TestProductDetailDelete::test_delete_shows_confirmation`
- `TestProductDetailDelete::test_cancel_delete_keeps_product`
- `TestProductDetailSession::test_page_accessible_after_login`
- `TestProductDetailSecurity::test_xss_in_name`
- `TestProductDetailSecurity::test_xss_event_handler_in_name`
- `TestProductDetailSecurity::test_sql_injection_in_name`
- `TestProductDetailSecurity::test_html_injection_in_description`
- `TestProductDetailAdvancedSecurity::test_null_bytes_in_name`
- `TestProductDetailAdvancedSecurity::test_path_traversal_in_name`
- `TestProductDetailAdvancedSecurity::test_command_injection_in_name`
- `TestProductDetailAdvancedSecurity::test_ldap_injection_in_name`

**Root Cause:**
```
E   AssertionError: PRECONDITION: No product rows found in products list
```

<details>
<summary>Full Traceback</summary>

```python
[gw1] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/product_detail/conftest.py:113: in detail_page
    assert len(rows) > 0, "PRECONDITION: No product rows found in products list"
E   AssertionError: PRECONDITION: No product rows found in products list
E   assert 0 > 0
E    +  where 0 = len([])
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:35:49 - pages.base_page - INFO - select_shop:37 - Selecting shop: Zara
2026-02-16 09:35:49 - pages.base_page - INFO - select_shop:50 - Shop 'Zara' selected
------------------------------ Captured log setup ------------------------------
INFO     pages.base_page:product_detail_page.py:37 Selecting shop: Zara
INFO     pages.base_page:product_detail_page.py:50 Shop 'Zara' selected
```
</details>

---

### ERR-010: `tests/product_detail/test_product_detail_ui.py` (16 tests)

**Affected Tests:**
- `TestProductDetailAccessibility::test_focus_visible_on_fields`
- `TestProductDetailAccessibility::test_keyboard_tab_navigation`
- `TestProductDetailAccessibility::test_escape_closes_dialogs`
- `TestProductDetailRobustness::test_double_click_save`
- `TestProductDetailRobustness::test_rapid_field_changes`
- `TestProductDetailRobustness::test_page_refresh_preserves_url`
- `TestProductDetailValidationUX::test_error_messages_visible`
- `TestProductDetailValidationUX::test_error_clears_on_valid_input`
- `TestProductDetailValidationUX::test_toast_on_save`
- `TestProductDetailUI::test_page_loads`
- `TestProductDetailUI::test_product_name_displayed`
- `TestProductDetailUI::test_product_has_data`
- `TestProductDetailUI::test_textbox_fields_present`
- `TestProductDetailUI::test_action_buttons_present`
- `TestProductDetailUI::test_page_url_contains_product_id`
- `TestProductDetailUI::test_back_navigation_available`

**Root Cause:**
Fixture setup timeout or navigation failure.

---

### ERR-011: `tests/product_detail/test_product_detail_validation.py` (28 tests)

**Affected Tests:**
- `TestProductDetailEmptyFields::test_empty_uz_name_shows_error`
- `TestProductDetailEmptyFields::test_empty_ru_name_shows_error`
- `TestProductDetailEmptyFields::test_empty_price_shows_error`
- `TestProductDetailEmptyFields::test_all_fields_empty_shows_errors`
- `TestProductDetailBoundary::test_name_one_char`
- `TestProductDetailBoundary::test_name_max_255`
- `TestProductDetailBoundary::test_name_over_256`
- `TestProductDetailBoundary::test_description_under_50`
- `TestProductDetailBoundary::test_price_zero`
- `TestProductDetailBoundary::test_price_negative`
- `TestProductDetailBoundary::test_price_alpha_input`
- `TestProductDetailWhitespace::test_name_only_spaces`
- `TestProductDetailWhitespace::test_name_tabs`
- `TestProductDetailWhitespace::test_name_leading_trailing_spaces`
- `TestProductDetailWhitespace::test_name_newlines`
- `TestProductDetailWhitespace::test_name_nbsp`
- `TestProductDetailPriceDiscount::test_discount_greater_than_price`
- `TestProductDetailPriceDiscount::test_discount_equal_to_price`
- `TestProductDetailPriceDiscount::test_discount_negative`
- `TestProductDetailSkuBarcode::test_sku_special_chars`
- `TestProductDetailSkuBarcode::test_sku_with_spaces`
- `TestProductDetailSkuBarcode::test_barcode_alpha`
- `TestProductDetailSkuBarcode::test_barcode_too_short`
- `TestProductDetailSkuBarcode::test_sku_xss`
- `TestProductDetailInvalidFormat::test_emoji_in_name`
- `TestProductDetailInvalidFormat::test_mixed_cyrillic_latin`
- `TestProductDetailInvalidFormat::test_only_digits_in_name`
- `TestProductDetailInvalidFormat::test_special_chars_in_name`

**Root Cause:**
Fixture setup timeout or navigation failure.

---

## Shop Create (56 errors)

### ERR-012: `tests/shop_create/test_shop_create_e2e.py` (4 tests)

**Affected Tests:**
- `TestShopCreateRobustness::test_submit_during_upload`
- `TestShopCreateConcurrent::test_form_state_after_error`
- `TestShopCreateConcurrent::test_modal_new_tab`
- `TestShopCreateConcurrent::test_long_idle_before_submit`

**Root Cause:**
```
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
    assert "dashboard" in page.url.lower(), \
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x1083b32d0>()
E    +    where <built-in method lower of str object at 0x1083b32d0> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:41:56 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
2026-02-16 09:41:56 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_e2e
2026-02-16 09:41:56 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:41:56 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_e2e_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_e2e
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
```
</details>

---

### ERR-013: `tests/shop_create/test_shop_create_files.py` (9 tests)

**Affected Tests:**
- `TestShopCreateFileUpload::test_upload_large_file`
- `TestShopCreateFileUpload::test_upload_wrong_format_txt`
- `TestShopCreateFileUpload::test_upload_empty_file`
- `TestShopCreateFileUpload::test_upload_fake_extension`
- `TestShopCreateFileUpload::test_submit_without_files`
- `TestShopCreateAdvancedFileUpload::test_upload_svg_xss`
- `TestShopCreateAdvancedFileUpload::test_upload_double_extension`
- `TestShopCreateAdvancedFileUpload::test_upload_corrupted_image`
- `TestShopCreateAdvancedFileUpload::test_replace_uploaded_file`

**Root Cause:**
```
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
    assert "dashboard" in page.url.lower(), \
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x10840b270>()
E    +    where <built-in method lower of str object at 0x10840b270> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:00 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_files_test_data.js
2026-02-16 09:42:00 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_files
2026-02-16 09:42:00 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:00 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_files_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_files
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
```
</details>

---

### ERR-014: `tests/shop_create/test_shop_create_functional.py` (4 tests)

**Affected Tests:**
- `TestShopCreateFunctional::test_fill_all_required_fields`
- `TestShopCreateFunctional::test_logo_upload`
- `TestShopCreateFunctional::test_banner_upload`
- `TestShopCreateFunctional::test_cancel_discards_changes`

**Root Cause:**
```
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
    assert "dashboard" in page.url.lower(), \
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x108af16f0>()
E    +    where <built-in method lower of str object at 0x108af16f0> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:09 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_functional_test_da
2026-02-16 09:42:09 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_functional
2026-02-16 09:42:09 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:10 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_functional_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_functional
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
```
</details>

---

### ERR-015: `tests/shop_create/test_shop_create_security.py` (9 tests)

**Affected Tests:**
- `TestShopCreateSecurity::test_path_traversal_awareness`
- `TestShopCreateAdvancedSecurity::test_html_injection_shop_name`
- `TestShopCreateAdvancedSecurity::test_null_byte_injection`
- `TestShopCreateAdvancedSecurity::test_ldap_injection`
- `TestShopCreateAdvancedSecurity::test_command_injection`
- `TestShopCreateAdvancedSecurity::test_path_traversal_description`
- `TestShopCreateDescriptionInjection::test_xss_in_description_uz`
- `TestShopCreateDescriptionInjection::test_xss_in_description_ru`
- `TestShopCreateDescriptionInjection::test_sql_injection_description`

**Root Cause:**
```
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
    assert "dashboard" in page.url.lower(), \
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x108213f30>()
E    +    where <built-in method lower of str object at 0x108213f30> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:13 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data
2026-02-16 09:42:13 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_security
2026-02-16 09:42:13 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:13 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
_ ERROR at setup of TestShopCreateAdvancedSecurity.test_html_injection_shop_name _
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
    assert "dashboard" in page.url.lower(), \
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x1085a6690>()
E    +    where <built-in method lower of str object at 0x1085a6690> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:14 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data
2026-02-16 09:42:14 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_security
2026-02-16 09:42:14 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:14 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_security_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_security
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
__ ERROR at setup of TestShopCreateAdvancedSecurity.test_null_byte_injection ___
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
... (16 more lines)
```
</details>

---

### ERR-016: `tests/shop_create/test_shop_create_ui.py` (17 tests)

**Affected Tests:**
- `TestShopCreateUI::test_modal_opens`
- `TestShopCreateUI::test_shop_name_field_visible`
- `TestShopCreateUI::test_slug_field_visible`
- `TestShopCreateUI::test_sku_field_visible`
- `TestShopCreateUI::test_description_uz_field_visible`
- `TestShopCreateUI::test_description_ru_field_visible`
- `TestShopCreateUI::test_save_button_visible`
- `TestShopCreateUI::test_file_inputs_exist`
- `TestShopCreateUI::test_slug_auto_generation`
- `TestShopCreateUI::test_sku_auto_generation`
- `TestShopCreateUI::test_modal_can_close`
- `TestShopCreateAccessibility::test_focus_states`
- `TestShopCreateAccessibility::test_aria_attributes`
- `TestShopCreateAccessibility::test_keyboard_navigation`
- `TestShopCreateValidationUX::test_realtime_validation`
- `TestShopCreateValidationUX::test_validation_on_blur`
- `TestShopCreateValidationUX::test_error_messages_localized`

**Root Cause:**
```
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
    assert "dashboard" in page.url.lower(), \
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x10825ec30>()
E    +    where <built-in method lower of str object at 0x10825ec30> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:21 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_ui_test_data.json
2026-02-16 09:42:21 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_ui
2026-02-16 09:42:21 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:22 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_ui_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_ui
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
```
</details>

---

### ERR-017: `tests/shop_create/test_shop_create_validation.py` (13 tests)

**Affected Tests:**
- `TestShopCreateEmptyFields::test_submit_all_empty`
- `TestShopCreateEmptyFields::test_submit_only_name`
- `TestShopCreateEmptyFields::test_submit_without_description_uz`
- `TestShopCreateEmptyFields::test_submit_without_description_ru`
- `TestShopCreateEmptyFields::test_clear_shop_name_after_fill`
- `TestShopCreateInvalidFormat::test_shop_name_only_spaces`
- `TestShopCreateInvalidFormat::test_shop_name_special_chars_only`
- `TestShopCreateInvalidFormat::test_shop_name_too_short`
- `TestShopCreateInvalidFormat::test_description_only_numbers`
- `TestShopCreateInvalidFormat::test_shop_name_html_tags`
- `TestShopCreateInvalidFormat::test_shop_name_unicode_emoji`
- `TestShopCreateInvalidFormat::test_shop_name_mixed_script`
- `TestShopCreateInvalidFormat::test_description_tabs_newlines`

**Root Cause:**
```
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
```

<details>
<summary>Full Traceback</summary>

```python
[gw5] darwin -- Python 3.9.6 /Applications/Xcode.app/Contents/Developer/usr/bin/python3
tests/shop_create/conftest.py:26: in dashboard_page
    assert "dashboard" in page.url.lower(), \
E   AssertionError: FAILED: Expected dashboard URL, got https://staging-seller.greatmall.uz/auth/login
E   assert 'dashboard' in 'https://staging-seller.greatmall.uz/auth/login'
E    +  where 'https://staging-seller.greatmall.uz/auth/login' = <built-in method lower of str object at 0x108dc84b0>()
E    +    where <built-in method lower of str object at 0x108dc84b0> = 'https://staging-seller.greatmall.uz/auth/login'.lower
E    +      where 'https://staging-seller.greatmall.uz/auth/login' = <Page url='https://staging-seller.greatmall.uz/auth/login'>.url
---------------------------- Captured stdout setup -----------------------------
2026-02-16 09:42:37 - utils.test_data_loader - ERROR - load:56 - Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_validation_test_da
2026-02-16 09:42:37 - conftest - WARNING - test_data:498 - No test data found for module: shop_create_validation
2026-02-16 09:42:37 - pages.base_page - INFO - navigate_to:83 - Navigating to: https://staging-seller.greatmall.uz/dashboard
2026-02-16 09:42:37 - pages.base_page - INFO - navigate_to:87 - Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
------------------------------ Captured log setup ------------------------------
ERROR    utils.test_data_loader:test_data_loader.py:56 Test data file not found: /Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation/test_data/shop_create_validation_test_data.json
WARNING  conftest:conftest.py:498 No test data found for module: shop_create_validation
INFO     pages.base_page:base_page.py:83 Navigating to: https://staging-seller.greatmall.uz/dashboard
INFO     pages.base_page:base_page.py:87 Successfully navigated to: https://staging-seller.greatmall.uz/dashboard
```
</details>

---
