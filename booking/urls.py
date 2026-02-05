from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.all, name="all"),
    path("booking_list/", booking_views.booking_list, name="booking_list"),
    path("booking_list/<int:booking_id>/", booking_views.get_booking_by_id, name="booking_details"),
    path("tickets_list/", booking_views.air_tickets_list, name="air_tickets_list"),
    path("tickets_list/<int:ticket_id>/", booking_views.get_air_ticket_by_id, name="ticket_details"),
    path("rooms_list/", booking_views.rooms_list, name="rooms_list"),
    path("rooms_list/<int:room_id>/", booking_views.get_room_by_id, name="rooms_details"),
]
