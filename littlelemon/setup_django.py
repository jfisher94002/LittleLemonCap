#!/usr/bin/env python
"""
Django test configuration script
Run this before any test imports to ensure Django is properly configured
"""
import os
import sys
import django
from django.conf import settings

def setup_django():
    """Setup Django configuration for testing"""
    
    # Add current directory to Python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    # Set DJANGO_SETTINGS_MODULE if not already set
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')
    
    # Configure Django if not already configured
    if not settings.configured:
        django.setup()
    
    print(f"Django configured with settings: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

if __name__ == "__main__":
    setup_django()
