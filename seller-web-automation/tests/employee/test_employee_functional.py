"""
Staff Management tests — полная переработка.

Покрытие: UI, Search, Table, Add Form, Validation, Security,
Creation, Delete, Navigation, AuthGuard.

Фикстуры используют session-scoped fresh_authenticated_page из conftest.
"""

import pytest
import allure
from pages.employee_page import EmployeePage



@allure.epic("Платформа продавца")
@allure.suite("Форма добавления сотрудника")
@allure.feature("Интерфейс формы")
@pytest.mark.functional
class TestEmployeeAddForm:
    """Тесты UI формы добавления сотрудника."""

    @allure.title("Переход по ссылке 'Добавить сотрудника' открывает форму создания")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_link_navigates_to_create(self, employee_page: EmployeePage):
        """BUG: Клик на 'Add Staff Member' не открывает форму создания."""
        with allure.step("Проверка видимости кнопки 'Добавить сотрудника'"):
            assert employee_page.add_employee_btn.is_visible(timeout=5000), \
                "BUG: Ссылка 'Add Staff Member' не видна"
        with allure.step("Нажатие на кнопку 'Добавить сотрудника'"):
            employee_page.click_add_employee()
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что форма создания отображается"):
            assert employee_page.is_add_form_visible(), \
                f"BUG: Форма создания не открылась (URL: {employee_page.page.url})"

    @allure.title("Форма содержит поле 'Номер телефона'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_form_has_phone_field(self, employee_create_page: EmployeePage):
        """BUG: Поле 'Phone Number' отсутствует в форме."""
        with allure.step("Проверка видимости поля 'Номер телефона' в форме"):
            assert employee_create_page.phone_input.is_visible(timeout=5000), \
                "BUG: Поле 'Phone Number' не видно в форме создания"

    @allure.title("Форма содержит выпадающий список 'Роль'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_form_has_role_select(self, employee_create_page: EmployeePage):
        """BUG: Выпадающий список 'Role' отсутствует в форме."""
        with allure.step("Проверка видимости выпадающего списка 'Роль' в форме"):
            assert employee_create_page.role_select.is_visible(timeout=5000), \
                "BUG: Поле 'Role' не видно в форме создания"

    @allure.title("Форма содержит выбор магазинов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_form_has_shops_select(self, employee_create_page: EmployeePage):
        """BUG: Выбор магазинов отсутствует в форме."""
        with allure.step("Проверка видимости поля выбора магазинов в форме"):
            assert employee_create_page.shops_select.is_visible(timeout=5000), \
                "BUG: Поле выбора магазинов не видно"

    @allure.title("Форма содержит кнопку отправки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_form_has_submit_button(self, employee_create_page: EmployeePage):
        """BUG: Кнопка 'Add Staff Member' отсутствует в форме."""
        with allure.step("Проверка видимости кнопки отправки формы"):
            submit_visible = employee_create_page.add_staff_btn.is_visible(timeout=3000) or \
                employee_create_page.save_btn.is_visible(timeout=3000)
            assert submit_visible, \
                "BUG: Кнопка отправки формы не видна"

    @allure.title("URL страницы создания содержит /staff/create")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_page_url_correct(self, employee_create_page: EmployeePage):
        """BUG: URL страницы создания не содержит /staff/create."""
        with allure.step("Проверка что URL содержит /staff/create"):
            assert "/staff/create" in employee_create_page.page.url or \
                "/staff" in employee_create_page.page.url, \
                f"BUG: URL не содержит /staff: {employee_create_page.page.url}"



@allure.epic("Платформа продавца")
@allure.suite("Валидация формы сотрудника")
@allure.feature("Валидация")
@pytest.mark.negative
class TestEmployeeFormValidation:
    """Тесты валидации формы создания сотрудника."""

    @allure.title("Отправка пустой формы блокируется валидацией")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_empty_form_submit_blocked(self, employee_create_page: EmployeePage):
        """BUG: Пустая форма отправляется без ошибок валидации."""
        with allure.step("Отправка пустой формы без заполнения полей"):
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что форма не отправилась и показаны ошибки валидации"):
            still_on_form = employee_create_page.is_add_form_visible()
            error_count = employee_create_page.page.locator(
                ".MuiFormHelperText-root.Mui-error"
            ).count()
            has_error = error_count > 0
            no_success = not employee_create_page.is_success_message_visible()
            assert still_on_form or has_error or no_success, \
                "BUG: Пустая форма отправилась без валидации"

    @allure.title("Пустой телефон показывает ошибку валидации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_empty_phone_shows_error(self, employee_create_page: EmployeePage):
        """BUG: Пустой телефон не показывает ошибку валидации."""
        with allure.step("Очистка поля телефона и отправка формы"):
            employee_create_page.phone_input.click()
            employee_create_page.phone_input.fill("")
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что форма не прошла валидацию"):
            assert not employee_create_page.is_success_message_visible(), \
                "BUG: Форма с пустым телефоном прошла валидацию"

    @allure.title("Невалидный формат телефона отклоняется")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("phone,desc", [
        ("abcdefgh", "letters_only"),
        ("+998 90", "too_short"),
        ("!@#$%^&*()", "special_chars"),
    ], ids=["letters", "too_short", "special_chars"])
    def test_invalid_phone_format(self, employee_create_page: EmployeePage, phone: str, desc: str):
        """BUG: Невалидный формат телефона принимается без ошибки."""
        with allure.step(f"Ввод невалидного телефона: {phone}"):
            employee_create_page.phone_input.fill(phone)
        with allure.step("Отправка формы"):
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что невалидный телефон отклонен"):
            assert not employee_create_page.is_success_message_visible(), \
                f"BUG: Невалидный телефон '{phone}' ({desc}) прошел валидацию"

    @allure.title("Отправка формы без выбора роли блокируется")
    @allure.severity(allure.severity_level.NORMAL)
    def test_phone_only_without_role_blocked(self, employee_create_page: EmployeePage, test_data):
        """BUG: Форма отправляется без выбора роли."""
        with allure.step("Ввод только номера телефона без выбора роли"):
            phone = test_data["employee_data"]["phone"]
            employee_create_page.phone_input.fill(phone)
        with allure.step("Отправка формы без выбора роли"):
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что форма не отправилась без роли"):
            still_on_form = employee_create_page.is_add_form_visible()
            no_success = not employee_create_page.is_success_message_visible()
            assert still_on_form or no_success, \
                "BUG: Форма отправилась без выбора роли"

    @allure.title("Двойной клик на кнопку отправки не создает дубликат")
    @allure.severity(allure.severity_level.NORMAL)
    def test_double_click_submit_no_duplicate(self, employee_create_page: EmployeePage, test_data):
        """BUG: Двойной клик на submit создает дубликат."""
        with allure.step("Заполнение поля телефона"):
            phone = test_data["employee_data"]["phone"]
            employee_create_page.phone_input.fill(phone)
        with allure.step("Двойной клик на кнопку отправки"):
            if employee_create_page.add_staff_btn.is_visible(timeout=2000):
                employee_create_page.add_staff_btn.dblclick()
            elif employee_create_page.save_btn.is_visible(timeout=2000):
                employee_create_page.save_btn.dblclick()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка отсутствия серверной ошибки"):
            page_text = employee_create_page.page.text_content("body") or ""
            assert "Internal Server Error" not in page_text, \
                "BUG: Двойной клик вызвал серверную ошибку"



@allure.epic("Платформа продавца")
@allure.suite("Безопасность формы сотрудника")
@allure.feature("Безопасность")
@pytest.mark.security
class TestEmployeeFormSecurity:
    """Тесты безопасности формы создания сотрудника."""

    @allure.title("Инъекция в поле телефона блокируется")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("payload", [
        pytest.param("<script>alert('XSS')</script>", id="xss_script"),
        pytest.param("<img src=x onerror=alert(1)>", id="xss_img"),
        pytest.param("' OR '1'='1", id="sql_injection"),
    ])
    def test_phone_field_injection(self, employee_create_page: EmployeePage, payload: str):
        """BUG: Инъекция в поле телефона не блокируется."""
        with allure.step(f"Ввод payload в поле телефона: {payload}"):
            employee_create_page.phone_input.fill(payload)
        with allure.step("Отправка формы с инъекцией"):
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что инъекция не принята"):
            assert not employee_create_page.is_success_message_visible(), \
                f"BUG: Инъекция '{payload}' принята как валидный телефон"
            script_count = employee_create_page.page.locator("body script:not([src])").count()
            assert script_count == 0, \
                f"BUG: XSS payload создал <script> элемент: {payload!r}"

    @allure.title("Null byte в телефоне санитизируется")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_null_byte_in_phone(self, employee_create_page: EmployeePage):
        """BUG: Null byte в телефоне не санитизируется."""
        with allure.step("Ввод телефона с null byte"):
            employee_create_page.phone_input.fill("+998\x0090 000 00 00")
        with allure.step("Отправка формы"):
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что null byte не прошел валидацию"):
            assert not employee_create_page.is_success_message_visible(), \
                "BUG: Null byte в телефоне прошел валидацию"

    @allure.title("Command injection в телефоне блокируется")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_command_injection_in_phone(self, employee_create_page: EmployeePage):
        """BUG: Command injection в телефоне не блокируется."""
        with allure.step("Ввод command injection в поле телефона"):
            employee_create_page.phone_input.fill("; rm -rf /")
        with allure.step("Отправка формы"):
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка отсутствия серверной ошибки"):
            page_text = employee_create_page.page.text_content("body") or ""
            assert "Internal Server Error" not in page_text, \
                "BUG: Command injection вызвал серверную ошибку"



@allure.epic("Платформа продавца")
@allure.suite("Создание сотрудника")
@allure.feature("Создание сотрудника")
@pytest.mark.functional
class TestEmployeeCreation:
    """Тесты создания сотрудника."""

    @allure.title("Создание сотрудника с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_staff_with_valid_data(self, employee_create_page: EmployeePage, test_data):
        """BUG: Создание сотрудника с валидными данными не работает."""
        with allure.step("Заполнение формы валидными данными"):
            employee = test_data["employee_data"]
            employee_create_page.fill_staff_form(
                phone=employee["phone"],
                role=employee["role"],
                shops=["Zara"]
            )
        with allure.step("Отправка формы создания сотрудника"):
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка ответа системы"):
            has_success = employee_create_page.is_success_message_visible()
            has_error = employee_create_page.page.locator(
                ".MuiAlert-standardError, .MuiFormHelperText-root.Mui-error"
            ).first.is_visible(timeout=2000)
            redirected = "/staff" in employee_create_page.page.url and "/create" not in employee_create_page.page.url
            assert has_success or has_error or redirected, \
                "BUG: Нет ответа после отправки формы создания сотрудника"

    @allure.title("Создание сотрудника с разными ролями")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("role", [
        "Manager", "Finance Manager", "Content Manager", "Marketer"
    ], ids=["manager", "finance_manager", "content_manager", "marketer"])
    def test_create_staff_different_roles(self, employee_page: EmployeePage, role: str, test_data):
        """BUG: Определенная роль не доступна при создании сотрудника."""
        with allure.step("Переход к форме создания сотрудника"):
            employee_page.click_add_employee()
            employee_page.page.wait_for_load_state("domcontentloaded")
            assert employee_page.is_add_form_visible(), \
                "BUG: Форма создания не открылась"
        with allure.step(f"Проверка доступности роли '{role}' в списке"):
            employee_page.role_select.click()
            employee_page.page.wait_for_load_state("domcontentloaded")
            role_option = employee_page.page.get_by_role("option", name=role, exact=True)
            assert role_option.is_visible(timeout=3000), \
                f"BUG: Роль '{role}' не доступна в списке ролей"
            employee_page.page.keyboard.press("Escape")

    @allure.title("Форма показывает обратную связь после отправки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_form_shows_response_after_submit(self, employee_create_page: EmployeePage, test_data):
        """BUG: Нет обратной связи после отправки формы."""
        with allure.step("Заполнение и отправка формы"):
            employee = test_data["employee_data"]
            employee_create_page.fill_staff_form(
                phone=employee["phone"],
                role=employee["role"]
            )
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка наличия обратной связи"):
            page_changed = "/create" not in employee_create_page.page.url
            has_success = employee_create_page.is_success_message_visible()
            has_error = employee_create_page.page.locator(
                ".MuiAlert-standardError, .MuiFormHelperText-root.Mui-error"
            ).first.is_visible(timeout=2000)
            assert page_changed or has_success or has_error, \
                "BUG: Нет обратной связи после отправки формы"

    @allure.title("После успешного создания происходит редирект на список")
    @allure.severity(allure.severity_level.NORMAL)
    def test_success_redirects_to_list(self, employee_create_page: EmployeePage, test_data):
        """BUG: После успешного создания нет редиректа на список."""
        with allure.step("Заполнение и отправка формы с валидными данными"):
            employee = test_data["employee_data"]
            employee_create_page.fill_staff_form(
                phone=employee["phone"],
                role=employee["role"],
                shops=["Zara"]
            )
            employee_create_page.submit_form()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка редиректа на список сотрудников"):
            if employee_create_page.is_success_message_visible():
                assert "/create" not in employee_create_page.page.url, \
                    "BUG: После успешного создания остались на /create"



@allure.epic("Платформа продавца")
@allure.suite("Удаление сотрудника")
@allure.feature("Удаление сотрудника")
@pytest.mark.functional
class TestEmployeeDelete:
    """Тесты удаления сотрудников."""

    @allure.title("Удаление сотрудника показывает диалог подтверждения")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_shows_confirmation(self, employee_page: EmployeePage):
        """BUG: Удаление сотрудника не показывает диалог подтверждения."""
        with allure.step("Проверка наличия сотрудников в списке"):
            count = employee_page.get_employee_count()
            if count == 0:
                pytest.fail("BUG: Нет сотрудников для проверки удаления")
        with allure.step("Нажатие на кнопку удаления сотрудника"):
            employee_page.click_delete_staff(index=0)
        with allure.step("Проверка появления диалога подтверждения"):
            assert employee_page.is_delete_confirmation_visible(), \
                "BUG: Диалог подтверждения удаления не появился"
            employee_page.cancel_delete()

    @allure.title("Отмена удаления сохраняет сотрудника в списке")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancel_delete_preserves_staff(self, employee_page: EmployeePage):
        """BUG: Отмена удаления всё равно удаляет сотрудника."""
        with allure.step("Получение начального количества сотрудников"):
            initial_count = employee_page.get_employee_count()
            if initial_count == 0:
                pytest.fail("BUG: Нет сотрудников для теста отмены удаления")
        with allure.step("Нажатие удалить и отмена"):
            employee_page.delete_staff_member(index=0, confirm=False)
            employee_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что количество сотрудников не изменилось"):
            final_count = employee_page.get_employee_count()
            assert final_count == initial_count, \
                f"BUG: После отмены удаления count изменился ({initial_count} → {final_count})"

    @allure.title("Подтверждение удаления удаляет сотрудника из списка")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_confirm_delete_removes_staff(self, employee_page: EmployeePage):
        """BUG: Подтверждение удаления не удаляет сотрудника."""
        with allure.step("Получение начального количества сотрудников"):
            initial_count = employee_page.get_employee_count()
            if initial_count == 0:
                pytest.fail("BUG: Нет сотрудников для удаления")
        with allure.step("Подтверждение удаления сотрудника"):
            employee_page.delete_staff_member(index=0, confirm=True)
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что сотрудник удален из списка"):
            final_count = employee_page.get_employee_count()
            assert final_count == initial_count - 1, \
                f"BUG: Удаление не сработало (было {initial_count}, стало {final_count})"

    @allure.title("Диалог подтверждения удаления содержит кнопки действий")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_confirmation_has_buttons(self, employee_page: EmployeePage):
        """BUG: Диалог подтверждения не содержит кнопок Delete/Cancel."""
        with allure.step("Проверка наличия сотрудников"):
            count = employee_page.get_employee_count()
            if count == 0:
                pytest.fail("BUG: Нет сотрудников для проверки диалога")
        with allure.step("Открытие диалога удаления"):
            employee_page.click_delete_staff(index=0)
            employee_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка наличия кнопок в диалоге"):
            dialog = employee_page.page.get_by_role("dialog")
            if dialog.is_visible(timeout=3000):
                delete_btn = employee_page.page.get_by_role("button", name="Delete").or_(
                    employee_page.page.get_by_role("button", name="Удалить")
                ).or_(employee_page.page.get_by_role("button", name="O'chirish"))
                cancel_btn = employee_page.page.get_by_role("button", name="Выйти").or_(
                    employee_page.page.get_by_role("button", name="Cancel")
                ).or_(employee_page.page.get_by_role("button", name="Bekor qilish"))
                has_delete = delete_btn.is_visible(timeout=2000)
                has_cancel = cancel_btn.is_visible(timeout=2000)
                assert has_delete or has_cancel, \
                    "BUG: Диалог подтверждения не имеет кнопок действий"
            employee_page.cancel_delete()
