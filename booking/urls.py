from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.booking_list, name="posts_list"),
]
