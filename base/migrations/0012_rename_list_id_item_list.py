# Generated by Django 5.1.1 on 2024-10-08 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_item_list_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='list_id',
            new_name='list',
        ),
    ]
