# Generated by Django 5.1.1 on 2024-10-08 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_item_options_alter_lists_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.lists'),
        ),
    ]
