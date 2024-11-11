#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn configs.wsgi --bind 0.0.0.0:8000 --workers=3 --worker-connections=12 --worker-class=gevent
