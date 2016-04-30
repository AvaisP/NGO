from django.contrib import admin
from .models import Volunteer, School, Student, Event

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Event)