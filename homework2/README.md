# Homework 2
A movie booking app created using Django and Bootstrap.

Run a `python manage.py migrate` to preload the database with some test data.
This includes two users: `user1` and `user2`. Their login information is explicitly given on the login screen.
Use one user to create some bookings, then switch to the other user to obvserve they cannot view each other's information, but seats remain booked.

## Endpoints
The API endpoints give some UI-based DB management. These endpoints are also used within the app to create/edit/delete objects

- `api/`
    - `movies/`
    - `bookings/`
    - `seats/`

The user-facing endpoints allow a user to view available movies

- `movies/`: view available movies, and select one for booking
    - `<int:movie_id>/seats/`: Select a seat for the selected movie
- `bookings/`: Show current user's bookes seats and movies. Allow a user to cancel bookings.
- `login/`: Automatically redirected here if not logged in.
- `logout/`

ChatGPT was used extensively for the boilerplate parts of the app while learning this new framework.
