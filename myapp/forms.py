from django import forms
from .models import *

class ProprietaireForm(forms.ModelForm):
    

    class Meta:
        model = Proprietaire
        fields = ['nom','telephone', 'email', 'username','password']
        #fields = "__all__"


class AppartementForm(forms.ModelForm):
    #images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Appartement
        fields = "__all__"
        #fields = ['adresse', 'taille', 'nombre_chambres', 'prix']


class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = "__all__"
