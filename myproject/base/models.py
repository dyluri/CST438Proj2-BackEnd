from django.db import models

# Create your models here.

class Lists(models.Model):
    user_id = models.IntegerField()
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=32)
    # TODO: this is temporary need to change in the future 
    # to allow for an sql join from lists and item tables to get items in list
    item_list = models.TextField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'lists'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    signed_in = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    class Meta:
        managed = False
        db_table = 'users'

