# Seller Web Automation Framework Constitution

## Core Principles

### I. Hybrid Architecture First
- Framework supports **both UI and API** testing in single codebase
- UI tests use **Page Object Model (POM)** pattern
- API tests use **Endpoint classes** with **Pydantic models**
- Shared utilities and configuration for both layers
- Tests can combine UI and API operations for E2E scenarios

### II. Test Independence (NON-NEGOTIABLE)
- Each test must be **completely independent**
- Tests must not depend on execution order
- Function-scoped fixtures for test isolation
- No shared state between tests
- Parallel execution must be possible

### III. Data-Driven Testing
- Test data in **JSON files** only (no hardcoded values)
- UI test data: `test_data/*.json`
- API test data: `test_data/api/*.json`
- Use `TestDataLoader` for caching and validation
- Pydantic models validate API request/response data

### IV. Robust Selectors (UI)
- Use **semantic selectors**: `get_by_role`, `get_by_label`, `get_by_placeholder`
- Avoid dynamic CSS classes (`css-123abc`)
- Fallback locator patterns when needed
- No XPath unless absolutely necessary
- Locators must survive minor UI changes

### V. API Contract Validation
- All API requests validated via **Pydantic models**
- Response status codes properly checked
- Use `APIResponse` wrapper for consistent handling
- Log all requests/responses for debugging
- Clear error messages on validation failures

### VI. Observability & Logging
- Structured logging via `utils/logger.py`
- All test actions logged with context
- Failed requests captured automatically
- Screenshots on test failure
- Console logs captured for debugging

---

## Technology Standards

### Required Stack
| Layer | Technology | Version |
|-------|------------|---------|
| UI Automation | Playwright | 1.51.0+ |
| API Automation | httpx | 0.28.0+ |
| Data Validation | Pydantic | 2.10.0+ |
| Test Framework | pytest | 8.4.0+ |
| Reporting | Allure | 2.13.0+ |
| Language | Python | 3.13+ |

### Forbidden Practices
- `time.sleep()` - use proper waits
- Hardcoded credentials - use env vars
- Dynamic CSS selectors (`css-xyz123`)
- Shared mutable state between tests
- Direct HTTP requests without `BaseAPI`
- Unvalidated API request/response data

---

## Code Quality Standards

### File Organization
```
api/
├── base_api.py          # Base HTTP client
├── endpoints/           # One class per API domain
│   ├── auth_api.py
│   ├── seller_api.py
│   ├── product_api.py
│   └── invoice_api.py
└── models/              # Pydantic models
    ├── auth_models.py
    ├── seller_models.py
    ├── product_models.py
    └── invoice_models.py

pages/
├── base_page.py         # Base page class
├── login_page.py        # One class per page
├── dashboard_page.py
└── ...

tests/
├── api/                 # API tests
│   └── test_*_api.py
└── test_*.py            # UI tests
```

### Naming Conventions
| Type | Convention | Example |
|------|------------|---------|
| API Class | `{Domain}API` | `AuthAPI`, `ProductAPI` |
| Page Class | `{Page}Page` | `LoginPage`, `DashboardPage` |
| Test Class | `Test{Feature}` | `TestLogin`, `TestAuthAPI` |
| Test Method | `test_{action}_{scenario}` | `test_login_valid_credentials` |
| Model Class | `{Action}Request/Response` | `LoginRequest`, `ProductResponse` |

### Method Size Limits
- Maximum **15 lines** per method (KISS principle)
- Maximum **500 lines** per file
- Split complex logic into helper methods
- One responsibility per method (SRP)

---

## Testing Requirements

### Test Markers
```python
@pytest.mark.smoke       # Critical path tests
@pytest.mark.functional  # Full feature tests
@pytest.mark.negative    # Error/edge cases
@pytest.mark.api         # API-only tests
```

### Required Test Coverage
| Feature | UI Tests | API Tests |
|---------|----------|-----------|
| Login | Required | Required |
| Registration | Required | Required |
| Seller Registration | Required | Required |
| Product Management | Required | Required |
| Invoice Operations | Required | Required |

### Assertion Standards
- Use meaningful assertions with clear messages
- Check response status codes (API)
- Verify visible elements (UI)
- Validate data structure (API responses)
- Assert expected vs actual values

---

## Development Workflow

### Before Coding
1. Read `CLAUDE.md` and this Constitution
2. Understand existing patterns
3. Plan changes before implementing
4. Create/update test data if needed

### Commit Checklist
- [ ] Tests pass locally
- [ ] Code follows patterns
- [ ] No hardcoded values
- [ ] Type hints added
- [ ] Docstrings for public methods
- [ ] No flaky tests

### Review Criteria
- Follows POM/Endpoint patterns
- Proper error handling
- Meaningful logging
- Test isolation maintained
- Data validation in place

---

## Governance

- This Constitution **supersedes** all other practices
- Amendments require documentation and team approval
- All code must comply with these standards
- Use `CLAUDE.md` for implementation guidance
- Constitution violations must be justified and documented

**Version**: 1.0.0 | **Created**: 2025-12-18 | **Last Amended**: 2025-12-18