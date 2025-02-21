from rest_framework import serializers
from .models import Movie, Seat, Booking


class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seat
    fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
  movie = MovieSerializer(read_only=True)
  seat = SeatSerializer(read_only=True)

  class Meta:
    model = Booking
    fields = '__all__'
