from time import timezone
from django.shortcuts import render
from .models import *
from django.utils import timezone
from appointments.models import *
# Create your views here.
def index(request):
    doctor_profile = Doctorprofile.objects.all()
    context ={
        'doctor_profile':doctor_profile,
    }
    return render(request, 'index.html', context)


def treatment(request):
    return render(request, 'treatment.html')

def treatmentDetails(request,slug):
    treatments = Treatment.objects.get(slug=slug)
    treatmentImageGallery = TreatmentImageGallery.objects.filter(treatment=treatments)

    context ={
        'treatments':treatments,
        'treatmentImageGallery':treatmentImageGallery,
    }
    return render(request, 'treatmentdetails.html',context )

def MembershipPlansDetails(request,slug):
    membership_plans = MembershipPlan.objects.get(slug=slug)
    membershipBannerImage = MembershipBannerImage.objects.filter(membership_plans=membership_plans)
    membershipDescription =MembershipDescription.objects.filter(membership_plans=membership_plans)
    
    context ={
        'membership_plans':membership_plans,
        'membershipBannerImage':membershipBannerImage,
        'membershipDescription':membershipDescription,
    }
    
    return render(request, 'membershipplansdetails.html',context )

def PatientSafetyDetails(request,slug):
    patientsafety = PatientSafety.objects.get(slug=slug)
    date = timezone.now()
    context ={
        'patientsafety':patientsafety,
        'date':date,
    }
    print(date)
    
    return render(request, 'patientsafety.html',context )