from django.contrib import admin
from doctordetails.models import *
# Register your models here.

admin.site.register(District)
admin.site.register(Country)
admin.site.register(Depertment)
admin.site.register(Jobtitle)

admin.site.register(Specialization)
admin.site.register(Representative)
admin.site.register(Company)

admin.site.register(Doctorprofile)