# Bugs Report - 120 Failed Tests

Generated: 2026-02-06 (Updated)

## Summary
- **Total Failed**: 120
- **Most Affected**: Dashboard (46 bugs), Product Create (24 bugs), Returns (18 bugs), Multi Product (12 bugs)

### По приоритету:
| Приоритет | Количество | Описание |
|-----------|------------|----------|
| P0 (Critical) | 8 | Безопасность (auth bypass, injection) |
| P1 (High) | 25 | Валидация не работает |
| P2 (Medium) | 15 | UI видимость |
| P3 (Low) | 72 | Функционал, UX |

---

## Dashboard (46 bugs)

### UI (3)
- `test_verify_breadcrumb_navigation` - Breadcrumb not visible
- `test_verify_footer_section` - Footer not visible
- `test_verify_language_selector` - Language selector (RU/UZ) not visible

### Sidebar (2)
- `test_verify_sidebar_collapse_button` - Collapse button not working
- `test_verify_submenu_expansion` - Submenu doesn't expand

### Navigation (7)
- `test_navigate_to_products` - Products nav broken
- `test_navigate_to_orders` - Orders nav broken
- `test_navigate_to_returns` - Returns nav broken
- `test_navigate_to_invoices` - Invoices nav broken
- `test_navigate_to_finance` - Finance nav broken
- `test_navigate_to_analytics` - Analytics nav broken
- `test_browser_forward_button` - Forward button broken

### Widgets (4)
- `test_chart_displayed` - Chart not visible
- `test_date_range_selector` - Date selector broken
- `test_quick_actions_section` - Quick actions not visible
- `test_revenue_widget` - Revenue widget broken

### Search Input (8)
- `test_search_empty_submit` - Empty search fails
- `test_search_special_characters` - Special chars not handled
- `test_search_xss_injection` - XSS vulnerability
- `test_search_sql_injection` - SQL injection vulnerability
- `test_search_html_injection` - HTML injection vulnerability
- `test_search_null_bytes` - Null bytes not sanitized
- `test_search_max_length` - Max length not enforced
- `test_search_whitespace_only` - Whitespace not handled

### Security (2)
- `test_ldap_injection_search` - LDAP injection vulnerability
- `test_command_injection_search` - Command injection vulnerability

### Session (2)
- `test_logout_button_accessible` - Logout button not found
- `test_session_survives_navigation` - Session lost on navigation

### Date Range (2)
- `test_date_range_selector_exists` - Selector missing
- `test_date_range_interaction` - Interaction broken

### Language (2)
- `test_language_switch_persistence` - Language doesn't persist
- `test_language_switch_ui_update` - UI doesn't update on switch

### E2E (3)
- `test_widget_interaction_flow` - Widget flow broken
- `test_notification_to_action_flow` - Notification flow broken
- `test_search_and_navigate_flow` - Search+navigate broken

### Functional (4)
- `test_help_support_link` - Help link broken
- `test_language_switch` - Language switch broken
- `test_notification_panel_opens` - Notifications don't open
- `test_multiple_navigations` - Multiple nav fails

### Robustness (2)
- `test_double_click_nav_items` - Double-click breaks nav
- `test_rapid_widget_refresh` - Rapid refresh fails

### Advanced Input (3)
- `test_copy_paste_search` - Copy/paste broken
- `test_input_methods_search` - Input methods broken
- `test_keyboard_shortcuts` - Shortcuts not working

### Performance (1)
- `test_navigation_performance` - Slow navigation

---

## Login (5 bugs)

- `test_verify_login_with_invalid_credentials` - No error message for invalid login
- `test_complete_login_logout_flow` - Logout button not accessible
- `test_successful_login_after_failure` - No error feedback for wrong password
- `test_keyboard_only_navigation` - Keyboard navigation broken
- `test_autocomplete_attributes` - Autocomplete not configured

---

## Returns (18 bugs)

### API Sync (2)
- `test_returns_api_sync` - API sync broken
- `test_widgets_table_sync` - Widgets/table out of sync

### Actions (4)
- `test_api_approve_non_requested` - Approve non-requested fails
- `test_api_reject_non_requested` - Reject non-requested fails
- `test_approve_already_approved` - Re-approve fails
- `test_reject_already_rejected` - Re-reject fails

### Filters (3)
- `test_clear_filters` - Clear filters broken
- `test_filter_by_invalid_id` - Invalid ID filter fails
- `test_filter_by_product_name` - Product name filter broken

