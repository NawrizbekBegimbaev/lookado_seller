"""
Login Test Suite — Authentication Functionality.

Senior QA approach: minimal tests, maximum coverage.
Each test finds a unique bug that no other test can find.
"""

import pytest
import allure
from pages.login_page import LoginPage


@pytest.fixture
def login_page(browser, request):
    """Fresh login page instance per test — isolated context."""
    from config import settings
    headless = request.config.getoption("headless")
    if headless:
        ctx_opts = settings.get_browser_context_options_with_viewport()
    else:
        ctx_opts = settings.get_browser_context_options()
    context = browser.new_context(**ctx_opts)
    page = context.new_page()
    lp = LoginPage(page)
    lp.open_login_page()
    lp.email_field.wait_for(state="visible", timeout=10000)
    yield lp
    context.close()


# =============================================================================
# SMOKE — Critical path (must pass for release)
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Авторизация")
@allure.feature("Аутентификация")
class TestLoginSmoke:
    """Core login functionality — if these fail, nothing works."""

    @allure.title("Проверка видимости элементов формы входа")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_form_elements_visible(self, login_page):
        """All essential form elements are present on page load."""
        with allure.step("Проверка видимости всех элементов формы входа"):
            assert login_page.is_email_field_visible(), "Email/phone field missing"
            assert login_page.is_password_field_visible(), "Password field missing"
            assert login_page.is_login_button_visible(), "Login button missing"
            assert login_page.is_registration_link_visible(), "Registration link missing"

    @allure.title("Вход с валидными учётными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_login_with_valid_credentials(self, login_page, test_data):
        """Valid credentials redirect to dashboard."""
        with allure.step("Ввод валидных учётных данных и отправка формы"):
            login_page.perform_login(
                test_data["valid_credentials"]["email"],
                test_data["valid_credentials"]["password"]
            )
        with allure.step("Проверка перенаправления на дашборд"):
            assert login_page.is_redirected_to_dashboard(), \
                "Valid credentials should redirect to dashboard"

    @allure.title("Вход с невалидными учётными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_with_invalid_credentials(self, login_page, test_data):
        """Wrong password shows error, does not redirect."""
        with allure.step("Ввод невалидного пароля и отправка формы"):
            login_page.perform_login(
                test_data["valid_credentials"]["email"],
                test_data["wrong_password"]
            )
            login_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка отображения ошибки и отсутствия перенаправления"):
            assert login_page.is_error_displayed() or login_page.has_validation_errors(), \
                "BUG: No error shown for invalid credentials"
            assert "dashboard" not in login_page.page.url, \
                "Invalid credentials should not reach dashboard"

    @allure.title("Полный цикл входа и выхода из системы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_complete_login_logout_flow(self, login_page, test_data):
        """Полный цикл: логин -> дашборд -> клик на профиль -> сайдбар -> Sign Out."""
        page = login_page.page

        with allure.step("Вход в систему с валидными данными"):
            login_page.perform_login(
                test_data["valid_credentials"]["email"],
                test_data["valid_credentials"]["password"]
            )
            assert "dashboard" in page.url, \
                f"Should redirect to dashboard, got: {page.url}"

        with allure.step("Нажатие на аватар профиля в заголовке"):
            account_btn = page.get_by_role("button", name="Account button")
            account_btn.wait_for(state="visible", timeout=10000)
            account_btn.click()

        with allure.step("Нажатие кнопки выхода из системы"):
            logout_btn = page.locator("button:has-text('Chiqish'), button:has-text('Выйти'), button:has-text('Sign Out')").first
            logout_btn.wait_for(state="visible", timeout=5000)
            logout_btn.click()

        with allure.step("Проверка перенаправления на страницу входа"):
            page.wait_for_url("**/auth/login**", timeout=15000)
            assert "login" in page.url, \
                f"After logout should be on login page, got: {page.url}"


# =============================================================================
# VALIDATION — Input handling and form validation
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Авторизация")
@allure.feature("Валидация ввода")
class TestLoginValidation:
    """Form validation — catches client-side validation bugs."""

    @allure.title("Валидация пустых полей формы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("email,password,scenario", [
        ("", "", "both_empty"),
        ("", "76543217", "email_empty"),
        ("998001112233", "", "password_empty"),
    ], ids=["both-empty", "email-empty", "password-empty"])
    def test_empty_field_validation(self, login_page, email, password, scenario):
        """Empty fields must show validation errors."""
        with allure.step(f"Заполнение формы для сценария: {scenario}"):
            if email:
                login_page.enter_email(email)
            if password:
                login_page.enter_password(password)
        with allure.step("Отправка формы и проверка ошибки валидации"):
            login_page.click_login()
            login_page.page.wait_for_load_state("networkidle")
            assert login_page.is_error_displayed() or login_page.has_validation_errors(), \
                f"BUG: No validation error for scenario: {scenario}"

    @allure.title("Граничные значения длины пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("password,should_error", [
        ("1234567", True),    # 7 chars — below min
        ("12345678", False),  # 8 chars — at boundary
        ("123456789", False), # 9 chars — above boundary
    ], ids=["7-chars-error", "8-chars-ok", "9-chars-ok"])
    def test_password_length_boundary(self, login_page, test_data, password, should_error):
        """Password min length is 8 chars. Below = validation error."""
        with allure.step(f"Ввод пароля длиной {len(password)} символов"):
            login_page.enter_email(test_data["valid_credentials"]["email"])
            login_page.enter_password(password)
        with allure.step("Отправка формы и проверка граничного значения"):
            login_page.click_login()
            login_page.page.wait_for_load_state("networkidle")
            has_length_error = login_page.has_validation_errors()
            if should_error:
                assert has_length_error, \
                    f"BUG: Password '{password}' ({len(password)} chars) should show length error"

    @allure.title("Отклонение невалидного email")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("invalid_email", [
        "userexample.com",       # no @
        "user@@example.com",     # multiple @
        "@",                     # just @
        "a",                     # single char
        "   ",                   # whitespace only
        "a" * 300 + "@test.com", # too long
    ], ids=["no-at", "double-at", "only-at", "single-char", "whitespace", "too-long"])
    def test_invalid_email_rejected(self, login_page, test_data, invalid_email):
        """Invalid email formats must show error or be rejected."""
        with allure.step(f"Ввод невалидного email: '{invalid_email[:30]}'"):
            login_page.enter_email(invalid_email)
            login_page.enter_password(test_data["valid_credentials"]["password"])
        with allure.step("Отправка формы и проверка отклонения"):
            login_page.click_login()
            login_page.page.wait_for_load_state("networkidle")
            assert login_page.is_error_displayed() or login_page.has_validation_errors(), \
                f"BUG: No error for invalid email: '{invalid_email[:30]}'"

    @allure.title("Переключение видимости пароля")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_password_visibility_toggle(self, login_page, test_data):
        """Eye icon toggles password field between masked and visible."""
        page = login_page.page
        with allure.step("Ввод пароля и проверка маскировки"):
            login_page.enter_password(test_data["valid_credentials"]["password"])
            assert login_page.password_field.get_attribute("type") == "password", \
                "Password should be masked initially"

        with allure.step("Нажатие на иконку переключения видимости пароля"):
            toggle = page.locator(
                "button[aria-label*='visibility'], button[aria-label*='password'], "
                "[data-testid='visibility-toggle'], button:has(svg)"
            ).filter(has=page.locator("svg")).first
            assert toggle.is_visible(timeout=2000), "BUG: Visibility toggle not found"
            toggle.click()
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка что пароль стал видимым"):
            assert login_page.password_field.get_attribute("type") == "text", \
                "BUG: Password should be visible after toggle click"

    @allure.title("Отправка формы клавишей Enter")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.functional
    def test_enter_key_submits_form(self, login_page, test_data):
        """Pressing Enter in password field submits the form."""
        with allure.step("Заполнение формы входа"):
            login_page.enter_email(test_data["valid_credentials"]["email"])
            login_page.enter_password(test_data["valid_credentials"]["password"])
        with allure.step("Отправка формы клавишей Enter"):
            login_page.page.keyboard.press("Enter")
            login_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка успешной отправки формы"):
            current_url = login_page.page.url
            assert "dashboard" in current_url or "login" not in current_url, \
                "Enter key should submit the form"


# =============================================================================
# SECURITY — Authentication security checks
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Авторизация")
@allure.feature("Безопасность")
class TestLoginSecurity:
    """Security tests — catches vulnerabilities."""

    @allure.title("Поле пароля замаскировано")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.regression
    def test_password_field_masked(self, login_page):
        """Password field has type=password (input is hidden)."""
        with allure.step("Проверка что поле пароля замаскировано (type=password)"):
            field_type = login_page.password_field.get_attribute("type")
            assert field_type == "password", \
                f"BUG: Password field type should be 'password', got '{field_type}'"

    @allure.title("Проверка HTTPS соединения")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.regression
    def test_https_connection(self, login_page):
        """Login page is served over HTTPS."""
        with allure.step("Проверка что страница загружена по HTTPS"):
            assert login_page.page.url.startswith("https://"), \
                f"BUG: Login must use HTTPS, got: {login_page.page.url}"

    @allure.title("Отклонение инъекционных payload")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.security
    @pytest.mark.parametrize("payload,name", [
        ("' OR '1'='1", "sql_injection"),
        ("<script>alert('XSS')</script>", "xss"),
        ("<img src=x onerror=alert(1)>", "html_injection"),
        ("user\x00admin", "null_byte"),
        ("*)(uid=*))(|(uid=*", "ldap_injection"),
        ("; rm -rf /", "command_injection"),
        ("../../etc/passwd", "path_traversal"),
    ], ids=["sql", "xss", "html", "null-byte", "ldap", "command", "path-traversal"])
    def test_injection_payloads_rejected(self, login_page, test_data, payload, name):
        """Injection payloads must not bypass authentication."""
        with allure.step(f"Ввод инъекционного payload: {name}"):
            login_page.enter_email(payload)
            login_page.enter_password(test_data["valid_credentials"]["password"])
        with allure.step("Отправка формы и проверка что инъекция не прошла"):
            login_page.click_login()
            login_page.page.wait_for_load_state("networkidle")
            assert "dashboard" not in login_page.page.url, \
                f"BUG: {name} payload bypassed authentication!"

    @allure.title("Проверка атрибутов автозаполнения")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_autocomplete_attributes(self, login_page):
        """Form fields must have autocomplete attributes for password managers."""
        with allure.step("Проверка атрибута autocomplete на поле email"):
            email_autocomplete = login_page.email_field.get_attribute("autocomplete")
            assert email_autocomplete is not None, \
                "BUG: Email field missing autocomplete attribute (breaks password managers)"
        with allure.step("Проверка атрибута autocomplete на поле пароля"):
            password_autocomplete = login_page.password_field.get_attribute("autocomplete")
            assert password_autocomplete is not None, \
                "BUG: Password field missing autocomplete attribute (breaks password managers)"

    @allure.title("Множественные неудачные попытки входа")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.security
    def test_multiple_failed_attempts(self, login_page, test_data):
        """Multiple failed logins should not crash or bypass auth."""
        with allure.step("Выполнение 5 неудачных попыток входа"):
            email = test_data["valid_credentials"]["email"]
            for i in range(5):
                login_page.enter_email(email)
                login_page.enter_password(f"wrong_pass_{i}")
                login_page.click_login()
                login_page.page.wait_for_load_state("networkidle")

        with allure.step("Проверка что страница не сломалась после множественных попыток"):
            assert "login" in login_page.page.url or "auth" in login_page.page.url, \
                "After 5 failed attempts, should still be on login page"
            assert login_page.is_email_field_visible(), \
                "BUG: Login form broken after multiple failed attempts"


# =============================================================================
# SESSION — Navigation and session state
# =============================================================================
@allure.epic("Платформа продавца")
@allure.suite("Авторизация")
@allure.feature("Управление сессиями")
class TestLoginSession:
    """Session behavior — catches state management bugs."""

    @allure.title("Навигация по ссылке регистрации")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.functional
    def test_registration_link_navigation(self, login_page):
        """Registration link navigates to registration page."""
        with allure.step("Нажатие на ссылку регистрации"):
            login_page.click_registration_link()
            login_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка перехода на страницу регистрации"):
            assert "registration" in login_page.page.url, \
                f"BUG: Registration link should navigate to /registration, got: {login_page.page.url}"

    @allure.title("Сохранение сессии после обновления страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_session_persists_after_refresh(self, login_page, test_data):
        """Login session survives page refresh."""
        with allure.step("Вход в систему"):
            login_page.perform_login(
                test_data["valid_credentials"]["email"],
                test_data["valid_credentials"]["password"]
            )
            assert login_page.is_redirected_to_dashboard(), "Should be on dashboard"
        with allure.step("Обновление страницы и проверка сохранения сессии"):
            login_page.page.reload()
            login_page.page.wait_for_load_state("load")
            assert "login" not in login_page.page.url, \
                "BUG: Session lost after page refresh"

    @allure.title("Кнопка назад после входа")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_back_button_after_login(self, login_page, test_data):
        """Back button after login should not expose login form with filled credentials."""
        with allure.step("Вход в систему"):
            login_page.perform_login(
                test_data["valid_credentials"]["email"],
                test_data["valid_credentials"]["password"]
            )
            assert login_page.is_redirected_to_dashboard(), "Should be on dashboard"
        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            login_page.page.go_back()
            login_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что пароль не отображается после возврата"):
            current_url = login_page.page.url
            if "login" in current_url:
                password_value = login_page.password_field.input_value()
                assert password_value == "", \
                    "BUG: Password field should be empty after back navigation"
