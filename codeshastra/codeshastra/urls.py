"""codeshastra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from NGO import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.testview),
    url(r'^allschools/$', views.allSchools, name = 'allSchools'), 
    url(r'^98761234([A-z]+)/$', views.studentsOfSchool, name = 'studentsOfSchool'),
    url(r'^incrementdayspresent/(\d+)/98761234([A-z]+)/$', views.incrementDaysPresent),
    url(r'^incrementtotaldays/(\d+)/98761234([A-z]+)/$', views.incrementTotalDays),
    url(r'^addnewschool/$', views.addNewSchool, name = "addnewschool"),
    url(r'^addnewstudent/$', views.addNewStudent, name = "addnewstudent"),
    url(r'^searchstudent/$', views.searchStudent, name = "searchStudent"),
    url(r'^searchSchool/$', views.searchSchool, name = "searchSchool"),
    url(r'^average(\d+)/$', views.marksheet, name = "marksheet"),
    url(r'^addmarks/(\d+)/$', views.addMarks, name = "addMarks"),
    url(r'^98761234[A-z]+/(\d+)/$', views.StudentProfile, name ="Profile"),
    url(r'^98761234([A-z]+)/(\d+)/sponsor/$', views.confirmSponsor, name = "ConfirmSponsor"),
    url(r'^98761234([A-z]+)/(\d+)/sponsor/confirmedPaymentKey/$', views.sponsorChild, name = "sponsorChild"),
    url(r'^addnewevent/$', views.addEvent, name = "addEvent"),
    url(r'^allevents/$', views.allEvents, name = "allEvents"),
    url(r'^searchEvent/$', views.searchEvent, name = "searchEvent"),
    url(r'^12349876(\d+)/$', views.eventDesc, name = "eventDesc"),
    url(r'^signupforevent(\d+)/$', views.signUpEvent, name = "signUpEvent"),
    url(r'^(\d+)registerations/$', views.eventRegisterations, name = "eventRegisterations"),
     
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.logmein, name='login'),
    url(r'^logout/', views.user_logout, name='user_logout'),
    url(r'^sponsor/', views.sponsor, name='sponsor'),
    url(r'^sponsor_3/', views.sponsor_3, name='sponsor_3'),
    url(r'^success/', views.success, name='success'),
    
]
