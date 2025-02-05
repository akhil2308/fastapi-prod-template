#!/bin/bash -e

python -V

# Apply database migrations
alembic upgrade head

# Running server
gunicorn -c gunicorn_conf.py
