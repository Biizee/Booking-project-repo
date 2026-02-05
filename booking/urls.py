from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.all, name="all"),
    path("booking_list/", booking_views.booking_list, name="booking_list"),
    path("booking_list/<int:booking_id>/", booking_views.get_booking_by_id, name="booking_details"),
]
