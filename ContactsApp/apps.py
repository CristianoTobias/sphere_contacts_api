from django.apps import AppConfig


class ContactsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ContactsApp'

    def ready(self):
        import ContactsApp.signals



    