### Status Tabs (2)
- `test_active_tab_highlighted` - Active tab not highlighted
- `test_switch_status_tab` - Tab switch broken

### Security (3)
- `test_sql_injection_filter` - SQL injection vulnerability
- `test_xss_in_search` - XSS vulnerability
- `test_unauthorized_access` - Auth bypass possible

### Performance (2)
- `test_filter_performance` - Slow filters
- `test_large_dataset_load` - Slow with large data

### Other (2)
- `test_no_returns_state` - Empty state broken
- `test_export_empty_data` - Export empty fails
- `test_concurrent_actions` - Concurrent actions fail
- `test_returns_widgets_data_format` - Data format wrong

---

## Registration (5 bugs)

- `test_login_link_navigation` - Login link broken
- `test_interactive_otp_verification` - OTP verification broken
- `test_interactive_otp_resend` - OTP resend broken
- `test_html_injection_name` - HTML injection vulnerability
- `test_null_byte_injection` - Null byte vulnerability

---

## Orders (4 bugs)

- `test_order_search_invalid_id` - Invalid ID search fails
- `test_order_search_by_customer_name` - Customer search broken
- `test_pagination_state_after_detail_view` - Pagination state lost
- `test_empty_state_no_orders` - Empty state broken

---

## Employee (3 bugs)

- `test_staff_toolbar_elements` - Toolbar elements missing
- `test_search_by_name` - Staff search broken
- `test_delete_staff_member` - Delete staff fails

---

## Product Create (24 bugs)

### Security (5)
- `test_requires_authentication` - Страница доступна без авторизации
- `test_null_byte_injection` - Null byte (\x00) не санитизируется
- `test_javascript_uri` - JavaScript URI не блокируется
- `test_union_select_injection` - SQL UNION SELECT не блокируется

### Barcode Validation (4)
- `test_barcode_alpha_characters` - Принимает буквы (ABCDEF)
- `test_barcode_special_chars` - Принимает спецсимволы (123-456-789)
- `test_barcode_too_short` - Принимает 3 цифры (мин. 8)
- `test_barcode_too_long` - Принимает 30 символов (нет лимита)

### Dimensions/Weight Validation (4)
- `test_zero_width` - Zero width (0) принимается
- `test_negative_dimensions` - Negative (-100) принимается
- `test_zero_weight` - Zero weight (0) принимается
- `test_negative_weight` - Negative weight (-5) принимается

### Other Validation (2)
- `test_price_negative` - Negative price принимается
- `test_empty_product_names_error` - Пустые имена не показывают ошибку

### UI Visibility (5)
- `test_barcode_field_visible` - Barcode поле не видно
- `test_price_field_visible` - Price поле не видно
- `test_discount_price_field_visible` - Discount price не видно
- `test_dimension_fields_visible` - Dimensions не видны
- `test_weight_field_visible` - Weight поле не видно

### Functional (4)
- `test_ikpu_partial_search` - Частичный поиск не работает
- `test_country_list_loads` - Список стран не загружается
- `test_description_character_counter` - Счетчик символов не работает
- `test_submit_without_image` - Submit без изображения не блокируется
- `test_wrong_format_rejected` - Неправильный формат принимается

---

## Products List (1 bug)

- `test_unauthorized_access_redirect` - Auth redirect broken

---

## Multi Product (12 bugs)

### Security (1)
- `test_session_required_for_multi_create` - Страница доступна без авторизации

### Step 3 Not Working (4)
- `test_on_step3` - Step 3 не работает
- `test_variant_comboboxes_visible` - Variant comboboxes не видны
- `test_next_button_initially_disabled` - Next button состояние не определяется
- `test_create_multi_product_complete` - E2E создание не работает

### Validation (5)
- `test_empty_uz_name_shows_error` - Пустое UZ имя не показывает ошибку
- `test_empty_ru_name_shows_error` - Пустое RU имя не показывает ошибку
- `test_empty_ikpu_shows_error` - Пустой IKPU не показывает ошибку
- `test_uz_name_max_length` - Имя 255+ символов принимается
- `test_uz_name_over_max_length` - Имя 256+ символов принимается

### Other (2)
- `test_on_step2` - Step 2 не определяется правильно
- `test_sku_min_length` - SKU min length не проверяется

---

## Become Seller (1 bug)

- `test_requires_auth` - Auth check broken
