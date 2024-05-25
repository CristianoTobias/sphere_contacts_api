from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Contacts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = User.objects.get(username='admin')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
