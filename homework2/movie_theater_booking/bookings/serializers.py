from rest_framework import serializers
from .models.movie import Movie
from .models.seat import Seat
from .models.booking import Booking


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # auto-assign user
    
    class Meta:
        model = Booking
        fields = '__all__'
