## CLAUDE.md – Правила и руководство проекта (UI Автоматизация)

### КРИТИЧЕСКИЕ ПРАВИЛА

* **Если не знаешь — скажи "Я не знаю". НЕ ври и НЕ придумывай.**
* Читай `README.md` и `CLAUDE.md` перед любой новой задачей
* **НЕ** изменяй и не удаляй тесты без явного запроса
* **НЕ** трогай файлы, которые не упомянуты в задаче
* **НЕ** усложняй локаторы (избегай динамических CSS типа `css-123abc`)
* Используй **надежные селекторы** (`get_by_role`, `get_by_placeholder`, `has-text`) вместо нестабильных классов

---

### 📋 ТЕКУЩИЙ ПЛАН РАБОТЫ (2026-02-08)

**Цель:** Исправить все тесты чтобы они были PASSED или FAILED (не BROKEN/SKIPPED)

| # | Задача | Статус |
|---|--------|--------|
| 1 | Разобрать **BROKEN** тесты (216) - уточнить по UI | ⏳ В процессе |
| 2 | Разобрать **FAILED** тесты (207) - уточнить по UI | ⬜ Ожидает |
| 3 | Разобрать **SKIPPED** тесты (36) - уточнить по UI | ⬜ Ожидает |

### 🎯 ПРАВИЛО УТОЧНЕНИЯ ПО UI

**"Уточнение по UI"** = спросить у пользователя о наличии элементов в интерфейсе.

Когда тест падает из-за локатора (элемент не найден), Claude должен спросить:
- "Есть ли на странице X элемент Y?"
- "Виден ли пользователю кнопка/поле/секция Z?"
- "Как называется этот элемент на узбекском/русском?"

**Пользователь ответит:**
- Да/Нет - есть элемент или нет
- Название на нужном языке (UZ/RU/EN)
- Где именно находится элемент

**Пример:**
```
Claude: "Есть ли на Step 2 поле 'Barcode'?"
User: "Да, называется 'Shtrix-kod raqami' на узбекском"
Claude: [исправляет локатор]
```

---

### 🔥 ЖЕСТКОЕ ТЕСТИРОВАНИЕ - Стандарты QA Senior Engineer

## ⛔ КРИТИЧЕСКОЕ ПРАВИЛО: ТЕСТЫ ДИКТУЮТ, НЕ ПОДСТРАИВАЮТСЯ!

**НИКОГДА не изменяй тест чтобы он прошел если система работает неправильно!**

```python
# ❌ ЗАПРЕЩЕНО - подстраивать тест под систему:
def test_null_byte_injection(self):
    if has_null_bytes:
        logger.warning("Not sanitized")  # просто warning, тест PASS

# ✅ ПРАВИЛЬНО - тест показывает БАГ:
def test_null_byte_injection(self):
    assert "\x00" not in value, "BUG: Null bytes not sanitized!"
```

**Если тест падает - это БАГ в системе, а не проблема теста!**

| Ситуация | Неправильно ❌ | Правильно ✅ |
|----------|--------------|-------------|
| Тест падает | Изменить assertion на warning | Оставить FAIL - это БАГ |
| Система не валидирует | "Документировать поведение" | assert has_errors - это БАГ |
| Нет санитизации | Убрать проверку | assert sanitized - это БАГ |

**FAILED тесты = БАГИ которые нужно исправлять в СИСТЕМЕ!**

---

**ОБЯЗАТЕЛЬНО для всех тестов:**

| Правило | Плохо ❌ | Хорошо ✅ |
|---------|---------|----------|
| НЕТ SKIPPED | `pytest.skip("причина")` | `pytest.fail("FAILED: причина")` |
| НЕТ pass | `pass` | `assert condition, "сообщение"` |
| НЕТ assert True | `assert True` | `assert page.has_validation_errors()` |
| Реальная валидация | `assert "login" in url` | `assert error_count > 0` |
| НЕ подстраивать | `if error: logger.warning()` | `assert not error, "BUG!"` |

**Каждый Page Object ДОЛЖЕН иметь методы валидации:**
```python
def get_validation_error_count(self) -> int:
    """Получить количество ошибок валидации MUI."""
    return self.page.locator(".MuiFormHelperText-root.Mui-error").count()

def has_validation_errors(self) -> bool:
    """Проверить есть ли ошибки валидации."""
    return self.get_validation_error_count() > 0

def get_validation_error_messages(self) -> list:
    """Получить все сообщения об ошибках из UI."""

def has_error_for_field(self, field_name: str) -> bool:
    """Проверить есть ли ошибка у конкретного поля."""
```

