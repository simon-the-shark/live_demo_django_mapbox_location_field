#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn live_demo_django_mapbox_location_field.wsgi --bind=0.0.0.0:80