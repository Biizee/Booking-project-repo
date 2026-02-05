from django.shortcuts import render
from booking.models import Booking, Air_tickets, Room

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


def get_booking_by_id(request, booking_id):
    booking = Booking.objects.get(id = booking_id)
    context = {
        "booking": booking,
    }
    return render(
        request,
        template_name="booking/booking_details.html",
        context=context,
    )


def air_tickets_list(request):
    tickets = Air_tickets.objects.all()
    context = {
        "tickets_list": tickets,
    }
    return render(
        request,
        template_name = "booking/tickets_list.html",
        context=context,
    )



def get_air_ticket_by_id(request, ticket_id):
    ticket = Air_tickets.objects.get(id = ticket_id)
    context = {
        "ticket" : ticket,
    }
    return render(
        request,
        template_name = "booking/tickets_details.html",
        context=context,
    )


def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms_list": rooms,
    }
    return render(
        request,
        template_name = "booking/rooms_list.html",
        context=context,
    )


def get_room_by_id(request, room_id):
    room = Room.objects.get(id = room_id)
    context = {
        "room": room,
    }
    return render(
        request,
        template_name = "booking/rooms_details.html",
        context=context,
    )

