#!/bin/bash

# Abort the script if any command fails
set -e

# Function to print an error message and exit
function error_exit {
    echo "$1" 1>&2
    exit 1
}

# Build the project
echo "Building the project..."
python3.12 -m pip install -r requirements.txt || error_exit "Failed to install requirements"

echo "Make Migration..."
python3.12 manage.py makemigrations --noinput || error_exit "Failed to make migrations"
python3.12 manage.py migrate --noinput || error_exit "Failed to migrate"

echo "Collect Static..."
python3.12 manage.py collectstatic --noinput --clear || error_exit "Failed to collect static files"
