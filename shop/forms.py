from django import forms
from . import models

class EmailForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'
