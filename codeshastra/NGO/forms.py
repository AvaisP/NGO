from django import forms
from django.contrib.auth.models import User
from .models import Volunteer, School, Student, Event, VolunteerAdmin

class SchoolForm(forms.ModelForm):
	name = forms.CharField(label='School:', max_length=150)
	district = forms.CharField(label='District', max_length=150)

	class Meta:
		model = School
		fields = ('name', 'district')


class StudentForm(forms.ModelForm):
	name = forms.CharField(label = 'Name:', max_length = 150)
	age = forms.IntegerField(label = 'Age:')
	school = forms.ModelChoiceField(label = 'School:', queryset = School.objects.all())
	location = forms.IntegerField(label = 'Location:')

	class Meta:
		model = Student
		fields = ('name', 'age', 'school', 'location',)

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.",widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	email = forms.CharField(help_text="Please enter your email.", widget=forms.TextInput(attrs={'placeholder': 'Email adress'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), help_text="Please enter a password.")
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class VolunteerForm(forms.ModelForm):
	mobile = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': '10-digit Mobile Number'}))
	class Meta:
		model = Volunteer
		fields = ['mobile']


class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'registeredBy', 'description')
