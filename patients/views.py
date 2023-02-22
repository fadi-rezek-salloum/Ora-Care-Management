from django.shortcuts import redirect, render
from django.db.models import Q, Sum, F
from django.contrib.auth.decorators import login_required

from .forms import PatientProfile
from .models import Patient

from main.models import Appointment

@login_required
def maleList(request):
    patients = Patient.objects.filter(gender='male')

    context = {
        'patients': patients,
    }

    return render(request, 'patients/patients_list.html', context)

@login_required
def femaleList(request):
    patients = Patient.objects.filter(gender='female')

    context = {
        'patients': patients,
    }

    return render(request, 'patients/patients_list.html', context)

@login_required
def search(request):
    if request.GET.get('q'):
        patients = Patient.objects.filter(Q(name__icontains=request.GET.get('q')))
    
    else:
        patients = Patient.objects.all()

    context = {
        'patients': patients,
    }

    return render(request, 'patients/patients_list.html', context)

@login_required
def accounting(request):
    patients = Patient.objects.all().annotate(total_debt = F('bill') - F('payed')).order_by('total_debt')

    cash = Patient.objects.all().aggregate(cash=Sum('bill')-Sum('payed'))

    context = {
        'patients': patients,
        'cash': cash
    }

    return render(request, 'patients/accounting.html', context)

@login_required
def profile(request, id):
    patient = Patient.objects.get(id=id)
    appointments = Appointment.objects.filter(patient=patient)

    form = PatientProfile(instance=patient)

    if request.method == 'POST':
        form = PatientProfile(request.POST, instance=patient)

        if form.is_valid():
            form.save()

            return redirect(f'/patients/profile/{patient.id}/')

    context = {
        'patient': patient,
        'form': form,
        'appointments': appointments,
    }

    return render(request, 'patients/profile.html', context)