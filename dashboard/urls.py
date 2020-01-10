from django.urls import path
from . import views # the dot refers to the current directory
#import views from the dashboard and not the project level views

urlpatterns = [
    path('', views.home, name = 'dashboard-home'), #specify the homepage with empty quotes
    path('about/', views.about, name = 'dashboard-about'),
]

#call the function views.home because you imported that module
