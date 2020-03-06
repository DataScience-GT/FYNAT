from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from dashboard.forms import HomeForm
from dashboard.models import Post
from django.contrib.auth.models import User

# Create your views here.



class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

    def get(self, request): #Handling get requests
        form = HomeForm() #empty constructor renders blank form
        posts = Post.objects.all() #get all post objects in the database, query database
        users = User.objects.all()
        return render(request, self.template_name, {'form': form, 'users':users})
    def post(self, request):
        form = HomeForm(request.POST) #fills out form that was received with post request
        if form.is_valid():
            post = form.save(commit=False) #save data that was passed in to Post object, form has been associated with model.
            #In the meta class it specifies the model = Post so that's how Django knows to store post data in the post model
            post.user = request.user #needs association bc declared this to be a mandatory field by default
            post.save()

            text = form.cleaned_data['class1'] #extra security measure provided by Django to prevent malicious attack
            text2 = form.cleaned_data['class2']
            text3 = form.cleaned_data['class3']
            form = HomeForm() #after post request you have a new blank form
            #return redirect('profile: profile')
        args = {'form': form, 'text': text, 'text2': text2, 'text3': text3}
        return render(request, self.template_name, args)