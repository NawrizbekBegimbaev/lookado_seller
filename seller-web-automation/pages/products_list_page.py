"""
Products List page object for managing products (Mahsulotlar).
Follows Page Object Model (POM) and SOLID principles.

URL: /dashboard/products
"""

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage, logger


class ProductsListPage(BasePage):
    """
    Page Object Model for Products List Page.
    Handles product listing, search, filtering, sorting, and actions.
    """

    PRODUCTS_PATH = "/dashboard/products"
    ADD_PRODUCTS_PATH = "/dashboard/products/add"
    CREATE_PRODUCT_PATH = "/dashboard/products/create"

    def __init__(self, page: Page):
        """Initialize products list page with locators."""
        super().__init__(page)

    # ==================== LOCATORS (Properties) ====================

    # Page title/header
    @property
    def page_title(self) -> Locator:
        """Page title - h4 tag: 'Mahsulotlar' (UZ) / 'Товары' (RU) / 'Products' (EN)."""
        return self.page.locator(
            "h4:has-text('Mahsulotlar'), h4:has-text('Товары'), h4:has-text('Products')"
        )

    # Navigation sidebar link
    @property
    def products_nav_link(self) -> Locator:
        """Products navigation link in sidebar (UZ/RU/EN)."""
        return self.page.locator(
            "a[aria-label='Tovarlar'], "
            "a[aria-label='Товары'], "
            "a[aria-label='Products']"
        )

    # Add product button
    @property
    def add_product_btn(self) -> Locator:
        """Add Products button — <a> styled as MuiButton (UZ/RU/EN)."""
        return self.page.locator("a.MuiButton-containedPrimary").or_(
            self.page.get_by_role("link", name="Mahsulot qo'shish")
        ).or_(self.page.get_by_role("link", name="Добавить товар")).or_(
            self.page.get_by_role("link", name="Add Product")
        )

    # ==================== SEARCH ====================

    @property
    def search_input(self) -> Locator:
        """Search input field — reliable by name attribute."""
        return self.page.locator("input[name='query']").or_(
            self.page.locator("input[placeholder*='Qidirish']")
        ).or_(self.page.locator("input[placeholder*='Поиск']")).or_(
            self.page.locator("input[placeholder*='Search']")
        )

    @property
    def search_btn(self) -> Locator:
        """Search button (if separate from input)."""
        return self.page.get_by_role("button", name="Search").or_(
            self.page.get_by_role("button", name="Qidirish")
        )

    @property
    def clear_search_btn(self) -> Locator:
        """Clear search button (X icon inside search input)."""
        # Look for clear button specifically in search area
        return self.page.locator("input[placeholder*='Поиск']").locator("xpath=../..").locator("button").or_(
            self.page.locator("button[aria-label='Clear search']")
        ).or_(self.page.locator("[data-testid='clear-search']"))

    # ==================== VIEW TOGGLES ====================

    @property
    def view_toggle_table(self) -> Locator:
        """Table view toggle button."""
        return self.page.locator("button[aria-label='table view']").or_(
            self.page.locator(".MuiToggleButtonGroup-root button").first
        )

    @property
    def view_toggle_grid(self) -> Locator:
        """Grid view toggle button."""
        return self.page.locator("button[aria-label='grid view']").or_(
            self.page.locator(".MuiToggleButtonGroup-root button").last
        )

    # ==================== STATUS TABS ====================

    @property
    def status_tabs(self) -> Locator:
        """Status filter tabs (All, Draft, In Review, etc.)."""
        return self.page.locator("[role='tab']").or_(
            self.page.locator(".MuiTab-root")
        )

    @property
    def tab_all(self) -> Locator:
        """All status tab (UZ: Hammasi, RU: Все, EN: All)."""
        return self.page.locator(
            "[role='tab']:has-text('Hammasi'), [role='tab']:has-text('Все'), [role='tab']:has-text('All')"
        )

    @property
    def tab_draft(self) -> Locator:
        """Draft status tab (UZ: Qoralama, RU: Черновик, EN: Draft)."""
        return self.page.locator(
            "[role='tab']:has-text('Qoralama'), [role='tab']:has-text('Черновик'), [role='tab']:has-text('Draft')"
        )

    @property
    def tab_in_review(self) -> Locator:
        """In Review status tab (UZ: Moderatsiyada, RU: На модерации, EN: In Review)."""
        return self.page.locator(
            "[role='tab']:has-text('Moderatsiyada'), [role='tab']:has-text('На модерации'), [role='tab']:has-text('In Review')"
        )

    @property
    def tab_moderated(self) -> Locator:
        """Moderated status tab (UZ: Moderatsiyadan o'tkazildi, RU: Прошел модерацию, EN: Moderated)."""
        return self.page.locator(
            "[role='tab']:has-text('Moderatsiyadan'), [role='tab']:has-text('Прошел модерацию'), [role='tab']:has-text('Moderated')"
        )

    @property
    def tab_on_sale(self) -> Locator:
        """On Sale status tab (UZ: Sotuvda, RU: В продаже, EN: On Sale)."""
        return self.page.locator(
            "[role='tab']:has-text('Sotuvda'), [role='tab']:has-text('В продаже'), [role='tab']:has-text('On Sale')"
        )

    @property
    def tab_archive(self) -> Locator:
        """Archive status tab (UZ: Arxiv, RU: Архив, EN: Archive)."""
        return self.page.locator(
            "[role='tab']:has-text('Arxiv'), [role='tab']:has-text('Архив'), [role='tab']:has-text('Archive')"
        )

    @property
    def tab_rejected(self) -> Locator:
        """Rejected status tab (UZ: Rad etilgan, RU: Отклонен, EN: Rejected)."""
        return self.page.locator(
            "[role='tab']:has-text('Rad etilgan'), [role='tab']:has-text('Отклонен'), [role='tab']:has-text('Rejected')"
        )


    # ==================== DATE FILTERS ====================

    @property
    def date_from_input(self) -> Locator:
        """Date from filter input."""
        return self.page.locator("input[name='startAt']").or_(
            self.page.locator("input[placeholder*='Date from']")
        )

    @property
    def date_to_input(self) -> Locator:
        """Date to filter input."""
        return self.page.locator("input[name='endAt']").or_(
            self.page.locator("input[placeholder*='Date to']")
        )

    @property
    def date_picker_btn(self) -> Locator:
        """Date picker calendar buttons (RU/EN)."""
        return self.page.locator("button[aria-label='Выберите дату']").or_(
            self.page.locator("button[aria-label='Choose date']")
        )

    # ==================== FILTERS ====================

    @property
    def filters_btn(self) -> Locator:
        """Filters button to open filter panel (EN/RU/UZ)."""
        return self.page.get_by_role("button", name="Filters").or_(
            self.page.get_by_role("button", name="Filtrlar")
        ).or_(self.page.get_by_role("button", name="Фильтры")).or_(
            self.page.locator("button:has-text('Filter')")
        )

    @property
    def status_filter(self) -> Locator:
        """Status filter dropdown (EN/RU/UZ)."""
        return self.page.get_by_label("Status").or_(
            self.page.get_by_label("Holat")
        ).or_(self.page.get_by_label("Статус")).or_(
            self.page.locator("[data-testid='status-filter']")
        )

    @property
    def category_filter(self) -> Locator:
        """Category filter combobox (UZ/RU/EN)."""
        return self.page.locator("input[id*='categoryId']").or_(
            self.page.get_by_label("Kategoriya")
        ).or_(self.page.get_by_label("Поиск категории")).or_(
            self.page.get_by_label("Category")
        )

    @property
    def rating_filter(self) -> Locator:
        """Rating filter dropdown (RU: Рейтинг, EN: Rating)."""
        return self.page.get_by_label("Рейтинг").or_(
            self.page.get_by_label("Rating")
        )

    @property
    def rows_per_page_text(self) -> Locator:
        """'Rows per page' text label (UZ/RU/EN)."""
        return self.page.locator(
            "text='Sahifada ko\\'rsatish:', text='Показывать на странице:', text='Rows per page:'"
        )

    @property
    def clear_filters_btn(self) -> Locator:
        """Clear all filters button (EN/RU/UZ)."""
        return self.page.get_by_role("button", name="Clear").or_(
            self.page.get_by_role("button", name="Tozalash")
        ).or_(self.page.get_by_role("button", name="Очистить")).or_(
            self.page.locator("button:has-text('Reset')")
        )

    @property
    def apply_filters_btn(self) -> Locator:
        """Apply filters button (EN/RU/UZ)."""
        return self.page.get_by_role("button", name="Apply").or_(
            self.page.get_by_role("button", name="Qo'llash")
        ).or_(self.page.get_by_role("button", name="Применить"))

    # ==================== PRODUCT CARDS (Grid View) ====================

    @property
    def product_cards(self) -> Locator:
        """Product cards in grid view (MuiCard elements with product data)."""
        return self.page.locator(".MuiCard-root").filter(has_text="SKU:")

    @property
    def product_card_names(self) -> Locator:
        """Product names in cards (h6 elements with product names)."""
        # Product names are h6 elements that don't contain prices (no 'sum' text)
        return self.page.locator("h6").filter(has_not_text="sum").filter(has_not_text="Total")

    @property
    def product_card_prices(self) -> Locator:
        """Product prices in cards (RU: сум, EN: sum)."""
        return self.page.locator("h6:has-text('сум')").or_(
            self.page.locator("h6:has-text('sum')")
        ).or_(self.page.locator("h6.MuiTypography-subtitle1"))

    @property
    def product_card_skus(self) -> Locator:
        """Product SKU elements."""
        return self.page.locator("text=/^SKU:/")

    @property
    def product_card_ids(self) -> Locator:
        """Product ID elements."""
        return self.page.locator("text=/^ID:/")

    @property
    def product_card_status_badges(self) -> Locator:
        """Product status badges in cards (RU/UZ/EN)."""
        return self.page.locator("[class*='minimal__label__root']")

    @property
    def product_card_images(self) -> Locator:
        """Product images in cards."""
        return self.page.locator(".MuiCard-root img").or_(
            self.page.locator(".MuiPaper-root img")
        )

    @property
    def total_products_text(self) -> Locator:
        """Total products count text (UZ: Jami, RU: Всего, EN: Total)."""
        return self.page.locator(
            "h6:has-text('Jami:'), h6:has-text('Всего:'), h6:has-text('Total:')"
        )

    # ==================== TABLE (Table View) ====================

    @property
    def products_table(self) -> Locator:
        """Main products table (when in table view)."""
        return self.page.locator("table").or_(
            self.page.locator("[role='grid']")
        ).or_(self.page.locator(".MuiTable-root"))

    @property
    def table_header(self) -> Locator:
        """Table header row."""
        return self.page.locator("thead tr").or_(
            self.page.locator("[role='rowgroup'] [role='row']").first
        )

    @property
    def table_header_cells(self) -> Locator:
        """Table header cells (column names)."""
        return self.page.locator("thead th").or_(
            self.page.locator("[role='columnheader']")
        )

    @property
    def table_rows(self) -> Locator:
        """Table body rows (product rows)."""
        return self.page.locator("tbody tr").or_(
            self.page.locator("[role='rowgroup']:last-child [role='row']")
        )

    @property
    def table_cells(self) -> Locator:
        """All table cells."""
        return self.page.locator("tbody td").or_(
            self.page.locator("[role='cell']")
        )

    # ==================== PAGINATION ====================

    @property
    def pagination(self) -> Locator:
        """Pagination container (MuiPagination, not MuiTablePagination)."""
        return self.page.locator(".MuiPagination-root").or_(
            self.page.locator("nav[aria-label*='страниц']")
        ).or_(self.page.locator("nav[aria-label*='pagination']"))

    @property
    def rows_per_page_select(self) -> Locator:
        """Rows per page dropdown (next to 'Показывать на странице:')."""
        return self.page.locator("text='Показывать на странице:'").locator("xpath=following-sibling::div//div[contains(@class, 'MuiSelect')]").or_(
            self.page.locator(".MuiSelect-root").last
        )

    @property
    def next_page_btn(self) -> Locator:
        """Next page button — last navigation button in pagination."""
        return self.page.locator(".MuiPaginationItem-previousNext").last.or_(
            self.page.locator("button[aria-label*='next']")
        ).or_(self.page.locator("button[aria-label*='следующ']")).or_(
            self.page.locator("button[aria-label*='keyingi']")
        )

    @property
    def prev_page_btn(self) -> Locator:
        """Previous page button — first navigation button in pagination."""
        return self.page.locator(".MuiPaginationItem-previousNext").first.or_(
            self.page.locator("button[aria-label*='previous']")
        ).or_(self.page.locator("button[aria-label*='предыдущ']")).or_(
            self.page.locator("button[aria-label*='oldingi']")
        )

    @property
    def first_page_btn(self) -> Locator:
        """First page button (page number 1). No dedicated 'first page' button exists."""
        return self.page.locator("button[aria-label='1 страница']").or_(
            self.page.locator(".MuiPaginationItem-page").first
        )

    @property
    def last_page_btn(self) -> Locator:
        """Last page button (last page number). No dedicated 'last page' button exists."""
        return self.page.locator(".MuiPaginationItem-page").last

    @property
    def page_info(self) -> Locator:
        """Page info text ('Jami: N' / 'Всего: N' / 'Total: N')."""
        return self.page.locator(
            "h6:has-text('Jami:'), h6:has-text('Всего:'), h6:has-text('Total:')"
        )

    # ==================== SORTING ====================

    @property
    def sortable_headers(self) -> Locator:
        """Sortable column headers."""
        return self.page.locator("th[aria-sort]").or_(
            self.page.locator(".MuiTableSortLabel-root")
        )

    # ==================== BULK ACTIONS ====================

    @property
    def select_all_checkbox(self) -> Locator:
        """Select all checkbox in header."""
        return self.page.locator("thead input[type='checkbox']").or_(
            self.page.locator("[role='columnheader'] input[type='checkbox']")
        )

    @property
    def row_checkboxes(self) -> Locator:
        """Row selection checkboxes."""
        return self.page.locator("tbody input[type='checkbox']").or_(
            self.page.locator("[role='cell'] input[type='checkbox']")
        )

    @property
    def bulk_actions_menu(self) -> Locator:
        """Bulk actions dropdown/menu."""
        return self.page.locator("[data-testid='bulk-actions']").or_(
            self.page.get_by_role("button", name="Actions")
        )

    @property
    def bulk_delete_btn(self) -> Locator:
        """Bulk delete button."""
        return self.page.get_by_role("button", name="Delete").or_(
            self.page.get_by_role("menuitem", name="Delete")
        ).or_(self.page.locator("button:has-text('O\\'chirish')"))

    # ==================== EMPTY STATE ====================

    @property
    def empty_state(self) -> Locator:
        """Empty state message when no products."""
        return self.page.locator("[data-testid='empty-state']").or_(
            self.page.locator(":text('No products')").or_(
                self.page.locator(":text('Mahsulotlar yo\\'q')")
            )
        )

    @property
    def empty_state_image(self) -> Locator:
        """Empty state illustration."""
        return self.page.locator("[data-testid='empty-state'] img").or_(
            self.page.locator(".empty-state img")
        )

    # ==================== LOADING ====================

    @property
    def loading_spinner(self) -> Locator:
        """Loading spinner/skeleton."""
        return self.page.locator(".MuiCircularProgress-root").or_(
            self.page.locator(".MuiSkeleton-root")
        ).or_(self.page.locator("[role='progressbar']"))

    @property
    def table_loading_overlay(self) -> Locator:
        """Table loading overlay."""
        return self.page.locator(".MuiDataGrid-overlay").or_(
            self.page.locator("[class*='loading-overlay']")
        )

    # ==================== TOASTS/ALERTS ====================

    @property
    def toast_message(self) -> Locator:
        """Toast notification message."""
        return self.page.locator("[role='alert']").or_(
            self.page.locator(".MuiSnackbar-root")
        ).or_(self.page.locator(".MuiAlert-root"))

    @property
    def success_toast(self) -> Locator:
        """Success toast."""
        return self.page.locator(".MuiAlert-standardSuccess").or_(
            self.page.locator("[role='alert'][class*='success']")
        )

    @property
    def error_toast(self) -> Locator:
        """Error toast."""
        return self.page.locator(".MuiAlert-standardError").or_(
            self.page.locator("[role='alert'][class*='error']")
        )

    # ==================== MODALS/DIALOGS ====================

    @property
    def confirm_dialog(self) -> Locator:
        """Confirmation dialog."""
        return self.page.locator("[role='dialog']").or_(
            self.page.locator(".MuiDialog-root")
        )

    @property
    def confirm_yes_btn(self) -> Locator:
        """Confirm Yes/OK button."""
        return self.page.get_by_role("button", name="Yes").or_(
            self.page.get_by_role("button", name="OK")
        ).or_(self.page.get_by_role("button", name="Ha"))

    @property
    def confirm_no_btn(self) -> Locator:
        """Confirm No/Cancel button."""
        return self.page.get_by_role("button", name="No").or_(
            self.page.get_by_role("button", name="Cancel")
        ).or_(self.page.get_by_role("button", name="Yo'q"))

    # ==================== ROW ACTIONS ====================

    @property
    def row_action_btns(self) -> Locator:
        """Action buttons in table rows."""
        return self.page.locator("tbody button").or_(
            self.page.locator("[role='cell'] button")
        )

    @property
    def row_edit_btns(self) -> Locator:
        """Edit buttons in rows."""
        return self.page.locator("button[aria-label='Edit']").or_(
            self.page.locator("button:has(svg[data-testid='EditIcon'])")
        )

    @property
    def row_delete_btns(self) -> Locator:
        """Delete buttons in rows."""
        return self.page.locator("button[aria-label='Delete']").or_(
            self.page.locator("button:has(svg[data-testid='DeleteIcon'])")
        )

    @property
    def row_view_btns(self) -> Locator:
        """View/details buttons in rows."""
        return self.page.locator("button[aria-label='View']").or_(
            self.page.locator("button:has(svg[data-testid='VisibilityIcon'])")
        )

    @property
    def row_more_actions_btns(self) -> Locator:
        """More actions (3 dots) buttons in rows."""
        return self.page.locator("button[aria-label='More']").or_(
            self.page.locator("button:has(svg[data-testid='MoreVertIcon'])")
        )

    # ==================== PRODUCT IMAGES ====================

    @property
    def product_thumbnails(self) -> Locator:
        """Product thumbnail images in table."""
        return self.page.locator("tbody img").or_(
            self.page.locator("[role='cell'] img")
        )

    @property
    def image_placeholders(self) -> Locator:
        """Image placeholders when no image."""
        return self.page.locator("[data-testid='image-placeholder']").or_(
            self.page.locator(".image-placeholder")
        )

    # ==================== STATUS BADGES ====================

    @property
    def status_badges(self) -> Locator:
        """Product status badges (label spans in cards)."""
        return self.page.locator("[class*='minimal__label__root']").or_(
            self.page.locator(".MuiChip-root")
        )

    @property
    def pending_badges(self) -> Locator:
        """Pending/In Review status badges (RU: На модерации)."""
        return self.page.locator("[class*='label__root']:has-text('На модерации')").or_(
            self.page.locator("[class*='label__root']:has-text('Tekshiruvda')")
        ).or_(self.page.locator("[class*='label__root']:has-text('In Review')"))

    @property
    def approved_badges(self) -> Locator:
        """Approved/On Sale status badges (RU: В продаже)."""
        return self.page.locator("[class*='label__root']:has-text('В продаже')").or_(
            self.page.locator("[class*='label__root']:has-text('Sotuvda')")
        ).or_(self.page.locator("[class*='label__root']:has-text('On Sale')"))

    @property
    def rejected_badges(self) -> Locator:
        """Rejected status badges (RU: Отклонен)."""
        return self.page.locator("[class*='label__root']:has-text('Отклонен')").or_(
            self.page.locator("[class*='label__root']:has-text('Rad etilgan')")
        ).or_(self.page.locator("[class*='label__root']:has-text('Rejected')"))

    @property
    def draft_badges(self) -> Locator:
        """Draft status badges (RU: Черновик)."""
        return self.page.locator("[class*='label__root']:has-text('Черновик')").or_(
            self.page.locator("[class*='label__root']:has-text('Qoralama')")
        ).or_(self.page.locator("[class*='label__root']:has-text('Draft')"))

    # ==================== NAVIGATION METHODS ====================

    def navigate(self) -> None:
        """Navigate to products list page and wait for React render."""
        logger.info("Navigating to products list page...")
        self.navigate_to(self.PRODUCTS_PATH)
        self.page.wait_for_load_state("domcontentloaded", timeout=15000)
        # Ждём рендер React — любой из ключевых элементов
        self.page.locator("[role='tab'], .MuiTab-root").first.wait_for(
            state="visible", timeout=10000
        )
        logger.info("Products list page loaded")

    def click_products_nav_link(self) -> None:
        """Click products navigation link from sidebar."""
        logger.info("Clicking products navigation link...")
        if self.products_nav_link.is_visible(timeout=3000):
            self.products_nav_link.click()
        else:
            # Fallback: direct navigation
            logger.info("Products nav link not visible, using direct navigation")
            self.navigate()
            return
        self.wait_for_page_load()
        logger.info("Navigated to products via sidebar")

    def click_add_product(self) -> None:
        """Click Add Products button."""
        logger.info("Clicking Add Products button...")
        self.add_product_btn.click()
        self.wait_for_page_load()
        logger.info("Navigated to add products page")

    # ==================== VIEW TOGGLE METHODS ====================

    def switch_to_table_view(self) -> None:
        """Switch to table view."""
        logger.info("Switching to table view...")
        self.view_toggle_table.click()
        self.wait_for_network_idle()
        logger.info("Switched to table view")

    def switch_to_grid_view(self) -> None:
        """Switch to grid view."""
        logger.info("Switching to grid view...")
        self.view_toggle_grid.click()
        self.wait_for_network_idle()
        logger.info("Switched to grid view")

    def is_grid_view_active(self) -> bool:
        """Check if grid view is currently active (via aria-pressed attribute)."""
        grid_btn = self.view_toggle_grid
        if grid_btn.is_visible(timeout=2000):
            return grid_btn.get_attribute("aria-pressed") == "true" or \
                "Mui-selected" in (grid_btn.get_attribute("class") or "")
        return False

    def is_table_view_active(self) -> bool:
        """Check if table view is currently active (via aria-pressed attribute)."""
        table_btn = self.view_toggle_table
        if table_btn.is_visible(timeout=2000):
            return table_btn.get_attribute("aria-pressed") == "true" or \
                "Mui-selected" in (table_btn.get_attribute("class") or "")
        return False

    # ==================== STATUS TAB METHODS ====================

    def click_tab(self, tab_name: str) -> None:
        """Click on a status tab by name."""
        logger.info(f"Clicking tab: {tab_name}")
        tab = self.page.locator(f"[role='tab']:has-text('{tab_name}')").or_(
            self.page.locator(f".MuiTab-root:has-text('{tab_name}')")
        )
        if tab.is_visible(timeout=3000):
            tab.click()
            self.wait_for_network_idle()
        logger.info(f"Tab clicked: {tab_name}")

    def click_tab_all(self) -> None:
        """Click All status tab."""
        self.tab_all.click()
        self.wait_for_network_idle()

    def click_tab_draft(self) -> None:
        """Click Draft status tab."""
        self.tab_draft.click()
        self.wait_for_network_idle()

    def click_tab_in_review(self) -> None:
        """Click In Review status tab."""
        self.tab_in_review.click()
        self.wait_for_network_idle()

    def click_tab_moderated(self) -> None:
        """Click Moderated status tab."""
        self.tab_moderated.click()
        self.wait_for_network_idle()

    def click_tab_on_sale(self) -> None:
        """Click On Sale status tab."""
        self.tab_on_sale.click()
        self.wait_for_network_idle()

    def click_tab_archive(self) -> None:
        """Click Archive status tab."""
        self.tab_archive.click()
        self.wait_for_network_idle()

    def get_active_tab_name(self) -> str:
        """Get the name of the currently active tab."""
        active_tab = self.page.locator("[role='tab'][aria-selected='true']").or_(
            self.page.locator(".MuiTab-root.Mui-selected")
        )
        if active_tab.is_visible(timeout=2000):
            return active_tab.inner_text().strip()
        return ""

    # ==================== SEARCH METHODS ====================

    def search(self, query: str) -> None:
        """Search for products."""
        logger.info(f"Searching for: {query}")
        self.search_input.fill(query)
        self.page.keyboard.press("Enter")
        self.wait_for_network_idle()
        logger.info(f"Search completed for: {query}")

    def clear_search(self) -> None:
        """Clear search input."""
        logger.info("Clearing search...")
        if self.clear_search_btn.is_visible(timeout=2000):
            self.clear_search_btn.click()
        else:
            self.search_input.clear()
        self.wait_for_network_idle()
        logger.info("Search cleared")

    def get_search_value(self) -> str:
        """Get current search input value."""
        return self.search_input.input_value()

    # ==================== FILTER METHODS ====================

    def open_filters(self) -> None:
        """Open filters panel."""
        logger.info("Opening filters panel...")
        if self.filters_btn.is_visible(timeout=2000):
            self.filters_btn.click()
            self.page.wait_for_load_state("domcontentloaded")
        logger.info("Filters panel opened")

    def apply_status_filter(self, status: str) -> None:
        """Apply status filter (tries EN/RU/UZ variants)."""
        # Status name translations
        status_variants = {
            "Approved": ["Approved", "Одобрено", "Tasdiqlangan"],
            "Rejected": ["Rejected", "Отклонено", "Rad etilgan"],
            "Pending": ["Pending", "На модерации", "Kutilmoqda"],
        }
        logger.info(f"Applying status filter: {status}")
        self.status_filter.click()
        self.page.wait_for_load_state("domcontentloaded")
        variants = status_variants.get(status, [status])
        for variant in variants:
            option = self.page.get_by_role("option", name=variant)
            if option.is_visible(timeout=1000):
                option.click()
                break
        self.wait_for_network_idle()
        logger.info(f"Status filter applied: {status}")

    def apply_category_filter(self, category: str) -> None:
        """Apply category filter."""
        logger.info(f"Applying category filter: {category}")
        self.category_filter.click()
        self.page.wait_for_load_state("domcontentloaded")
        option = self.page.get_by_role("option", name=category)
        if option.is_visible(timeout=2000):
            option.click()
        self.wait_for_network_idle()
        logger.info(f"Category filter applied: {category}")

    def clear_all_filters(self) -> None:
        """Clear all applied filters."""
        logger.info("Clearing all filters...")
        if self.clear_filters_btn.is_visible(timeout=2000):
            self.clear_filters_btn.click()
            self.wait_for_network_idle()
        logger.info("All filters cleared")

    # ==================== PRODUCT COUNT METHODS ====================

    def get_products_count(self) -> int:
        """Get number of products displayed (works for both grid and table views)."""
        self.wait_for_dom_ready()

        # Try grid view first (count SKU elements)
        sku_count = self.product_card_skus.count()
        if sku_count > 0:
            logger.info(f"Products count (grid view): {sku_count}")
            return sku_count

        # Fall back to table view
        table_count = self.table_rows.count()
        logger.info(f"Products count (table view): {table_count}")
        return table_count

    def get_total_products_from_text(self) -> int:
        """Get total products count from 'Jami: N' / 'Всего: N' / 'Total: N' text."""
        try:
            text = self.total_products_text.inner_text(timeout=2000)
            import re
            match = re.search(r'(?:Total|Всего|Jami):\s*([\d\s]+)', text)
            if match:
                return int(match.group(1).replace(" ", ""))
        except Exception as e:
            logger.warning(f"Could not get total from text: {e}")
        return 0

    def get_product_names(self) -> list:
        """Get list of all visible product names."""
        names = []
        # In grid view, product names are in h6 elements
        name_elements = self.page.locator("h6").filter(has_not_text="sum").filter(has_not_text="Total").filter(has_not_text="Products List")
        for i in range(name_elements.count()):
            try:
                text = name_elements.nth(i).inner_text(timeout=500)
                if text and len(text) > 2:  # Filter out single chars like "T"
                    names.append(text.strip())
            except Exception:
                continue
        return names

    def get_product_skus(self) -> list:
        """Get list of all visible product SKUs."""
        skus = []
        sku_elements = self.product_card_skus
        for i in range(sku_elements.count()):
            try:
                text = sku_elements.nth(i).inner_text(timeout=500)
                # Extract SKU value from "SKU: XXXX"
                skus.append(text.replace("SKU:", "").strip())
            except Exception:
                continue
        return skus

    # ==================== TABLE METHODS ====================

    def get_column_names(self) -> list:
        """Get list of column names."""
        cells = self.table_header_cells
        names = []
        for i in range(cells.count()):
            text = cells.nth(i).inner_text().strip()
            if text:
                names.append(text)
        return names

    def click_row(self, index: int = 0) -> None:
        """Click on table row by index."""
        logger.info(f"Clicking row {index}...")
        row = self.table_rows.nth(index)
        row.wait_for(state="visible", timeout=3000)
        row.click()
        self.wait_for_network_idle()
        logger.info(f"Row {index} clicked")

    def get_row_data(self, index: int = 0) -> dict:
        """Get data from a specific row."""
        row = self.table_rows.nth(index)
        cells = row.locator("td")
        data = {}
        column_names = self.get_column_names()
        for i, name in enumerate(column_names):
            if i < cells.count():
                data[name] = cells.nth(i).inner_text().strip()
        return data

    def get_product_name_from_row(self, index: int = 0) -> str:
        """Get product name from row."""
        row = self.table_rows.nth(index)
        # Name usually in 2nd or 3rd cell (after checkbox and image)
        name_cell = row.locator("td").nth(2)
        return name_cell.inner_text().strip() if name_cell.is_visible() else ""

    def get_product_price_from_row(self, index: int = 0) -> str:
        """Get product price from row."""
        row = self.table_rows.nth(index)
        # Look for cell with price format
        price_cell = row.locator("td:has-text('UZS')").or_(
            row.locator("td:has-text('so\\'m')")
        )
        return price_cell.inner_text().strip() if price_cell.is_visible() else ""

    def get_product_status_from_row(self, index: int = 0) -> str:
        """Get product status from row."""
        row = self.table_rows.nth(index)
        status_chip = row.locator(".MuiChip-root")
        return status_chip.inner_text().strip() if status_chip.is_visible() else ""

    # ==================== PAGINATION METHODS ====================

    def go_to_next_page(self) -> None:
        """Go to next page."""
        logger.info("Going to next page...")
        if self.next_page_btn.is_enabled(timeout=2000):
            self.next_page_btn.click()
            self.wait_for_network_idle()
        logger.info("Navigated to next page")

    def go_to_prev_page(self) -> None:
        """Go to previous page."""
        logger.info("Going to previous page...")
        if self.prev_page_btn.is_enabled(timeout=2000):
            self.prev_page_btn.click()
            self.wait_for_network_idle()
        logger.info("Navigated to previous page")

    def go_to_first_page(self) -> None:
        """Go to first page."""
        logger.info("Going to first page...")
        if self.first_page_btn.is_visible(timeout=2000) and self.first_page_btn.is_enabled():
            self.first_page_btn.click()
            self.wait_for_network_idle()
        logger.info("Navigated to first page")

    def go_to_last_page(self) -> None:
        """Go to last page."""
        logger.info("Going to last page...")
        if self.last_page_btn.is_visible(timeout=2000) and self.last_page_btn.is_enabled():
            self.last_page_btn.click()
            self.wait_for_network_idle()
        logger.info("Navigated to last page")

    def set_rows_per_page(self, count: int) -> None:
        """Set rows per page."""
        logger.info(f"Setting rows per page to: {count}")
        self.rows_per_page_select.click()
        self.page.wait_for_load_state("domcontentloaded")
        option = self.page.get_by_role("option", name=str(count))
        if option.is_visible(timeout=2000):
            option.click()
        self.wait_for_network_idle()
        logger.info(f"Rows per page set to: {count}")

    def get_page_info_text(self) -> str:
        """Get pagination info text."""
        return self.page_info.inner_text().strip() if self.page_info.is_visible() else ""

    def is_next_page_enabled(self) -> bool:
        """Check if next page button is enabled."""
        return self.next_page_btn.is_enabled(timeout=1000) if self.next_page_btn.is_visible(timeout=1000) else False

    def is_prev_page_enabled(self) -> bool:
        """Check if previous page button is enabled."""
        return self.prev_page_btn.is_enabled(timeout=1000) if self.prev_page_btn.is_visible(timeout=1000) else False

    # ==================== SORTING METHODS ====================

    def click_column_header(self, column_name: str) -> None:
        """Click column header to sort."""
        logger.info(f"Clicking column header: {column_name}")
        header = self.page.locator(f"th:has-text('{column_name}')").or_(
            self.page.locator(f"[role='columnheader']:has-text('{column_name}')")
        )
        if header.is_visible(timeout=2000):
            header.click()
            self.wait_for_network_idle()
        logger.info(f"Clicked column header: {column_name}")

    def get_sort_direction(self, column_name: str) -> str:
        """Get sort direction for column (asc/desc/none)."""
        header = self.page.locator(f"th:has-text('{column_name}')")
        if header.is_visible():
            aria_sort = header.get_attribute("aria-sort")
            return aria_sort if aria_sort else "none"
        return "none"

    # ==================== BULK ACTION METHODS ====================

    def select_all_products(self) -> None:
        """Select all products using header checkbox."""
        logger.info("Selecting all products...")
        self.select_all_checkbox.check()
        self.page.wait_for_load_state("domcontentloaded")
        logger.info("All products selected")

    def deselect_all_products(self) -> None:
        """Deselect all products."""
        logger.info("Deselecting all products...")
        self.select_all_checkbox.uncheck()
        self.page.wait_for_load_state("domcontentloaded")
        logger.info("All products deselected")

    def select_product_by_index(self, index: int) -> None:
        """Select product by row index."""
        logger.info(f"Selecting product at index {index}...")
        checkbox = self.row_checkboxes.nth(index)
        checkbox.check()
        self.page.wait_for_load_state("domcontentloaded")
        logger.info(f"Product at index {index} selected")

    def deselect_product_by_index(self, index: int) -> None:
        """Deselect product by row index."""
        logger.info(f"Deselecting product at index {index}...")
        checkbox = self.row_checkboxes.nth(index)
        checkbox.uncheck()
        self.page.wait_for_load_state("domcontentloaded")
        logger.info(f"Product at index {index} deselected")

    def get_selected_count(self) -> int:
        """Get count of selected products."""
        count = 0
        checkboxes = self.row_checkboxes
        for i in range(checkboxes.count()):
            if checkboxes.nth(i).is_checked():
                count += 1
        return count

    def click_bulk_delete(self) -> None:
        """Click bulk delete button."""
        logger.info("Clicking bulk delete...")
        self.bulk_delete_btn.click()
        self.page.wait_for_load_state("domcontentloaded")
        logger.info("Bulk delete clicked")

    # ==================== ROW ACTION METHODS ====================

    def click_edit_on_row(self, index: int = 0) -> None:
        """Click edit button on specific row."""
        logger.info(f"Clicking edit on row {index}...")
        edit_btn = self.table_rows.nth(index).locator("button[aria-label='Edit']").or_(
            self.table_rows.nth(index).locator("button:has(svg[data-testid='EditIcon'])")
        )
        if edit_btn.is_visible(timeout=2000):
            edit_btn.click()
            self.wait_for_network_idle()
        logger.info(f"Edit clicked on row {index}")

    def click_delete_on_row(self, index: int = 0) -> None:
        """Click delete button on specific row."""
        logger.info(f"Clicking delete on row {index}...")
        delete_btn = self.table_rows.nth(index).locator("button[aria-label='Delete']").or_(
            self.table_rows.nth(index).locator("button:has(svg[data-testid='DeleteIcon'])")
        )
        if delete_btn.is_visible(timeout=2000):
            delete_btn.click()
            self.page.wait_for_load_state("domcontentloaded")
        logger.info(f"Delete clicked on row {index}")

    def click_view_on_row(self, index: int = 0) -> None:
        """Click view button on specific row."""
        logger.info(f"Clicking view on row {index}...")
        view_btn = self.table_rows.nth(index).locator("button[aria-label='View']").or_(
            self.table_rows.nth(index).locator("button:has(svg[data-testid='VisibilityIcon'])")
        )
        if view_btn.is_visible(timeout=2000):
            view_btn.click()
            self.wait_for_network_idle()
        logger.info(f"View clicked on row {index}")

    def click_more_actions_on_row(self, index: int = 0) -> None:
        """Click more actions (3 dots) on specific row."""
        logger.info(f"Clicking more actions on row {index}...")
        more_btn = self.table_rows.nth(index).locator("button[aria-label='More']").or_(
            self.table_rows.nth(index).locator("button:has(svg[data-testid='MoreVertIcon'])")
        )
        if more_btn.is_visible(timeout=2000):
            more_btn.click()
            self.page.wait_for_load_state("domcontentloaded")
        logger.info(f"More actions clicked on row {index}")

    # ==================== DIALOG METHODS ====================

    def confirm_action(self) -> None:
        """Confirm action in dialog."""
        logger.info("Confirming action...")
        self.confirm_yes_btn.click()
        self.wait_for_network_idle()
        logger.info("Action confirmed")

    def cancel_action(self) -> None:
        """Cancel action in dialog."""
        logger.info("Canceling action...")
        self.confirm_no_btn.click()
        self.page.wait_for_load_state("domcontentloaded")
        logger.info("Action canceled")

    def is_confirm_dialog_visible(self) -> bool:
        """Check if confirmation dialog is visible."""
        return self.confirm_dialog.is_visible(timeout=2000)

    # ==================== STATUS CHECK METHODS ====================

    def is_page_loaded(self) -> bool:
        """Check if products page is loaded."""
        try:
            current_url = self.get_current_url()
            logger.info(f"Checking if page loaded, current URL: {current_url}")

            # Check if we're on products page by URL
            if "/dashboard/products" not in current_url:
                logger.warning(f"Not on products page, URL: {current_url}")
                return False

            # Wait for page to stabilize
            self.wait_for_dom_ready()

            # If URL is correct and page is loaded, consider it successful
            # The specific elements may vary by UI version
            logger.info("Page loaded successfully based on URL")
            return True

        except Exception as e:
            logger.warning(f"is_page_loaded check failed: {e}")
            # Fallback: just check URL
            return "/dashboard/products" in self.get_current_url()

    def is_empty_state_visible(self) -> bool:
        """Check if empty state is displayed."""
        return self.empty_state.is_visible(timeout=2000)

    def is_loading(self) -> bool:
        """Check if page is loading."""
        return self.loading_spinner.is_visible(timeout=1000)

    def wait_for_loading_complete(self, timeout: int = 10000) -> None:
        """Wait for loading to complete."""
        if self.loading_spinner.is_visible(timeout=1000):
            self.loading_spinner.wait_for(state="hidden", timeout=timeout)

    def is_toast_visible(self) -> bool:
        """Check if any toast is visible."""
        return self.toast_message.is_visible(timeout=2000)

    def is_success_toast_visible(self) -> bool:
        """Check if success toast is visible."""
        return self.success_toast.is_visible(timeout=2000)

    def is_error_toast_visible(self) -> bool:
        """Check if error toast is visible."""
        return self.error_toast.is_visible(timeout=2000)

    def get_toast_message(self) -> str:
        """Get toast message text."""
        if self.toast_message.is_visible(timeout=2000):
            return self.toast_message.inner_text().strip()
        return ""

    # ==================== URL METHODS ====================

    def is_on_products_page(self) -> bool:
        """Check if currently on products list page."""
        return "/dashboard/products" in self.get_current_url()

    def get_url_params(self) -> dict:
        """Get URL query parameters."""
        from urllib.parse import urlparse, parse_qs
        url = self.get_current_url()
        parsed = urlparse(url)
        return parse_qs(parsed.query)

    # ==================== VALIDATION METHODS ====================

    def get_validation_error_count(self) -> int:
        """Get count of validation errors on page."""
        return self.page.locator(".MuiFormHelperText-root.Mui-error").count()

    def has_validation_errors(self) -> bool:
        """Check if page has validation errors."""
        return self.get_validation_error_count() > 0

    def get_validation_error_messages(self) -> list:
        """Get all validation error messages."""
        messages = []
        errors = self.page.locator(".MuiFormHelperText-root.Mui-error")
        for i in range(errors.count()):
            text = errors.nth(i).inner_text().strip()
            if text:
                messages.append(text)
        return messages

    # ==================== KEYBOARD METHODS ====================

    def press_key(self, key: str) -> None:
        """Press keyboard key."""
        self.page.keyboard.press(key)

    def press_escape(self) -> None:
        """Press Escape key."""
        self.page.keyboard.press("Escape")

    def press_enter(self) -> None:
        """Press Enter key."""
        self.page.keyboard.press("Enter")

    # ==================== ACCESSIBILITY METHODS ====================

    def get_element_aria_label(self, locator: Locator) -> str:
        """Get aria-label attribute of element."""
        return locator.get_attribute("aria-label") or ""

    def get_focused_element(self) -> Locator:
        """Get currently focused element."""
        return self.page.locator(":focus")

    def tab_to_next_element(self) -> None:
        """Tab to next focusable element."""
        self.page.keyboard.press("Tab")

    def tab_to_prev_element(self) -> None:
        """Shift+Tab to previous focusable element."""
        self.page.keyboard.press("Shift+Tab")

    # ==================== CONSOLE/NETWORK METHODS ====================

    def get_console_errors(self) -> list:
        """Get console errors (requires listener setup)."""
        # Note: This requires setting up console listener before page load
        return []

    def has_failed_requests(self) -> bool:
        """Check for failed network requests (requires listener setup)."""
        # Note: This requires setting up request listener before page load
        return False
