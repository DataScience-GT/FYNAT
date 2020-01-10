from django.urls import path

from accounts import views as account_views


urlpatterns = [
    path('signup/', account_views.signup, name='signup'),
]
