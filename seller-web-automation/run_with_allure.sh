#!/bin/bash
# =====================================================
# Allure TestOps bilan Test Run qilish
# =====================================================

# Environment variables
export ALLURE_ENDPOINT="https://greatmalldigital.testops.cloud"
export ALLURE_TOKEN="ee2b462c-77fa-4cfb-8db7-3f47d308d68f"
export ALLURE_PROJECT_ID="36"
export ALLURE_LAUNCH_NAME="Seller Web Automated Tests"

# 1. LOKAL RUN (allure-results yaratadi)
echo "=== Running tests locally ==="
pytest tests/test_multiproduct.py -v --alluredir=allure-results

# 2. ALLURE TESTOPS'GA YUBORISH
echo "=== Uploading results to Allure TestOps ==="
./allurectl upload --project-id $ALLURE_PROJECT_ID allure-results

# 3. ALLURE REPORT KO'RISH (lokal)
# allure serve allure-results
