"""
WSGI config for bitvavo_dca project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

from bitvavo_dca.setup import setup_env

setup_env()

application = get_wsgi_application()
