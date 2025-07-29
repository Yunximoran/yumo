import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "services.yumoback.settings.settings")

try:
    django.setup()
except RuntimeError:
    pass