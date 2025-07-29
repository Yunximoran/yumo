#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import uvicorn

import pymysql
pymysql.install_as_MySQLdb()

def startasgi(host="localhost", port=8000, reload:bool=True):
    uvicorn.run(
        app="services.yumoback.settings.asgi:application",
        host=host, 
        port=port,
        reload=reload
        )

def startup(argv=sys.argv):
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "services.yumoback.settings.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(argv)

def initdb(app="models"):
    startup([sys.argv[0], "makemigrations", app])
    startup([sys.argv[0], "migrate", app])

__all__ = [
    "startup",
    "startasgi",
    "initdb"
]
if __name__ == "__main__":
    startup()
