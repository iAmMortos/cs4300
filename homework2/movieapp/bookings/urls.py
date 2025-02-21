from django.urls import path
from .views import (
  MovieListCreateView, MovieDetailView,
  SeatListCreateView, SeatDetailView,
  BookingListCreateView, BookingDetailView
)

urlpatterns = [
  path('movies/', MovieListCreateView.as_view(), name="movie-list"),
  path('movies/<int:pk>/', MovieDetailView.as_view(), name="movie-detail"),

  path('seats/', SeatListCreateView.as_view(), name='seat-list'),
  path('seats/<int:pk>/', SeatDetailView.as_view(), name='seat-detail'),

  path('bookings/', BookingListCreateView.as_view(), name='booking-list'),
  path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail')
]