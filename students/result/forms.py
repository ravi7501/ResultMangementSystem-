from django import forms
from .models import Students

class InputForm(forms.Form):
   
    Sr_No = forms.IntegerField()
    Name = forms.CharField(max_length = 200)
    