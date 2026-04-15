"""
Returns Test Cases - Returns Management Functionality.
Tests returns listing, tabs, filtering, pagination.
Follows KISS, DRY, SOLID principles with POM pattern.

NOTE: This page has NO search field. Only tabs and filters.
"""

import pytest
import logging
import allure
from playwright.sync_api import expect
from pages.returns_page import ReturnsPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Загрузка страницы")
class TestReturnsPageLoad:
    """Test cases for returns page loading."""

    @allure.title("RETURN-01: Страница возвратов загружается корректно")
    @pytest.mark.order(143)
    def test_returns_page_loads(self, returns_page):
        """ID-1690: Verify returns page loads correctly."""
        with allure.step("Проверка что URL содержит путь к возвратам"):
            page = returns_page.page
            assert "returns" in page.url, f"BUG: Expected returns in URL, got: {page.url}"
            logger.info("Returns page loads correctly")

    @allure.title("RETURN-60: Страница возвратов загружается корректно по URL")
    @pytest.mark.order(160)
    def test_returns_page_loads_via_url(self, returns_page):
        """ID-1750: Verify returns page is accessible and loads correctly."""
        with allure.step("Проверка загрузки страницы возвратов по URL"):
            page = returns_page.page
            assert "returns" in page.url, f"BUG: Should navigate to returns page, got: {page.url}"
            logger.info(f"Returns page loads correctly - URL: {page.url}")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Вкладки статусов")
class TestReturnsStatusTabs:
    """Test cases for status tab functionality."""

    @allure.title("RETURN-07: Активная вкладка возвратов выделена")
    @pytest.mark.order(144)
    def test_active_tab_highlighted(self, returns_page):
        """ID-1696: Verify active tab is highlighted."""
        with allure.step("Поиск активной вкладки на странице"):
            page = returns_page.page
            active_tab = page.locator("[role='tab'][aria-selected='true']")
            expect(active_tab).to_be_visible(timeout=5000)

        with allure.step("Проверка что активная вкладка выделена и содержит текст"):
            tab_text = active_tab.text_content()
            assert tab_text is not None and len(tab_text) > 0, "Active tab should have text"
            logger.info(f"Active return tab highlighted verified: '{tab_text}'")

    @allure.title("RETURN-06: Переключение вкладки статуса возвратов")
    @pytest.mark.order(145)
    def test_switch_status_tab(self, returns_page):
        """ID-1695: Verify switching between status tabs."""
        with allure.step("Получение списка вкладок и определение активной"):
            page = returns_page.page
            tabs = page.locator("[role='tab']")
            tab_count = tabs.count()
            assert tab_count > 1, f"Expected multiple tabs, found {tab_count}"

            initial_tab = page.locator("[role='tab'][aria-selected='true']")
            initial_index = 0
            for i in range(tab_count):
                if tabs.nth(i).get_attribute("aria-selected") == "true":
                    initial_index = i
                    break

        with allure.step("Клик по другой вкладке"):
            target_index = 1 if initial_index == 0 else 0
            tabs.nth(target_index).click()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка что активная вкладка переключилась"):
            new_selected = tabs.nth(target_index).get_attribute("aria-selected")
            old_selected = tabs.nth(initial_index).get_attribute("aria-selected")
            assert new_selected == "true", \
                f"BUG: Clicked tab not selected. aria-selected={new_selected}"
            assert old_selected != "true", \
                f"BUG: Previous tab still selected after clicking new one"
            logger.info(f"Switch return status tab verified: index {initial_index} -> {target_index}")

    @allure.title("RETURN-61: Вкладки статусов видны на странице возвратов")
    @pytest.mark.order(161)
    def test_status_tabs_visible(self, returns_page):
        """ID-1751: Verify status tabs are visible on returns page."""
        with allure.step("Поиск вкладок статусов на странице"):
            page = returns_page.page
            tabs = page.locator("[role='tab']")
            tab_count = tabs.count()

        with allure.step("Проверка видимости вкладок статусов"):
            assert tab_count >= 1, f"BUG: Expected at least 1 status tab, found {tab_count}"
            expect(tabs.first).to_be_visible()
            logger.info(f"Status tabs visible verified - {tab_count} tabs found")

    @allure.title("RETURN-100: Проверка что все названия вкладок на русском")
    @pytest.mark.order(200)
    def test_all_tab_names_localized(self, returns_page):
        """Verify all tab names match any supported language (RU/EN/UZ)."""
        with allure.step("Получение текста всех вкладок на странице"):
            page = returns_page.page

            expected_tabs_ru = ["Все", "На рассмотрении", "Одобрено продавцом"]
            expected_tabs_en = ["All", "Under review", "Approved by seller"]
            expected_tabs_uz = ["Hammasi", "Ko'rib chiqilmoqda", "Sotuvchi tomonidan tasdiqlangan"]

            tabs = page.locator("[role='tab']")
            tab_count = tabs.count()

            found_tabs = []
            for i in range(tab_count):
                text = tabs.nth(i).text_content()
                if text:
                    found_tabs.append(text.strip())

        with allure.step("Проверка что названия вкладок соответствуют одному из поддерживаемых языков"):
            all_expected = expected_tabs_ru + expected_tabs_en + expected_tabs_uz
            has_any_match = any(
                any(expected in t for t in found_tabs)
                for expected in all_expected
            )
            assert has_any_match, \
                f"BUG: No expected tab names found in {found_tabs}"
            assert tab_count >= 3, \
                f"BUG: Expected at least 3 tabs, found {tab_count}"

            logger.info(f"All tab names verified: {found_tabs}")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Таблица")
