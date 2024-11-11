#!/bin/sh
cd /usr/src/api
celery -A configs.celery_cfg worker -l info -B
