#!/bin/sh

# Start Gunicorn
#chmod +x /usr/src/api/gunicorn.sh
#/usr/src/api/gunicorn.sh &

# Start Danphne
chmod +x /usr/src/api/daphne.sh
/usr/src/api/daphne.sh &


# Start Celery
chmod +x /usr/src/api/celery_start.sh
/usr/src/api/celery_start.sh &

# Wait for all background processes to finish
wait