# Generated by Django 3.2.12 on 2023-04-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharam_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_details',
            name='otp_verify',
            field=models.BooleanField(default=False),
        ),
    ]