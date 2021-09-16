from django import forms
from django.forms import fields, widgets
from .models import Phonebook


class PhoneContacts(forms.ModelForm):
    class  Meta:
        model = Phonebook
        fields=['name','phone_num']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone_num':forms.NumberInput(attrs={'class':'form-control'})
        }
