"""Deep exploration of Reviews and Promotions pages."""
import sys
sys.path.insert(0, "/Users/n.begimbayevgreatmall.uz/Downloads/auto/seller-web-automation")

from playwright.sync_api import sync_playwright

BASE_URL = "https://staging-seller.greatmall.uz"


def explore():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Login
        page.goto(f"{BASE_URL}/auth/login")
        page.fill("input[name='login']", "998001112233")
        page.fill("input[name='password']", "76543217")
        page.click("button[type='submit']")
        page.wait_for_url("**/dashboard**", timeout=15000)
        print(f"Logged in: {page.url}\n")

        # ======= REVIEWS PAGE =======
        print("=" * 60)
        print("REVIEWS PAGE - DETAILED EXPLORATION")
        print("=" * 60)
        page.goto(f"{BASE_URL}/dashboard/reviews?page=1&size=10", wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(2000)
        print(f"URL: {page.url}\n")

        # 1. Statistics cards
        print("--- STATISTICS CARDS ---")
        papers = page.locator(".MuiPaper-root, .MuiCard-root").all()
        for i, paper in enumerate(papers):
            text = paper.text_content().strip()
            if text and len(text) < 200:
                print(f"  Paper[{i}]: {text[:100]}")

        # 2. Status tabs
        print("\n--- STATUS TABS ---")
        tabs = page.locator("button").all()
        for tab in tabs:
            text = tab.text_content().strip()
            role = tab.get_attribute("role") or ""
            aria_selected = tab.get_attribute("aria-selected") or ""
            classes = tab.get_attribute("class") or ""
            if text and "tab" in classes.lower() or "tab" in role.lower():
                print(f"  Tab: '{text}' role={role} selected={aria_selected}")

        # Try broader tab search
        print("\n  All visible buttons with text:")
        for btn in tabs:
            text = btn.text_content().strip()
            if text and len(text) < 30:
                print(f"    '{text}'")

        # 3. Filters
        print("\n--- FILTERS ---")
        inputs = page.locator("input:visible").all()
        for inp in inputs:
            placeholder = inp.get_attribute("placeholder") or ""
            name = inp.get_attribute("name") or ""
            label_id = inp.get_attribute("id") or ""
            print(f"  Input: name='{name}' placeholder='{placeholder}' id='{label_id}'")

        # Select/dropdown elements
        selects = page.locator("[role='combobox'], select, .MuiSelect-root").all()
        for s in selects:
            text = s.text_content().strip()[:50]
            label = s.get_attribute("aria-labelledby") or s.get_attribute("aria-label") or ""
            print(f"  Select: text='{text}' label='{label}'")

        # 4. DataGrid columns
        print("\n--- DATAGRID ---")
        grid = page.locator("[role='grid'], .MuiDataGrid-root")
        print(f"  Grid visible: {grid.first.is_visible(timeout=2000)}")

        col_headers = page.locator("[role='columnheader']").all()
        print(f"  Column headers ({len(col_headers)}):")
        for ch in col_headers:
            text = ch.text_content().strip()
            field = ch.get_attribute("data-field") or ""
            print(f"    '{text}' (field={field})")

        # 5. Empty state
        print("\n--- EMPTY STATE ---")
        empty = page.locator("text='Данные отсутствуют'").or_(
            page.locator(".MuiDataGrid-overlay")
        )
        if empty.first.is_visible(timeout=2000):
            print(f"  Empty state text: {empty.first.text_content().strip()}")

        # 6. Toolbar buttons
        print("\n--- TOOLBAR ---")
        toolbar = page.locator(".MuiDataGrid-toolbarContainer, [class*='toolbar']")
        if toolbar.first.is_visible(timeout=2000):
            toolbar_btns = toolbar.locator("button").all()
            print(f"  Toolbar buttons ({len(toolbar_btns)}):")
            for btn in toolbar_btns:
                print(f"    '{btn.text_content().strip()[:40]}'")

        # 7. Page title/breadcrumb
        print("\n--- TITLES ---")
        for selector in ["h1", "h2", "h3", ".MuiBreadcrumbs-root", "[class*='title']"]:
            elements = page.locator(selector).all()
            for el in elements:
                text = el.text_content().strip()
                if text and len(text) < 100:
                    print(f"  {selector}: '{text}'")

        # 8. All text content elements for labels
        print("\n--- LABELS/TEXT ---")
        body_text = page.text_content("body") or ""
        # Find key labels
        for label in ["Reviews", "Statistics", "New", "With Responses", "Waiting Response",
                      "My Rating", "All", "Moderation", "Processed", "Rejected",
                      "Date From", "Date To", "Review Rating", "Review Type",
                      "Product", "Status", "Rating"]:
            if label in body_text:
                print(f"  Found: '{label}'")

        # ======= PROMOTIONS PAGE =======
        print("\n" + "=" * 60)
        print("PROMOTIONS PAGE - DETAILED EXPLORATION")
        print("=" * 60)
        page.goto(f"{BASE_URL}/dashboard/promotions", wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(2000)
        print(f"URL: {page.url}\n")

        # 1. Tabs
        print("--- TABS ---")
        all_btns = page.locator("button:visible").all()
        for btn in all_btns:
            text = btn.text_content().strip()
            if text and len(text) < 40:
                print(f"  Button: '{text}'")

        # 2. Content
        print("\n--- CONTENT ---")
        body_text = page.text_content("body") or ""
        clean = " ".join(body_text.split())
        # Extract meaningful parts
        for keyword in ["Promotions", "Available", "Upcoming", "Participated",
                        "Not Participated", "Completed", "Данные отсутствуют",
                        "promotion", "discount", "скидка"]:
            if keyword.lower() in clean.lower():
                print(f"  Found: '{keyword}'")

        # 3. Try clicking a tab
        print("\n--- TAB CLICK TEST ---")
        for tab_name in ["Upcoming", "Participated", "Completed"]:
            tab = page.locator(f"button:has-text('{tab_name}')").first
            if tab.is_visible(timeout=2000):
                tab.click()
                page.wait_for_timeout(1000)
                current_url = page.url
                print(f"  After '{tab_name}' click: {current_url}")

        # 4. Check for cards/list items
        print("\n--- CARDS/ITEMS ---")
        cards = page.locator(".MuiCard-root").all()
        print(f"  MuiCard-root: {len(cards)}")
        list_items = page.locator("[role='listitem'], .MuiListItem-root").all()
        print(f"  ListItems: {len(list_items)}")
        papers = page.locator(".MuiPaper-root").all()
        print(f"  Papers: {len(papers)}")

        # 5. Empty state
        empty = page.locator("text='Данные отсутствуют'")
        if empty.first.is_visible(timeout=2000):
            print(f"  Empty state: '{empty.first.text_content().strip()}'")

        browser.close()


if __name__ == "__main__":
    explore()
