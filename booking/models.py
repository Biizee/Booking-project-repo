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
    


class Air_tickets(models.Model):
    tickets_from = models.CharField(max_length=512)
    tickets_to = models.CharField(max_length=512)
    time = models.DateTimeField()
    airline_company = models.TextField()
    flight_number = models.IntegerField()

    def __str__(self):
        return f"{self.tickets.tickets_from}/{self.tickets.tickets_to}"
    
    class Meta:
        verbose_name = "Air ticket"
        verbose_name_plural = "Air tickets"
        ordering = ["time"]


        