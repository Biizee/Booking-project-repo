from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.all, name="all"),
    path("booking_list/", booking_views.booking_list, name="booking_list"),
]
