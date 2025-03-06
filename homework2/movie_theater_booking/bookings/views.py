from .models.movie import Movie
from .models.seat import Seat
from .models.booking import Booking
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class MovieViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    ViewSet for managing movies (CRUD)
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SeatViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for checking seat availability.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    ViewSet for managing bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Each user can only view their own bookings.
        """
        return Booking.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Custom create method to ensure seat is available before booking.
        """
        seat_id = request.data.get("seat")
        movie_id = request.data.get("movie")

        try:
            seat = Seat.objects.get(id=seat_id)
            if seat.is_booked:
                return Response({"error": "Seat is already booked."}, status=status.HTTP_400_BAD_REQUEST)
            seat.is_booked = True
            seat.save()

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raisee_exception=True)
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Seat.DoesNotExist:
            return Response({"error": "Seat not found."}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.

class MovieListView(LoginRequiredMixin, View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'bookings/movie_list.html', {'movies': movies})

class SeatBookingView(LoginRequiredMixin, View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        available_seats = Seat.objects.filter(is_booked=False)
        booked_seats = Booking.objects.filter(movie=movie)
        return render(request, 'bookings/seat_booking.html', {'movie': movie, 'available_seats': available_seats, 'booked_seats': booked_seats})
    def post(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        seat_id = request.POST.get('seat_id')
        try:
            seat = Seat.objects.get(id=seat_id)
            if seat.is_booked:
                return render(request, 'bookings/seat_booking.html', {'movie': movie, 'error': 'Seat is already booked'})
            seat.is_booked = True
            seat.save()
            Booking.objects.create(movie=movie, seat=seat, user=request.user)
            return redirect('booking-history')
        except Seat.DoesNotExist:
            return render(request, 'bookings/seat_booking.html', {'movie': movie, 'error': 'Seat not found'})

class BookingHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'bookings/booking_history.html', {'bookings': bookings})


class UserLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")