**Каждый тест ДОЛЖЕН проверять реальное поведение:**
```python
# ПЛОХО - слабая проверка:
def test_empty_form(self):
    page.click_submit()
    assert "login" in page.url  # НЕ проверяет реальное поведение!

# ХОРОШО - жесткая проверка:
def test_empty_form(self):
    page.click_submit()
    assert page.has_validation_errors(), \
        "FAILED: Нет ошибок валидации для пустой формы"
    assert page.get_validation_error_count() >= 2, \
        f"FAILED: Ожидалось 2+ ошибки, получено {page.get_validation_error_count()}"
```

**Обязательные категории тестов для каждой страницы:**
- UI Elements (видимость, состояние элементов)
- Empty Fields (все пустые, частично пустые)
- Invalid Format (спецсимволы, XSS, SQL injection)
- Boundary Values (min/max длина, пробелы)
- Security (XSS, SQL injection, обход авторизации)
- Functional (основные рабочие процессы)
- Session (авторизация, сохранение сессии)
- E2E (полные сценарии от начала до конца)

---

### 🚀 АВТОМАТИЧЕСКОЕ ПРАВИЛО - Все возможные тесты

**БЕЗ ВОПРОСОВ добавлять ВСЕ возможные варианты тестов при работе над страницей!**

## ⛔ НО: Только тесты для РЕАЛЬНО СУЩЕСТВУЮЩИХ элементов!

**НЕ писать тесты для:**
- Элементов которых НЕТ на странице (кнопок, полей, секций)
- Функционала который НЕ реализован в UI
- Полей/кнопок которые существуют на других страницах, но НЕ на текущей
- Файловых загрузок если на странице НЕТ file upload
- Slug/SKU полей если их НЕТ на странице
- Любых элементов, в существовании которых Claude НЕ уверен

**Если Claude НЕ уверен есть ли элемент — СПРОСИТЬ у пользователя, а не писать тест!**

```
# ❌ ЗАПРЕЩЕНО — писать тест для несуществующего элемента
def test_file_upload_large(self):
    page.upload_file(...)  # На странице НЕТ загрузки файлов!

# ❌ ЗАПРЕЩЕНО — придумывать элементы
def test_description_xss(self):
    page.fill_description(...)  # Поля "description" НЕТ на этой странице!

# ✅ ПРАВИЛЬНО — спросить если не уверен
# Claude: "Есть ли на этой странице поле для загрузки файлов?"
# User: "Нет" → НЕ писать FileUpload тесты
# User: "Да" → Писать ВСЕ FileUpload тесты
```

При переходе на новую страницу АВТОМАТИЧЕСКИ:
1. Проанализировать ВСЕ **реально существующие** поля формы на странице
2. Проанализировать ВСЕ **реально существующие** кнопки и действия
3. Написать ВСЕ категории тестов **только для тех элементов которые ЕСТЬ**
4. **НЕ спрашивать "добавить ли еще тесты?" - добавлять сразу ВСЕ для существующих элементов**
5. **Если не уверен в наличии элемента — СПРОСИТЬ у пользователя**

