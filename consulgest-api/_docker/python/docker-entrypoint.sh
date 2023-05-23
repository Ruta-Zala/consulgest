#!/bin/bash

echo "Updating database migrations"
python manage.py makemigrations

echo "Applying database migrations"
python manage.py migrate

echo "Syncing DB"
python manage.py migrate --run-syncdb

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
