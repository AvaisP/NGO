from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import SchoolForm, StudentForm, VolunteerForm, EventForm, UserForm 
from django.http import HttpResponseRedirect, HttpResponse
from .models import School, Student, Volunteer, Event, VolunteerAdmin
from django.utils import timezone

# Create your views here.
# SchoolForm, StudentForm like PostForm in Blog Done.
# Update :
# Create an All Schools page like all books ib ELib. Done
# Use dynamic URLs to display all students of the school. Layout same as allbooks.Done
# Create functions to increment days present, total days, view sponsor(T or F)Done and update marks Done
# Optional : Add sponsored by in the Student Model Done
# Have an add new school / student in their respective pages.Done
# Have a search button.Done

def testview(request):
	return render(request, 'index.html')

def allSchools(request):
	schools = School.objects.all()
	return render(request, 'allSchool.html', {'schools' : schools})

def studentsOfSchool(request, school):
	schoolObject = School.objects.get(name = school)
	students = Student.objects.filter(school = schoolObject)
	computeAverage()
	return render(request, 'allStudents.html', {'students': students})

def incrementDaysPresent(request, studentID, school):
	student = Student.objects.get(id = studentID)
	student.days_present += 1
	student.save()
	url = "/98761234" + school +"/"
	return HttpResponseRedirect(url)

def incrementTotalDays(request, studentID, school):
	student = Student.objects.get(id = studentID)
	student.days_total += 1
	student.save()
	url = "/98761234" + school +"/"
	return HttpResponseRedirect(url)

# MARKS	
def marksheet(request, studentID):
	student = Student.objects.get(id = studentID)
	marksheet = student.marks.split(",")
	subject = []
	marksInSubject = []
	marksheetDict = {}
	if marksheet[0]:
		for marks in marksheet :
			mark = marks.split(":")
			subject.append(mark[0])
			marksInSubject.append(int(mark[1]))
		marksheetDict = dict(zip(subject, marksInSubject))	
	return render(request, "marksheet.html", {'marksheetDict': marksheetDict, 'student' : student})

def addMarks(request, studentID):
	if request.user.is_superuser:
		student = Student.objects.get(id = studentID)
		if request.method == 'POST':
			ExamName = request.POST.get("ExamName")
			Marks = request.POST.get("Marks")
			student.marks += "," + ExamName + ":" + Marks 
			student.save() 
			url = "/average" + studentID + "/"	
			return HttpResponseRedirect(url)
		else:
			return render(request, 'newmarks.html',)

def computeAverage():
	students = Student.objects.all()
	for student in students :
		marksheet = student.marks.split(",")
		marksInSubject = []
		average = 0
		for marks in marksheet :
			if marks :
				mark = marks.split(":")
				marksInSubject.append(int(mark[1]))
				average += int(mark[1])
		if len(marksInSubject) > 0 :		
			average /= len(marksInSubject)	
			student.average = average	
			student.save()


