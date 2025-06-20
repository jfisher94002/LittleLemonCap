#!/bin/bash
# Local CI script to run the same checks as GitHub Actions

echo "🚀 Running Local CI Checks..."
echo ""

echo "📋 Running Django system checks..."
python manage.py check
if [ $? -ne 0 ]; then
    echo "❌ Django system checks failed"
    exit 1
fi
echo "✅ Django system checks passed"
echo ""

echo "🧪 Running tests..."
python manage.py test
if [ $? -ne 0 ]; then
    echo "❌ Tests failed"
    exit 1
fi
echo "✅ Tests passed"
echo ""

echo "🔍 Running flake8 syntax checks..."
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
if [ $? -ne 0 ]; then
    echo "❌ Syntax errors found"
    exit 1
fi
echo "✅ No syntax errors"
echo ""

echo "📝 Running flake8 style checks..."
flake8 . --count --exit-zero --statistics
echo "✅ Style check completed"
echo ""

echo "🎨 Checking code formatting with black..."
black --check --diff .
if [ $? -ne 0 ]; then
    echo "⚠️  Code formatting issues found (run 'black .' to fix)"
else
    echo "✅ Code formatting is good"
fi
echo ""

echo "📦 Checking import sorting with isort..."
isort --check-only --diff .
if [ $? -ne 0 ]; then
    echo "⚠️  Import sorting issues found (run 'isort .' to fix)"
else
    echo "✅ Import sorting is good"
fi
echo ""

echo "🔒 Running security checks with bandit..."
bandit -r . -x ./venv,./env,./.venv
if [ $? -ne 0 ]; then
    echo "⚠️  Security issues found"
else
    echo "✅ No security issues found"
fi
echo ""

echo "🎉 All checks completed!"
