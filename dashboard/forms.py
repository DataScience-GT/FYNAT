from django import forms


class StudentProfileForm(forms.Form):
  first_name = forms.CharField(label='What\'s your first name? ', max_length=200)
  last_name = forms.CharField(label='What\'s your last name?', max_length=200)
  interested_orgs = forms.CharField(label='What organizations are you interested in? ', max_length=200)
  major = forms.CharField(label='What is your major? ', max_length=100)
  year = forms.CharField(label='What year are you? ', max_length=100)
  hobbies = forms.CharField(label='What are your hobbies? ', max_length=200)
  favorites = forms.CharField(label='What are some of your favorite things? Could be anything (study spots, food, music, movies, sports etc)! ', max_length=500)
  curr_skills = forms.CharField(label='What are some of your skills? ', max_length=500)
  look_to_learn = forms.CharField(label='What are you looking to learn at Tech (could be anything)? ', max_length=500)
  self_descriptor = forms.CharField(label='In a few words or sentence describe yourself or personality.', max_length=150)
  where_from = forms.CharField(label='What are you from? ', max_length=150)
  residence_area = forms.CharField(label='What are you staying?', max_length=100)