**Чек-лист для каждого поля ввода:**
- [ ] Пустое значение
- [ ] Только пробелы
- [ ] Минимальная длина (1-2 символа)
- [ ] Максимальная длина (255+ символов)
- [ ] Спецсимволы (@#$%^&*)
- [ ] Unicode/эмодзи (🏪)
- [ ] HTML теги (`<script>alert('XSS')</script>`)
- [ ] SQL injection (`'; DROP TABLE users; --`)
- [ ] Кириллица + латиница смешанная
- [ ] Только цифры
- [ ] Табы и переносы строк

**Чек-лист для загрузки файлов:**
- [ ] Правильный формат и размер (успешная загрузка)
- [ ] Слишком большой файл (>5MB)
- [ ] Неправильный формат (.exe, .pdf вместо изображения)
- [ ] Пустой файл (0 bytes)
- [ ] Поддельное расширение (jpg переименованный в png)
- [ ] Без файла (обязательное поле)

**Чек-лист для кнопок/действий:**
- [ ] Клик в обычном состоянии
- [ ] Двойной клик
- [ ] Клик во время загрузки
- [ ] Отмена действия
- [ ] Повторное действие

**НЕ СПРАШИВАТЬ - ДЕЛАТЬ СРАЗУ!**

---

### ⚡ ПРОИЗВОДИТЕЛЬНОСТЬ И СКОРОСТЬ ТЕСТОВ

## ⛔ КРИТИЧЕСКОЕ ПРАВИЛО: НЕ ЛОГИНИТЬСЯ В КАЖДОМ ТЕСТЕ!

**Авторизация должна происходить ОДИН РАЗ за сессию, а не перед каждым тестом.**

### Обязательная структура conftest.py

```python
import pytest
import json
from pathlib import Path

AUTH_STATE_PATH = Path("test_data/.auth_state.json")


@pytest.fixture(scope="session")
def auth_state(browser):
    """Логин ОДИН раз за всю сессию, сохранение storage state."""
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://staging-seller.greatmall.uz/auth/login")
    page.fill("input[name='login']", "998001112233")
    page.fill("input[name='password']", "76543217")
    page.click("button[type='submit']")
    page.wait_for_url("**/dashboard/**", timeout=15000)
    state = context.storage_state()
    # Сохраняем на диск для параллельных воркеров
    AUTH_STATE_PATH.write_text(json.dumps(state))
    context.close()
    return state


@pytest.fixture
def authenticated_page(browser, auth_state):
    """Новая страница с уже авторизованным состоянием (без повторного логина)."""
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="class")
def authenticated_context(browser, auth_state):
    """Один контекст на весь класс тестов — для тестов одной страницы."""
    context = browser.new_context(storage_state=auth_state)
    yield context
    context.close()
```

### Правила scope для фикстур

| Scope | Когда использовать | Пример |
|-------|-------------------|--------|
| `session` | Авторизация, browser setup | `auth_state` |
| `class` | Все тесты одной страницы/класса | `shop_create_page` |
| `function` | Тесты которые меняют состояние (create/delete) | `clean_page` (свежая страница) |

```python
# ✅ ПРАВИЛЬНО — один контекст на класс, навигация один раз
@pytest.fixture(scope="class")
def shop_create_page(authenticated_context):
    page = authenticated_context.new_page()
    page.goto("/shops/create")
    return ShopCreatePage(page)

# ❌ ЗАПРЕЩЕНО — логин + навигация в каждом тесте
@pytest.fixture
def shop_create_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("/auth/login")
    # ... логин заново ...
    page.goto("/shops/create")
    return ShopCreatePage(page)
```

### Правила ожиданий (waits)

```python
# ❌ ЗАПРЕЩЕНО — никогда не использовать sleep
import time
time.sleep(3)
page.wait_for_timeout(5000)

# ✅ ПРАВИЛЬНО — явные ожидания конкретных событий
page.wait_for_url("**/dashboard/**", timeout=15000)
page.wait_for_selector(".MuiFormHelperText-root", state="visible")
page.wait_for_load_state("networkidle")
page.locator("button[type='submit']").wait_for(state="visible")

# ✅ ПРАВИЛЬНО — ожидание API ответа (для форм)
with page.expect_response("**/api/shops/**") as response_info:
    page.click("button[type='submit']")
response = response_info.value
```

| Запрещено ❌ | Правильно ✅ |
|-------------|-------------|
| `time.sleep(N)` | `page.wait_for_selector(...)` |
| `page.wait_for_timeout(N)` | `page.wait_for_url(...)` |
| Фиксированные задержки | `page.wait_for_load_state(...)` |
| `asyncio.sleep(N)` | `page.expect_response(...)` |

### Параллельный запуск

```bash
# Установить pytest-xdist
pip install pytest-xdist

# Запуск в 4 параллельных воркера
pytest -n 4

# Запуск с авто-определением количества ядер
pytest -n auto

# Запуск только рабочих тестов параллельно
pytest -n 4 -m "not broken"
```

**Правила для параллельных тестов:**
- Тесты НЕ должны зависеть друг от друга
- Каждый тест работает в своём browser context
- Тестовые данные не должны конфликтовать (уникальные имена, ID)
- Использовать `auth_state` из файла для всех воркеров

### Маркировка для оптимизации запуска

```python
import pytest

# Маркировать broken тесты чтобы не тратить время
@pytest.mark.broken
def test_something_broken(self):
    ...

# Маркировать по приоритету
@pytest.mark.smoke       # Быстрые критичные тесты (запускать первыми)
@pytest.mark.functional  # Основной функционал
@pytest.mark.security    # Тесты безопасности
@pytest.mark.negative    # Негативные сценарии
@pytest.mark.e2e         # Долгие end-to-end тесты (запускать последними)
```

```bash
# Быстрая проверка — только smoke
pytest -m smoke -n 4

# Полный прогон без broken
pytest -m "not broken" -n 4

# Только security тесты
pytest -m security
```

---

### 🧩 ЭФФЕКТИВНОСТЬ КОДА — DRY и переиспользование

## ⛔ КРИТИЧЕСКОЕ ПРАВИЛО: PARAMETRIZE ВМЕСТО КОПИПАСТЫ!

**Однотипные тесты (спецсимволы, injection, boundary) — ВСЕГДА через parametrize.**

### Общие тестовые данные (test_data/)

```
test_data/
├── security_payloads.json    # XSS, SQL, injection — для ВСЕХ страниц
├── boundary_values.json      # Min/max длина — для ВСЕХ страниц
├── whitespace_values.json    # Пробелы, табы, NBSP — для ВСЕХ страниц
├── file_upload_data.json     # Файловые тесты — для ВСЕХ страниц
├── shop_create_data.json     # Данные конкретной страницы
└── .auth_state.json          # Авторизация (автогенерация)
```

**security_payloads.json — переиспользуется на ВСЕХ страницах:**
```json
{
    "xss": [
        "<script>alert('XSS')</script>",
        "<img onerror=alert(1) src=x>",
        "javascript:alert('XSS')",
        "<svg onload=alert(1)>"
    ],
    "sql_injection": [
        "'; DROP TABLE users; --",
        "1' OR '1'='1",
        "' UNION SELECT * FROM users --"
    ],
    "special_chars": [
        "!@#$%^&*()",
        "🏪📦🎉",
        "<>&\"'\\/"
    ],
    "command_injection": [
        "; rm -rf /",
        "| cat /etc/passwd",
        "$(whoami)"
    ],
    "path_traversal": [
        "../../../etc/passwd",
        "..\\..\\windows\\system32"
    ],
    "null_bytes": [
        "test\u0000value",
        "%00admin"
    ]
}
```

### Parametrize — обязательный паттерн

```python
import json
import pytest
from pathlib import Path

# Загрузка общих тестовых данных
SECURITY = json.loads(Path("test_data/security_payloads.json").read_text())

class TestShopCreateSecurity:
    """Тесты безопасности — через parametrize, НЕ копипаста."""

    # ✅ ПРАВИЛЬНО — один тест, 4 payload, 4 строки в отчёте
    @pytest.mark.parametrize("payload", SECURITY["xss"])
    def test_name_field_rejects_xss(self, shop_page, payload):
        shop_page.fill_name(payload)
        shop_page.click_submit()
        assert shop_page.has_validation_errors(), \
            f"BUG: XSS не отклонён: {payload}"

    # ✅ ПРАВИЛЬНО — один тест покрывает все SQL injection
    @pytest.mark.parametrize("payload", SECURITY["sql_injection"])
    def test_name_field_rejects_sql(self, shop_page, payload):
        shop_page.fill_name(payload)
        shop_page.click_submit()
        assert shop_page.has_validation_errors(), \
            f"BUG: SQL injection не отклонён: {payload}"

    # ❌ ЗАПРЕЩЕНО — копипаста одного и того же теста
    # def test_xss_script_tag(self):
    #     page.fill_name("<script>alert('XSS')</script>")
    #     ...
    # def test_xss_img_onerror(self):
    #     page.fill_name("<img onerror=alert(1)>")
    #     ...
```

### Правила parametrize

| Когда | Как |
|-------|-----|
| Одно поле, разные значения | `@pytest.mark.parametrize("value", VALUES)` |
| Разные поля, одно значение | `@pytest.mark.parametrize("field", FIELDS)` |
| Комбинации | `@pytest.mark.parametrize("field,value", COMBOS)` |
| Данные из JSON | Загружать из `test_data/` |

### Переиспользуемые фикстуры для категорий

```python
# conftest.py — общие фикстуры для всех тестов

@pytest.fixture
def security_payloads():
    """Общие payload для тестов безопасности — загружается из JSON."""
    return json.loads(Path("test_data/security_payloads.json").read_text())

@pytest.fixture
def boundary_values():
    """Общие граничные значения — загружается из JSON."""
    return json.loads(Path("test_data/boundary_values.json").read_text())

@pytest.fixture
def whitespace_values():
    """Общие whitespace значения для тестов пробелов."""
    return [
        " ",           # один пробел
        "   ",         # множественные пробелы
        "\t",          # таб
        "\n",          # перевод строки
        "\u00A0",      # NBSP
        " test ",      # leading/trailing
        "te  st",      # множественные внутри
    ]
```

---

### 📁 СТРУКТУРА ФАЙЛОВ — Правило разбиения

## ⛔ КРИТИЧЕСКОЕ ПРАВИЛО: Максимум 500 строк на файл!

**Для страниц с 70-90 тестами — разбивать на 4-6 файлов по категориям:**

```
tests/shop_create/
├── __init__.py
├── conftest.py                         # Фикстуры специфичные для shop_create
├── test_shop_create_ui.py              # UI + Accessibility + ValidationUX (~15-18 тестов)
├── test_shop_create_validation.py      # Empty + Invalid + Boundary + Whitespace (~20-25 тестов)
├── test_shop_create_security.py        # Security + AdvancedSecurity + Injection (~15-18 тестов)
├── test_shop_create_files.py           # FileUpload + AdvancedFileUpload (~8-10 тестов)
└── test_shop_create_functional.py      # Functional + E2E + Robustness + Concurrent + Session (~20-25 тестов)
```

**Правила разбиения:**

| Файл | Категории из чеклиста | Примерно тестов | Примерно строк |
|------|----------------------|-----------------|----------------|
| `_ui.py` | UI, Accessibility, ValidationUX | 15-18 | 200-300 |
| `_validation.py` | Empty, Invalid, Boundary, Whitespace | 20-25 | 300-400 |
| `_security.py` | Security, AdvancedSecurity, Injection | 15-18 | 250-350 |
| `_files.py` | FileUpload, AdvancedFileUpload | 8-10 | 150-200 |
| `_functional.py` | Functional, E2E, Robustness, Concurrent, Session | 20-25 | 300-450 |

**Page Objects — тоже разбивать если >500 строк:**

```
pages/
├── shop_create/
│   ├── __init__.py
│   ├── shop_create_page.py          # Основные методы (навигация, заполнение, клики)
│   └── shop_create_validators.py    # Методы валидации (ошибки, состояния)
```

### conftest.py внутри тестовой папки

```python
# tests/shop_create/conftest.py
import pytest
from pages.shop_create.shop_create_page import ShopCreatePage


@pytest.fixture(scope="class")
def shop_page(authenticated_context):
    """Страница Shop Create — один контекст на класс."""
    page = authenticated_context.new_page()
    page.goto("/shops/create")
    yield ShopCreatePage(page)
    page.close()


@pytest.fixture
def fresh_shop_page(authenticated_page):
    """Свежая страница Shop Create — для тестов которые меняют состояние."""
    authenticated_page.goto("/shops/create")
    return ShopCreatePage(authenticated_page)
```

---

### Архитектура проекта

Это **UI automation framework** на базе Playwright:

```
seller_web1/
├── pages/                  # Page Object Model (классы страниц)
│   ├── base_page.py        # Базовый класс с общими методами
│   ├── login_page.py       # Страница логина
│   └── shop_create/        # Сложные страницы — в папках
│       ├── shop_create_page.py
│       └── shop_create_validators.py
├── tests/                  # UI тесты
│   ├── conftest.py         # Глобальные фикстуры (auth_state, payloads)
│   ├── test_login/         # Тесты по страницам
│   └── shop_create/        # Тесты разбиты по категориям
│       ├── conftest.py     # Фикстуры для shop_create
│       ├── test_shop_create_ui.py
│       ├── test_shop_create_validation.py
│       ├── test_shop_create_security.py
│       ├── test_shop_create_files.py
│       └── test_shop_create_functional.py
├── test_data/              # Тестовые данные (JSON файлы)
│   ├── security_payloads.json
│   ├── boundary_values.json
│   └── whitespace_values.json
├── utils/                  # Общие утилиты
└── config/                 # Конфигурация
```

---

### Принципы KISS и SOLID

* **KISS**: Методы маленькие и простые (до 15 строк)
* **SRP (Единая ответственность)**: Каждый Page класс отвечает только за одну страницу
* **OCP (Открыт/Закрыт)**: Пиши переиспользуемые методы вместо хардкода
* **DRY (Не повторяйся)**: Используй `@pytest.mark.parametrize` и общие JSON данные, избегай копипасты тестов
* **ISP и DIP**: Абстракции понятные (тесты используют методы, не сырые локаторы)

---

### Правила UI тестирования

* Всегда следуй **Page Object Model (POM)**
* Тестовые файлы должны быть **на основе классов** с понятными fixtures
* Каждый метод описывает **что**, а не **как** (например, `select_category("Электроника")`)
* Assertions должны быть осмысленными (проверка видимости, состояния, навигации)
* Используй **pytest маркеры** (`@pytest.mark.smoke`, `@pytest.mark.functional`, `@pytest.mark.negative`)

---

### Правила разработки

* Используй **английский** для кода (имена переменных, функций, классов), **комментарии на русском**
* Файлы не больше **500 строк**
* Всегда **запускай тесты локально** перед коммитом
* Коммить только **рабочий код**; никаких `TODO` или закомментированного кода
* Тестовые данные храни в **JSON или fixtures**, не хардкодь внутри тестов
* Используй **type hints** для всех параметров и возвращаемых значений

---

### Управление контекстом

* Перед большими фичами: используй `/clear`
* Ссылайся на `README.md` + `CLAUDE.md` при запросе изменений
* Для новых фич:
  1. Попроси план
  2. Согласуй структуру
  3. Только потом начинай код

---

### Чек-лист перед коммитом

* [ ] Код следует POM паттернам и SOLID
* [ ] Нет дублирующихся локаторов
* [ ] Тесты стабильные (нет flakiness, правильные ожидания)
* [ ] Нет `time.sleep()` или `wait_for_timeout()` — только явные waits
* [ ] `@pytest.mark.parametrize` использован для однотипных тестов
* [ ] Авторизация через `auth_state` фикстуру, не логин в каждом тесте
* [ ] Файлы не больше 500 строк
* [ ] Добавлены/обновлены тестовые данные если нужно
* [ ] Все тесты проходят локально

---

## Используемые технологии

**UI Автоматизация:**
- Python 3.13 + Playwright 1.51.0
- pytest 8.4.2
- pytest-xdist (параллельный запуск)
- allure-pytest 2.13.5

**Общее:**
- JSON файлы для тестовых данных (test_data/)
- Централизованный конфиг (config/settings.py)
- Общие утилиты (utils/)

---

## Запуск тестов

```bash
# Запустить все тесты (параллельно)
pytest -n 4

# Быстрая проверка — только smoke
pytest -m smoke -n 4

# Полный прогон без broken тестов
pytest -m "not broken" -n 4

# Только security тесты
pytest -m security -n 4

# Запуск конкретной страницы
pytest tests/shop_create/ -n 4

# Запуск с Allure отчетом
pytest --alluredir=allure-results -n 4
allure serve allure-results
```

---

## QA Senior Engineer - Плагины и команды

### Установленные плагины

| Плагин | Описание | Использование |
|--------|----------|---------------|
| **playwright** | Автоматизация браузера | Интерактивное тестирование, скриншоты |
| **security-guidance** | Лучшие практики безопасности | Обнаружение XSS, SQL injection |
| **code-review** | Автоматический код ревью | Ревью PR с оценкой уверенности |
| **pr-review-toolkit** | Комплексный ревью PR | Покрытие тестами, обработка ошибок |
| **feature-dev** | Разработка фич | 7-фазная разработка |
| **gitlab** | Интеграция с GitLab | MR, CI/CD пайплайны |
| **commit-commands** | Git автоматизация | /commit, /commit-push-pr |
| **code-simplifier** | Рефакторинг кода | Упрощение, читаемость |
| **pyright-lsp** | Проверка типов Python | Статический анализ |

---

### Slash команды

#### `/commit` - Автокоммит с умным сообщением
```bash
/commit
# Claude анализирует изменения, добавляет файлы, создает коммит
```

#### `/commit-push-pr` - Полный PR workflow
```bash
/commit-push-pr
# Создает ветку → коммит → пуш → создает PR с описанием
```

#### `/code-review` - Автоматический код ревью
```bash
/code-review
# Запускает 4 агента параллельно:
# - Соответствие CLAUDE.md
# - Поиск багов
# - Контекст git истории
# Показывает проблемы с оценкой ≥80
```

#### `/feature-dev` - 7-фазная разработка фич
```bash
/feature-dev Добавить тесты для страницы Shop Create
# Фаза 1: Выяснение требований
# Фаза 2: Исследование кодовой базы
# Фаза 3: Уточняющие вопросы
# Фаза 4: Проектирование архитектуры
# Фаза 5: Реализация
# Фаза 6: Ревью качества
# Фаза 7: Итог
```

#### `/clean_gone` - Очистка удаленных веток
```bash
/clean_gone
# Удаляет локальные ветки, удаленные на remote
```

---

### Агенты для ревью PR (автоматические)

#### pr-test-analyzer
**Фокус**: Качество покрытия тестами
```
"Проверь достаточно ли тестов"
"Ревью покрытия тестами для этого PR"
"Есть ли критические пробелы в тестах?"
```

#### silent-failure-hunter
**Фокус**: Обработка ошибок
```
"Проверь обработку ошибок"
"Найди тихие провалы"
"Проанализируй catch блоки"
```

#### comment-analyzer
**Фокус**: Точность документации
```
"Проверь правильные ли комментарии"
"Ревью документации которую я добавил"
```

#### code-reviewer
**Фокус**: Соответствие CLAUDE.md
```
"Проверь мои последние изменения"
"Все ли выглядит хорошо?"
```

#### code-simplifier
**Фокус**: Упрощение кода
```
"Упрости этот код"
"Сделай это понятнее"
```

---

### Агенты для разработки фич

#### code-explorer
**Когда использовать**: Понимание существующего кода
```
"Запусти code-explorer чтобы понять как работают login тесты"
"Исследуй как реализован Page Object Model"
```

#### code-architect
**Когда использовать**: Проектирование новых фич
```
"Запусти code-architect для проектирования тестов Shop Create"
"Спроектируй архитектуру для нового page object"
```

---

### Встроенные навыки

| Навык | Описание |
|-------|----------|
| webapp-testing | Взаимодействие с браузером Playwright |
| write-tests | Генерация комплексных тестов |
| test-quality-analyzer | Анализ качества тестов |
| generate-test-cases | Генерация тест-кейсов с покрытием |
| setup-visual-testing | Настройка визуального регрессионного тестирования |

---

### Примеры QA workflow

#### 1. После написания тестов
```
"Проверь мои последние изменения"
"Достаточно ли тестов?"
"Ревью покрытия тестами"
```

#### 2. Перед созданием PR
```
/code-review
# Или вручную:
"Запусти pr-test-analyzer и code-reviewer параллельно"
```

#### 3. Полная разработка фичи
```
/feature-dev Добавить тесты для страницы Invoice
# Следует 7-фазному workflow
```

#### 4. Быстрый коммит и PR
```
/commit              # Коммит с авто-сообщением
/commit-push-pr      # Полный workflow: коммит → пуш → PR
```

#### 5. Проверка качества кода
```
"Упрости этот тестовый класс"
"Проверь тихие провалы в обработке ошибок"
"Ревью дизайна типов Page Object"
```

---

### Лучшие практики QA

1. **Перед коммитом**: Запусти `/code-review` или попроси "Проверь мои последние изменения"
2. **После добавления тестов**: Спроси "Достаточно ли тестов?"
3. **Для новых фич**: Используй `/feature-dev` для управляемой разработки
4. **Регулярная очистка**: Запускай `/clean_gone` еженедельно
5. **Создание PR**: Используй `/commit-push-pr` для полного workflow

---

### Оценка уверенности

| Оценка | Значение |
|--------|----------|
| 0-25 | Низкая уверенность, скорее всего ложное срабатывание |
| 50-74 | Средняя, реальная но минорная проблема |
| **75-100** | Высокая уверенность, точно реальная проблема |

Только проблемы с оценкой ≥80 показываются в `/code-review`.

---

## 🎯 ПОЛНЫЙ QA ЧЕКЛИСТ - Проверка страниц

**ИСПОЛЬЗУЙ ЭТОТ ЧЕКЛИСТ для проверки полноты тестов на КАЖДОЙ странице!**

### Обязательные классы тестов (19 категорий)

```
✅ = есть и проверено
⚠️ = частично покрыто
❌ = отсутствует
```

| # | Класс | Описание | Тестов |
|---|-------|----------|--------|
| 1 | **UI** | Видимость элементов, состояния кнопок | 8-12 |
| 2 | **EmptyFields** | Пустые поля, частично заполненные формы | 4-6 |
| 3 | **InvalidFormat** | Спецсимволы, emoji, HTML теги, смешанные скрипты | 6-10 |
| 4 | **FileUpload** | Large file, wrong format, empty, fake extension | 4-6 |
| 5 | **Boundary** | Min/max длина, пробелы, граничные значения | 4-6 |
| 6 | **Security** | XSS, SQL injection, JavaScript URI | 4-6 |
| 7 | **Functional** | CRUD операции, основной workflow | 6-10 |
| 8 | **Session** | Авторизация, сохранение сессии, refresh | 3-5 |
| 9 | **E2E** | Полные сценарии от начала до конца | 4-6 |
| 10 | **Whitespace** | Tabs, newlines, NBSP, leading/trailing spaces | 4-5 |
| 11 | **AdvancedSecurity** | HTML/LDAP/Command/Null byte injection, path traversal | 5-6 |
| 12 | **AdvancedInput** | Copy/paste, input methods, autocomplete | 3-4 |
| 13 | **Robustness** | Double-click, slow network, rapid changes | 4-5 |
| 14 | **Accessibility** | Focus states, ARIA, keyboard navigation | 3-4 |
| 15 | **SlugSku** | (если есть) Slug/SKU валидация, спецсимволы | 4-6 |
| 16 | **DescriptionInjection** | (если есть) XSS/SQL в описаниях | 3-4 |
| 17 | **AdvancedFileUpload** | SVG XSS, double extension, corrupted | 3-5 |
| 18 | **Concurrent** | Multi-tab, state after error, idle timeout | 3-4 |
| 19 | **ValidationUX** | Realtime validation, blur, localization | 3-4 |

**Минимум для полного покрытия: ~70-90 тестов на страницу**

---

### Чеклист для каждого текстового поля

```markdown
[ ] Пустое значение → должна быть ошибка
[ ] Только пробелы → должна быть ошибка или trim
[ ] 1 символ → min length проверка
[ ] 2-3 символа → граничное значение
[ ] 255+ символов → max length проверка
[ ] Спецсимволы (!@#$%^&*) → санитизация
[ ] Unicode emoji (🏪📦) → обработка
[ ] HTML теги (<script>alert('XSS')</script>) → экранирование
[ ] SQL injection ('; DROP TABLE; --) → безопасная обработка
[ ] Кириллица + латиница (Test Тест) → обработка
[ ] Только цифры (123456) → валидация
[ ] Tabs (\t) → удаление или замена
[ ] Newlines (\n) → удаление в однострочных полях
[ ] NBSP (\u00A0) → обработка
[ ] Leading/trailing пробелы → trim
[ ] Множественные пробелы → нормализация
[ ] Null bytes (\x00) → удаление (сервер)
[ ] LDAP injection (*)(uid=*) → безопасная обработка
[ ] Command injection (; rm -rf /) → безопасная обработка
[ ] Path traversal (../../../etc/passwd) → блокировка
```

---

### Чеклист для файловых загрузок

```markdown
[ ] Правильный формат и размер → успешная загрузка
[ ] Большой файл (>5MB) → ошибка размера
[ ] Неправильный формат (.txt, .exe) → ошибка формата
[ ] Пустой файл (0 bytes) → ошибка
[ ] Fake extension (txt renamed to png) → проверка magic bytes
[ ] SVG с XSS payload → блокировка или санитизация
[ ] Двойное расширение (image.png.exe) → блокировка
[ ] Corrupted/битый файл → ошибка
[ ] Замена загруженного файла → корректная работа
[ ] Без обязательного файла → ошибка валидации
```

---

### Чеклист для slug/SKU полей (если есть)

```markdown
[ ] Пробелы в slug → замена на дефисы или ошибка
[ ] Спецсимволы в slug (!@#$) → удаление
[ ] Кириллица в slug → транслитерация или ошибка
[ ] Дубликат slug → ошибка конфликта
[ ] Дубликат SKU → ошибка конфликта
[ ] Спецсимволы в SKU → обработка
[ ] Auto-generation → проверка генерации
[ ] Manual edit → возможность редактирования
```

---

### Чеклист для кнопок и действий

```markdown
[ ] Обычный клик → корректная работа
[ ] Double-click → идемпотентность (не создавать дубликаты)
[ ] Клик во время загрузки → блокировка или очередь
[ ] Disabled состояние → кнопка неактивна когда форма невалидна
[ ] Cancel/отмена → данные не сохраняются
[ ] Повторное действие → корректная работа
[ ] Submit во время upload → ожидание загрузки
```

---

### Чеклист для concurrent/state

```markdown
[ ] Данные сохраняются после ошибки валидации
[ ] Независимая работа в разных вкладках
[ ] Корректная работа после долгого idle
[ ] Session timeout handling
[ ] Refresh не теряет данные (если applicable)
```

---

### Чеклист для accessibility

```markdown
[ ] Видимые focus states на полях
[ ] Правильные ARIA атрибуты (role, aria-label)
[ ] Полная keyboard navigation (Tab, Enter, Escape)
[ ] Escape закрывает модальные окна
[ ] Screen reader support (labels)
```

---

### Чеклист для validation UX

```markdown
[ ] Realtime validation при вводе
[ ] Validation on blur (потеря фокуса)
[ ] Локализованные сообщения об ошибках
[ ] Понятные error messages
[ ] Error состояние визуально заметно
```

---

### Как использовать чеклист

**При работе над страницей:**

1. Открой этот чеклист
2. Пройди по всем 19 категориям
3. Отметь что уже покрыто ✅
4. Добавь недостающие тесты ❌
5. Результат: 70-90+ тестов на страницу

**Пример для Shop Create (92 теста):**
```
✅ UI (11)
✅ EmptyFields (5)
✅ InvalidFormat (8)
✅ FileUpload (5)
✅ Boundary (4)
✅ Security (4)
✅ Functional (9)
✅ Session (3)
✅ E2E (5)
✅ Whitespace (5)
✅ AdvancedSecurity (5)
✅ AdvancedInput (3)
✅ Robustness (4)
✅ Accessibility (3)
✅ SlugSku (5)
✅ DescriptionInjection (3)
✅ AdvancedFileUpload (4)
✅ Concurrent (3)
✅ ValidationUX (3)
─────────────────────
TOTAL: 92 тестов ✅
```

**НЕ СПРАШИВАТЬ - ПРОВЕРЯТЬ ПО ЧЕКЛИСТУ И ДОБАВЛЯТЬ!**

---

## 📋 ПРОГРЕСС И ПЛАН

> **Актуальный план и прогресс → см. `~/.claude/NOW.md` (MASTER PLAN)**
> CLAUDE.md = стабильные правила. NOW.md = динамический прогресс.

### Логин (для всех тестов)

- URL: `https://staging-seller.greatmall.uz/auth/login`
- Селекторы: `input[name='login']`, `input[name='password']`, `button[type='submit']`
- Credentials: `998001112233` / `76543217`
- После логина: редирект на `/dashboard/become-seller`
- `wait_for_url("**/dashboard/**", timeout=15000)` — надёжный способ ждать
