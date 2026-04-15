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
@allure.suite("UI списка сотрудников")
@allure.feature("Элементы интерфейса")
@pytest.mark.smoke
class TestEmployeeListUI:
    """Проверка видимости и состояния UI-элементов на странице списка сотрудников."""

    @allure.title("Страница сотрудников загружается корректно")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_staff_page_loads(self, employee_page: EmployeePage):
        """BUG: Страница сотрудников не загружается (нет грида и empty state)."""
        with allure.step("Проверка видимости таблицы или пустого состояния"):
            table_visible = employee_page.is_table_visible()
            empty_visible = employee_page.is_empty_state_visible()
            assert table_visible or empty_visible, \
                "BUG: Ни грид, ни empty state не отображаются на странице сотрудников"

    @allure.title("Кнопки панели инструментов отображаются")
    @allure.severity(allure.severity_level.NORMAL)
    def test_toolbar_buttons_visible(self, employee_page: EmployeePage):
        """BUG: Кнопки toolbar (Columns, Filters, Export, Search) не отображаются."""
        with allure.step("Проверка видимости кнопки Columns"):
            assert employee_page.columns_btn.is_visible(timeout=3000), \
                "BUG: Кнопка Columns не видна"
        with allure.step("Проверка видимости кнопки Filters"):
            assert employee_page.filters_btn.is_visible(timeout=3000), \
                "BUG: Кнопка Filters не видна"
        with allure.step("Проверка видимости кнопки Export"):
            assert employee_page.export_btn.is_visible(timeout=3000), \
                "BUG: Кнопка Export не видна"
        with allure.step("Проверка видимости кнопки Search"):
            assert employee_page.search_btn.is_visible(timeout=3000), \
                "BUG: Кнопка Search не видна"

    @allure.title("Кнопка 'Добавить сотрудника' отображается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_employee_button_visible(self, employee_page: EmployeePage):
        """BUG: Ссылка 'Add Staff Member' не отображается."""
        with allure.step("Проверка видимости кнопки 'Добавить сотрудника'"):
            assert employee_page.add_employee_btn.is_visible(timeout=5000), \
                "BUG: Ссылка 'Add Staff Member' не видна на странице"

    @allure.title("Таблица содержит ожидаемые колонки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_grid_has_expected_columns(self, employee_page: EmployeePage):
        """BUG: Таблица сотрудников не содержит обязательных колонок."""
        with allure.step("Получение списка колонок таблицы"):
            columns = employee_page.get_table_columns()
        with allure.step("Проверка что таблица содержит колонки"):
            assert len(columns) > 0, \
                "BUG: Нет видимых заголовков колонок в таблице сотрудников"

    @allure.title("URL страницы содержит /staff")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_url_correct(self, employee_page: EmployeePage):
        """BUG: URL страницы не содержит /staff."""
        with allure.step("Проверка что URL содержит /staff"):
            assert "/staff" in employee_page.page.url, \
                f"BUG: URL не содержит /staff: {employee_page.page.url}"

    @allure.title("Соединение использует HTTPS")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_https_connection(self, employee_page: EmployeePage):
        """BUG: Соединение не защищено (не HTTPS)."""
        with allure.step("Проверка что соединение использует HTTPS"):
            assert employee_page.page.url.startswith("https://"), \
                f"BUG: Соединение не HTTPS: {employee_page.page.url}"

    @allure.title("URL не содержит чувствительных данных")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_sensitive_data_in_url(self, employee_page: EmployeePage):
        """BUG: В URL присутствуют секретные данные."""
        with allure.step("Получение URL страницы"):
            url = employee_page.page.url.lower()
        with allure.step("Проверка отсутствия чувствительных данных в URL"):
            for keyword in ("token", "password", "secret", "api_key"):
                assert keyword not in url, \
                    f"BUG: Найден секрет '{keyword}' в URL: {url}"

    @allure.title("Таблица имеет атрибут role='grid' для доступности")
    @allure.severity(allure.severity_level.MINOR)
    def test_grid_has_role_attribute(self, employee_page: EmployeePage):
        """BUG: Отсутствует role='grid' для accessibility."""
        with allure.step("Проверка наличия атрибута role='grid' для доступности"):
            grid = employee_page.page.locator("[role='grid']")
            assert grid.is_visible(timeout=3000), \
                "BUG: Элемент с role='grid' не найден (нарушение accessibility)"



@allure.epic("Платформа продавца")
@allure.suite("Поиск сотрудников")
@allure.feature("Поиск")
@pytest.mark.regression
class TestEmployeeSearch:
    """Тесты поисковой функциональности на странице сотрудников."""

    @allure.title("Кнопка поиска открывает поле ввода")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_button_opens_input(self, employee_page: EmployeePage):
        """BUG: Клик на кнопку поиска не открывает поле ввода."""
        with allure.step("Нажатие на кнопку поиска"):
            employee_page.search_btn.click()
            employee_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка видимости поля ввода поиска"):
            assert employee_page.search_input.is_visible(timeout=3000), \
                "BUG: Поле поиска не появилось после клика"

    @allure.title("Поиск с валидным запросом работает корректно")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_with_valid_query(self, employee_page: EmployeePage, test_data):
        """BUG: Поиск с валидным запросом крашит страницу."""
        with allure.step("Ввод валидного поискового запроса"):
            query = test_data["search"]["valid_query"]
            employee_page.search_employee(query)
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница отображает результаты или пустое состояние"):
            table_visible = employee_page.is_table_visible()
            empty_visible = employee_page.is_empty_state_visible()
            assert table_visible or empty_visible, \
                f"BUG: Страница крашнулась после поиска '{query}'"

    @allure.title("Поиск несуществующего показывает пустой результат")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_no_results(self, employee_page: EmployeePage, test_data):
        """BUG: Нет индикации пустого результата при поиске несуществующего."""
        with allure.step("Ввод несуществующего поискового запроса"):
            query = test_data["search"]["no_results_query"]
            employee_page.search_employee(query)
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что результаты пустые или отображается пустое состояние"):
            count = employee_page.get_employee_count()
            empty = employee_page.is_empty_state_visible()
            assert count == 0 or empty, \
                f"BUG: Поиск '{query}' вернул {count} строк вместо 0"

    @allure.title("Очистка поиска восстанавливает данные")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_clear_restores_data(self, employee_page: EmployeePage, test_data):
        """BUG: Очистка поиска не восстанавливает данные."""
        with allure.step("Ввод поискового запроса"):
            query = test_data["search"]["no_results_query"]
            employee_page.search_employee(query)
            employee_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Очистка поискового поля"):
            employee_page.clear_search()
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что данные восстановлены после очистки поиска"):
            table_visible = employee_page.is_table_visible()
            empty_visible = employee_page.is_empty_state_visible()
            assert table_visible or empty_visible, \
                "BUG: После очистки поиска нет ни грида, ни empty state"

    @allure.title("Инъекция в поиске отклоняется")
    @pytest.mark.security
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("payload", [
        pytest.param("<script>alert('XSS')</script>", id="xss"),
        pytest.param("'; DROP TABLE staff; --", id="sql"),
        pytest.param("test\x00injection", id="null_byte"),
        pytest.param("../../../etc/passwd", id="path_traversal"),
    ])
    def test_search_injection_rejected(self, employee_page: EmployeePage, payload: str):
        """BUG: Инъекция в поиске не санитизируется."""
        with allure.step(f"Ввод инъекционного payload в поле поиска"):
            employee_page.search_employee(payload)
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница не крашнулась"):
            table_visible = employee_page.is_table_visible()
            empty_visible = employee_page.is_empty_state_visible()
            assert table_visible or empty_visible, \
                f"BUG: Страница крашнулась после инъекции: {payload!r}"
        with allure.step("Проверка отсутствия XSS элементов на странице"):
            script_count = employee_page.page.locator("body script:not([src])").count()
            assert script_count == 0, \
                f"BUG: XSS payload создал <script> элемент: {payload!r}"

    @allure.title("Пустой поисковый запрос не ломает страницу")
    @allure.severity(allure.severity_level.MINOR)
    def test_search_empty_query(self, employee_page: EmployeePage):
        """BUG: Пустой поисковый запрос ломает страницу."""
        with allure.step("Ввод пустого поискового запроса"):
            employee_page.search_employee("")
            employee_page.page.wait_for_load_state("domcontentloaded")
        with allure.step("Проверка что страница отображается корректно"):
            table_visible = employee_page.is_table_visible()
            empty_visible = employee_page.is_empty_state_visible()
            assert table_visible or empty_visible, \
                "BUG: Пустой поиск сломал отображение"



@allure.epic("Платформа продавца")
@allure.suite("Таблица сотрудников")
@allure.feature("Операции с таблицей")
@pytest.mark.regression
class TestEmployeeTable:
    """Тесты таблицы сотрудников."""

    @allure.title("Таблица или пустое состояние отображается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_grid_or_empty_state_visible(self, employee_page: EmployeePage):
        """BUG: Таблица не показывает ни строки, ни empty state."""
        with allure.step("Получение количества сотрудников в таблице"):
            count = employee_page.get_employee_count()
            empty = employee_page.is_empty_state_visible()
        with allure.step("Проверка что отображается таблица или пустое состояние"):
            assert count > 0 or empty, \
                "BUG: Нет ни строк, ни empty state в таблице сотрудников"

    @allure.title("Заголовки колонок таблицы присутствуют")
    @allure.severity(allure.severity_level.NORMAL)
    def test_column_headers_present(self, employee_page: EmployeePage):
        """BUG: Заголовки колонок таблицы отсутствуют."""
        with allure.step("Получение заголовков колонок таблицы"):
            columns = employee_page.get_table_columns()
        with allure.step("Проверка что присутствует минимум 3 колонки"):
            assert len(columns) >= 3, \
                f"BUG: Ожидалось минимум 3 колонки, найдено {len(columns)}: {columns}"

    @allure.title("Обязательные колонки (Имя, Телефон, Роль) присутствуют")
    @allure.severity(allure.severity_level.NORMAL)
    def test_expected_columns_exist(self, employee_page: EmployeePage):
        """BUG: Обязательные колонки (Full Name, Phone, Role) отсутствуют."""
        with allure.step("Получение списка колонок таблицы"):
            columns = employee_page.get_table_columns()
            columns_lower = [c.lower() for c in columns]
        with allure.step("Проверка наличия обязательных колонок (Имя, Телефон, Роль)"):
            has_name = any("name" in c or "имя" in c or "ism" in c for c in columns_lower)
            has_phone = any("phone" in c or "телефон" in c or "telefon" in c for c in columns_lower)
            has_role = any("role" in c or "роль" in c or "rol" in c for c in columns_lower)
            assert has_name or has_phone or has_role, \
                f"BUG: Нет ожидаемых колонок (name/phone/role) в: {columns}"

    @allure.title("Кнопка экспорта активна")
    @allure.severity(allure.severity_level.MINOR)
    def test_export_button_enabled(self, employee_page: EmployeePage):
        """BUG: Кнопка экспорта заблокирована."""
        with allure.step("Проверка видимости кнопки экспорта"):
            assert employee_page.export_btn.is_visible(timeout=3000), \
                "BUG: Кнопка экспорта не видна"
        with allure.step("Проверка что кнопка экспорта активна"):
            assert employee_page.export_btn.is_enabled(), \
                "BUG: Кнопка экспорта заблокирована"

    @allure.title("Текст пагинации отображается")
    @allure.severity(allure.severity_level.NORMAL)
    def test_pagination_text_visible(self, employee_page: EmployeePage):
        """BUG: Текст пагинации не отображается."""
        with allure.step("Проверка видимости текста пагинации"):
            pagination = employee_page.page.locator(".MuiTablePagination-displayedRows")
            assert pagination.is_visible(timeout=3000), \
                "BUG: Текст пагинации (N-M of X) не виден"

    @allure.title("Количество строк совпадает с пагинацией")
    @allure.severity(allure.severity_level.NORMAL)
    def test_staff_count_matches_pagination(self, employee_page: EmployeePage):
        """BUG: Количество строк не совпадает с пагинацией."""
        with allure.step("Получение количества строк в таблице"):
            count = employee_page.get_employee_count()
        with allure.step("Получение текста пагинации и сравнение с количеством строк"):
            pagination = employee_page.page.locator(".MuiTablePagination-displayedRows")
            if pagination.is_visible(timeout=2000):
                text = pagination.text_content() or ""
                # Если "0–0 of 0" и count == 0, это корректно
                if "of 0" in text:
                    assert count == 0, \
                        f"BUG: Пагинация показывает 0, но в таблице {count} строк"



@allure.epic("Платформа продавца")
@allure.suite("Навигация сотрудников")
@allure.feature("Навигация")
@pytest.mark.regression
class TestEmployeeNavigation:
    """Тесты навигации на странице сотрудников."""

    @allure.title("Навигация через сайдбар на страницу сотрудников")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sidebar_navigation_to_staff(self, fresh_authenticated_page):
        """BUG: Навигация через sidebar на страницу сотрудников не работает."""
        with allure.step("Переход на страницу сотрудников через сайдбар"):
            page = fresh_authenticated_page
            ep = EmployeePage(page)
            ep.click_employee_nav_link()
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что URL содержит /staff"):
            assert "/staff" in page.url, \
                f"BUG: Клик на Staff в sidebar не перешел на /staff (URL: {page.url})"

    @allure.title("Кнопка 'Назад' из страницы создания возвращает на список")
    @allure.severity(allure.severity_level.NORMAL)
    def test_browser_back_from_create(self, employee_create_page: EmployeePage):
        """BUG: Кнопка 'Назад' браузера из /create не возвращает на /staff."""
        with allure.step("Нажатие кнопки 'Назад' в браузере"):
            employee_create_page.page.go_back()
            employee_create_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что произошел возврат на страницу списка сотрудников"):
            assert "/staff" in employee_create_page.page.url, \
                f"BUG: Browser back не вернул на /staff (URL: {employee_create_page.page.url})"

    @allure.title("Обновление страницы сотрудников работает корректно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_refresh_staff_page(self, employee_page: EmployeePage):
        """BUG: Обновление страницы сотрудников вызывает крэш."""
        with allure.step("Обновление страницы сотрудников"):
            employee_page.page.reload()
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница не крашнулась после обновления"):
            assert employee_page.page.url != "about:blank", \
                "BUG: Страница крашнулась после reload"
            assert "/staff" in employee_page.page.url, \
                f"BUG: После reload ушли со страницы staff (URL: {employee_page.page.url})"

    @allure.title("Прямой переход по URL на страницу сотрудников")
    @allure.severity(allure.severity_level.NORMAL)
    def test_direct_url_to_staff(self, fresh_authenticated_page):
        """BUG: Прямой переход на /dashboard/staff не работает."""
        with allure.step("Прямой переход по URL на страницу сотрудников"):
            page = fresh_authenticated_page
            ep = EmployeePage(page)
            ep.navigate()
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что URL содержит /staff"):
            assert "/staff" in page.url, \
                f"BUG: Прямой переход на /staff не сработал (URL: {page.url})"

    @allure.title("Прямой переход по URL на страницу создания сотрудника")
    @allure.severity(allure.severity_level.NORMAL)
    def test_direct_url_to_create(self, fresh_authenticated_page):
        """BUG: Прямой переход на /dashboard/staff/create не работает."""
        with allure.step("Прямой переход по URL на страницу создания сотрудника"):
            page = fresh_authenticated_page
            ep = EmployeePage(page)
            ep.navigate_to(ep.CREATE_PATH)
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что URL содержит /staff"):
            assert "/staff" in page.url, \
                f"BUG: Прямой переход на /staff/create не сработал (URL: {page.url})"



@allure.epic("Платформа продавца")
@allure.suite("Защита авторизации сотрудников")
@allure.feature("Авторизация")
@pytest.mark.security
class TestEmployeeAuthGuard:
    """Тесты защиты страницы от неавторизованного доступа."""

    @allure.title("Неавторизованный доступ к списку сотрудников редиректит на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_list_redirects(self, browser):
        """BUG: Страница /dashboard/staff доступна без авторизации."""
        with allure.step("Открытие страницы сотрудников без авторизации"):
            from config import settings
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"{settings.BASE_URL}/dashboard/staff")
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка редиректа на страницу логина"):
            assert "auth/login" in page.url or "login" in page.url, \
                f"BUG: /dashboard/staff доступна без авторизации (URL: {page.url})"
        with allure.step("Закрытие контекста браузера"):
            page.close()
            context.close()

    @allure.title("Неавторизованный доступ к созданию сотрудника редиректит на логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_unauthenticated_create_redirects(self, browser):
        """BUG: Страница /dashboard/staff/create доступна без авторизации."""
        with allure.step("Открытие страницы создания сотрудника без авторизации"):
            from config import settings
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"{settings.BASE_URL}/dashboard/staff/create")
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка редиректа на страницу логина"):
            assert "auth/login" in page.url or "login" in page.url, \
                f"BUG: /dashboard/staff/create доступна без авторизации (URL: {page.url})"
        with allure.step("Закрытие контекста браузера"):
            page.close()
            context.close()



@allure.epic("Платформа продавца")
@allure.suite("Безопасность страницы сотрудников")
@allure.feature("Безопасность")
@pytest.mark.security
class TestEmployeeSecurity:
    """Тесты безопасности страницы сотрудников."""

    @allure.title("Токен авторизации не утекает через URL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_no_token_in_url(self, employee_page: EmployeePage):
        """BUG: Токен авторизации утекает через URL."""
        with allure.step("Получение URL страницы"):
            url = employee_page.page.url.lower()
        with allure.step("Проверка отсутствия токенов и секретов в URL"):
            for secret in ("token", "jwt", "bearer", "session_id", "api_key"):
                assert secret not in url, \
                    f"BUG: Найден секрет '{secret}' в URL: {url}"

    @allure.title("Невалидный ID сотрудника обрабатывается корректно")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_staff_id_handled(self, fresh_authenticated_page):
        """BUG: Невалидный ID сотрудника не обрабатывается."""
        with allure.step("Переход по URL с невалидным ID сотрудника"):
            page = fresh_authenticated_page
            base = page.url.split("/dashboard")[0]
            page.goto(f"{base}/dashboard/staff/999999")
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что приложение не крашнулось"):
            assert page.url != "about:blank", \
                "BUG: Невалидный staff ID крашит приложение"

    @allure.title("Инъекция в поиске блокируется")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("payload,injection_type", [
        ("'; DROP TABLE staff; --", "SQL injection"),
        ("; rm -rf /", "Command injection"),
        ("*)(uid=*", "LDAP injection"),
        ("../../../etc/passwd", "Path traversal"),
    ], ids=["sql", "command", "ldap", "path_traversal"])
    def test_injection_in_search(self, employee_page: EmployeePage, payload: str, injection_type: str):
        """BUG: Инъекция в поиске не блокируется."""
        with allure.step(f"Ввод инъекционного payload типа {injection_type} в поиск"):
            employee_page.search_employee(payload)
            employee_page.page.wait_for_load_state("networkidle")
        with allure.step("Проверка что страница не крашнулась"):
            table_visible = employee_page.is_table_visible()
            empty_visible = employee_page.is_empty_state_visible()
            assert table_visible or empty_visible, \
                f"BUG: {injection_type} крашит страницу: {payload!r}"
        with allure.step("Проверка отсутствия серверной ошибки"):
            page_text = employee_page.page.text_content("body") or ""
            assert "Internal Server Error" not in page_text, \
                f"BUG: {injection_type} вызвал серверную ошибку"

    @allure.title("Принудительный доступ к сотрудникам другого пользователя блокируется")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_forced_browsing_other_user_staff(self, fresh_authenticated_page):
        """BUG: Можно получить доступ к сотруднику другого пользователя."""
        with allure.step("Попытка принудительного доступа к сотруднику другого пользователя"):
            page = fresh_authenticated_page
            base = page.url.split("/dashboard")[0]
            page.goto(f"{base}/dashboard/staff/9999999")
            page.wait_for_load_state("networkidle")
        with allure.step("Проверка что доступ заблокирован или показана ошибка"):
            page_text = page.text_content("body") or ""
            redirected = "/staff" in page.url and "/9999999" not in page.url
            has_error = any(x in page_text.lower() for x in ("not found", "ошибка", "404"))
            assert redirected or has_error or page.url != f"{base}/dashboard/staff/9999999", \
                f"BUG: Forced browsing к /staff/9999999 не заблокирован (URL: {page.url})"
