from django import forms
from nameApp.models import PetInterest

class PetInterestForm(forms.ModelForm):
    class Meta:
        model = PetInterest
        fields = ['name', 'surname', 'phone','email', 'pet', 'moreInfo']