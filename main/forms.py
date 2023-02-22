from cProfile import label
from django import forms

from .models import Appointment

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)

class CreateAppointment(forms.ModelForm):
    name = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=30, required=False)
    gender = forms.ChoiceField(choices=GENDER)

    class Meta:
        model = Appointment
        fields = ('name', 'phone', 'gender', 'reservation_date', 'reservation_time',)
