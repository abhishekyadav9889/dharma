# Generated by Django 4.2 on 2023-04-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharam_api', '0009_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('posted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
