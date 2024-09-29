from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username