import os, sys

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "services.django.service.settings"
)
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc

from lib import resolver

class Django:
    START = "runserver"
    CREATESUPERUSER = "cratesuperuser"

    _conf = resolver("services", "django")
    _host = _conf.search("host").data
    _port = _conf.search("port").data
    _reload = _conf.search("reload").data

    def __init__(self):
        sys.argv = [sys.argv[0], "runserver", "{}:{}".format(self._host, self._port)]
        if self._reload is False:
            sys.argv.append("--noreload")
        execute_from_command_line(sys.argv)


if __name__ == "__main__":
    Django()