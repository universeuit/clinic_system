from audioop import reverse
from distutils.command import upload
from email.mime import image
from turtle import title
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ImageField
from django.urls import reverse
# Create your models here.


# Treatment start

class Treatment(models.Model):
    title = models.CharField(max_length=50)
    slug  = models.SlugField(blank=True) 
    short_Description  = RichTextUploadingField()
    long_description = RichTextUploadingField()
    image = models.ImageField(upload_to='Treatmentimage')
    icon_image  = models.ImageField()

    def __str__(self):
        return self.title

class TreatmentImageGallery(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    after_image = models.ImageField(upload_to='TreatmentImageGallery')
    before_image = models.ImageField(upload_to='TreatmentImageGallery')
    
    def __str__(self):
        return self.treatment.title + '//' + self.title

# Treatment end

# MembershipPlan start

class MembershipPlan(models.Model):
    title = models.CharField(max_length = 150)
    slug  = models.SlugField(blank=True)
    image = models.ImageField(upload_to='MembershipImg')
    
    def __str__(self):
        return self.title


class MembershipBannerImage(models.Model):
    membership_plans  = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='MembershipImg')

    def __str__(self):
        return self.membership_plans.title

class MembershipDescription(models.Model):
    membership_plans  = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    description = RichTextUploadingField()


# MembershipPlan end
    

# PATIENT SAFETY start

class PatientSafety(models.Model):
    title = models.CharField(max_length = 150)
    slug  = models.SlugField(blank=True)
    image = models.ImageField(upload_to='PatientSafety')
    short_description  = models.TextField()
    long_description = RichTextUploadingField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PatientSafety'
        verbose_name_plural = 'PatientSafeties'

