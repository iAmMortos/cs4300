Based on your requirements, I'll provide a revised implementation for the views and templates. I'll also create a new view for rendering the movie list with booking functionality.

First, let's update the `movies` view to handle CRUD operations. We'll create a `MovieViewSet` in `views.py`:

```python
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

Create a `serializers.py` file with the following content:

```python
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
```

Now, let's create views for the `seats` and `booking` pages.

Create a new view `SeatView` in `views.py`:

```python
from django.shortcuts import render, redirect
from .models import Seat, Movie, Booking
from django.contrib.auth.decorators import login_required

@login_required
def seat_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    available_seats = Seat.objects.filter(is_booked=False)
    booked_seats = Booking.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'available_seats': available_seats,
        'booked_seats': booked_seats
    }
    return render(request, 'bookings/seat_booking.html', context)
```

Update the `seat_booking.html` template:

```html
{% extends "bookings/base.html" %}

{% block title %}Seat Booking{% endblock %}

{% block content %}
    <div class="container mt-4">
        <h2 class="mb-4">Available Seats for {{ movie.title }}</h2>
        <form method="post">
            {% csrf_token %}
            <select name="seat_id">
                {% for seat in available_seats %}
                    <option value="{{ seat.id }}">{{ seat.seat_number }}</option>
                {% endfor %}
            </select>
            <button type="submit">Book Seat</button>
        </form>
        <p>Booked Seats:</p>
        <ul>
            {% for booking in booked_seats %}
                <li>{{ booking.seat.seat_number }}</li>
            {% endfor %}
        </ul>
    </div>
{% endblock %}
```

Create a new view `book_view` in `views.py` to handle the booking form submission:

```python
from django.shortcuts import render, redirect
from .models import Booking, Seat, Movie
from django.contrib.auth.decorators import login_required

@login_required
def book_view(request, movie_id):
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = Seat.objects.get(id=seat_id)
        movie = Movie.objects.get(id=movie_id)
        Booking.objects.create(movie=movie, seat=seat, user=request.user)
        seat.is_booked = True
        seat.save()
        return redirect('booking_history')
    return redirect('seat_booking', movie_id=movie_id)
```

Create a new view `booking_history_view` in `views.py` to display the user's booking history:

```python
from django.shortcuts import render
from .models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def booking_history_view(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/booking_history.html', context)
```

Update the `urls.py` file to include the new views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieViewSet.as_view({'get': 'list'}), name='movie_list'),
    path('seats/<int:movie_id>/', views.seat_view, name='seat_booking'),
    path('book/<int:movie_id>/', views.book_view, name='book'),
    path('booking/history/', views.booking_history_view, name='booking_history'),
]
```

Finally, update the `movies.html` template to include a link to the `seat_booking` view for each movie:

```html
{% extends "bookings/base.html" %}

{% block title %}Movie List{% endblock %}

{% block content %}
    <div class="container mt-4">
        <h2 class="mb-4">Available Movies</h2>
        <div class="row">
            {% for movie in movies %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">{{ movie.title }}</h5>
                            <p class="card-text">{{ movie.description }}</p>
                            <p><strong>Release Date:</strong> {{ movie.release_date }}</p>
                            <p><strong>Duration:</strong> {{ movie.duration }} min</p>
                            <a href="{% url 'seat_booking' movie.id %}">Book a Seat</a>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
{% endblock %}
```

This implementation should provide the desired functionality. Note that you may need to modify the templates and views to fit your specific requirements.

