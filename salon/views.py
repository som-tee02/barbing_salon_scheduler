from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta, time, date as current_date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment, Service, Barber


def home(request):
    services = Service.objects.all()
    barbers = Barber.objects.all()

    context = {
        'services': services,
        'barbers': barbers,
        'service_count': services.count(),
        'barber_count': barbers.count(),
    }

    return render(request, 'salon/home.html', context)

def services(request):
    services = Service.objects.all()
    return render(request, 'salon/services.html', {'services': services})

@login_required(login_url='login')
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            barber = form.cleaned_data['barber']
            service = form.cleaned_data['service']
            appointment_date = form.cleaned_data['date']
            selected_time = form.cleaned_data['time']

            new_start = datetime.combine(appointment_date, selected_time)
            new_end = new_start + timedelta(minutes=service.duration_minutes)

            # Prevent booking in the past
            if appointment_date < current_date.today():
                form.add_error(None, 'You cannot book an appointment in the past.')

            else:
                # Python weekday numbers:
                # Monday = 0, Tuesday = 1, Wednesday = 2,
                # Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6
                day_of_week = appointment_date.weekday()

                # Block Sundays
                if day_of_week == 6:
                    form.add_error(None, 'The salon is closed on Sundays. Please choose another day.')

                else:
                    # Saturday opening hours
                    if day_of_week == 5:
                        opening_time = time(10, 0)
                        closing_time = time(18, 0)

                    # Monday to Friday opening hours
                    else:
                        opening_time = time(9, 0)
                        closing_time = time(19, 0)

                    opening_datetime = datetime.combine(appointment_date, opening_time)
                    closing_datetime = datetime.combine(appointment_date, closing_time)

                    # Check if selected time is before opening
                    if new_start < opening_datetime:
                        form.add_error(None, 'The selected time is before salon opening hours.')

                    # Check if appointment ends after closing
                    elif new_end > closing_datetime:
                        form.add_error(None, 'This appointment will end after salon closing time. Please choose an earlier time.')

                    else:
                        existing_appointments = Appointment.objects.filter(
                            barber=barber,
                            date=appointment_date
                        ).exclude(status='Cancelled')

                        conflict_found = False

                        for appointment in existing_appointments:
                            existing_start = datetime.combine(appointment.date, appointment.time)
                            existing_end = existing_start + timedelta(
                                minutes=appointment.service.duration_minutes
                            )

                            if new_start < existing_end and new_end > existing_start:
                                conflict_found = True
                                break

                        if conflict_found:
                            form.add_error(
                                None,
                                'This barber already has an appointment during that time. Please choose another time or barber.'
                            )

                        else:
                            appointment = form.save(commit=False)
                            appointment.customer = request.user
                            appointment.save()
                            messages.success(request, 'Appointment booked successfully.')
                            return redirect('appointment_list')

    else:
        form = AppointmentForm()

    return render(request, 'salon/book_appointment.html', {'form': form})

@login_required(login_url='login')
def appointment_list(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.filter(customer=request.user).order_by('-date', '-time')
        return render(request, 'salon/appointment_list.html', {'appointments': appointments})
    else:
        return redirect('login')

@login_required(login_url='login')
def customer_dashboard(request):
    appointments = Appointment.objects.filter(customer=request.user)

    total_appointments = appointments.count()
    pending_appointments = appointments.filter(status='Pending').count()
    approved_appointments = appointments.filter(status='Approved').count()
    cancelled_appointments = appointments.filter(status='Cancelled').count()
    completed_appointments = appointments.filter(status='Completed').count()

    latest_appointment = appointments.order_by('-date', '-time').first()

    context = {
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'approved_appointments': approved_appointments,
        'cancelled_appointments': cancelled_appointments,
        'completed_appointments': completed_appointments,
        'latest_appointment': latest_appointment,
    }

    return render(request, 'salon/dashboard.html', context)

@login_required(login_url='login')
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        customer=request.user
    )

    if request.method == 'POST':
        appointment.status = 'Cancelled'
        appointment.save()
        messages.success(request, 'Appointment cancelled successfully')
        return redirect('appointment_list')

    return redirect('appointment_list')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully. Welcome!')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'salon/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'salon/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def about(request):
    return render(request, 'salon/about.html')