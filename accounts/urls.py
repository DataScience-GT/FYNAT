from django.urls import path

from accounts import views as account_views


urlpatterns = [
    url(r'^register/$', views.view_profile, name = 'view_profile'),
    url(r'^register/(?)$', views.view_profile, name = 'view_profile_with_pk'),
    path('signup/', account_views.signup, name='signup'),
]
