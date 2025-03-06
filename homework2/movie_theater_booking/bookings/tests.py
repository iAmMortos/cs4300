
from django.test import TestCase
from django.contrib.auth.models import User
from bookings.models import Booking, Movie, Seat

class BookingModelTest(TestCase):
    def test_booking_creation(self):
        user = User.objects.create_user(username="testuser", password="password")
        movie = Movie.objects.create(title="Test Movie", description="Test Desc", release_date="2025-01-01", duration=120)
        seat = Seat.objects.create(seat_number="A1", is_booked=False)
        
        booking = Booking.objects.create(user=user, movie=movie, seat=seat)
        self.assertEqual(booking.user.username, "testuser")
