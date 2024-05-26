#!/bin/bash

# Build the project
echo "Building the project..."
python3.12 -m pip install -r requirements.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.ph migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noimput --clear