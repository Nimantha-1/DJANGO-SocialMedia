# Generated by Django 4.1.13 on 2024-11-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
