# Fresh Cut Barbing Salon Scheduler

Fresh Cut Barbing Salon Scheduler is a personal scheduling web application built with Python and Django. The system allows customers to create an account, log in, view salon services, book appointments, choose a barber, track appointment status, and view payment status.

## Features

- Customer registration
- Customer login and logout
- Salon services management
- Barber/staff management
- Appointment booking
- Customer dashboard
- My appointments page
- Booking reference number generation
- Appointment status tracking
- Payment method and payment status tracking
- Appointment cancellation
- Prevention of double booking
- Service-duration based appointment conflict checking
- Opening hours validation
- Sunday booking restriction
- Past-date booking prevention
- Django admin dashboard
- Responsive and styled user interface

## Business Type

Barbing Salon

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Git and GitHub

## How the System Works

Customers can register and log in to the web application. After logging in, they can view available services, select a barber, choose a date and time, select a payment method, and book an appointment.

The system checks if the selected barber is available at the chosen time. It also checks the salon opening hours and prevents bookings on Sundays or in the past.

The admin can manage services, barbers, appointments, appointment status, and payment status through the Django admin dashboard.

## Opening Hours

- Monday - Friday: 9:00 AM - 7:00 PM
- Saturday: 10:00 AM - 6:00 PM
- Sunday: Closed

## How to Run the Project

1. Clone the repository:

    git clone https://github.com/som-tee02/barbing_salon_scheduler.git

2. Move into the project folder:

    cd barbing_salon_scheduler

3. Create a virtual environment:

    python -m venv .venv

4. Activate the virtual environment:

    For macOS/Linux:

    source .venv/bin/activate

    For Windows:

    .venv\Scripts\activate

5. Install Django:

    pip install django

6. Run migrations:

    python manage.py migrate

7. Create a superuser:

    python manage.py createsuperuser

8. Start the server:

    python manage.py runserver

9. Open the application in your browser:

    http://127.0.0.1:8000/

## Admin Panel

The admin panel can be accessed through:

    http://127.0.0.1:8000/admin/

The admin can manage:

- Services
- Barbers
- Appointments
- Appointment status
- Payment status

## Main User Flow

1. Customer creates an account.
2. Customer logs in.
3. Customer views available services.
4. Customer books an appointment.
5. System generates a unique booking reference.
6. Admin reviews the appointment.
7. Admin approves, cancels, or completes the appointment.
8. Admin updates payment status.
9. Customer views updated appointment and payment status.

## Project Status

This project is developed as a Django-based personal scheduling web application for a barbing salon business.
