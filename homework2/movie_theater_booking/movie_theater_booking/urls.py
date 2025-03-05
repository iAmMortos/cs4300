"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include
from bookings.views import MovieListView, SeatBookingView, BookingHistoryView, UserLoginView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')),
    path('movies/', MovieListView.as_view(), name="movie-list"),
    path('movies/<int:movie_id>/seats/',SeatBookingView.as_view(), name="seat-booking"),
    # path('seats/', SeatBookingView.as_view(), name="seat-booking"),
    path('bookings/', BookingHistoryView.as_view(), name="booking-history"),
    path('', RedirectView.as_view(url='movies/')),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
