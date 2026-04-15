"""
Employee page object for managing staff members (Staff).
Follows Page Object Model (POM) and SOLID principles.
"""

from playwright.sync_api import Page
from pages.base_page import BasePage, logger
from config.settings import settings


class EmployeePage(BasePage):
    """
    Page Object Model for Staff Management Page.
    Handles staff listing, filtering, adding, editing, and status management.
    """

    EMPLOYEE_PATH = "/dashboard/staff"
    CREATE_PATH = "/dashboard/staff/create"

    def __init__(self, page: Page):
        """Initialize employee page with locators."""
        super().__init__(page)

        # Navigation - actual UI uses "Staff" / "Сотрудники" / "Xodimlar"
        self.employee_nav_link = self.page.get_by_role("link", name="Staff").or_(
            self.page.get_by_role("link", name="Сотрудники")
        ).or_(self.page.get_by_role("link", name="Xodimlar"))

        # Search/Filter controls - UI uses searchbox role (multi-language)
        self.search_input = self.page.get_by_role("searchbox").or_(
            self.page.get_by_placeholder("Search")
        ).or_(self.page.get_by_placeholder("Поиск")).or_(
            self.page.get_by_placeholder("Qidirish")
        )

        # Toolbar buttons (multi-language: EN/RU)
        self.columns_btn = self.page.get_by_role("button", name="Columns").or_(
            self.page.get_by_role("button", name="Столбцы")
        ).or_(self.page.get_by_role("button", name="Ustunlar"))
        self.filters_btn = self.page.get_by_role("button", name="Filters").or_(
            self.page.get_by_role("button", name="Фильтры")
        ).or_(self.page.get_by_role("button", name="Filtrlar"))
        self.export_btn = self.page.get_by_role("button", name="Export").or_(
            self.page.get_by_role("button", name="Экспорт")
        ).or_(self.page.get_by_role("button", name="Eksport"))
        self.search_btn = self.page.get_by_role("button", name="Search").or_(
            self.page.get_by_role("button", name="Поиск")
        ).or_(self.page.get_by_role("button", name="Qidirish"))

        # Add Staff Member - it's a LINK, not a button! (multi-language)
        self.add_employee_btn = self.page.get_by_role("link", name="Add Staff Member").or_(
            self.page.get_by_role("link", name="Добавить сотрудника")
        ).or_(self.page.get_by_role("link", name="Xodim qo'shish")).or_(
            self.page.locator("a[href*='/staff/create']")
        )

        # Staff table - uses grid role
        self.employee_table = self.page.locator("[role='grid']").or_(
            self.page.locator("table")
        )
        # Grid uses row elements, not tbody tr
        self.table_rows = self.page.locator("[role='grid'] [role='row']").filter(
            has=self.page.locator("[role='gridcell']")
        )

        # Form fields for staff creation (multi-language: EN/RU/UZ)
        self.phone_input = self.page.get_by_role("textbox", name="Phone Number").or_(
            self.page.get_by_role("textbox", name="Номер телефона")
        ).or_(self.page.get_by_role("textbox", name="Telefon raqami")).or_(
            self.page.locator("input[name='phone']")
        ).or_(self.page.locator("input[name='phoneNumber']")).or_(
            self.page.locator("input[type='tel']")
        )
        self.role_select = self.page.get_by_role("combobox", name="Role").or_(
            self.page.get_by_role("combobox", name="Роль")
        ).or_(self.page.get_by_role("combobox", name="Rol"))
        # Shops combobox - use specific ID selector
        self.shops_select = self.page.locator("#mui-component-select-shopIds")

        # Action buttons
        self.add_staff_btn = self.page.get_by_role("button", name="Add Staff Member").or_(
            self.page.get_by_role("button", name="Добавить сотрудника")
        ).or_(self.page.get_by_role("button", name="Xodim qo'shish"))
        self.save_btn = self.page.get_by_role("button", name="Save").or_(
            self.page.get_by_role("button", name="Сохранить")
        )
        self.cancel_btn = self.page.get_by_role("button", name="Cancel").or_(
            self.page.get_by_role("button", name="Отмена")
        )

        # Messages - toast notifications
        self.success_message = self.page.locator("[class*='success']").or_(
            self.page.locator(".MuiAlert-standardSuccess")
        )
        self.error_message = self.page.locator("[class*='error']").or_(
            self.page.locator(".MuiAlert-standardError")
        )

    def navigate(self) -> None:
        """Navigate to staff page."""
        logger.info("Navigating to staff page...")
        self.navigate_to(self.EMPLOYEE_PATH)
        self.wait_for_page_load()
        logger.info("Staff page loaded")

    def ensure_on_page(self) -> None:
        """Navigate to staff list page only if not already there (no page refresh)."""
        current_url = self.page.url
        # If on create page, use browser back or breadcrumb link
        if self.CREATE_PATH in current_url:
            logger.info("On create page, going back to staff list...")
            # Try breadcrumb link first (real user behavior)
            staff_link = self.page.get_by_role("link", name="Staff List").or_(
                self.page.get_by_role("link", name="Staff")
            )
            if staff_link.first.is_visible(timeout=settings.SHORT_TIMEOUT):
                staff_link.first.click()
                self.page.wait_for_load_state("networkidle")
            else:
                # Use browser back button
                self.page.go_back()
                self.page.wait_for_load_state("networkidle")
        elif self.EMPLOYEE_PATH not in current_url:
            logger.info("Not on staff page, clicking nav link...")
            self.click_employee_nav_link()
        else:
            logger.info("Already on staff list page")

    def click_employee_nav_link(self) -> None:
        """Click staff navigation link from dashboard."""
        logger.info("Clicking staff navigation link...")
        if self.employee_nav_link.is_visible(timeout=settings.SHORT_TIMEOUT):
            self.employee_nav_link.click()
            self.page.wait_for_load_state("networkidle")
        else:
            logger.info("Nav link not visible, using direct navigation")
            self.navigate()
        logger.info("Navigated to staff page")

    def get_employee_count(self) -> int:
        """Get number of staff members in the list."""
        self.page.wait_for_load_state("domcontentloaded")
        count = self.table_rows.count()
        logger.info(f"Staff count: {count}")
        return count

    def search_employee(self, search_text: str) -> None:
        """Search for staff member by name."""
        logger.info(f"Searching for staff: {search_text}")
        # Click search button first to reveal searchbox
        if self.search_btn.is_visible(timeout=settings.SHORT_TIMEOUT):
            self.search_btn.click()
        if self.search_input.is_visible(timeout=settings.SHORT_TIMEOUT):
            self.search_input.fill(search_text)
            self.page.keyboard.press("Enter")
            self.page.wait_for_load_state("networkidle")
        logger.info(f"Search completed: {search_text}")

    def clear_search(self) -> None:
        """Clear search input."""
        logger.info("Clearing search...")
        if self.search_input.is_visible(timeout=settings.SHORT_TIMEOUT):
            self.search_input.clear()
            self.page.keyboard.press("Enter")
            self.page.wait_for_load_state("networkidle")
        logger.info("Search cleared")

    def click_add_employee(self) -> None:
        """Click Add Staff Member link."""
        logger.info("Clicking Add Staff Member link...")
        # Wait for page to be ready
        self.page.wait_for_load_state("networkidle")
        if self.add_employee_btn.is_visible(timeout=settings.MEDIUM_TIMEOUT):
            self.add_employee_btn.click()
            self.page.wait_for_load_state("networkidle")
            logger.info("Add Staff Member form opened")
        else:
            # Try scrolling to top and waiting
            self.page.evaluate("window.scrollTo(0, 0)")
            if self.add_employee_btn.is_visible(timeout=settings.SHORT_TIMEOUT):
                self.add_employee_btn.click()
                self.page.wait_for_load_state("networkidle")
                logger.info("Add Staff Member form opened after scroll")
            else:
                logger.warning("Add Staff Member link not found")

    def fill_staff_form(self, phone: str, role: str = None, shops: list = None) -> None:
        """Fill staff creation form with provided data (based on codegen recording)."""
        logger.info(f"Filling staff form: phone={phone}, role={role}, shops={shops}")

        # Fill phone number
        if phone:
            self.phone_input.click()
            self.phone_input.fill(phone)

        # Select role
        if role:
            self.role_select.click()
            self.page.get_by_role("option", name=role, exact=True).click()

        # Select shops (checkbox based selection)
        if shops:
            self.shops_select.click()
            self.page.wait_for_load_state("domcontentloaded")
            for shop in shops:
                shop_option = self.page.get_by_role("option", name=shop)
                checkbox = shop_option.get_by_role("checkbox")
                if checkbox.is_visible(timeout=settings.SHORT_TIMEOUT):
                    checkbox.check()
                else:
                    shop_option.click()
            # Close dropdown by pressing Escape
            self.page.keyboard.press("Escape")

        logger.info("Staff form filled")

    def submit_form(self) -> None:
        """Submit the staff form."""
        logger.info("Submitting form...")
        if self.add_staff_btn.is_visible(timeout=settings.SHORT_TIMEOUT):
            self.add_staff_btn.click()
        elif self.save_btn.is_visible(timeout=settings.SHORT_TIMEOUT):
            self.save_btn.click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Form submitted")

    def click_employee_row(self, index: int = 0) -> None:
        """Click on staff row to view/edit."""
        logger.info(f"Clicking staff row {index}...")
        row = self.table_rows.nth(index)
        if row.is_visible(timeout=settings.SHORT_TIMEOUT):
            row.click()
            self.page.wait_for_load_state("domcontentloaded")
        logger.info("Staff row clicked")

    def is_add_form_visible(self) -> bool:
        """Check if add staff form is visible."""
        return self.CREATE_PATH in self.page.url or \
               self.phone_input.is_visible(timeout=settings.SHORT_TIMEOUT)

    def is_success_message_visible(self) -> bool:
        """Check if success message is visible."""
        return self.success_message.is_visible(timeout=settings.MEDIUM_TIMEOUT)

    def is_error_message_visible(self) -> bool:
        """Check if error message is visible."""
        return self.error_message.is_visible(timeout=settings.SHORT_TIMEOUT)

    def is_empty_state_visible(self) -> bool:
        """Check if empty state message is visible."""
        # Actual UI shows "Данные отсутствуют" heading
        empty = self.page.get_by_role("heading", name="Данные отсутствуют").or_(
            self.page.get_by_role("img", name="Empty content")
        )
        return empty.first.is_visible(timeout=settings.SHORT_TIMEOUT)

    def is_validation_error_visible(self) -> bool:
        """Check if validation error is displayed."""
        validation = self.page.locator("[class*='error']").or_(
            self.page.locator(".MuiFormHelperText-root.Mui-error")
        )
        return validation.is_visible(timeout=settings.SHORT_TIMEOUT)

    def is_table_visible(self) -> bool:
        """Check if staff table/grid is visible."""
        return self.employee_table.is_visible(timeout=settings.MEDIUM_TIMEOUT)

    def get_table_columns(self) -> list:
        """Get list of table column headers."""
        headers = self.page.locator("[role='columnheader']")
        columns = []
        for i in range(headers.count()):
            text = headers.nth(i).text_content()
            if text and text.strip():
                columns.append(text.strip())
        return columns

    def click_delete_staff(self, index: int = 0) -> None:
        """Click delete button for staff member at given index."""
        logger.info(f"Clicking delete button for staff at index {index}...")
        row = self.table_rows.nth(index)
        delete_btn = row.get_by_label("Delete Staff Member")
        if delete_btn.is_visible(timeout=settings.SHORT_TIMEOUT):
            # First click shows tooltip, second click opens dialog
            delete_btn.click()
            # Check if dialog appeared, if not click again
            dialog = self.page.get_by_role("dialog", name="Confirmation")
            if not dialog.is_visible(timeout=settings.SHORT_TIMEOUT):
                delete_btn.click()
            logger.info("Delete button clicked, confirmation dialog should appear")
        else:
            logger.warning(f"Delete button not found for row {index}")

    def confirm_delete(self) -> None:
        """Confirm staff deletion in the confirmation dialog."""
        logger.info("Confirming staff deletion...")
        confirm_btn = self.page.get_by_role("button", name="Delete").or_(
            self.page.get_by_role("button", name="Удалить")
        ).or_(self.page.get_by_role("button", name="O'chirish"))
        if confirm_btn.is_visible(timeout=settings.MEDIUM_TIMEOUT):
            confirm_btn.click()
            self.page.wait_for_load_state("networkidle")
            # Reload page to get fresh data
            self.page.reload()
            self.page.wait_for_load_state("networkidle")
            logger.info("Staff deletion confirmed, page reloaded")
        else:
            logger.warning("Delete confirmation button not found")

    def cancel_delete(self) -> None:
        """Cancel staff deletion in the confirmation dialog."""
        logger.info("Cancelling staff deletion...")
        cancel_btn = self.page.get_by_role("button", name="Выйти").or_(
            self.page.get_by_role("button", name="Cancel")
        ).or_(self.page.get_by_role("button", name="Bekor qilish"))
        if cancel_btn.is_visible(timeout=settings.SHORT_TIMEOUT):
            cancel_btn.click()
            logger.info("Staff deletion cancelled")
        else:
            logger.warning("Cancel button not found")

    def delete_staff_member(self, index: int = 0, confirm: bool = True) -> None:
        """Delete staff member at given index with optional confirmation."""
        logger.info(f"Deleting staff member at index {index}, confirm={confirm}")
        self.click_delete_staff(index)
        if confirm:
            self.confirm_delete()
        else:
            self.cancel_delete()

    def is_delete_confirmation_visible(self) -> bool:
        """Check if delete confirmation dialog is visible."""
        dialog = self.page.get_by_role("dialog", name="Confirmation")
        return dialog.is_visible(timeout=settings.SHORT_TIMEOUT)

    def get_staff_name_at_index(self, index: int = 0) -> str:
        """Get staff member name at given index."""
        row = self.table_rows.nth(index)
        # Full Name is in the second gridcell (after checkbox)
        name_cell = row.locator("[role='gridcell']").nth(1)
        if name_cell.is_visible(timeout=settings.SHORT_TIMEOUT):
            return name_cell.text_content() or ""
        return ""

    # ==================== VALIDATION METHODS ====================

    def get_validation_error_count(self) -> int:
        """Get count of MUI validation errors on the page."""
        return self.page.locator(".MuiFormHelperText-root.Mui-error").count()

    def has_validation_errors(self) -> bool:
        """Check if there are any validation errors on the page."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """Get all validation error messages from the page."""
        errors = self.page.locator(".MuiFormHelperText-root.Mui-error").all()
        return [e.inner_text() for e in errors if e.is_visible()]

    def has_error_for_field(self, field_name: str) -> bool:
        """Check if a specific field has a validation error."""
        field = self.page.get_by_role("textbox", name=field_name)
        if field.count() > 0:
            parent = field.locator("xpath=ancestor::div[contains(@class,'MuiFormControl')]")
            if parent.count() > 0:
                error = parent.locator(".MuiFormHelperText-root.Mui-error")
                return error.count() > 0 and error.is_visible()
        return False
