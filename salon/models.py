import uuid
from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(default=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Barber(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    specialty = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('Haircut', 'Haircut'),
        ('Beard Trim', 'Beard Trim'),
        ('Haircut + Beard', 'Haircut + Beard'),
        ('Hair Dyeing', 'Hair Dyeing'),
        ('Children Haircut', 'Children Haircut'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Transfer', 'Bank Transfer'),
        ('POS', 'POS'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    ]

    booking_reference = models.CharField(max_length=20, unique=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    barber =models.ForeignKey(Barber, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='Cash')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.booking_reference} - {self.full_name}"

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            self.booking_reference = f"APT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def get_end_time(self):
        if self.service and self.time:
            from datetime import datetime, timedelta
            start_datetime = datetime.combine(self.date, self.time)
            end_datetime = start_datetime + timedelta(minutes=self.service.duration_minutes)
            return end_datetime.time()
        return None