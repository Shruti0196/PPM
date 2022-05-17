# from django.forms import ModelForm, fields
# from .models import Todo,WorkDetails
# from django import forms

# class TodoForm(ModelForm):
#     class Meta:
#         model=Todo
#         fields=['Work','studiesrelated']

# class DetailsForm(ModelForm):
#     class Meta:
#         model=WorkDetails
#         fields='__all__'

# accounts/forms.py

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User

# class UserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = User
#         fields = ('username','email','password1','password2')

# class MyUserChangeForm(UserChangeForm):

#     class Meta(UserChangeForm):
#         model = MyUser
#         fields = ('username', 'mobile_number', 'birth_date')
