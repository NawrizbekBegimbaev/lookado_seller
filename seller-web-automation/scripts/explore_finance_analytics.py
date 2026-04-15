"""Explore Finance and Analytics pages on staging."""
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
        print(f"Logged in. URL: {page.url}")

        # Collect all sidebar nav links
        print("\n=== SIDEBAR NAVIGATION ===")
        nav_links = page.locator("nav a, [role='navigation'] a, aside a").all()
        for link in nav_links:
            text = link.text_content().strip()
            href = link.get_attribute("href") or ""
            if text:
                print(f"  [{text}] -> {href}")

        # Try Finance page
        print("\n=== FINANCE PAGE ===")
        page.goto(f"{BASE_URL}/dashboard/finance", wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(2000)
        print(f"URL: {page.url}")
        print(f"Title: {page.title()}")

        # Get main content
        body_text = page.text_content("body") or ""
        # Clean up - take first 500 chars
        clean_text = " ".join(body_text.split())[:500]
        print(f"Body text (first 500): {clean_text}")

        # Check for key elements
        headings = page.locator("h1, h2, h3, h4, h5, h6").all()
        print(f"Headings ({len(headings)}):")
        for h in headings[:10]:
            print(f"  {h.evaluate('el => el.tagName')}: {h.text_content().strip()}")

        # Check for tables/grids
        tables = page.locator("table, [role='grid'], .MuiDataGrid-root").count()
        print(f"Tables/Grids: {tables}")

        # Check for cards/widgets
        cards = page.locator(".MuiCard-root, .MuiPaper-root").count()
        print(f"Cards/Papers: {cards}")

        # Check for charts
        charts = page.locator("canvas, svg.recharts-surface, .recharts-wrapper").count()
        print(f"Charts: {charts}")

        # Check visible buttons
        buttons = page.locator("button:visible").all()
        print(f"Buttons ({len(buttons)}):")
        for btn in buttons[:10]:
            print(f"  {btn.text_content().strip()[:50]}")

        # Try Analytics page
        print("\n=== ANALYTICS PAGE ===")
        page.goto(f"{BASE_URL}/dashboard/analytics", wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(2000)
        print(f"URL: {page.url}")
        print(f"Title: {page.title()}")

        body_text = page.text_content("body") or ""
        clean_text = " ".join(body_text.split())[:500]
        print(f"Body text (first 500): {clean_text}")

        headings = page.locator("h1, h2, h3, h4, h5, h6").all()
        print(f"Headings ({len(headings)}):")
        for h in headings[:10]:
            print(f"  {h.evaluate('el => el.tagName')}: {h.text_content().strip()}")

        tables = page.locator("table, [role='grid'], .MuiDataGrid-root").count()
        print(f"Tables/Grids: {tables}")

        cards = page.locator(".MuiCard-root, .MuiPaper-root").count()
        print(f"Cards/Papers: {cards}")

        charts = page.locator("canvas, svg.recharts-surface, .recharts-wrapper").count()
        print(f"Charts: {charts}")

        buttons = page.locator("button:visible").all()
        print(f"Buttons ({len(buttons)}):")
        for btn in buttons[:10]:
            print(f"  {btn.text_content().strip()[:50]}")

        # Explore Promotions page
        print("\n=== PROMOTIONS PAGE ===")
        page.goto(f"{BASE_URL}/dashboard/promotions", wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(2000)
        print(f"URL: {page.url}")
        body_text = " ".join((page.text_content("body") or "").split())[:500]
        print(f"Body (500): {body_text}")
        tables = page.locator("table, [role='grid'], .MuiDataGrid-root").count()
        print(f"Tables/Grids: {tables}")
        cards = page.locator(".MuiCard-root, .MuiPaper-root").count()
        print(f"Cards/Papers: {cards}")
        buttons = page.locator("button:visible").all()
        print(f"Buttons ({len(buttons)}):")
        for btn in buttons[:15]:
            t = btn.text_content().strip()[:50]
            if t:
                print(f"  {t}")

        # Explore Reviews page
        print("\n=== REVIEWS PAGE ===")
        page.goto(f"{BASE_URL}/dashboard/reviews", wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(2000)
        print(f"URL: {page.url}")
        body_text = " ".join((page.text_content("body") or "").split())[:500]
        print(f"Body (500): {body_text}")
        tables = page.locator("table, [role='grid'], .MuiDataGrid-root").count()
        print(f"Tables/Grids: {tables}")
        cards = page.locator(".MuiCard-root, .MuiPaper-root").count()
        print(f"Cards/Papers: {cards}")
        buttons = page.locator("button:visible").all()
        print(f"Buttons ({len(buttons)}):")
        for btn in buttons[:15]:
            t = btn.text_content().strip()[:50]
            if t:
                print(f"  {t}")

        browser.close()


if __name__ == "__main__":
    explore()
