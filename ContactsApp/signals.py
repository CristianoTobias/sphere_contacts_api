from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Contacts

@receiver(pre_save, sender=Contacts)
def set_default_user(sender, instance, **kwargs):
    if not instance.user_id:
        instance.user = User.objects.get(username='admin')