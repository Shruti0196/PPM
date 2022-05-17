from rest_framework import serializers
from.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'password']

    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=['street', 'city', 'state', 'postal_code']

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qualification
        fields=['clg_name','passing_yr','percentage']

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields=['Acct_num','Bank_name','IFSC_code']

class personaldetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalDetails
        fields=['name','dob','blood_grp','contact_num','email']

class PastJobExpSerializer(serializers.ModelSerializer):
    class Meta:
        model=PastJobExp
        fields=['comp_name','job_role','experience']

class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aadhar
        fields=['aadhar_num','Is_active','address','qualification','bank','prsnl_details','past_job_exp']