from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
classes_info = [
    {
        'Name': "Akshay Iyer",
        "Year": "Sophomore",
        "Classes": "CS 2110, CS 3600, MUS 3161, MATH 3012, INTA 2050"
    },
    {
        "Name": "Sally Bird",
        "Year": "Sophomore",
        "Classes": "CS 1332, BIO 1220, MATH 3215, BME 2000"
    }
]

def home(request): #logic for handling what happens when user goes to the home page
    context = {
        "classes_info": classes_info #dictionary with key of "classes_info, containing values of the list of dictionaries that was made above"
    }
    # we can have access to this in the home template
    return render(request, 'dashboard/home.html', context)

def about(request):
    return render(request, 'dashboard/about.html')