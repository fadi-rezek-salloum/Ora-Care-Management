from django.db import models
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    reservation_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    reservation_time = models.TimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def get_reservation_year(self):
        return str(self.reservation_date).split('-')[0]
    
    def get_reservation_month(self):
        return str(self.reservation_date).split('-')[1]

    def get_reservation_day(self):
        return str(self.reservation_date).split('-')[2]

    class Meta:
        ordering = ['reservation_date', 'reservation_time']

    def __str__(self):
        return f'{self.patient.name}'
    