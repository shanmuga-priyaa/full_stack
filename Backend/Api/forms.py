from django import forms
from .models import *
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class  UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        