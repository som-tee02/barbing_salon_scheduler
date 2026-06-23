from decimal import Decimal
from django.db import migrations


def seed_services_and_barbers(apps, schema_editor):
    Service = apps.get_model('salon', 'Service')
    Barber = apps.get_model('salon', 'Barber')

    services = [
        {
            'name': 'Classic Haircut',
            'price': Decimal('1500.00'),
            'duration_minutes': 30,
            'description': 'A neat and professional haircut suitable for school, work, and everyday appearance.'
        },
        {
            'name': 'Skin Fade',
            'price': Decimal('2000.00'),
            'duration_minutes': 40,
            'description': 'A clean fade haircut with sharp blending for a modern and stylish look.'
        },
        {
            'name': 'Low Cut',
            'price': Decimal('1200.00'),
            'duration_minutes': 25,
            'description': 'A simple, clean, and low-maintenance haircut for a fresh appearance.'
        },
        {
            'name': 'Beard Trim',
            'price': Decimal('800.00'),
            'duration_minutes': 20,
            'description': 'Professional beard trimming and shaping for a neat facial look.'
        },
        {
            'name': 'Haircut and Beard Trim',
            'price': Decimal('2500.00'),
            'duration_minutes': 50,
            'description': 'A complete grooming package that includes haircut, beard trim, and clean finishing.'
        },
        {
            'name': 'Hair Dyeing',
            'price': Decimal('3500.00'),
            'duration_minutes': 60,
            'description': 'Professional hair coloring service for customers who want a fresh and stylish change.'
        },
        {
            'name': 'Hair Wash',
            'price': Decimal('1000.00'),
            'duration_minutes': 20,
            'description': 'Refreshing hair wash service to keep the scalp clean before or after a haircut.'
        },
        {
            'name': 'Dreadlocks Maintenance',
            'price': Decimal('5000.00'),
            'duration_minutes': 90,
            'description': 'Maintenance and styling service for dreadlocks to keep them neat and well-arranged.'
        },
        {
            'name': 'Children Haircut',
            'price': Decimal('1000.00'),
            'duration_minutes': 25,
            'description': 'A neat haircut service specially handled for children.'
        },
        {
            'name': 'VIP Grooming Package',
            'price': Decimal('6000.00'),
            'duration_minutes': 90,
            'description': 'Premium grooming package including haircut, beard trim, wash, and luxury finishing.'
        },
    ]

    for service in services:
        Service.objects.get_or_create(
            name=service['name'],
            defaults={
                'price': service['price'],
                'duration_minutes': service['duration_minutes'],
                'description': service['description'],
            }
        )

    barbers = [
        {
            'name': 'Emeka Johnson',
            'phone': '08012345678',
            'specialty': 'Skin Fade Specialist'
        },
        {
            'name': 'Chidi Okoro',
            'phone': '08098765432',
            'specialty': 'Beard Styling Expert'
        },
        {
            'name': 'David Martins',
            'phone': '08123456789',
            'specialty': 'Hair Dyeing and Modern Cuts'
        },
        {
            'name': 'Kelvin Nwosu',
            'phone': '08104567890',
            'specialty': 'Dreadlocks Maintenance'
        },
        {
            'name': 'Samuel Eze',
            'phone': '09033445566',
            'specialty': 'Classic Haircuts and Children Cuts'
        },
    ]

    for barber in barbers:
        Barber.objects.get_or_create(
            name=barber['name'],
            defaults={
                'phone': barber['phone'],
                'specialty': barber['specialty'],
            }
        )


def remove_services_and_barbers(apps, schema_editor):
    Service = apps.get_model('salon', 'Service')
    Barber = apps.get_model('salon', 'Barber')

    Service.objects.filter(
        name__in=[
            'Classic Haircut',
            'Skin Fade',
            'Low Cut',
            'Beard Trim',
            'Haircut and Beard Trim',
            'Hair Dyeing',
            'Hair Wash',
            'Dreadlocks Maintenance',
            'Children Haircut',
            'VIP Grooming Package',
        ]
    ).delete()

    Barber.objects.filter(
        name__in=[
            'Emeka Johnson',
            'Chidi Okoro',
            'David Martins',
            'Kelvin Nwosu',
            'Samuel Eze',
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0007_appointment_booking_reference'),
    ]

    operations = [
        migrations.RunPython(seed_services_and_barbers, remove_services_and_barbers),
    ]