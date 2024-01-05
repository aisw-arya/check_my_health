from django import forms
from diseases.models import Routine

class Form(forms.ModelForm):
    class Meta:
        model=Routine
        fields="__all__"
