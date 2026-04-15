"""
Profile Settings page object for managing profile and settings.
Follows Page Object Model (POM) and SOLID principles.
"""

from playwright.sync_api import Page
from pages.base_page import BasePage, logger


class ProfileSettingsPage(BasePage):
    """
    Page Object Model for Profile Settings Page.
    Handles bank accounts, documents, VAT toggle, and moderation.
    """

    SETTINGS_PATH = "/dashboard/profile/settings"
    PROFILE_PATH = "/dashboard/profile"

    def __init__(self, page: Page):
        """Initialize profile settings page with locators."""
        super().__init__(page)

        # Navigation
        self.settings_nav_link = self.page.get_by_role("link", name="Настройки").or_(
            self.page.get_by_role("link", name="Settings")
        )
        self.profile_nav_link = self.page.get_by_role("link", name="Профиль").or_(
            self.page.get_by_role("link", name="Profile")
        )

        # Language toggle
        self.language_toggle = self.page.locator("[data-testid='language-toggle']").or_(
            self.page.get_by_role("button", name="RU")
        ).or_(self.page.get_by_role("button", name="UZ"))

        # Bank account section
        self.add_bank_btn = self.page.get_by_role("button", name="Добавить счёт").or_(
            self.page.get_by_role("button", name="Add Bank Account")
        ).or_(self.page.locator("[data-testid='add-bank']"))
        self.bank_account_input = self.page.get_by_label("Номер счёта").or_(
            self.page.get_by_label("Account Number")
        ).or_(self.page.get_by_placeholder("Номер счёта"))
        self.bank_name_input = self.page.get_by_label("Название банка").or_(
            self.page.get_by_label("Bank Name")
        )
        self.bank_table = self.page.locator("[data-testid='bank-accounts']").or_(
            self.page.locator("table")
        )
        self.delete_bank_btn = self.page.get_by_role("button", name="Удалить").or_(
            self.page.get_by_role("button", name="Delete")
        )

        # Document upload section
        self.upload_doc_btn = self.page.get_by_role("button", name="Загрузить").or_(
            self.page.get_by_role("button", name="Upload")
        )
        self.file_input = self.page.locator("input[type='file']")
        self.document_list = self.page.locator("[data-testid='documents']").or_(
            self.page.locator(".document-list")
        )
        self.delete_doc_btn = self.page.locator("[data-testid='delete-document']").or_(
            self.page.get_by_role("button", name="Удалить документ")
        )

        # VAT percentage field
        self.vat_input = self.page.get_by_label("НДС").or_(
            self.page.get_by_label("VAT")
        ).or_(self.page.locator("input[name='vat']")).or_(
            self.page.locator("input[name='vatRate']")
        )

        # Moderation section
        self.send_moderation_btn = self.page.get_by_role("button", name="Отправить на модерацию").or_(
            self.page.get_by_role("button", name="Send for Moderation")
        )
        self.moderation_status = self.page.locator("[data-testid='moderation-status']").or_(
            self.page.locator(".moderation-status")
        )

        # Confirmation modal
        self.confirm_modal = self.page.locator("[role='dialog']").or_(
            self.page.locator(".MuiDialog-root")
        )
        self.confirm_btn = self.page.get_by_role("button", name="Подтвердить").or_(
            self.page.get_by_role("button", name="Confirm")
        )
        self.cancel_btn = self.page.get_by_role("button", name="Отмена").or_(
            self.page.get_by_role("button", name="Cancel")
        )

        # Save button
        self.save_btn = self.page.get_by_role("button", name="Сохранить").or_(
            self.page.get_by_role("button", name="Save")
        )

        # Messages
        self.success_message = self.page.locator("[class*='success']").or_(
            self.page.locator(".MuiAlert-standardSuccess")
        )
        self.error_message = self.page.locator("[class*='error']").or_(
            self.page.locator(".MuiAlert-standardError")
        )

    def navigate_to_settings(self) -> None:
        """Navigate to settings page."""
        logger.info("Navigating to settings page...")
        self.navigate_to(self.SETTINGS_PATH)
        self.wait_for_page_load()
        logger.info("Settings page loaded")

    def navigate_to_profile(self) -> None:
        """Navigate to profile page."""
        logger.info("Navigating to profile page...")
        self.navigate_to(self.PROFILE_PATH)
        self.wait_for_page_load()
        logger.info("Profile page loaded")

    def click_settings_nav_link(self) -> None:
        """Click settings navigation link."""
        logger.info("Clicking settings navigation link...")
        self.settings_nav_link.click()
        self.wait_for_network_idle()
        logger.info("Navigated to settings page")

    def click_profile_nav_link(self) -> None:
        """Click profile navigation link."""
        logger.info("Clicking profile navigation link...")
        self.profile_nav_link.click()
        self.wait_for_network_idle()
        logger.info("Navigated to profile page")

    def toggle_language(self) -> None:
        """Toggle language setting."""
        logger.info("Toggling language...")
        if self.language_toggle.is_visible(timeout=2000):
            self.language_toggle.click()
            self.page.wait_for_load_state("domcontentloaded")
        logger.info("Language toggled")

    def click_add_bank_account(self) -> None:
        """Click add bank account button."""
        logger.info("Clicking add bank account...")
        if self.add_bank_btn.is_visible(timeout=2000):
            self.add_bank_btn.click()
            self.page.wait_for_load_state("domcontentloaded")
        logger.info("Add bank account form opened")

    def fill_bank_account(self, account_number: str, bank_name: str = None) -> None:
        """Fill bank account form."""
        logger.info(f"Filling bank account: {account_number}")
        if self.bank_account_input.is_visible(timeout=2000):
            self.bank_account_input.fill(account_number)
        if bank_name and self.bank_name_input.is_visible(timeout=2000):
            self.bank_name_input.fill(bank_name)
        logger.info("Bank account form filled")

    def delete_bank_account(self, index: int = 0) -> None:
        """Delete bank account at specified index."""
        logger.info(f"Deleting bank account at index {index}...")
        delete_btns = self.page.locator("[data-testid='delete-bank']").or_(
            self.page.locator("button:has-text('Удалить')")
        )
        if delete_btns.nth(index).is_visible(timeout=2000):
            delete_btns.nth(index).click()
            self.page.wait_for_load_state("domcontentloaded")
            if self.confirm_btn.is_visible(timeout=2000):
                self.confirm_btn.click()
            self.wait_for_network_idle()
        logger.info("Bank account deleted")

    def upload_document(self, file_path: str) -> None:
        """Upload document file."""
        logger.info(f"Uploading document: {file_path}")
        if self.file_input.count() > 0:
            self.file_input.set_input_files(file_path)
            self.wait_for_network_idle()
        logger.info("Document uploaded")

    def delete_document(self, index: int = 0) -> None:
        """Delete document at specified index."""
        logger.info(f"Deleting document at index {index}...")
        delete_btns = self.page.locator("[data-testid='delete-document']")
        if delete_btns.nth(index).is_visible(timeout=2000):
            delete_btns.nth(index).click()
            self.page.wait_for_load_state("domcontentloaded")
            if self.confirm_btn.is_visible(timeout=2000):
                self.confirm_btn.click()
            self.wait_for_network_idle()
        logger.info("Document deleted")

    def set_vat_percentage(self, percentage: str) -> None:
        """Set VAT percentage value."""
        logger.info(f"Setting VAT to {percentage}%...")
        if self.vat_input.is_visible(timeout=2000):
            self.vat_input.fill(percentage)
            self.page.wait_for_load_state("domcontentloaded")
        logger.info(f"VAT set to {percentage}%")

    def send_for_moderation(self) -> None:
        """Send profile for moderation."""
        logger.info("Sending for moderation...")
        if self.send_moderation_btn.is_visible(timeout=2000):
            self.send_moderation_btn.click()
            self.page.wait_for_load_state("domcontentloaded")
            if self.confirm_btn.is_visible(timeout=2000):
                self.confirm_btn.click()
            self.wait_for_network_idle()
        logger.info("Profile sent for moderation")

    def save_settings(self) -> None:
        """Save settings."""
        logger.info("Saving settings...")
        if self.save_btn.is_visible(timeout=2000):
            self.save_btn.click()
            self.wait_for_network_idle()
        logger.info("Settings saved")

    def is_success_message_visible(self) -> bool:
        """Check if success message is visible."""
        return self.success_message.is_visible(timeout=3000)

    def is_error_message_visible(self) -> bool:
        """Check if error message is visible."""
        return self.error_message.is_visible(timeout=2000)

    def is_validation_error_visible(self) -> bool:
        """Check if validation error is displayed."""
        validation = self.page.locator("[class*='error']").or_(
            self.page.locator(".MuiFormHelperText-root.Mui-error")
        ).or_(self.page.locator(":text('обязательное')"))
        return validation.is_visible(timeout=2000)

    def is_confirmation_modal_visible(self) -> bool:
        """Check if confirmation modal is visible."""
        return self.confirm_modal.is_visible(timeout=2000)

    def get_moderation_status(self) -> str:
        """Get current moderation status."""
        if self.moderation_status.is_visible(timeout=2000):
            return self.moderation_status.text_content() or ""
        return ""

    def is_profile_approved(self) -> bool:
        """Check if profile is approved."""
        status = self.get_moderation_status().lower()
        return "одобрен" in status or "approved" in status

    def is_profile_rejected(self) -> bool:
        """Check if profile is rejected."""
        status = self.get_moderation_status().lower()
        return "отклонен" in status or "rejected" in status

    def get_bank_accounts_count(self) -> int:
        """Get number of bank accounts."""
        rows = self.page.locator("[data-testid='bank-account-row']").or_(
            self.page.locator("tbody tr")
        )
        return rows.count()

    def get_documents_count(self) -> int:
        """Get number of uploaded documents."""
        docs = self.page.locator("[data-testid='document-item']").or_(
            self.page.locator(".document-item")
        )
        return docs.count()

    def get_vat_percentage(self) -> str:
        """Get current VAT percentage value."""
        if self.vat_input.is_visible(timeout=2000):
            return self.vat_input.input_value()
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
