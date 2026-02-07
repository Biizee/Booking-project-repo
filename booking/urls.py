from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.all, name="all"),
    path("booking-list/", booking_views.booking_list, name="booking-list"),
    path("booking-list/<int:pk>/", booking_views.get_booking_by_id, name="booking-details"),
    path("tickets-list/", booking_views.air_tickets_list, name="air-tickets-list"),
    path("tickets-list/<int:pk>/", booking_views.get_air_ticket_by_id, name="ticket-details"),
    path("rooms-list/", booking_views.rooms_list, name="rooms-list"),
    path("rooms-list/<int:pk>/", booking_views.get_room_by_id, name="rooms-details"),
    path("book-room/", booking_views.book_room, name="book-room"),
    path("create-room/", booking_views.create_room, name="create-room"),
]
