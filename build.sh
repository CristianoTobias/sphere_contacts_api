#!/bin/bash

# Ativar ambiente virtual Python
source /python312/bin/activate

# Instalar as dependências do projeto
pip install -r requirements.txt

# Executar as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate
