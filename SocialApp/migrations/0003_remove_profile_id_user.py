# Generated by Django 4.1.13 on 2024-11-13 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0002_alter_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]
