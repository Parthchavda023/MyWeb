from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields = '__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields = ['id', 'firstname', 'lastname', 'username', 'password', 'city', 'state', 'mobile']

class notesForm(forms.ModelForm):
    class Meta:
        model = notesModel
        fields = '__all__'

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedbackModel
        fields = '__all__'
