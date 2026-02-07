from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return f"Room #{self.number} - {self.capacity}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time"]


class Air_tickets(models.Model):
    tickets_from = models.CharField(max_length=512)
    tickets_to = models.CharField(max_length=512)
    time = models.DateTimeField()
    airline_company = models.TextField()
    flight_number = models.IntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return f"#{self.flight_number} {self.tickets_from}/{self.tickets_to} - {self.airline_company}"
    
    class Meta:
        verbose_name = "Air ticket"
        verbose_name_plural = "Air tickets"
        ordering = ["time"]