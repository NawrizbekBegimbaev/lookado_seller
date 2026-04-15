"""
Order Detail page object for viewing and managing individual orders.
Follows Page Object Model (POM) and SOLID principles.

URL: /dashboard/orders-management/orders/[order_id]

TODO: Доработать после исследования реальной структуры страницы через браузер
"""

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage, logger


class OrderDetailPage(BasePage):
    """
    Page Object Model for Order Detail Page.
    Handles viewing order details, products, customer info, and order actions.
    """

    ORDERS_LIST_PATH = "/dashboard/orders-management/orders"
    ORDER_DETAIL_PATH = "/dashboard/orders-management/orders/"  # + order_id

    def __init__(self, page: Page):
        """Initialize order detail page with locators."""
        super().__init__(page)

    # ===============================
    # Locators (Properties)
    # ===============================

    @property
    def page_title(self) -> Locator:
        """Page title heading (usually 'Orders 1', 'Orders 2', etc)."""
        return self.page.locator("h1, h2, h3, h4, h5, h6").first

    @property
    def back_button(self) -> Locator:
        """Back to orders list button/link."""
        return self.page.locator(
            "a[href*='/orders']:not([href*='/orders/']), button:has-text('Back'), button:has-text('Назад')"
        ).first

    # --- Order Information Section ---

    @property
    def order_id_field(self) -> Locator:
        """Order ID field/label (EN/RU/UZ)."""
        return self.page.locator(
            "text=/Order ID|Номер заказа|Buyurtma raqami/"
        ).or_(self.page.locator("[data-testid='order-id']"))

    @property
    def order_status_badge(self) -> Locator:
        """Order status badge/chip."""
        return self.page.locator(
            "[class*='status'], [class*='badge'], [class*='chip']"
        ).first

    @property
    def order_date_field(self) -> Locator:
        """Order creation date (EN/RU/UZ)."""
        return self.page.locator("text=/Date|Дата|Sana/")

    @property
    def order_total_field(self) -> Locator:
        """Order total amount (EN/RU/UZ)."""
        return self.page.locator("text=/Total|Итого|Сумма|Jami/")

    # --- Customer Information Section ---

    @property
    def customer_name_field(self) -> Locator:
        """Customer name field (EN/RU/UZ)."""
        return self.page.locator("text=/Customer|Покупатель|Клиент|Xaridor/")

    @property
    def customer_phone_field(self) -> Locator:
        """Customer phone number (EN/RU/UZ)."""
        return self.page.locator("text=/Phone|Телефон|Telefon/")

    @property
    def customer_address_field(self) -> Locator:
        """Delivery address (EN/RU/UZ)."""
        return self.page.locator("text=/Address|Адрес|Manzil/")

    # --- Products Table/Grid ---

    @property
    def products_table(self) -> Locator:
        """Products table or grid."""
        return self.page.locator("table, [role='grid']").first

    @property
    def product_rows(self) -> Locator:
        """Product rows in the table."""
        return self.page.locator("table tbody tr, table.MuiTable-root tbody tr")

    # --- Action Buttons ---

    @property
    def update_status_button(self) -> Locator:
        """Update order status button (EN/RU/UZ)."""
        return self.page.locator(
            "button:has-text('Update'), button:has-text('Обновить'), button:has-text('Yangilash')"
        ).first

    @property
    def cancel_order_button(self) -> Locator:
        """Cancel order button (EN/RU/UZ)."""
        return self.page.locator(
            "button:has-text('Cancel'), button:has-text('Отменить'), button:has-text('Bekor qilish')"
        ).first

    @property
    def refund_button(self) -> Locator:
        """Refund button (EN/RU/UZ)."""
        return self.page.locator(
            "button:has-text('Refund'), button:has-text('Возврат'), button:has-text('Qaytarish')"
        ).first

    @property
    def print_button(self) -> Locator:
        """Print order button (EN/RU/UZ)."""
        return self.page.locator(
            "button:has-text('Print'), button:has-text('Печать'), button:has-text('Chop etish')"
        ).first

    # NOTE: Tabs НЕТ на Order Detail странице (проверено 2026-01-24)

    # ===============================
    # Navigation Methods
    # ===============================

    def navigate_to_order_detail(self, order_id: str) -> None:
        """
        Navigate to specific order detail page.

        Args:
            order_id: Order ID to view
        """
        logger.info(f"Navigating to order detail: {order_id}")
        self.navigate_to(f"{self.ORDER_DETAIL_PATH}{order_id}")
        self.page.wait_for_load_state("networkidle")
        self.wait_for_dom_ready()
        logger.info(f"Navigated to order detail: {order_id}")

    def navigate_back_to_list(self) -> None:
        """Navigate back to orders list."""
        logger.info("Navigating back to orders list...")
        self.back_button.click()
        self.wait_for_page_load()
        logger.info("Navigated back to orders list")

    # ===============================
    # Order Information Methods
    # ===============================

    def get_order_id(self) -> str:
        """Get order ID from page."""
        try:
            text = self.order_id_field.inner_text(timeout=3000)
            logger.info(f"Order ID: {text}")
            return text
        except Exception as e:
            logger.warning(f"Could not get order ID: {e}")
            return ""

    def get_order_status(self) -> str:
        """Get current order status."""
        try:
            status = self.order_status_badge.inner_text(timeout=3000)
            logger.info(f"Order status: {status}")
            return status
        except Exception as e:
            logger.warning(f"Could not get order status: {e}")
            return ""

    def get_order_total(self) -> str:
        """Get order total amount."""
        try:
            total = self.order_total_field.inner_text(timeout=3000)
            logger.info(f"Order total: {total}")
            return total
        except Exception as e:
            logger.warning(f"Could not get order total: {e}")
            return ""

    # ===============================
    # Products Methods
    # ===============================

    def get_products_count(self) -> int:
        """Get number of products in order."""
        try:
            count = self.product_rows.count()
            logger.info(f"Products in order: {count}")
            return count
        except Exception as e:
            logger.warning(f"Could not count products: {e}")
            return 0

    def is_products_table_visible(self) -> bool:
        """Check if products table is visible."""
        try:
            return self.products_table.is_visible(timeout=3000)
        except Exception:
            return False

    # ===============================
    # Action Methods
    # ===============================

    def click_update_status(self) -> None:
        """Click update status button."""
        logger.info("Clicking update status button...")
        self.update_status_button.click()
        logger.info("Clicked update status button")

    def click_cancel_order(self) -> None:
        """Click cancel order button."""
        logger.info("Clicking cancel order button...")
        self.cancel_order_button.click()
        logger.info("Clicked cancel order button")

    def click_print(self) -> None:
        """Click print button."""
        logger.info("Clicking print button...")
        self.print_button.click()
        logger.info("Clicked print button")

    # NOTE: Tab methods removed - no tabs on Order Detail page

    # ===============================
    # Validation Methods
    # ===============================

    def is_on_order_detail_page(self) -> bool:
        """Check if currently on order detail page."""
        url = self.get_current_url()
        return "/orders/" in url and url != self.ORDERS_LIST_PATH

    def get_current_order_id_from_url(self) -> str:
        """Extract order ID from current URL."""
        url = self.get_current_url()
        if "/orders/" in url:
            parts = url.split("/orders/")
            if len(parts) > 1:
                order_id = parts[1].split("?")[0].split("#")[0]
                return order_id
        return ""

    def is_page_loaded(self) -> bool:
        """Check if order detail page is fully loaded."""
        try:
            # Проверяем что есть заголовок И таблица товаров ИЛИ статус заказа
            title_visible = self.page_title.is_visible(timeout=3000)
            # Check for content: products table OR status label (class*='label') OR print button
            has_content = (
                self.products_table.is_visible(timeout=2000) or
                self.page.locator("[class*='label']").first.is_visible(timeout=2000) or
                self.print_button.is_visible(timeout=2000)
            )
            return title_visible and has_content
        except Exception:
            return False

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
