from django import forms
from dashboard.models import Post

class HomeForm(forms.ModelForm): #use a model form so that our form data can be accessed
#in a proper place
    class1 = forms.CharField()
    class2 = forms.CharField()
    class3 = forms.CharField()

    class Meta:
        model = Post
        fields = ('class1','class2', 'class3') #use a tuple, fields form is required for creating a ModelForm