def addNewSchool(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = SchoolForm(data = request.POST)
			if form.is_valid():
				school = form.save(commit = False)
				school.save()
				return redirect("/allschools/")
		else : 
			form = SchoolForm()
			return render(request, 'newschool.html', {'form':form})            
	else:
		return HttpResponse("You dont have permission to view this page.")

def addNewStudent(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = StudentForm(data = request.POST)
			if form.is_valid():
				student = form.save(commit = False)
				student.save()
				return studentsOfSchool(request, student.school.name)
		else : 
			form = StudentForm()
			return render(request, 'newstudent.html', {'form':form})            
	else:
		return HttpResponse("You dont have permission to view this page.")

def searchStudent(request):
	if request.method == 'POST':
		keyword = request.POST['keyword']
		result = Student.objects.filter(name__icontains = keyword)
		return render(request, 'searchresultstudent.html', {'result' : result},) 
	else:
		return render(request, 'searchform.html')

def searchSchool(request):
	if request.method == 'POST':
		keyword = request.POST['keyword']
		result = School.objects.filter(name__icontains = keyword)
		return render(request, 'searchresultschool.html', {'result' : result},) 
	else:
		return render(request, 'searchform.html')	

def searchEvent(request):
	if request.method == 'POST':
		keyword = request.POST['keyword']
		result = Event.objects.filter(name__icontains = keyword)
		return render(request, 'searchresultevent.html', {'result' : result},) 
	else:
		return render(request, 'searchform.html')

@login_required(login_url = '/login/')
def addEvent(request) :
	if request.user.is_superuser:
		if request.method == "POST":
			form = EventForm(data = request.POST)
			if form.is_valid():
				event = form.save(commit = False)
				event.save()
				return HttpResponseRedirect('/allevents/')
		else : 
			form = EventForm()
			return render(request, 'newevent.html', {'form':form})            
	else:
		return HttpResponse("You dont have permission to view this page.")

def eventRegisterations(request, eventID):
	if request.user.is_superuser:
		event = Event.objects.get(id = eventID)
		registerations = event.registeredBy.split(",")
		return render(request, "allregisterations.html", {"registerations" : registerations})
	else:
		return HttpResponseRedirect("Access Denied")


def allEvents(request):
	events = Event.objects.all()
	return render(request, 'allEvents.html', {'events' : events})

def eventDesc(request, eventID):
	event = Event.objects.get(id = eventID)
	return render(request, 'eventdescription.html', {'event' : event})

@login_required(login_url = '/login/')
def signUpEvent(request, eventID):
	event = Event.objects.get(id = eventID)
	event.registeredBy += "," + request.user.username
	event.save()
	return HttpResponse("Successfully signed up")

@login_required(login_url = '/login/')
def StudentProfile(request, studentID):
	student = Student.objects.get(id = studentID)
	return render(request, 'profile.html', {'student' : student})

@login_required(login_url = '/login/')
def confirmSponsor(request, school, studentID):
	url = "/98761234" + school + "/" + studentID + "/sponsor/confirmedPaymentKey/" 
	return render(request, 'confirm.html', {"url" : url})

@login_required(login_url = '/login/')
def sponsorChild(request, school, studentID):
	student = Student.objects.get(id = studentID)
	student.sponsoredBy = request.user.username
	student.sponsored = True
	student.save()
	url = "/98761234" + school + "/" + studentID + "/"
	return HttpResponseRedirect(url)



def sponsor_3(request):
#	return HttpResponse("Home Page");
	context = RequestContext(request);
	context_dict = {'message' : "We are really awesome"};
	return render(request, 'sponsor_3.html', context_dict);

def success(request):
#	return HttpResponse("Home Page");
	context = RequestContext(request);
	context_dict = {'message' : "We are really awesome"};
	return render(request, 'success.html', context_dict);


def sponsor(request):
	context = RequestContext(request);
	context_dict = {'message':"Sponsor a child today!"};
	return render(request, 'sponsor.html', context_dict);	

def register(request, reason=""):
	message = "";
	if reason != "":
		message = "Incorrect Attempt";
	# Like before, get the request's context.
	context = RequestContext(request)
	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False
	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and VolunteerForm.
		user_form = UserForm(data=request.POST)
		profile_form = VolunteerForm(data=request.POST)
		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save();
			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password);
			user.save();
			# Now sort out the Volunteer instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False);
			profile.user = user;
			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and put it in the Volunteer model.
			#if 'picture' in request.FILES:
			#profile.picture = request.FILES['picture']
			# Now we save the Volunteer model instance.
			profile.save()
			# Update our variable to tell the template registration was successful.
			registered = True
			return render_to_response(
				'register.html',
				{'user_form': user_form, 'profile_form': profile_form, 'registered': registered,},
				context)
		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print(user_form.errors, profile_form.errors);
			# Not a HTTP POST, so we render our form using two ModelForm instances.
			# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = VolunteerForm()
		# Render the template depending on the context.
	return render_to_response(
	'register.html',
	{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
	context)

def logmein(request):
	registered = ""
	# Like before, obtain the context for the user's request.
	context = RequestContext(request)
	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = "Admin"
		password = "test123"
		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)
		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user is not None:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your user account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render(request, 'logmein.html',)

from django.contrib.auth import logout
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)
	# Take the user back to the homepage.
	return HttpResponseRedirect('/')