from django.shortcuts import render, redirect
from booking.models import Booking, Air_tickets, Room
from django.http import HttpResponse

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


def get_booking_by_id(request, pk):
    booking = Booking.objects.get(id = pk)
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



def get_air_ticket_by_id(request, pk):
    ticket = Air_tickets.objects.get(id = pk)
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


def get_room_by_id(request, pk):
    room = Room.objects.get(id = pk)
    context = {
        "room": room,
    }
    return render(
        request,
        template_name = "booking/rooms_details.html",
        context=context,
    )


def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(number = room_number)

        except ValueError:
            return HttpResponse(
                "Wrong value for room number!",
                status=400
            )
        
        except Room.DoesNotExist:
            return HttpResponse(
                "This room number doesn't exist",
                status=400
            )
        
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )

        return redirect("booking-details", pk=booking.id)

    else:
        return render(request, template_name="booking/booking_form.html")


def create_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        capacity = request.POST.get("capacity")
        location = request.POST.get("location")

        try:
            room = Room.objects.get(number = room_number)
            if room:
                return HttpResponse(
                "This room already exist!",
                status=400
            )

        except ValueError:
            return HttpResponse(
                "Wrong value for room number!",
                status=400
            )
        
        except Room.DoesNotExist:
            room = Room.objects.create(
                number = room_number,
                capacity=capacity,
                location = location,
            )

            return redirect("rooms-details", pk=room.id)

    else:
        return render(request, template_name="booking/room_form.html")


def create_ticket(request):
    if request.method == "POST":
        from_ = request.POST.get("from")
        to = request.POST.get("to")
        time = request.POST.get("time")
        airline_company = request.POST.get("airline-company")
        flight_number = request.POST.get("flight-number")
        booking_id = request.POST.get("booking-id")

        try:
            booking = Booking.objects.get(id = booking_id)

        except ValueError:
            return HttpResponse(
                "Wrong value!",
                status=400
            )
        
        except Room.DoesNotExist:
            return HttpResponse(
                "This room booking doesn't exist",
                status=400
            )
        
        ticket = Air_tickets.objects.create(
            tickets_from = from_,
            tickets_to = to,
            time = time,
            airline_company = airline_company,
            flight_number = flight_number,
            booking = Booking.objects.get(id = booking_id)
        )

        return redirect("ticket-details", pk=ticket.id)

    else:
        return render(request, template_name="booking/ticket_form.html")

