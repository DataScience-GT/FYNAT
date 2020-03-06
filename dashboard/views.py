from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentProfileForm
from django.contrib import messages
from django.contrib.auth.models import User as currUser
from .models import User
from django.db import IntegrityError
# Create your views here.
classes_info = [
    {
        'Name': "Akshay Iyer",
        "Year": "Sophomore",
        "Classes": "CS 2110, CS 3600, MUS 3131, MATH 3012, INTA 2050"
    },
    {
        "Name": "Sally Bird",
        "Year": "Sophomore",
        "Classes": "CS 1332, BIO 1220, MATH 3215, BME 2000"
    }
]

def home(request): #logic for handling what happens when user goes to the home page
    context = {
      "classes_info": classes_info
      # dictionary with key of "classes_info, containing values of the list of dictionaries that was made above"
    }
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            interested_orgs = form.cleaned_data['interested_orgs']
            major = form.cleaned_data['major']
            year = form.cleaned_data['year']
            hobbies = form.cleaned_data['hobbies']
            favorites = form.cleaned_data['favorites']
            curr_skills = form.cleaned_data['curr_skills']
            look_to_learn = form.cleaned_data['look_to_learn']
            self_descriptor = form.cleaned_data['self_descriptor']
            where_from = form.cleaned_data['where_from']
            residence_area = form.cleaned_data['residence_area']

            try:
                user = User.users.register_new_user(username=request.user.get_username(), first_name=first_name, last_name=last_name, interested_orgs=interested_orgs, major=major, year=year,
                            hobbies=hobbies, favorites=favorites, curr_skills=curr_skills, look_to_learn=look_to_learn,
                            self_descriptor=self_descriptor, where_from=where_from, residence_area=residence_area)
                user.save()
                print(request.user.get_username(), "filled out questionnaire")
                messages.success(request,
                                 f'Cool! Your first name is {user.first_name} and your last name is {user.last_name}.\n Your profile description is very cool! - "{user.self_descriptor}"')
            except IntegrityError:
                print("User has already filled questionaire and should edit data on profile directly")

    # if a GET (or any other method) we'll create a blank form
    else:
      form = StudentProfileForm()
    '''context = {
        "classes_info": classes_info #dictionary with key of "classes_info, containing values of the list of dictionaries that was made above"
    }'''
    # we can have access to this in the home template
    return render(request, '../templates/home.html', {'form': form})

def about(request):
    return render(request, 'dashboard/about.html')
