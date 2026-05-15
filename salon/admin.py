from django.contrib import admin
from .models import Appointment, Barber, Service


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'booking_reference',
        'customer',
        'full_name',
        'service',
        'barber',
        'date',
        'time',
        'status',
        'payment_method',
        'payment_status',
    )

    list_filter = (
        'status',
        'payment_status',
        'payment_method',
        'service',
        'barber',
        'date',
    )

    search_fields = (
        'booking_reference',
        'full_name',
        'phone',
        'customer__username',
    )

    ordering = ('-date', '-time')


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'specialty')
    search_fields = ('name', 'phone', 'specialty')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes')
    search_fields = ('name',)