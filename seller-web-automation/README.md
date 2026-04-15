# Seller Web Automation Framework

[![Playwright](https://img.shields.io/badge/Playwright-v1.40+-brightgreen)](https://playwright.dev/)
[![pytest](https://img.shields.io/badge/pytest-v8.4+-blue)](https://pytest.org/)
[![Qase.io](https://img.shields.io/badge/Qase.io-Integrated-orange)](https://qase.io/)
[![Python](https://img.shields.io/badge/Python-3.13+-yellow)](https://www.python.org/)

Professional end-to-end test automation framework for the Seller Web platform, implementing **Playwright + Pytest** with **Page Object Model (POM)** architecture and integrated with **Qase.io TestOps** and **GitLab CI/CD**.

---

## 📊 Test Coverage Summary

| Suite                          | Total Tests | Automated | Coverage | Status      |
|--------------------------------|-------------|-----------|----------|-------------|
| Login                          | 7           | 7         | 100%     | ✅ Complete |
| Registration                   | 8           | 3         | 38%      | 🔄 In Progress |
| OTP                            | 6           | 0         | 0%       | ⏳ Planned  |
| Become Seller Registration     | 27          | 3         | 11%      | 🔄 In Progress |
| New Shop & Dashboard           | 24          | 0         | 0%       | ⏳ Planned  |
| Staff Create                   | 9           | 0         | 0%       | ⏳ Planned  |
| Products                       | 48          | 0         | 0%       | ⏳ Planned  |
| Consignment Notes              | 83          | 0         | 0%       | ⏳ Planned  |
| **TOTAL**                      | **212**     | **13**    | **6%**   | 🚀 Active   |

*Last updated: 2025-10-15*

> **📋 For detailed test mapping, see** [docs/test_mapping.csv](docs/test_mapping.csv)

---

## 🏗️ Architecture & Technology Stack

### Framework Architecture
- **Design Pattern:** Page Object Model (POM)
- **Programming Language:** Python 3.13+
- **Test Framework:** Pytest 8.4+
- **Browser Automation:** Playwright 1.40+
- **Test Management:** Qase.io TestOps
- **CI/CD:** GitLab CI/CD
- **Reporting:** pytest-html + Qase.io Dashboard

### Core Principles
- **KISS (Keep It Simple, Stupid)** — Clear, readable code
- **SOLID Principles** — Maintainable, scalable architecture
- **DRY (Don't Repeat Yourself)** — Reusable components
- **Robust Locators** — Accessibility-first selectors (`get_by_role`, `get_by_label`)

### Project Structure
```
seller_web1/
├── pages/                    # Page Object Models
│   ├── base_page.py         # Base page with common methods
│   ├── login_page.py        # Login page object
│   ├── registration_page.py # Registration page object
│   └── becomeseller_page.py # Become seller page object
├── tests/                   # Test suites
│   ├── test_login.py       # Login test cases (7 tests)
│   ├── test_registration.py # Registration tests (3 tests)
│   └── test_becomeseller.py # Become seller tests (3 tests)
├── test_data/              # Test data (JSON)
│   ├── login_test_data.json
│   ├── registration_test_data.json
│   └── becomeseller_test_data.json
├── reports/                # Test execution reports
├── docs/                   # Documentation
│   └── test_mapping.csv   # Test coverage mapping
├── scripts/               # Utility scripts
│   └── generate_mapping.py # Auto-generate test mapping
├── conftest.py           # Pytest configuration & fixtures
├── pytest.ini            # Pytest settings
├── .env                  # Environment configuration
├── .gitlab-ci.yml       # CI/CD pipeline
├── CLAUDE.md           # Development guidelines
└── README.md          # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd seller_web1
```

2. **Create virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install chromium
```

4. **Configure environment:**
Create a `.env` file with your credentials:
```bash
# Qase.io Configuration
QASE_MODE=testops
QASE_TESTOPS_MODE=testops
QASE_API_TOKEN=your_qase_api_token
QASE_PROJECT_CODE=SW
QASE_ENVIRONMENT=dev
QASE_RUN_COMPLETE=true

# Test Environment
BASE_URL=https://dev-seller.greatmall.uz
BROWSER=chromium
HEADLESS=false
```

---

## 🧪 Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test Suite
```bash
# Login tests
pytest tests/test_login.py -v

# Registration tests
pytest tests/test_registration.py -v

# Become seller tests
pytest tests/test_becomeseller.py -v
```

### Run by Test Marker
```bash
# Smoke tests only
pytest -m smoke -v

# Negative tests only
pytest -m negative -v

# Functional tests only
pytest -m functional -v
```

### Run Specific Test
```bash
pytest tests/test_login.py::TestLogin::test_verify_login_ui_elements -v
```

### Run with Different Browser
```bash
pytest tests/test_login.py --browser_name=firefox -v
pytest tests/test_login.py --browser_name=webkit -v
```

### Run Against Different Environment
```bash
pytest tests/test_login.py --url_name=https://staging-seller.greatmall.uz -v
```

---

## 📈 Test Reporting

### HTML Report
After test execution, open the HTML report:
```bash
open reports/report.html  # macOS
xdg-open reports/report.html  # Linux
start reports/report.html  # Windows
```

### Qase.io Dashboard
View real-time test results in Qase.io:
- **Project:** [SW - Seller Web](https://app.qase.io/project/SW)
- **Test Runs:** https://app.qase.io/run/SW/dashboard

After each test run, the console displays:
```
[Qase][16:09:53][info] Test run link: https://app.qase.io/run/SW/dashboard/24
```

### Generate Test Mapping Report
Update the test coverage mapping file:
```bash
python scripts/generate_mapping.py
```

This generates/updates `docs/test_mapping.csv` with the latest test status from Qase.io.

---

## 🔄 CI/CD Integration

### GitLab CI/CD Pipeline
The project includes automated test execution via GitLab CI/CD:

- **Trigger:** Push to `main` or `dev` branch, or manual trigger
- **Stages:** Install → Test → Report → Upload to Qase.io
- **Artifacts:** HTML reports, test mapping CSV
- **Notifications:** Test results sent to Qase.io

See [.gitlab-ci.yml](.gitlab-ci.yml) for pipeline configuration.

### Manual Pipeline Trigger
Go to GitLab → CI/CD → Pipelines → Run Pipeline

---

## 📝 Writing New Tests

### 1. Create Page Object (if needed)
```python
# pages/dashboard_page.py
from pages.base_page import BasePage
from playwright.sync_api import Locator

class DashboardPage(BasePage):
    @property
    def user_menu(self) -> Locator:
        return self.page.get_by_role("button", name="User Menu")

    def click_user_menu(self) -> None:
        self.user_menu.click()
```

### 2. Create Test File
```python
# tests/test_dashboard.py
import pytest
from qase.pytest import qase
from pages.dashboard_page import DashboardPage

class TestDashboard:
    @qase.id(10)  # Qase.io test case ID
    @qase.title("Verify dashboard user menu")
    @pytest.mark.smoke
    def test_verify_dashboard_user_menu(self, setup_pages):
        dashboard_page = setup_pages
        dashboard_page.click_user_menu()
        assert dashboard_page.is_user_menu_open()
```

### 3. Add Test Data (if needed)
```json
// test_data/dashboard_test_data.json
{
  "user_name": "Test User",
  "menu_items": ["Profile", "Settings", "Logout"]
}
```

See [CLAUDE.md](CLAUDE.md) for detailed development guidelines.

---

## 🛠️ Maintenance & Best Practices

### Code Quality Guidelines
- Follow **KISS** and **SOLID** principles
- Keep methods under 15 lines
- Use **robust locators** (`get_by_role`, `get_by_label`, `get_by_text`)
- Avoid dynamic CSS classes (`.css-123abc`)
- Write meaningful assertions
- Keep test data in JSON files

### Locator Strategy Priority
1. **ARIA roles:** `get_by_role("button", name="Login")`
2. **Labels:** `get_by_label("Email")`
3. **Text content:** `get_by_text("Submit")`
4. **Placeholder:** `get_by_placeholder("Enter email")`
5. **Test IDs:** `get_by_test_id("submit-btn")` (last resort)

### Test Stability
- Use `wait_for()` for dynamic elements
- Avoid hard `sleep()` — use Playwright's auto-waiting
- Handle flaky tests with proper waits and assertions

---

## 📚 Documentation

- **[CLAUDE.md](CLAUDE.md)** — Development rules & guidelines
- **[docs/test_mapping.csv](docs/test_mapping.csv)** — Test coverage mapping
- **[Qase.io Project](https://app.qase.io/project/SW)** — Test management platform
- **[HTML_REPORTING.md](HTML_REPORTING.md)** — HTML report configuration

---

## 🤝 Contributing

1. Create a feature branch from `dev`
2. Follow coding guidelines in [CLAUDE.md](CLAUDE.md)
3. Write tests following POM pattern
4. Run tests locally and ensure they pass
5. Create merge request to `dev` branch
6. Ensure CI/CD pipeline passes

---

## 📞 Support & Contact

- **QA Team Lead:** QA Automation Team
- **Qase.io Project:** https://app.qase.io/project/SW
- **GitLab Repository:** [Internal Repository]

---

## 📄 License

Internal project — Proprietary and confidential.

---

**Last Updated:** October 15, 2025
**Maintained by:** QA Automation Team