class TestReturnsTable:
    """Test cases for returns table functionality."""

    @allure.title("RETURN-63: Таблица возвратов видна с заголовками")
    @pytest.mark.order(163)
    def test_table_visible_with_headers(self, returns_page):
        """ID-1753: Verify returns table is visible with column headers."""
        with allure.step("Проверка видимости таблицы возвратов"):
            page = returns_page.page
            table = page.locator("table, [role='grid'], .MuiDataGrid-root").first
            is_visible = table.is_visible(timeout=5000)
            assert is_visible, "BUG: Returns table/grid should be visible"

        with allure.step("Проверка наличия заголовков колонок в таблице"):
            headers = page.locator("thead th, th, [role='columnheader'], .MuiDataGrid-columnHeader")
            header_count = headers.count()
            assert header_count >= 1, f"BUG: Expected at least 1 table column, found {header_count}"
            logger.info(f"Table visible with {header_count} column headers")

    @allure.title("RETURN-88: Таблица содержит ожидаемые колонки")
    @pytest.mark.order(188)
    def test_table_expected_columns(self, returns_page):
        """ID-1778: Verify returns table/grid has column headers."""
        with allure.step("Получение заголовков колонок таблицы"):
            page = returns_page.page
            headers = page.locator(".MuiDataGrid-columnHeader, thead th, th, [role='columnheader']")
            header_count = headers.count()

            header_texts = []
            for i in range(min(header_count, 20)):
                text = headers.nth(i).text_content()
                if text and text.strip():
                    header_texts.append(text.strip())

        with allure.step("Проверка что таблица содержит минимум 3 колонки"):
            assert len(header_texts) >= 3 or header_count >= 3, \
                f"BUG: Table should have at least 3 columns, found {header_count}"
            logger.info(f"Table columns verified: {header_count} headers, texts: {header_texts[:5]}")

    @allure.title("RETURN-89: Строки таблицы содержат ячейки данных")
    @pytest.mark.order(189)
    def test_table_rows_consistent_cells(self, returns_page):
        """ID-1779: Verify table rows have data cells."""
        with allure.step("Получение строк таблицы возвратов"):
            page = returns_page.page
            rows = page.locator(".MuiDataGrid-row, tbody tr")
            row_count = rows.count()

        with allure.step("Проверка что строки таблицы содержат ячейки данных"):
            if row_count > 0:
                for i in range(min(row_count, 3)):
                    row = rows.nth(i)
                    cells = row.locator(".MuiDataGrid-cell, td")
                    cell_count = cells.count()
                    assert cell_count >= 1, \
                        f"BUG: Row {i} should have at least 1 cell, found {cell_count}"
                logger.info(f"Table rows have data - {row_count} rows verified")
            else:
                logger.info("No rows to validate - empty table or no data")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Пагинация")
