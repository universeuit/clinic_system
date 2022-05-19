from django.urls import path
from .views import *

# app_name = 'appoinment'

urlpatterns = [
    path('', appointment, name='appointment'),
]