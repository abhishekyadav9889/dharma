# Generated by Django 4.2 on 2023-04-15 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dharam_api', '0013_whatsapp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='whatsapp',
            new_name='settings',
        ),
    ]