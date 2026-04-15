"""
Скрипт для исследования Order Detail страницы.
Логин → Orders List → клик на заказ → скриншот + анализ DOM.
"""

from playwright.sync_api import sync_playwright
import json
from pathlib import Path

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("1. Логинимся на стейджинг...")
        page.goto('https://staging-seller.greatmall.uz/auth/login')
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(2000)

        # Логин
        page.fill('input[name="login"]', '998001112233')
        page.fill('input[name="password"]', '76543217')

        # Клик submit и ждем либо редиректа либо ошибки
        page.click('button[type="submit"]')

        # Ждем 5 секунд и проверяем что произошло
        page.wait_for_timeout(5000)
        current_url = page.url
        print(f"   После логина: {current_url}")

        # Проверяем есть ли ошибка или OTP modal
        if "login" in current_url:
            # Все еще на login странице
            error = page.locator(".MuiFormHelperText-root.Mui-error, .error, [class*='error']").first
            if error.is_visible(timeout=1000):
                print(f"   ❌ Ошибка логина: {error.inner_text()}")

            otp_modal = page.locator("text=OTP, text=Код, text=Введите код").first
            if otp_modal.is_visible(timeout=1000):
                print("   ⚠️ Появился OTP модал - стейджинг требует OTP!")
                browser.close()
                return

            print("   ❌ Логин не прошел, URL не изменился")
            page.screenshot(path='/tmp/login_failed.png')
            browser.close()
            return

        print(f"   ✅ Залогинились: {current_url}")

        print("\n2. Переходим на Orders List...")
        page.goto('https://staging-seller.greatmall.uz/dashboard/orders-management/orders?page=1&size=10')
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(2000)

        # Скриншот Orders List
        page.screenshot(path='/tmp/orders_list.png', full_page=True)
        print("   Скриншот: /tmp/orders_list.png")

        print("\n3. Ищем первый заказ и кликаем на него...")
        # Попробуем найти ссылки на заказы
        order_links = page.locator("a[href*='/orders/']").all()

        if not order_links:
            print("   ⚠️ Заказов не найдено! Проверяем HTML...")
            content = page.content()
            Path('/tmp/orders_list_html.html').write_text(content, encoding='utf-8')
            print("   HTML сохранен: /tmp/orders_list_html.html")

            # Проверим есть ли таблица/грид
            rows = page.locator("tr, [role='row']").all()
            print(f"   Найдено строк в таблице: {len(rows)}")

            if len(rows) == 0:
                print("   ❌ Страница пустая - нет заказов")
                browser.close()
                return

        print(f"   Найдено заказов: {len(order_links)}")

        # Кликаем на первый заказ
        first_order = order_links[0]
        order_href = first_order.get_attribute('href')
        print(f"   Кликаем на: {order_href}")

        first_order.click()
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(2000)

        detail_url = page.url
        print(f"\n4. Order Detail URL: {detail_url}")

        # Скриншот Order Detail
        page.screenshot(path='/tmp/order_detail.png', full_page=True)
        print("   Скриншот: /tmp/order_detail.png")

        print("\n5. Анализ UI элементов...")

        # Заголовок страницы
        h1 = page.locator("h1, h2, h3").first
        if h1.is_visible(timeout=3000):
            print(f"   Заголовок: {h1.inner_text()}")

        # Кнопки
        buttons = page.locator("button").all()
        print(f"   Кнопок: {len(buttons)}")
        for i, btn in enumerate(buttons[:5]):  # первые 5
            try:
                text = btn.inner_text(timeout=500)
                if text.strip():
                    print(f"      - {text}")
            except:
                pass

        # Таблицы/Гриды
        tables = page.locator("table, [role='grid']").all()
        print(f"   Таблиц/Гридов: {len(tables)}")

        # Поля информации (типа Order ID, Status, Total)
        labels = page.locator("label, .label, [class*='Label']").all()
        print(f"   Labels: {len(labels)}")

        # Сохраняем HTML
        content = page.content()
        Path('/tmp/order_detail_html.html').write_text(content, encoding='utf-8')
        print("\n   HTML сохранен: /tmp/order_detail_html.html")

        # Собираем структуру
        structure = {
            "url": detail_url,
            "title": h1.inner_text() if h1.is_visible(timeout=1000) else "N/A",
            "buttons_count": len(buttons),
            "tables_count": len(tables),
            "labels_count": len(labels)
        }

        Path('/tmp/order_detail_structure.json').write_text(
            json.dumps(structure, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        print("\n✅ Структура сохранена: /tmp/order_detail_structure.json")
        print("\nОставляю браузер открытым на 30 секунд для ручного исследования...")
        page.wait_for_timeout(30000)

        browser.close()

if __name__ == "__main__":
    main()
