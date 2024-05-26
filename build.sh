#!/bin/bash

# Abort the script if any command fails
set -e

# Build the project
echo "Building the project..."
python3.12 -m pip install -r requirements.txt

echo "Make Migration..."
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

echo "Collect Static..."
python3.12 manage.py collectstatic --noinput --clear

# Criação do superusuário usando variáveis de ambiente
echo "Creating superuser..."
python3.12 manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.getenv('SUPERUSER_NAME')
email = os.getenv('SUPERUSER_EMAIL')
password = os.getenv('SUPERUSER_PASSWORD')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
EOF

echo "Superuser created successfully."