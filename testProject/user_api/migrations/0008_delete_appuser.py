# Generated by Django 4.1.13 on 2024-03-09 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0007_appuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppUser',
        ),
    ]
