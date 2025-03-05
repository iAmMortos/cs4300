# Generated by Django 4.2.19 on 2025-03-05 07:44

from bookings.models.seat import Seat
from django.db import migrations


def create_seats(apps, schema_editor):
    for n in range(1, 21):
        Seat.objects.create(seat_number=n)


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0003_preload_movies"),
    ]

    operations = [
        migrations.RunPython(create_seats)
    ]

