from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('first_name', 'last_name','email', 'biography')
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}
        widgets = {
            'biography': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('school', 'major', 'activities', 'start_year', 'end_year')
        labels = {'start_year': 'Start Year', 'end_year': 'End Year'}
        widgets = {
            'activities': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('company', 'position', 'description', 'start_year', 'end_year')
        labels = {'start_year': 'Start Year', 'end_year': 'End Year'}
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ('name','year', 'description')
        labels = {'year': 'Year Received'}
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }
