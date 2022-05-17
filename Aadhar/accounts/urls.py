from django.urls import path
from . import views
from .views import *

urlpatterns=[

    path('register',RegisterUser.as_view(), name='register'),
    path('staffregister',StaffUser.as_view(), name='staffregister'),
    path('login',views.userlogin, name='login'),
    path('listAadhar',views.listAadhar, name='listAadhar'),
    path('createAadhar',views.createAadhar, name='createAadhar'),
    path('updateAadhar/<str:pk>',views.updateAadhar, name='updateAadhar'),
    path('deleteAadhar/<str:pk>',views.deleteAadhar, name='deleteAadhar'),
    path('listaddress',views.listaddress, name='listaddress'),
    path('createaddress',views.createaddress, name='createaddress'),
    path('updateaddress/<int:pk>',views.updateaddress, name='updateaddress'),
    path('deleteaddress/<int:pk>',views.deleteaddress, name='deleteaddress'),
    path('listqualification',views.listqualification, name='listqualification'),
    path('createqualification',views.createqualification, name='createqualification'),
    path('updatequalification/<int:pk>',views.updatequalification, name='updatequalification'),
    path('deletequalification/<int:pk>',views.deletequalification, name='deletequalification'),
    path('listbank',views.listbank, name='listbank'),
    path('createbank',views.createbank, name='createbank'),
    path('updatebank/<int:pk>',views.updatebank, name='updatebank'),
    path('deletebank/<int:pk>',views.deletebank, name='deletebank'),
    path('listpersonaldetails',views.listpersonaldetails, name='listpersonaldetails'),
    path('createpersonaldetails',views.createpersonaldetails, name='createpersonaldetails'),
    path('updatepersonaldetails/<int:pk>',views.updatepersonaldetails, name='updatepersonaldetails'),
    path('deletepersonaldetails/<int:pk>',views.deletepersonaldetails, name='deletepersonaldetails'),
    path('listpastjobexp',views.listpastjobexp, name='listpastjobexp'),
    path('createpastjobexp',views.createpastjobexp, name='createpastjobexp'),
    path('updatepastjobexp/<int:pk>',views.updatepastjobexp, name='updatepastjobexp'),
    path('deletepastjobexp/<int:pk>',views.deletepastjobexp, name='deletepastjobexp'),
    path('aadharaddress/<str:pk>',views.aadharaddress, name='aadharaddress'),
    path('aadharqualification/<str:pk>',views.aadharqualification, name='aadharqualification'),
    path('aadharbank/<str:pk>',views.aadharbank, name='aadharbank'),
    path('aadharprsnldetails/<str:pk>',views.aadharprsnldetails, name='aadharprsnldetails'),
    path('aadharpastjobexp/<str:pk>',views.aadharpastjobexp, name='aadharpastjobexp'),
    path('aadhardata/<str:pk>',views.aadhardata, name='aadhardata'),
    path('aadharactive',views.aadharactive, name='aadharactive'),
    path('aadharinactive',views.aadharinactive, name='aadharinactive'),


]
