from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('treatments/', treatment, name='treatments'),
    path('treatments/<slug>/', treatmentDetails, name='treatments-details'),
    path('membership_plans/<slug>/', MembershipPlansDetails, name='membershipplans-details'),

]
