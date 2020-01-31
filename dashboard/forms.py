from django import forms


class StudentProfileForm(forms.Form):
  fav_class = forms.CharField(label='What is your favorite class? ', max_length=100)
  fav_hobby = forms.CharField(label='What is your favorite hobby? ', max_length=100)
  fun_fact = forms.CharField(label='What is a fun fact about yourself? ', max_length=100)