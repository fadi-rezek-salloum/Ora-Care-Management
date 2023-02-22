import uuid
from django.db import models

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=120)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=8, choices=GENDER, null=True, blank=True)

    medicines = models.TextField(null=True, blank=True)
    diseases = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    allergy = models.TextField(blank=True, null=True)

    bill = models.IntegerField(null=True, blank=True, default=0)
    payed = models.IntegerField(null=True, blank=True, default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    