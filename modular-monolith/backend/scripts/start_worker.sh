#! /bin/bash

watchmedo auto-restart -d /app -p '*.py' --recursive -- celery  --app $PROJECT worker -E --loglevel=INFO -B