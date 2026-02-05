from django.shortcuts import render
from booking.models import Booking

# Create your views here.


def all(request):
    context = {}
    return render(
        request,
        template_name="booking/all.html",
        context=context
    )


def booking_list(request):
    bookings = Booking.objects.all()
    context = {
        "booking_list": bookings,
    }
    return render(
        request,
        template_name = "booking/booking_list.html",
        context=context,
    )
