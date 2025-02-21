from rest_framework import generics
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render


# Movies
class MovieListCreateView(generics.ListCreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Seats
class SeatListCreateView(generics.ListCreateAPIView):
  queryset = Seat.objects.all()
  serializer_class = SeatSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class SeatDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Seat.objects.all()
  serializer_class = SeatSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Bookings
class BookingListCreateView(generics.ListCreateAPIView):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
