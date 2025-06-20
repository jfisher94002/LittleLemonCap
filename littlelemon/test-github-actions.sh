#!/bin/bash
# Test script to mimic GitHub Actions behavior

echo "🧪 Testing GitHub Actions workflow locally..."
echo ""

# Simulate the Django project detection logic
if [ -f "manage.py" ]; then
    DJANGO_DIR="."
    SETTINGS_MODULE="littlelemon.settings"
    echo "✅ Found Django project in root directory"
elif [ -f "littlelemon/manage.py" ]; then
    DJANGO_DIR="littlelemon"
    SETTINGS_MODULE="littlelemon.settings"
    echo "✅ Found Django project in littlelemon directory"
else
    echo "❌ ERROR: Could not find manage.py"
    find . -name "manage.py" -type f
    exit 1
fi

echo "📂 Django directory: $DJANGO_DIR"
echo "⚙️  Settings module: $SETTINGS_MODULE"
echo ""

# Change to Django directory
cd "$DJANGO_DIR"

# Set Django settings
export DJANGO_SETTINGS_MODULE="$SETTINGS_MODULE"

echo "📋 Running Django system checks..."
python manage.py check
if [ $? -ne 0 ]; then
    echo "❌ Django checks failed"
    exit 1
fi
echo "✅ Django checks passed"
echo ""

echo "🗄️  Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "❌ Migrations failed"
    exit 1
fi
echo "✅ Migrations completed"
echo ""

echo "🧪 Running tests..."
python manage.py test
if [ $? -ne 0 ]; then
    echo "❌ Tests failed"
    exit 1
fi
echo "✅ Tests passed"
echo ""

echo "🎉 All GitHub Actions simulation checks passed!"
