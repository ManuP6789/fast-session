#!/bin/bash
# Create directories if they don't exist
mkdir -p /var/www/html
mkdir -p /var/www/backend

# Stop any running Flask application
pkill -f app.py || true
