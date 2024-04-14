#!/usr/bin/env bash

set -e

# echo $(date) - Applying migrations
# python manage.py migrate --no-input

echo $(date) - Starting Uvicorn/gunicorn
gunicorn -b 0.0.0.0:8000 -w 16 -k uvicorn.workers.UvicornWorker broker.asgi:application