# Generated by Django 4.2.19 on 2025-03-05 05:39

from django.db import migrations
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    User.objects.create_user(username="user1", password="user1")
    User.objects.create_user(username="user2", password="user2")



class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
