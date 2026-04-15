"""Script to inspect Products List page structure in detail."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to login
    page.goto('https://staging-seller.greatmall.uz/auth/login')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(2000)

    # Login
    page.get_by_role("textbox").first.fill("998001112233")
    page.get_by_role("textbox").nth(1).fill("76543217")
    page.locator("button[type='submit']").click()
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(3000)

    # Select Zara shop
    page.locator("text=Test Shop Automation").first.click()
    page.wait_for_timeout(1000)
    page.locator("text=Zara").first.click()
    page.wait_for_timeout(2000)

    # Navigate to products
    page.goto('https://staging-seller.greatmall.uz/dashboard/products')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(3000)

    print("=== PAGE URL ===")
    print(page.url)

    print("\n=== PAGE TITLE / H ELEMENTS ===")
    for h_tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        elements = page.locator(h_tag).all()
        for el in elements:
            try:
                text = el.inner_text(timeout=300)
                print(f"<{h_tag}>: '{text[:60]}'")
            except:
                pass

    print("\n=== BUTTONS ===")
    buttons = page.locator("button").all()
    for i, btn in enumerate(buttons[:30]):
        try:
            text = btn.inner_text(timeout=300).replace('\n', ' ')[:50]
            classes = btn.get_attribute("class") or ""
            aria = btn.get_attribute("aria-label") or ""
            print(f"{i}: '{text}' aria='{aria}' class='{classes[:40]}'")
        except:
            pass

    print("\n=== TABS (status filters) ===")
    tabs = page.locator("[role='tab'], button:has-text('All'), button:has-text('Draft'), button:has-text('Review'), button:has-text('Sale')").all()
    for i, tab in enumerate(tabs[:10]):
        try:
            text = tab.inner_text(timeout=300)
            selected = tab.get_attribute("aria-selected") or ""
            print(f"{i}: '{text[:30]}' selected={selected}")
        except:
            pass

    print("\n=== INPUTS (search, filters) ===")
    inputs = page.locator("input").all()
    for i, inp in enumerate(inputs[:15]):
        try:
            placeholder = inp.get_attribute("placeholder") or ""
            name = inp.get_attribute("name") or ""
            inp_type = inp.get_attribute("type") or ""
            value = inp.get_attribute("value") or ""
            print(f"{i}: name='{name}' type='{inp_type}' placeholder='{placeholder[:30]}' value='{value[:20]}'")
        except:
            pass

    print("\n=== PRODUCT CARDS (divs with product info) ===")
    # Look for product cards - they seem to have image, name, SKU, price
    cards = page.locator("[class*='card'], [class*='Card'], [class*='product'], [class*='Product']").all()
    print(f"Found {len(cards)} card-like elements")

    # Look for elements containing SKU
    skus = page.locator("text=/SKU:/i").all()
    print(f"Found {len(skus)} SKU elements")
    for i, sku in enumerate(skus[:3]):
        try:
            text = sku.inner_text(timeout=300)
            parent = sku.locator("xpath=ancestor::div[contains(@class,'Mui') or contains(@class,'product') or contains(@class,'card')]").first
            parent_classes = parent.get_attribute("class") or "" if parent.count() > 0 else ""
            print(f"{i}: '{text}' - parent class: {parent_classes[:60]}")
        except:
            pass

    print("\n=== ADD PRODUCT BUTTON ===")
    add_btns = page.locator("text=/Add Product|Mahsulot qo'shish/i, a[href*='add'], button:has-text('Add')").all()
    for i, btn in enumerate(add_btns[:5]):
        try:
            text = btn.inner_text(timeout=300)
            href = btn.get_attribute("href") or ""
            tag = btn.evaluate("el => el.tagName")
            print(f"{i}: <{tag}> '{text[:40]}' href='{href}'")
        except:
            pass

    print("\n=== PAGINATION ===")
    pagination = page.locator("[class*='agination'], [aria-label*='pagination'], button:has-text('Next'), button:has-text('Previous')").all()
    print(f"Found {len(pagination)} pagination elements")

    # Look for "Total" text
    total = page.locator("text=/Total|Jami/i").all()
    for t in total[:3]:
        try:
            text = t.inner_text(timeout=300)
            print(f"Total text: '{text[:50]}'")
        except:
            pass

    # Look for page size selector
    page_size = page.locator("text=/rows per page|per page|size/i").all()
    for ps in page_size[:3]:
        try:
            text = ps.inner_text(timeout=300)
            print(f"Page size text: '{text[:50]}'")
        except:
            pass

    print("\n=== VIEW TOGGLE (grid/list) ===")
    view_toggles = page.locator("[aria-label*='view'], [aria-label*='grid'], [aria-label*='list'], button:has(svg)").all()
    for i, vt in enumerate(view_toggles[:10]):
        try:
            aria = vt.get_attribute("aria-label") or ""
            classes = vt.get_attribute("class") or ""
            if "view" in aria.lower() or "grid" in aria.lower() or "list" in aria.lower():
                print(f"{i}: aria='{aria}' class='{classes[:50]}'")
        except:
            pass

    print("\n=== DATE FILTERS ===")
    date_inputs = page.locator("input[type='date'], input[placeholder*='date'], input[placeholder*='Date'], input[placeholder*='DD'], input[placeholder*='MM']").all()
    print(f"Found {len(date_inputs)} date inputs")
    for i, di in enumerate(date_inputs[:5]):
        try:
            placeholder = di.get_attribute("placeholder") or ""
            label = di.get_attribute("aria-label") or ""
            print(f"{i}: placeholder='{placeholder}' label='{label}'")
        except:
            pass

    print("\n=== CHECKBOXES (for bulk select) ===")
    checkboxes = page.locator("input[type='checkbox'], [role='checkbox'], .MuiCheckbox-root").all()
    print(f"Found {len(checkboxes)} checkboxes")

    print("\n=== STATUS BADGES (On Sale, Draft, etc) ===")
    badges = page.locator("[class*='badge'], [class*='Badge'], [class*='chip'], [class*='Chip'], [class*='status'], [class*='Status']").all()
    print(f"Found {len(badges)} badge-like elements")
    for i, badge in enumerate(badges[:10]):
        try:
            text = badge.inner_text(timeout=300)
            classes = badge.get_attribute("class") or ""
            print(f"{i}: '{text[:30]}' class='{classes[:50]}'")
        except:
            pass

    # Take final screenshot
    page.screenshot(path='/tmp/products_detail.png', full_page=True)
    print("\nScreenshot saved to /tmp/products_detail.png")

    browser.close()
