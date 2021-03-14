from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Movie

not_allowed_name = ["abc", "test", "dummy", "root"]


class CustomLoginForm(forms.Form):
    name = forms.CharField(max_length=233)
    password = forms.CharField(widget=forms.PasswordInput)



    # for adding custom valiation to the above name field
    def clean(self):
        super(CustomLoginForm, self).clean()
        name = self.cleaned_data.get("name")
        if name  in not_allowed_name:
            return ValidationError("name is not allowed")


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"