# Generated by Django 4.1.13 on 2024-11-21 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0022_alter_comment_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
