#!/bin/bash

# Azure App Service startup script for Python Flask app
echo "Starting Salary Prediction Flask Application..."

# Install dependencies if needed
pip install -r requirements.txt

# Start the application with gunicorn
echo "Starting gunicorn server..."
exec gunicorn --bind=0.0.0.0:$PORT app:app
