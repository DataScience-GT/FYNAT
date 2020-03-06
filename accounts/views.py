# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dashboard.models import User

# class SignUp(generic.CreateView):
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         messages.success(request, f'Account created for {username}!')
#         success_url = reverse_lazy('login')

#     template_name = 'signup.html'

def signup(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cool! Account created for {username}. Now you can login with your credentials')
            return redirect('') #name of the project-level homepage if you look under in the loginlogout urls.py file
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    #curr_user = User.users.filter(username=User.username)
    return render(request, 'profile.html') #, {'curr_user', curr_user})