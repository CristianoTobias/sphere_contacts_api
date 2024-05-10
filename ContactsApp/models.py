from django.db import models

class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.name