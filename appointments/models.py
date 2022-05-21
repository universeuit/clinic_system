from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from multiselectfield import MultiSelectField

# Create your models here.

class Depertment(models.Model):
    depertment_name = models.CharField(max_length = 500, blank=True, null=True)
    activate_status = models.BooleanField(default=True)

    def __str__(self):
        return self.depertment_name
	
class Doctorprofile(models.Model):
    doctor_name = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 100)
    avg_duration_min = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    avg_load_per_day = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    GENDER = (
        ('Male','Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    marriage_status = models.BooleanField()
    date_of_birth = models.DateField()
    connection_depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE, null=True, related_name='depertment')
    join_date = models.DateField()
    active_status = models.BooleanField()
    
    # x = Doctorprofile.objects.get(id=1)
    # x.connection_depertment.depertment_name

    BLOOD_GROUP=(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP)
    RELIGION = (
        ('Muslim', 'Muslim'),
        ('Christian', 'Christian'),
        ('Hindu', 'Hindu'),
        ('Buddhism', 'Buddhism'),
        ('Other', 'Other'),
    )
    religion = models.CharField(max_length = 100, choices=RELIGION)
    WEEKLY = (
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
    )
    weekly = MultiSelectField(max_length=100, max_choices=7, choices=WEEKLY)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.doctor_name