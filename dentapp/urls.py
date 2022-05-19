from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('treatments/', treatment, name='treatments'),
    # path('appointment/', appointment, name='appointment'),
    path('treatments/<slug>/', treatmentDetails, name='treatments-details'),
    path('membership_plans/<slug>/', MembershipPlansDetails, name='membershipplans-details'),
    path('patientsafety/<slug>/', PatientSafetyDetails, name='patientsafety-details'),

]
