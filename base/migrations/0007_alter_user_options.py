# Generated by Django 5.1.1 on 2024-10-03 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True},
        ),
    ]
