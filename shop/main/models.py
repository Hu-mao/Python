
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.png',
        blank=True
    )

    def __str__(self):
        return self.name
