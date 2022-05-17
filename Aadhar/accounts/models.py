from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
from django.conf import settings
# Create your models here.




class Address(models.Model):
    # aadhar1=models.ForeignKey()
    street = models.CharField(max_length=225,default='')
    city = models.CharField(max_length=225,default='')
    state = models.CharField(max_length=225,default='')
    postal_code = models.CharField(max_length=225,default='')

class Qualification(models.Model):
    clg_name=models.CharField(max_length=225,default='')
    passing_yr=models.CharField(max_length=225,default='')
    percentage=models.IntegerField(max_length=3)

class Bank(models.Model):
    Acct_num=models.CharField(max_length=225,default='')
    Bank_name=models.CharField(max_length=225,default='')
    IFSC_code=models.CharField(max_length=225,default='')

class PersonalDetails(models.Model):
    name=models.CharField(max_length=225,default='')
    dob=models.DateField()
    blood_grp=models.CharField(max_length=5,default='')
    contact_num=models.CharField(max_length=225,default='')
    email=models.EmailField()

class PastJobExp(models.Model):
    comp_name=models.CharField(max_length=225,default='')
    job_role=models.CharField(max_length=225,default='')
    experience=models.CharField(max_length=225,default='')

class Aadhar(models.Model):
    aadhar_num=models.CharField(primary_key=True,max_length=50)
    Is_active=models.BooleanField(default=True)
    address=models.ManyToManyField(Address)
    qualification=models.ForeignKey(Qualification,on_delete=models.CASCADE)
    bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
    prsnl_details=models.ForeignKey(PersonalDetails,on_delete=models.CASCADE)
    past_job_exp=models.ForeignKey(PastJobExp,on_delete=models.CASCADE)


