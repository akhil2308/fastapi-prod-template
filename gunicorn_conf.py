"""Gunicorn *development* config file"""

import os
from settings import logging_config

wsgi_app = "main:app"

# The granularity of Error log outputs
loglevel = "info"

# The number of worker processes for handling requests
workers = int(os.environ.get('WORKERS', 1))

worker_class = 'uvicorn.workers.UvicornWorker'

# The socket to bind
bind = "0.0.0.0:8000"

# Since there is no '--reload' flag in your command, I'm assuming it's not required for development
reload = False
# reload = True   

# Write access and error info to stdout and stderr respectively
accesslog = "-"
errorlog = "-"