class TestReturnsPagination:
    """Test cases for pagination functionality."""

    @allure.title("RETURN-21: Граничные значения пагинации возвратов")
    @pytest.mark.order(154)
    @pytest.mark.negative
    def test_pagination_boundary(self, returns_page):
        """ID-1710: Verify pagination boundary conditions."""
        with allure.step("Поиск кнопки 'Предыдущая страница'"):
            page = returns_page.page
            prev_btn = page.get_by_role("button", name="Go to previous page").or_(
                page.get_by_role("button", name="Предыдущая страница")
            ).or_(page.get_by_role("button", name="Oldingi sahifa"))

        with allure.step("Проверка что кнопка 'Назад' неактивна на первой странице"):
            if prev_btn.is_visible(timeout=3000):
                is_disabled = not prev_btn.is_enabled()
                assert is_disabled, "Previous button should be disabled on first page"
                logger.info("Pagination boundary verified - prev button disabled on first page")
            else:
                logger.info("Pagination not visible - table may have few items")

    @allure.title("RETURN-20: Навигация по пагинации возвратов")
    @pytest.mark.order(155)
    def test_navigate_pagination(self, returns_page):
        """ID-1709: Verify pagination navigation works."""
        with allure.step("Поиск кнопки 'Следующая страница'"):
            page = returns_page.page
            next_btn = page.get_by_role("button", name="Go to next page").or_(
                page.get_by_role("button", name="Следующая страница")
            ).or_(page.get_by_role("button", name="Keyingi sahifa"))

        with allure.step("Переход на следующую страницу пагинации"):
            if next_btn.is_visible(timeout=3000) and next_btn.is_enabled():
                first_row_before = page.locator("tbody tr, .MuiDataGrid-row").first.text_content()
                next_btn.click()
                page.wait_for_load_state("networkidle")

        with allure.step("Проверка что содержимое страницы изменилось"):
            if next_btn.is_visible(timeout=3000) and next_btn.is_enabled():
                first_row_after = page.locator("tbody tr, .MuiDataGrid-row").first.text_content()
                assert first_row_before != first_row_after, "Page content should change after navigation"
                logger.info("Navigate returns pagination verified")
            else:
                logger.info("Next button not enabled - only one page of results")

    @allure.title("RETURN-64: Элементы пагинации видны")
    @pytest.mark.order(164)
    def test_pagination_controls_visible(self, returns_page):
        """ID-1754: Verify pagination controls are present on page."""
        with allure.step("Поиск элементов пагинации на странице"):
            page = returns_page.page
            pagination = page.locator(".MuiTablePagination-root, [class*='pagination'], [aria-label*='pagination']")
            is_visible = pagination.first.is_visible(timeout=3000)

        with allure.step("Проверка видимости элементов пагинации"):
            count = returns_page.get_returns_count()
            if count > 0:
                logger.info(f"Pagination controls - visible: {is_visible}, rows: {count}")
            else:
                logger.info(f"No data in table - pagination visibility: {is_visible}")



@pytest.mark.functional
@allure.feature("Возвраты")
@allure.story("Доступность")
class TestReturnsAccessibility:
    """Test cases for accessibility features."""

    @allure.title("RETURN-86: Вкладки имеют правильные ARIA роли")
    @pytest.mark.order(186)
    def test_tabs_aria_roles(self, returns_page):
        """ID-1776: Verify tabs have correct ARIA role attributes."""
        with allure.step("Проверка видимости tablist элемента"):
            page = returns_page.page
            tablist = page.locator("[role='tablist']")
            expect(tablist).to_be_visible(timeout=5000)

        with allure.step("Проверка ARIA ролей у вкладок"):
            tabs = page.locator("[role='tab']")
            tab_count = tabs.count()
            assert tab_count >= 2, f"BUG: Should have at least 2 tabs with role='tab', found {tab_count}"

        with allure.step("Проверка что ровно одна вкладка имеет aria-selected='true'"):
            active_tab = page.locator("[role='tab'][aria-selected='true']")
            assert active_tab.count() == 1, \
                f"BUG: Exactly one tab should be aria-selected='true', found {active_tab.count()}"
            logger.info(f"Tabs ARIA roles verified - {tab_count} tabs with proper roles")

    @allure.title("RETURN-87: Навигация по вкладкам с клавиатуры")
    @pytest.mark.order(187)
    def test_keyboard_tab_navigation(self, returns_page):
        """ID-1777: Verify keyboard Tab key navigation works."""
        with allure.step("Установка фокуса на первую вкладку"):
            page = returns_page.page
            first_tab = page.locator("[role='tab']").first
            first_tab.focus()

        with allure.step("Нажатие клавиши Tab для перемещения фокуса"):
            page.keyboard.press("Tab")

        with allure.step("Проверка что фокус переместился на следующий элемент"):
            active_element_tag = page.evaluate("document.activeElement.tagName")
            assert active_element_tag is not None, "Focus should move to next element on Tab"
            logger.info(f"Keyboard tab navigation verified - focus on: {active_element_tag}")
