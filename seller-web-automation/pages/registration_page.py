from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from utils import SmartWaits, setup_logger

logger = setup_logger(__name__)


class RegistrationPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/auth/registration"

    @property
    def first_name_field(self) -> Locator:
        """First name input field (language-independent)."""
        return self.page.locator("input[name='firstName']")

    @property
    def phone_field(self) -> Locator:
        """Phone number input field (language-independent)."""
        return self.page.locator("input[name='phoneNumber']")

    @property
    def email_field(self) -> Locator:
        """Email input field (language-independent)."""
        return self.page.locator("input[name='email']")

    @property
    def password_field(self) -> Locator:
        """Password input field (language-independent)."""
        return self.page.locator("input[name='password']")

    @property
    def create_account_button(self) -> Locator:
        """Create account button (language-independent - uses type=submit)."""
        return self.page.locator("button[type='submit']")

    @property
    def validation_errors(self) -> Locator:

        return self.page.get_by_role("alert")

    @property
    def validation_errors_fallback(self) -> Locator:

        return self.page.locator("[data-testid='validation-error']")

    @property
    def otp_modal(self) -> Locator:

        return self.page.get_by_role("dialog")

    @property
    def otp_inputs(self) -> Locator:
        """OTP input fields (4 digits)."""
        return self.page.locator(".MuiOtpInput-Box input")

    @property
    def activate_button(self) -> Locator:
        """Activate button in OTP modal (language-independent - uses type=submit in OTP form)."""
        return self.page.locator("button[type='submit']")

    @property
    def resend_otp_button(self) -> Locator:
        """Resend OTP button (language-independent - button that's not submit type)."""
        return self.page.locator("button[type='button']").filter(has_not=self.page.locator("img"))

    @property
    def back_button(self) -> Locator:
        """Back button (arrow icon)."""
        return self.page.locator("button.MuiIconButton-root").first

    def open(self) -> None:

        logger.info("Navigating to registration page")
        self.navigate_to(self.url)
        self.wait_for_page_load()

    def is_loaded(self) -> bool:

        try:
            SmartWaits.wait_for_element_visible(
                self.first_name_field,
                timeout=5000
            )
            return True
        except Exception as e:
            logger.warning(f"Registration page not loaded: {e}")
            return False

    def fill_name(self, name: str) -> None:

        logger.debug(f"Filling name: {name}")
        self.first_name_field.fill(name)

    def fill_phone(self, phone: str) -> None:

        logger.debug(f"Filling phone: {phone}")
        self.phone_field.fill(phone)

    def fill_email(self, email: str) -> None:

        logger.debug(f"Filling email: {email}")
        self.email_field.fill(email)

    def fill_password(self, password: str) -> None:

        logger.debug("Filling password")
        self.password_field.fill(password)

    def fill_registration_form(
        self,
        name: str,
        phone: str,
        email: str,
        password: str
    ) -> None:

        logger.info("Filling registration form")
        self.fill_name(name)
        self.fill_phone(phone)
        self.fill_email(email)
        self.fill_password(password)

    def click_create_account(self) -> None:

        logger.info("Clicking create account button")
        SmartWaits.wait_for_element_clickable(self.create_account_button)
        self.create_account_button.click()

    def submit_registration(self) -> None:

        self.click_create_account()
        SmartWaits.wait_for_network_idle(self.page, timeout=5000)

    # ===============================
    # MUI Validation Error Methods
    # ===============================
    def get_validation_error_count(self) -> int:
        """Get count of MUI validation error messages displayed."""
        try:
            error_elements = self.page.locator(".MuiFormHelperText-root.Mui-error")
            return error_elements.count()
        except Exception:
            return 0

    def has_validation_errors(self) -> bool:
        """Check if form has any MUI validation errors displayed."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """Get all MUI validation error messages from the form."""
        messages = []
        try:
            error_elements = self.page.locator(".MuiFormHelperText-root.Mui-error")
            count = error_elements.count()
            for i in range(count):
                try:
                    text = error_elements.nth(i).inner_text(timeout=1000)
                    if text.strip():
                        messages.append(text.strip())
                except Exception:
                    pass
        except Exception:
            pass
        return messages

    def has_error_for_field(self, field_name: str) -> bool:
        """Check if a specific field has validation error."""
        try:
            # Check by label text with error class
            error_label = self.page.locator(f".Mui-error:has-text('{field_name}')")
            if error_label.count() > 0:
                return True
            # Also check parent MuiFormControl for error state
            form_control = self.page.locator(f".MuiFormControl-root:has(.Mui-error):has-text('{field_name}')")
            return form_control.count() > 0
        except Exception:
            return False

    def get_field_error_message(self, field_name: str) -> str:
        """Get error message for a specific field by name attribute."""
        try:
            field_locator = self.page.locator(f"input[name='{field_name}']")
            if field_locator.count() > 0:
                # Get parent form control and find helper text
                parent = field_locator.locator("xpath=ancestor::div[contains(@class, 'MuiFormControl')]").first
                helper_text = parent.locator(".MuiFormHelperText-root.Mui-error")
                if helper_text.count() > 0:
                    return helper_text.first.inner_text()
        except Exception as e:
            logger.debug(f"Could not get field error for {field_name}: {e}")
        return ""

    def has_toast_error(self) -> bool:
        """Check if toast/alert error is displayed."""
        try:
            return self.page.locator("[role='alert']").first.is_visible(timeout=2000)
        except Exception:
            return False

    def get_toast_error_message(self) -> str:
        """Get error message from toast/alert notification."""
        try:
            alert = self.page.locator("[role='alert']").first
            if alert.is_visible(timeout=2000):
                return alert.inner_text()
        except Exception:
            pass
        return ""

    def get_validation_error_text(self) -> str:
        """Get first validation error text (legacy method)."""
        messages = self.get_validation_error_messages()
        return messages[0] if messages else ""

    def is_still_on_registration_page(self) -> bool:

        current_url = self.get_current_url()
        return "registration" in current_url.lower()

    def is_otp_modal_visible(self) -> bool:
        """Check if OTP modal is visible by looking for OTP input fields."""
        try:
            # Only check for OTP inputs - this is the definitive indicator
            otp_visible = self.otp_inputs.count() == 4
            return otp_visible
        except Exception as e:
            logger.debug(f"OTP modal not visible: {e}")
            return False

    def enter_otp_digits(self, otp_code: str) -> None:


        if len(otp_code) != 4:
            logger.warning(f"OTP code should be 4 digits, got: {len(otp_code)}")

        otp_inputs = self.otp_inputs
        for i, digit in enumerate(otp_code[:4]):
            if i < otp_inputs.count():
                otp_inputs.nth(i).fill(digit)
                # Small delay for input processing - using type with delay instead
        self.wait_for_dom_ready()

    def click_activate_button(self) -> None:
        """Click activate button in OTP modal."""
        logger.info("Clicking activate button")
        SmartWaits.wait_for_element_clickable(self.activate_button)
        self.activate_button.click()

    def click_resend_otp(self) -> None:
        """Click resend OTP button."""
        logger.info("Clicking resend OTP button")
        SmartWaits.wait_for_element_clickable(self.resend_otp_button)
        self.resend_otp_button.click()

    def is_resend_button_available(self) -> bool:

        try:
            return (
                self.resend_otp_button.is_visible(timeout=1000) and
                self.resend_otp_button.is_enabled()
            )
        except Exception:
            return False

    def click_back_from_otp(self) -> None:
        """Click back button to return to registration form."""
        logger.info("Clicking back button from OTP")
        self.back_button.click()
        SmartWaits.wait_for_network_idle(self.page, timeout=2000)

    def verify_registration_fields_cleared(self) -> bool:

        name_value = self.first_name_field.input_value()
        phone_value = self.phone_field.input_value()
        email_value = self.email_field.input_value()
        password_value = self.password_field.input_value()

        all_empty = not any([name_value, phone_value, email_value, password_value])
        logger.debug(
            f"Fields after back: name='{name_value}', phone='{phone_value}', "
            f"email='{email_value}', password='{password_value}'"
        )

        return all_empty

    def get_otp_email_display(self) -> str:

        try:
            email_input = self.page.locator("input[name='email']").first
            if email_input.is_visible():
                return email_input.input_value() or ""
        except Exception as e:
            logger.debug(f"Could not get OTP email display: {e}")

        return ""

    def verify_email_auto_filled_in_otp(self, expected_email: str) -> bool:

        displayed_email = self.get_otp_email_display()
        is_correct = (
            expected_email in displayed_email or
            displayed_email in expected_email
        )

        logger.debug(
            f"Expected: {expected_email}, Displayed: {displayed_email}, "
            f"Match: {is_correct}"
        )

        return is_correct

    def complete_registration_to_otp(
        self,
        name: str,
        phone: str,
        email: str,
        password: str
    ) -> bool:

        logger.info("Completing registration to reach OTP")

        self.fill_registration_form(name, phone, email, password)
        self.submit_registration()
        # Wait for OTP modal to appear or URL to change
        self.wait_for_network_idle()
        self.wait_for_selector(".MuiOtpInput-Box input", state="visible", timeout=10000)

        otp_modal_visible = self.is_otp_modal_visible()
        url_contains_otp = "otp" in self.get_current_url().lower()
        success = otp_modal_visible or url_contains_otp
        logger.info(
            f"OTP check: modal={otp_modal_visible}, url_otp={url_contains_otp}, "
            f"reached={success}"
        )

        return success

    def wait_for_manual_otp_and_activate(self, timeout_seconds: int = 60) -> bool:

        logger.info("Waiting for manual OTP entry (check browser)...")

        for attempt in range(timeout_seconds // 2):
            try:
                if self.activate_button.is_enabled():
                    logger.info("Manual OTP detected - activate button enabled")
                    self.activate_button.click()
                    self.page.wait_for_load_state("networkidle")
                    logger.info("Activate button clicked")
                    return True
            except Exception as e:
                logger.debug(f"Waiting for OTP (attempt {attempt + 1}): {e}")

            self.page.wait_for_load_state("networkidle")

        logger.warning("Manual OTP timeout")
        return False

    def navigate_to_registration(self) -> None:
        """Backward compatibility - use open() instead."""
        logger.warning("navigate_to_registration() is deprecated, use open()")
        self.open()

    def is_registration_page_loaded(self) -> bool:
        """Backward compatibility - use is_loaded() instead."""
        logger.warning("is_registration_page_loaded() is deprecated, use is_loaded()")
        return self.is_loaded()