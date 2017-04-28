from django import forms
from .models import PhenoDb

class PhenoDBForm(forms.ModelForm):

    class Meta:
    	model = PhenoDb
    	fields = ['disease']