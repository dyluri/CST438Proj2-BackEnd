from django.db import models

# Create your models here.

class Lists(models.Model):
    user_id = models.IntegerField()
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=32)
    item_list = models.TextField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'lists'