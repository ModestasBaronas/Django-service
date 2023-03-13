from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentStepOneForm, AppointmentStepTwoForm
from .models import Appointment, Car, Customer


def home(request):
    return render(request, 'home.html')


def make_appointment_step_one(request):
    if request.method == 'POST':
        form = AppointmentStepOneForm(request.POST)
        if form.is_valid():
            # Create a new customer object or fetch an existing one if email already exists
            email = form.cleaned_data['email']
            customer, created = Customer.objects.get_or_create(email=email)
            if created:
                customer.name = form.cleaned_data['name']
                customer.phone_number = form.cleaned_data['phone_number']
                customer.save()

            # Create a new appointment object with the customer object
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            appointment = Appointment(date=date, time=time, customer=customer)
            appointment.save()

            # Store appointment ID in session and redirect to step two
            request.session['appointment_id'] = appointment.id
            return redirect('make_appointment_step_two')
    else:
        form = AppointmentStepOneForm()

    return render(request, 'appointment/make_appointment_step_one.html', {'form': form})


def make_appointment_step_two(request):
    # Get the appointment ID from the session
    appointment_id = request.session.get('appointment_id')
    if not appointment_id:
        messages.error(request, 'Appointment ID not found in session.')
        return redirect('make_appointment_step_one')

    # Fetch the appointment object
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        messages.error(request, 'Appointment object not found in database.')
        return redirect('make_appointment_step_one')

    if request.method == 'POST':
        form = AppointmentStepTwoForm(request.POST)
        if form.is_valid():
            # Create a new car object with the appointment object and form data
            year = form.cleaned_data['year']
            engine_type = form.cleaned_data['engine_type']
            make = form.cleaned_data['make']
            model = form.cleaned_data['model']
            engine_displacement = form.cleaned_data['engine_displacement']
            engine_power_kw = form.cleaned_data['engine_power_kw']
            car = Car(year=year, engine_type=engine_type, make=make, model=model,
                      engine_displacement=engine_displacement, engine_power_kw=engine_power_kw,
                      customer=appointment.customer)
            car.save()

            # Update the appointment object with the car object and change status to registered
            appointment.car = car
            appointment.status = 'registered'
            appointment.save()

            # Clear the appointment ID from the session and redirect to success page
            del request.session['appointment_id']
            return redirect('appointment_success')
    else:
        form = AppointmentStepTwoForm()

    return render(request, 'appointment/make_appointment_step_two.html', {'form': form})


def appointment_success(request):
    return render(request, 'appointment/appointment_success.html')