from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime

from patients.models import Patient

from .forms import CreateAppointment
from main.models import Appointment

@login_required
def home(request, year = None, month = None, day = None):
    if year is None:
        today = datetime.now()
        return redirect(f'/{today.year}/{today.month}/{today.day}/')
    
    else:
        form = CreateAppointment()
        reservation_date = date(year, month, day)
        appointments = Appointment.objects.filter(reservation_date=reservation_date)

        if request.method == 'POST':
            form = CreateAppointment(request.POST)
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')

            reservation_date = request.POST.get('reservation_date')
            reservation_time = request.POST.get('reservation_time')

            if form.is_valid():
                instance = Patient.objects.get_or_create(name=name)[0]

                instance.phone = phone

                instance.gender = gender

                instance.save()

                appointment = form.save(commit=False)

                appointment.patient = instance
                appointment.reservation_date = reservation_date
                appointment.reservation_time = reservation_time

                appointment.save()

                return redirect('/')

    context = {
        'appointments': appointments,
        'year': year,
        'month': month,
        'day': day,

        'form': form,
    }

    return render(request, 'main/home.html', context)

@login_required
def updateAppointment(request, year, month, day, id):
    appointment = get_object_or_404(Appointment, id=id)
    patient = appointment.patient

    form = CreateAppointment(instance=appointment)

    if request.method == 'POST':
            form = CreateAppointment(request.POST, instance=appointment)
            
            name = request.POST.get('name')
            phone = request.POST.get('phone')

            reservation_date = request.POST.get('reservation_date')
            reservation_time = request.POST.get('reservation_time')

            if form.is_valid():
                instance = Patient.objects.get(name=name)

                appointment = form.save(commit=False)

                patient.phone = phone

                patient.save()

                appointment.patient = instance

                appointment.reservation_date = reservation_date
                appointment.reservation_time = reservation_time

                appointment.save()

                return redirect(f'/{year}/{month}/{day}/')

    context = {
        'year': year,
        'month': month,
        'day': day,
        'form': form,
        'patient': patient,
        'update': True,
    }

    return render(request, 'main/home.html', context)

@login_required
def deleteAppointment(request, year, month, day, id):
    appointment = get_object_or_404(Appointment, id=id)

    appointment.delete()

    return redirect(f'/{year}/{month}/{day}/')

@login_required
def delete_patient(request, pk):
    patient = Patient.objects.get(pk=pk)

    patient.delete()

    return redirect('/')