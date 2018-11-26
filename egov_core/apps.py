from django.apps import AppConfig


class EgovCoreConfig(AppConfig):
    name = 'egov_core'
    verbose_name = 'eGov Core'

    def ready(self):
        import egov_core.signals
