#!/bin/bash

# Azure App Service startup script for Python Flask app
echo "Starting Salary Prediction Flask Application..."

# Set working directory
cd /home/site/wwwroot

# Install dependencies if needed
echo "Installing requirements..."
pip install -r requirements.txt

# Start the application with gunicorn
echo "Starting gunicorn server with explicit app reference..."
exec gunicorn --bind=0.0.0.0:$PORT --timeout 600 --access-logfile '-' --error-logfile '-' app:app
