from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentProfileForm
from django.contrib import messages
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
            fav_class = form.cleaned_data['fav_class']
            fav_hobby = form.cleaned_data['fav_hobby']
            fun_fact = form.cleaned_data['fun_fact']
            messages.success(request, f'Cool! Your favorite class is {fav_class} and your favorite hobby is {fav_hobby}.\n Your fun fact is very cool! - "{fun_fact}"')
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
