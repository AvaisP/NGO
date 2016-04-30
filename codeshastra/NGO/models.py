from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.

class Volunteer(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User, related_name="profile");
	# The additional attributes we wish to include.
	#website = models.URLField(blank=True);
	mobile = models.IntegerField(blank = False, null = False);
	date = models.DateField(blank=True, null=True);
	# Override the __unicode__() method to return out something meaningful!
	def __str__(self):
		return self.user.username

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'username', 'email', 'password');


class School(models.Model):
	name = models.CharField(max_length = 150)
	district = models.CharField(max_length = 150)

	def __str__(self):
		return self.name


class Student(models.Model):
	name = models.CharField(max_length = 150)
	description = models.TextField(blank = True)
	age = models.IntegerField(default = 0)
	school = models.ForeignKey(School)
	location = models.IntegerField(default = 400010)
	days_present = models.IntegerField(default = 0)
	days_total = models.IntegerField(default = 0)
	average = models.IntegerField(default = 0)
	marks = models.TextField(blank = True)
	sponsored = models.BooleanField(default = False)
	sponsoredBy = models.CharField(max_length = 150, blank = True, null = True)

	def __str__(self):
		return self.name 

class Event(models.Model):
	name = models.CharField(max_length = 150)
	registeredBy = models.TextField(blank = True)
	description = models.TextField(blank = True)

	def __str__(self):
		return self.name
