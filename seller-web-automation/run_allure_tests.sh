#!/bin/bash
# =====================================================
# Multiproduct Testlarni Allure TestOps'ga Yuklash
# =====================================================

set -e

# Configuration
ALLURE_ENDPOINT="https://greatmalldigital.testops.cloud"
ALLURE_TOKEN="ee2b462c-77fa-4cfb-8db7-3f47d308d68f"
ALLURE_PROJECT_ID="36"
TEMP_DIR="/tmp/seller-allure-results"
PROJECT_DIR="/Users/maxsudbekshavkatov/PycharmProjects/seller_web1"

# Clean temp directory
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

cd "$PROJECT_DIR"

echo "=== Running Multiproduct Tests ==="
QASE_MODE=off BASE_URL=https://staging-seller.greatmall.uz HEADLESS=true \
  python -m pytest tests/test_multiproduct.py \
  -v --alluredir="$TEMP_DIR" --tb=line || true

echo ""
echo "=== Test Results ==="
ls "$TEMP_DIR"/*.json 2>/dev/null | wc -l
echo " test result files generated"

echo ""
echo "=== Uploading to Allure TestOps ==="
./allurectl upload \
  --endpoint "$ALLURE_ENDPOINT" \
  --token "$ALLURE_TOKEN" \
  --project-id "$ALLURE_PROJECT_ID" \
  --launch-name "Multiproduct Tests $(date +%Y-%m-%d_%H:%M)" \
  "$TEMP_DIR"

echo ""
echo "=== Done! ==="
echo "View results at: $ALLURE_ENDPOINT/project/$ALLURE_PROJECT_ID/launches"
