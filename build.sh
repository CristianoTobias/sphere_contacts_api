#!/bin/bash

# Instalar as dependências do projeto
python pip install -r requirements.txt

# Executar as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate
