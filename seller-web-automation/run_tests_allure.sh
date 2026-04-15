#!/bin/bash
# Скрипт для запуска тестов с отправкой результатов в Allure TestOps

set -e

# Загрузка переменных окружения
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Проверка обязательных переменных
if [ -z "$ALLURE_ENDPOINT" ] || [ -z "$ALLURE_TOKEN" ] || [ -z "$ALLURE_PROJECT_ID" ]; then
    echo "ERROR: Заполните файл .env со следующими переменными:"
    echo "  ALLURE_ENDPOINT=https://your-allure-server.com"
    echo "  ALLURE_TOKEN=your-api-token"
    echo "  ALLURE_PROJECT_ID=your-project-id"
    exit 1
fi

echo "=== Allure TestOps Configuration ==="
echo "Endpoint: $ALLURE_ENDPOINT"
echo "Project ID: $ALLURE_PROJECT_ID"
echo ""

# Очистка старых результатов
rm -rf allure-results/*

# Создание Launch в Allure TestOps
LAUNCH_NAME="Automated Tests - $(date '+%Y-%m-%d %H:%M:%S')"

echo "=== Running Tests with Allure Watch ==="

# Запуск тестов через allurectl watch (загружает результаты в реальном времени)
./allurectl watch --endpoint "$ALLURE_ENDPOINT" \
    --token "$ALLURE_TOKEN" \
    --project-id "$ALLURE_PROJECT_ID" \
    --launch-name "$LAUNCH_NAME" \
    --results allure-results \
    -- pytest tests/ --alluredir=allure-results -v --headless "$@"

echo ""
echo "=== Tests Complete ==="
echo "View results in Allure TestOps: $ALLURE_ENDPOINT/project/$ALLURE_PROJECT_ID/launches"
