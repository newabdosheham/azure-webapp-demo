#!/bin/bash

# Create virtual environment if not exists
if [ ! -d "/home/site/wwwroot/antenv" ]; then
    python3 -m venv /home/site/wwwroot/antenv
fi

# Activate the virtual environment
source /home/site/wwwroot/antenv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r /home/site/wwwroot/requirements.txt

# Run Gunicorn to serve the app
exec gunicorn --bind 0.0.0.0:8000 app:app
