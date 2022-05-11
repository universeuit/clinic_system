from urllib import request
from django.db import models
from django.contrib.auth.models import User

import uuid
import random
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# def random_id(*args):
#     random_string = str(random.randint(10000, 99999))
#     return random_string


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Depertment(models.Model):
    depertment_no = models.AutoField(primary_key=True)
    def random_depertment_id():
        random_string = str(random.randint(1000, 9999))
        return random_string
    depertment_id = models.CharField(max_length = 4, default = random_depertment_id, unique=True)
    # depertment_id = models.CharField(max_length = 4, default = random_string)
    depertment_name = models.CharField(max_length = 500, blank=True, null=True)
    activate_status = models.BooleanField(default=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

class Jobtitle(models.Model):
    jobtitle_no = models.AutoField(primary_key=True)
    def random_jobtitle_id():
        random_string = str(random.randint(10000, 99999))
        return random_string
    jobtitle_id = models.CharField(max_length = 5, default = random_jobtitle_id, unique=True)
    # Jobtitle_id = models.CharField(max_length = 4, default = random_string)
    jobtitle_name = models.CharField(max_length = 500, blank=True, null=True)
    activate_status = models.BooleanField(default=True)

class Specialization(models.Model):
    specialization_no = models.AutoField(primary_key=True)

    def random_specialization_id():
        random_string = str(random.randint(100000, 999999))
        return random_string
    
    specialization_id = models.CharField(max_length = 6, default = random_specialization_id, unique=True)
    specialization_name = models.CharField(max_length = 500, blank=True, null=True)
    activate_status = models.BooleanField(default=True)

    def __str__(self):
        return self.specialization_name

class Representative(models.Model):
    sr_no = models.AutoField(primary_key=True)
    def random_representative_id():
        random_string = str(random.randint(1000000, 9999999))
        return random_string
    sr_id = models.CharField(max_length = 7, default = random_representative_id, unique=True)
    sr_name = models.CharField(max_length = 500, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    sr_number = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
    sr_email = models.EmailField(blank=True, null=True)
    wa_number = models.CharField(max_length = 100, blank=True, null=True)
    facebook_id = models.URLField(blank=True)
    activate_status = models.BooleanField(default=True)

class Company(models.Model):
    company_no = models.AutoField(primary_key=True)
    def random_company_id():
        random_string = str(random.randint(10000000, 99999999))
        return random_string
    company_id = models.CharField(max_length = 7, default = random_company_id, unique=True)
    company_name = models.CharField(max_length = 500, blank=True, null=True)

    present_address1 = models.CharField(max_length=100, blank=True, null=True)
    present_address2 = models.CharField(max_length=100, blank=True, null=True)
    present_address_post = models.CharField(max_length=10, blank=True, null=True)
    present_address_dist=models.ForeignKey(District, on_delete=models.CASCADE, null=True, related_name='company_district')
    present_address_coun=models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name='company_country')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
    company_email = models.EmailField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    facebook_id = models.URLField(blank=True, null=True)
    wa_number = models.CharField(max_length = 100, blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    activate_status = models.BooleanField(default=True)

class Doctorprofile(models.Model):
    doctot_no = models.AutoField(primary_key=True)

    def random_id():
        random_string = str(random.randint(10000, 99999))
        return random_string
    
    doctot_id = models.CharField(max_length = 5, default=random_id, unique=True)
    
    # doctot_id = models.UUIDField(default=uuid.uuid4, editable=True)
    # doctot_id = models.CharField(max_length = 5, default=random_string, unique=True)
    salutation_name = models.CharField(max_length = 10, blank=True, null=True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    father_name = models.CharField(max_length = 100, blank=True, null=True)
    mother_name = models.CharField(max_length = 100)
    husband_name = models.CharField(max_length = 100, blank=True, null=True)
    GENDER = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    marriage_status = models.BooleanField()
    date_of_birth = models.DateField()
    depertment_name = models.ForeignKey(Depertment, on_delete=models.CASCADE, null=True, related_name='depertment')
    join_date = models.DateField()
    jobtitle_no = models.ForeignKey(Jobtitle, on_delete=models.CASCADE, null=True, related_name='jobtitle')
    active_status = models.BooleanField()

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
    phone_home = models.CharField(max_length = 100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
    phone_office = models.CharField(max_length = 100)
    NATIONALITY=(
        ('Bangladeshi', 'Bangladeshi'),
        ('Indian', 'Indian'),
        ('Other', 'Other'),
    )
    nationality = models.CharField(max_length=30, choices=NATIONALITY)
    present_address1 = models.CharField(max_length=100, blank=True, null=True)
    present_address2 = models.CharField(max_length=100, blank=True, null=True)
    present_address3 = models.CharField(max_length=100, blank=True, null=True)
    present_address_post = models.CharField(max_length=10, blank=True, null=True)
    present_address_dist=models.ForeignKey(District, on_delete=models.CASCADE, null=True, related_name='district')
    present_address_coun=models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name='country')
    present_careof_address=models.CharField(max_length=100, blank=True, null=True)

    permanent_address1 = models.CharField(max_length=100, blank=True, null=True)
    permanent_address2 = models.CharField(max_length=100, blank=True, null=True)
    permanent_address3 = models.CharField(max_length=100, blank=True, null=True)
    permanent_address_post = models.CharField(max_length=10, blank=True, null=True)
    permanent_address_dist=models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    permanent_address_coun=models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    permanent_careof_address=models.CharField(max_length=100, blank=True, null=True)
    referal_flag = models.BooleanField(default=False)
    int_ext_flag = models.BooleanField(default=False)
    avg_duration_min = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    avg_load_per_day = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    block_load = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)], blank=True, null=True)
    specialization_no = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True)
    room_no = models.PositiveSmallIntegerField()
    offday_remarks = models.TextField(max_length=500, blank=True, null=True)
    doctor_signature = models.CharField(max_length=250, blank=True, null=True)
    salesrep_no = models.ForeignKey(Representative, on_delete=models.CASCADE, null=True)
    chamber_address1 = models.CharField(max_length=500, blank=True, null=True)
    chamber_address2 = models.CharField(max_length=500, blank=True, null=True)
    degree1 =  models.CharField(max_length=100)
    remarks = models.TextField(max_length=500, blank=True, null=True)
    email_personal = models.EmailField(blank=True, null=True)
    email_official = models.EmailField(blank=True, null=True)
    tin_no = models.BigIntegerField(blank=True, null=True)
    card_no = models.BigIntegerField()
    ss_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_name')
    # ss_creator = models.CharField(max_length=100)
    ss_created_no = models.DateTimeField(auto_now_add=True)
    ss_created_session = models.CharField(max_length=100, blank=True, null=True)
    ss_modifier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modifier_name')
    # ss_modifier = models.CharField(max_length=100)
    ss_modified_on = models.DateTimeField(auto_now=True)
    ss_modified_session = models.CharField(max_length=100)
    
    # company_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
    company_no = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    doctor_name = models.CharField(max_length=100)
    disc_allowed = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True)
    due_allowed = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(2000)],blank=True, null=True)
    doc_com_flag = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)],blank=True, null=True)
    doc_com_pct = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)],blank=True, null=True)
    doctor_photo = models.ImageField(upload_to = 'doctor_images', verbose_name='Doctor Photo',blank=True, null=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"











# from django.db import models

# from django.core.validators import MaxValueValidator, MinValueValidator

# import random
# from django.core.validators import RegexValidator


# # Create your models here.
# random_string = str(random.randint(10000, 99999))
# random_string_specialization = str(random.randint(3000, 9999))
# random_string_company = str(random.randint(4000, 9999))


# class District(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Country(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Depertment(models.Model):
#     depertment_no = models.AutoField(primary_key=True)
#     depertment_id = models.CharField(max_length = 4, default = random_string)
#     depertment_name = models.CharField(max_length = 500, blank=True, null=True)
#     activate_status = models.BooleanField(default=True)
#     parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

# class Jobtitle(models.Model):
#     Jobtitle_no = models.AutoField(primary_key=True)
#     Jobtitle_id = models.CharField(max_length = 4, default = random_string)
#     Jobtitle_name = models.CharField(max_length = 500, blank=True, null=True)
#     activate_status = models.BooleanField(default=True)

# class Specialization(models.Model):
#     specialization_no = models.AutoField(primary_key=True)
#     specialization_id = models.CharField(max_length = 4, default = random_string_specialization)
#     specialization_name = models.CharField(max_length = 500, blank=True, null=True)
#     activate_status = models.BooleanField(default=True)

# class Representative(models.Model):
#     sr_no = models.AutoField(primary_key=True)
#     sr_id = models.CharField(max_length = 4, default = random_string_specialization)
#     sr_name = models.CharField(max_length = 500, blank=True, null=True)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
#     sr_number = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
#     sr_email = models.EmailField(blank=True, null=True)
#     wa_number = models.CharField(max_length = 100)
#     facebook_id = models.URLField(blank=True)
#     activate_status = models.BooleanField(default=True)

# class Company(models.Model):
#     company_no = models.AutoField(primary_key=True)
#     company_id = models.CharField(max_length = 4, default = random_string_company)
#     company_name = models.CharField(max_length = 500, blank=True, null=True)

#     present_address1 = models.CharField(max_length=100, blank=True, null=True)
#     present_address2 = models.CharField(max_length=100, blank=True, null=True)
#     present_address_post = models.CharField(max_length=10, blank=True, null=True)
#     present_address_dist=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='district')
#     present_address_coun=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='country')

#     phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
#     company_email = models.EmailField(blank=True, null=True)
#     company_website = models.URLField(blank=True, null=True)
#     facebook_id = models.URLField(blank=True, null=True)
#     wa_number = models.CharField(max_length = 100, blank=True, null=True)
#     youtube_url = models.URLField(blank=True, null=True)
#     activate_status = models.BooleanField(default=True)


# class Doctorprofile(models.Model):
#     doctot_no = models.AutoField(primary_key=True)
#     doctot_id = models.CharField(max_length = 5, default = random_string, unique=True)
#     salutation_name = models.CharField(max_length = 10, blank=True, null=True)
#     f_name = models.CharField(max_length = 100)
#     l_name = models.CharField(max_length = 100)
#     father_name = models.CharField(max_length = 100, blank=True, null=True)
#     mother_name = models.CharField(max_length = 100)
#     husband_name = models.CharField(max_length = 100, blank=True, null=True)
#     GENDER = (
#         ('Male','Male'),
#         ('Female', 'Female'),
#     )
#     gender = models.CharField(max_length=100, choices=GENDER)
#     marriage_status = models.BooleanField()
#     date_of_birth = models.DateField()
#     # depertment_name = 
#     join_date = models.DateField()
#     # jobtitle_no = 
#     active_status = models.BooleanField()

#     BLOOD_GROUP=(
#         ('A+', 'A+'),
#         ('A-', 'A-'),
#         ('AB+', 'AB+'),
#         ('AB-', 'AB-'),
#         ('B+', 'B+'),
#         ('B-', 'B-'),
#         ('O+', 'O+'),
#         ('O-', 'O-'),
#     )
#     blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP)
#     religion = models.CharField(max_length = 100)
#     phone_home = models.CharField(max_length = 100)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
#     phone_office = models.CharField(max_length = 100)
#     NATIONALITY=(
#         ('Bangladeshi', 'Bangladeshi'),
#         ('Indian', 'Indian'),
#         ('Other', 'Other'),
#     )
#     nationality = models.CharField(max_length=30, choices=NATIONALITY)
#     present_address1 = models.CharField(max_length=100, blank=True, null=True)
#     present_address2 = models.CharField(max_length=100, blank=True, null=True)
#     present_address3 = models.CharField(max_length=100, blank=True, null=True)
#     present_address_post = models.CharField(max_length=10, blank=True, null=True)
#     present_address_dist=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='district')
#     present_address_coun=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='country')
#     present_careof_address=models.CharField(max_length=100, blank=True, null=True)

#     permanent_address1 = models.CharField(max_length=100, blank=True, null=True)
#     permanent_address2 = models.CharField(max_length=100, blank=True, null=True)
#     permanent_address3 = models.CharField(max_length=100, blank=True, null=True)
#     permanent_address_post = models.CharField(max_length=10, blank=True, null=True)
#     permanent_address_dist=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='district')
#     permanent_address_coun=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='country')
#     permanent_careof_address=models.CharField(max_length=100, blank=True, null=True)
#     referal_flag = models.BooleanField(default=False)
#     int_ext_flag = models.BooleanField(default=False)
#     avg_duration_min = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
#     avg_load_per_day = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
#     block_load = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True)
#     # specialization_no = 
#     room_no = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
#     offday_remarks = models.TextField(max_length=250, blank=True, null=True)
#     doctor_signature = models.CharField(max_length=250, blank=True, null=True)
#     # SALESREP_NO
#     chamber_address1 = models.CharField(max_length=500, blank=True, null=True)
#     chamber_address2 = models.CharField(max_length=500, blank=True, null=True)
#     degree1 =  models.CharField(max_length=100)
#     remarks = models.TextField(max_length=500, blank=True, null=True)
#     email_personal = models.EmailField(blank=True, null=True)
#     email_official = models.EmailField(blank=True, null=True)
#     tin_no = models.IntegerField()
#     card_no = models.IntegerField()
#     ss_creator = models.CharField(max_length=100)
#     ss_created_no = models.DateTimeField(auto_now_add=True)
#     ss_created_session = models.CharField(max_length=100)
#     ss_modifier = models.CharField(max_length=100)
#     ss_modified_on = models.DateTimeField(auto_now=True)
#     ss_modified_session = models.CharField(max_length=100)
#     # company_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
#     doctor_name = models.CharField(max_length=100)
#     disc_allowed = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
#     due_allowed = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
#     doc_com_flag = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
#     doc_com_pct = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
#     doctor_photo = models.ImageField(upload_to = 'doctor_images', verbose_name='Doctor Photo')