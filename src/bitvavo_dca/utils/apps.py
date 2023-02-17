from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "bitvavo_dca.utils"

    def ready(self):
        from . import checks  # noqa
