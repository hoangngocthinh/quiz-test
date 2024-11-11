#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

daphne --bind 0.0.0.0 --port 8000 configs.asgi:application