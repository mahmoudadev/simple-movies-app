from django import forms
from .models import Category, Movie

class CustomForm(forms.Form):
    name = forms.CharField(max_length=233)
    content = forms.CharField(widget=forms.Textarea)




class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"