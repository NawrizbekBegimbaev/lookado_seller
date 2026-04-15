"""Explore the Orders and Returns menu structure."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to login page
    page.goto('https://staging-seller.greatmall.uz/auth/login')
    page.wait_for_load_state('networkidle')

    # Login
    page.get_by_placeholder('Telefon raqami').fill('998001112233')
    page.get_by_placeholder('Parol').fill('76543217')
    page.get_by_role('button', name='Kirish').or_(page.get_by_role('button', name='Login')).click()

    # Wait for dashboard
    page.wait_for_url('**/dashboard**', timeout=15000)
    page.wait_for_timeout(2000)

    print(f"Current URL: {page.url}")

    # Select Zara shop
    shop_dropdown = page.locator("button:has-text('Active')").first
    if shop_dropdown.is_visible(timeout=3000):
        shop_dropdown.click()
        page.wait_for_timeout(500)
        zara_shop = page.get_by_role("menuitem").filter(has_text="Zara").first
        if zara_shop.is_visible(timeout=2000):
            zara_shop.click()
            page.wait_for_timeout(1000)
            print("Selected Zara shop")

    # Take screenshot of dashboard
    page.screenshot(path='/tmp/dashboard_zara.png')
    print("Screenshot saved: /tmp/dashboard_zara.png")

    # Click on "Orders and Returns" to expand submenu
    orders_menu = page.locator("a:has-text('Orders and Returns')").first
    if orders_menu.is_visible(timeout=3000):
        orders_menu.click()
        page.wait_for_timeout(1000)
        print("Clicked Orders and Returns menu")

    # Take screenshot after expanding menu
    page.screenshot(path='/tmp/orders_menu_expanded.png')
    print("Screenshot saved: /tmp/orders_menu_expanded.png")

    # Find all links in the sidebar
    sidebar_links = page.locator("nav a, aside a, [class*='sidebar'] a").all()
    print(f"\nFound {len(sidebar_links)} sidebar links:")
    for link in sidebar_links:
        try:
            text = link.text_content()
            href = link.get_attribute('href')
            print(f"  - {text.strip()}: {href}")
        except:
            pass

    # Take accessibility snapshot
    snapshot = page.accessibility.snapshot()
    print("\nAccessibility snapshot taken")

    browser.close()
