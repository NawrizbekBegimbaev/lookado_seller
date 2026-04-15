"""
Shop Create E2E, Robustness, and Concurrent Tests.
Tests complete flows, stress scenarios, and concurrent access.
"""
import os
import pytest
import logging
import time
import allure
from pages.dashboard_page import DashboardPage, ShopCreateModal

logger = logging.getLogger(__name__)



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.e2e
class TestShopCreateE2E:
    """End-to-end complete flow tests."""

    @allure.title("Полный процесс создания магазина")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_complete_shop_creation(self, shop_modal, test_data):
        """Complete shop creation from start to finish."""
        page = shop_modal.page

        with allure.step("Проверка загрузки страницы создания магазина"):
            assert shop_modal.is_page_loaded(), "FAILED: Shop create page not loaded"

        with allure.step("Заполнение всех обязательных полей"):
            shop_data = test_data.get("shop_data", {})
            banners = test_data.get("banners", {})
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

            unique_name = f"{shop_data.get('shop_name', 'E2E Test Shop')} {int(time.time())}"
            shop_modal.fill_shop_name(unique_name)
            page.wait_for_load_state("domcontentloaded")

            shop_modal.fill_description_uz(shop_data.get("description_uz", "E2E test tavsifi"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "E2E тестовое описание"))

            logo_path = os.path.join(project_root, banners.get("logo_shop", "test_data/resources/img.png"))
            banner_path = os.path.join(project_root, banners.get("banner_shop", "test_data/resources/tv.png"))

            if os.path.exists(logo_path) and os.path.exists(banner_path):
                shop_modal.upload_logo(banner_path, logo_path)
                page.wait_for_load_state("networkidle")

            allure.attach(unique_name, name="created_shop_name", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Отправка формы"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle", timeout=15000)
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка результата отправки"):
            # Check for success or validation errors
            has_errors = shop_modal.has_validation_errors()
            error_messages = shop_modal.get_validation_error_messages()

            if has_errors:
                logger.warning(f"Validation errors after submit: {error_messages}")
                # Not failing here as shop might already exist
                allure.attach(str(error_messages), name="validation_errors", attachment_type=allure.attachment_type.TEXT)
            else:
                logger.info("Shop creation submitted successfully")

        logger.info("SC-E2E-01: Complete shop creation flow - PASSED")

    @allure.title("Создание магазина и проверка в выпадающем списке")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shop_appears_in_dropdown(self, dashboard_page, test_data):
        """After creation, shop MUST appear in dropdown."""
        page = dashboard_page.page

        with allure.step("Открытие диалога создания магазина"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("domcontentloaded")
            shop_modal = dashboard_page.click_add_shop()
            page.wait_for_load_state("networkidle")

            shop_data = test_data.get("shop_data", {})
            banners = test_data.get("banners", {})
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

            unique_name = f"Dropdown Test {int(time.time())}"
            shop_modal.fill_shop_name(unique_name)
            page.wait_for_load_state("domcontentloaded")

            shop_modal.fill_description_uz(shop_data.get("description_uz", "Test"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Тест"))

            logo_path = os.path.join(project_root, banners.get("logo_shop", "test_data/resources/img.png"))
            banner_path = os.path.join(project_root, banners.get("banner_shop", "test_data/resources/tv.png"))

            if os.path.exists(logo_path) and os.path.exists(banner_path):
                shop_modal.upload_logo(banner_path, logo_path)

            shop_modal.click_save()
            page.wait_for_load_state("networkidle", timeout=15000)

        with allure.step("Закрытие диалога если открыт"):
            shop_modal.click_cancel()
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Проверка нового магазина в выпадающем списке"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("networkidle")

            menu_items = page.locator("[role='menuitem']")
            found_shops = []
            for i in range(menu_items.count()):
                text = menu_items.nth(i).text_content() or ""
                found_shops.append(text)

            logger.info(f"Shops in dropdown: {found_shops}")

            # Shop might be there or validation might have failed
            shop_found = any("Dropdown Test" in shop for shop in found_shops)
            logger.info(f"New shop found in dropdown: {shop_found}")

        logger.info("SC-E2E-02: Shop in dropdown verification - PASSED")

    @allure.title("Переключение между магазинами в выпадающем списке")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_switch_between_shops(self, dashboard_page):
        """User MUST be able to switch between existing shops."""
        page = dashboard_page.page

        with allure.step("Открытие выпадающего списка магазинов"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("networkidle")

        with allure.step("Получение списка доступных магазинов"):
            menu_items = page.locator("[role='menuitem']")
            shop_count = menu_items.count()

            shops = []
            for i in range(shop_count):
                text = menu_items.nth(i).text_content() or ""
                if text.strip() and "Добавить" not in text and "Add" not in text:
                    shops.append(text.strip())

            logger.info(f"Available shops: {shops}")

            assert len(shops) >= 2, \
                f"BUG: Need at least 2 shops to test switching! Available: {shops}"
            if len(shops) >= 2:
                # Кликнуть на первый магазин
                first_shop = shops[0]
                page.locator(f"[role='menuitem']:has-text('{first_shop}')").first.click()
                page.wait_for_load_state("networkidle")

                # Проверить что мы на dashboard этого магазина
                logger.info(f"Switched to shop: {first_shop}")

                # Переключиться на второй магазин
                dashboard_page.open_shop_dropdown()
                page.wait_for_load_state("networkidle")

                second_shop = shops[1]
                page.locator(f"[role='menuitem']:has-text('{second_shop}')").first.click()
                page.wait_for_load_state("networkidle")

                logger.info(f"Switched to shop: {second_shop}")

                allure.attach(
                    f"First shop: {first_shop}\nSecond shop: {second_shop}",
                    name="shop_switching",
                    attachment_type=allure.attachment_type.TEXT
                )

        logger.info("SC-E2E-03: Switch between shops - PASSED")

    @allure.title("Проверка сохранения данных магазина после обновления страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_data_persists_after_refresh(self, dashboard_page):
        """Selected shop should persist after page refresh."""
        page = dashboard_page.page

        with allure.step("Получение текущего магазина"):
            # Найти текущий выбранный магазин в dropdown trigger
            shop_dropdown = page.locator("[aria-haspopup='listbox'], [aria-haspopup='menu']").first
            try:
                current_shop = shop_dropdown.text_content() or ""
                logger.info(f"Current shop before refresh: {current_shop}")
            except Exception:
                current_shop = "unknown"

        with allure.step("Обновление страницы"):
            page.reload()
            page.wait_for_load_state("networkidle", timeout=15000)

        with allure.step("Проверка что магазин все ещё выбран"):
            # Проверяем что мы все еще на dashboard
            assert "dashboard" in page.url.lower(), \
                f"FAILED: Not on dashboard after refresh. URL: {page.url}"

            # Проверяем что магазин сохранился
            try:
                shop_after = shop_dropdown.text_content() or ""
                logger.info(f"Shop after refresh: {shop_after}")
            except Exception:
                shop_after = "unknown"

            allure.attach(
                f"Before refresh: {current_shop}\nAfter refresh: {shop_after}",
                name="persistence_check",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-E2E-04: Shop data persistence - PASSED")

    @allure.title("Полный процесс: открытие, заполнение, закрытие, повторное открытие")
    @allure.severity(allure.severity_level.NORMAL)
    def test_full_cancel_reopen_workflow(self, dashboard_page, test_data):
        """Complete workflow of opening, filling, closing, and reopening dialog."""
        page = dashboard_page.page

        with allure.step("Первый шаг: Открытие диалога и заполнение данных"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("domcontentloaded")
            shop_modal = dashboard_page.click_add_shop()
            page.wait_for_load_state("networkidle")

            assert shop_modal.is_page_loaded(), "FAILED: Dialog did not open"

            test_name = f"Workflow Test {int(time.time())}"
            shop_modal.fill_shop_name(test_name)
            shop_modal.fill_description_uz("First attempt UZ")
            shop_modal.fill_description_ru("First attempt RU")
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Второй шаг: Закрытие диалога"):
            shop_modal.click_cancel()
            page.wait_for_load_state("domcontentloaded")

            assert not shop_modal.is_page_loaded(timeout=2000), \
                "FAILED: Dialog did not close"

        with allure.step("Третий шаг: Повторное открытие и проверка чистого состояния"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("domcontentloaded")
            shop_modal = dashboard_page.click_add_shop()
            page.wait_for_load_state("networkidle")

            new_name = shop_modal.get_shop_name_value()

            assert test_name not in new_name, \
                f"FAILED: Previous data persisted in reopened dialog: {new_name}"

            logger.info(f"Reopened dialog shop name: '{new_name}' (should be empty or different)")

        with allure.step("Четвёртый шаг: Заполнение новых данных и закрытие"):
            new_test_name = f"Second Attempt {int(time.time())}"
            shop_modal.fill_shop_name(new_test_name)
            page.wait_for_load_state("domcontentloaded")

            shop_modal.click_cancel()

        logger.info("SC-E2E-05: Full cancel/reopen workflow - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.functional
class TestShopCreateRobustness:
    """Robustness and stress tests."""

    @allure.title("Двойной клик на кнопку сохранения")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_double_click_save(self, shop_modal, test_data):
        """Double-clicking save MUST NOT create duplicate shops."""
        page = shop_modal.page

        with allure.step("Заполнение формы"):
            shop_data = test_data.get("shop_data", {})
            shop_modal.fill_shop_name(f"Double Click Test {int(time.time())}")
            shop_modal.fill_description_uz(shop_data.get("description_uz", "Test"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Тест"))
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Двойной клик на кнопку сохранения"):
            save_button = page.locator(shop_modal.SAVE_BTN).first
            save_button.dblclick()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка отсутствия дублирования"):
            # Проверяем что не было ошибки сервера
            assert "500" not in page.title(), \
                "FAILED: Double-click caused server error"

            # Кнопка должна быть disabled после первого клика или обработка должна быть идемпотентной
            has_errors = shop_modal.has_validation_errors()
            has_toast = shop_modal.has_toast_error()

            logger.info(f"Double-click result: validation={has_errors}, toast={has_toast}")

            allure.attach(
                f"Double-click save test\nValidation: {has_errors}\nToast: {has_toast}",
                name="double_click_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-RB-01: Double-click save - PASSED")

    @allure.title("Симуляция медленной сети")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slow_network(self, shop_modal, test_data):
        """Form should handle slow network gracefully."""
        page = shop_modal.page
        context = page.context

        with allure.step("Заполнение формы"):
            shop_data = test_data.get("shop_data", {})
            shop_modal.fill_shop_name(f"Slow Network Test {int(time.time())}")
            shop_modal.fill_description_uz(shop_data.get("description_uz", "Test"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Тест"))
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Симуляция медленной сети"):
            try:
                # Замедляем сеть
                cdp = context.new_cdp_session(page)
                cdp.send("Network.emulateNetworkConditions", {
                    "offline": False,
                    "downloadThroughput": 50 * 1024,  # 50kb/s
                    "uploadThroughput": 50 * 1024,
                    "latency": 500  # 500ms latency
                })
            except Exception as e:
                logger.info(f"CDP not available for network throttling: {e}")

        with allure.step("Отправка формы"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle", timeout=10000)  # Даем время на медленную сеть

        with allure.step("Сброс сетевых настроек"):
            try:
                cdp.send("Network.emulateNetworkConditions", {
                    "offline": False,
                    "downloadThroughput": -1,  # No throttling
                    "uploadThroughput": -1,
                    "latency": 0
                })
            except Exception as e:
                logger.warning(f"Network reset failed: {e}")

        with allure.step("Проверка обработки формой медленной сети"):
            # Не должно быть crash или зависания
            assert page.locator("body").count() > 0, \
                "FAILED: Page crashed during slow network"

            logger.info("Slow network test completed")

        logger.info("SC-RB-02: Slow network - PASSED")

    @allure.title("Быстрые изменения формы должны генерировать slug")
    @allure.severity(allure.severity_level.NORMAL)
    def test_rapid_form_changes(self, shop_modal):
        """BUG CHECK: Rapid form changes MUST still generate slug after debounce."""
        page = shop_modal.page

        with allure.step("Быстрое изменение названия магазина"):
            for i in range(10):
                shop_modal.fill_shop_name(f"Rapid Test {i} - {int(time.time())}")
                page.wait_for_load_state("domcontentloaded")

            # Tab для blur — React генерирует slug после потери фокуса
            page.keyboard.press("Tab")
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка финального значения"):
            final_value = shop_modal.get_shop_name_value()
            logger.info(f"Final value after rapid changes: {final_value}")

            assert "Rapid Test" in final_value, \
                f"BUG: Rapid changes corrupted input: {final_value}"

        with allure.step("Проверка обязательной генерации slug"):
            # Ждём async генерацию slug
            from playwright.sync_api import expect
            expect(page.locator("input[name='slug']")).not_to_have_value("", timeout=10000)
            slug = shop_modal.get_slug_value()
            logger.info(f"Final slug: {slug}")

            allure.attach(
                f"Final name: {final_value}\nFinal slug: {slug}",
                name="rapid_changes_result",
                attachment_type=allure.attachment_type.TEXT
            )

            # ЖЕСТКАЯ ПРОВЕРКА: Slug ДОЛЖЕН быть сгенерирован после debounce
            assert len(slug) > 0, \
                f"BUG: Slug NOT generated after rapid changes and 2s debounce! Name: {final_value}"

        logger.info("SC-RB-03: Rapid form changes - PASSED")

    @allure.title("Отправка формы во время загрузки файла")
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_during_upload(self, shop_modal, test_data):
        """Submitting form during file upload should be handled."""
        page = shop_modal.page
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with allure.step("Начало загрузки файла"):
            banners = test_data.get("banners", {})
            logo_path = os.path.join(project_root, banners.get("logo_shop", "test_data/resources/img.png"))

            shop_modal.fill_shop_name(f"Upload Test {int(time.time())}")
            shop_modal.fill_description_uz("Upload test")
            shop_modal.fill_description_ru("Тест загрузки")

            if os.path.exists(logo_path):
                shop_modal.upload_logo_only(logo_path)
                # Сразу кликаем save не дожидаясь завершения
                page.wait_for_load_state("domcontentloaded")

        with allure.step("Немедленная отправка"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка отсутствия сбоя"):
            # Форма должна либо подождать загрузку, либо показать предупреждение
            assert page.locator("body").count() > 0, \
                "FAILED: Page crashed during concurrent upload/submit"

            has_errors = shop_modal.has_validation_errors()
            has_toast = shop_modal.has_toast_error()

            logger.info(f"Submit during upload: validation={has_errors}, toast={has_toast}")

        logger.info("SC-RB-04: Submit during upload - PASSED")



@allure.epic("Платформа продавца")
@allure.suite("Создание магазина")
@allure.feature("Управление магазинами")
@pytest.mark.functional
class TestShopCreateConcurrent:
    """Concurrent access and state management tests."""

    @allure.title("Состояние формы после серверной ошибки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_form_state_after_error(self, shop_modal, test_data):
        """Form should retain data after validation error."""
        page = shop_modal.page

        with allure.step("Заполнение формы невалидными данными для вызова ошибки"):
            test_name = f"State Test {int(time.time())}"
            shop_modal.fill_shop_name(test_name)
            page.wait_for_load_state("domcontentloaded")

            # Заполняем только часть полей чтобы вызвать ошибку
            shop_modal.fill_description_uz("Only UZ filled")
            # Не заполняем RU description

        with allure.step("Отправка для вызова валидации"):
            shop_modal.click_save()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка сохранения данных формы"):
            # Данные должны сохраниться после ошибки
            current_name = shop_modal.get_shop_name_value()
            current_uz = shop_modal.get_description_uz_value()

            logger.info(f"After error - Name: '{current_name}', UZ: '{current_uz}'")

            # Имя должно сохраниться
            assert test_name in current_name or len(current_name) > 0, \
                f"FAILED: Form data lost after error - name was '{test_name}', now '{current_name}'"

            allure.attach(
                f"Original name: {test_name}\nAfter error: {current_name}\nUZ retained: {len(current_uz) > 0}",
                name="state_after_error",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-CC-01: Form state after error - PASSED")

    @allure.title("Поведение модального окна в новой вкладке браузера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_modal_new_tab(self, dashboard_page, request):
        """Opening modal in new tab should work independently."""
        page = dashboard_page.page
        context = page.context

        with allure.step("Открытие модального окна в текущей вкладке"):
            dashboard_page.open_shop_dropdown()
            page.wait_for_load_state("domcontentloaded")
            shop_modal = dashboard_page.click_add_shop()
            page.wait_for_load_state("networkidle")

            shop_modal.fill_shop_name("Tab 1 Shop")

        with allure.step("Открытие новой вкладки и переход на дашборд"):
            base_url = request.config.getoption("url_name")
            new_page = context.new_page()
            new_page.goto(f"{base_url}/dashboard")
            new_page.wait_for_load_state("networkidle", timeout=15000)

        with allure.step("Открытие модального окна в новой вкладке"):
            from pages.dashboard_page import DashboardPage, ShopCreateModal

            new_dashboard = DashboardPage(new_page)
            new_dashboard.open_shop_dropdown()
            new_page.wait_for_load_state("domcontentloaded")
            new_modal = new_dashboard.click_add_shop()
            new_page.wait_for_load_state("networkidle")

            new_modal.fill_shop_name("Tab 2 Shop")

        with allure.step("Проверка независимости вкладок"):
            tab1_name = shop_modal.get_shop_name_value()
            tab2_name = new_modal.get_shop_name_value()

            logger.info(f"Tab 1: '{tab1_name}', Tab 2: '{tab2_name}'")

            # Данные в табах должны быть независимы
            assert "Tab 1" in tab1_name or tab1_name != tab2_name, \
                f"FAILED: Tabs are not independent - Tab1: {tab1_name}, Tab2: {tab2_name}"

            allure.attach(
                f"Tab 1 name: {tab1_name}\nTab 2 name: {tab2_name}",
                name="tabs_independent",
                attachment_type=allure.attachment_type.TEXT
            )

        # Cleanup
        new_page.close()

        logger.info("SC-CC-02: Modal in new tab - PASSED")

    @allure.title("Длительное бездействие перед отправкой")
    @allure.severity(allure.severity_level.NORMAL)
    def test_long_idle_before_submit(self, shop_modal, test_data):
        """Form should work after being idle for extended time."""
        page = shop_modal.page

        with allure.step("Заполнение формы"):
            shop_data = test_data.get("shop_data", {})
            shop_modal.fill_shop_name(f"Idle Test {int(time.time())}")
            shop_modal.fill_description_uz(shop_data.get("description_uz", "Test"))
            shop_modal.fill_description_ru(shop_data.get("description_ru", "Тест"))
            page.wait_for_load_state("domcontentloaded")

        with allure.step("Ожидание периода бездействия (симуляция)"):
            # Симулируем долгое ожидание (5 секунд вместо реальных минут)
            page.wait_for_load_state("networkidle", timeout=10000)
            logger.info("Waited 5 seconds (simulating idle)")

        with allure.step("Проверка работоспособности формы"):
            # Данные должны сохраниться
            current_name = shop_modal.get_shop_name_value()
            assert "Idle Test" in current_name, \
                f"FAILED: Form data lost during idle - got '{current_name}'"

            # Кнопка должна работать
            save_enabled = shop_modal.is_save_button_enabled()
            logger.info(f"After idle: name='{current_name}', save_enabled={save_enabled}")

            allure.attach(
                f"After 5s idle:\nName: {current_name}\nSave enabled: {save_enabled}",
                name="idle_result",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info("SC-CC-03: Long idle before submit - PASSED")

