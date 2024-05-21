#!/bin/bash
python3 manage.py migrate --noinput && python3 manage.py collectstatic --noinput && gunicorn user.wsgi:application --bind 0.0.0.0:8000
