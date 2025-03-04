from .models.movie import Movie
from .models.seat import Seat
from .models.booking import Booking
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render
from django.views import View


class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing movies (CRUD)
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SeatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for checking seat availability.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
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

class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'bookings/movie_list.html', {'movies': movies})

class SeatBookingView(View):
    def get(self, request):
        seats = Seat.objects.all()
        return render(request, 'bookings/seat_booking.html', {'seats': seats})

class BookingHistoryView(View):
    def get(self, request):
        history = Booking.objects.all()
        return render(request, 'bookings/booking_history.html', {'history': history})

