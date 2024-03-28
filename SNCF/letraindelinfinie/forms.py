from django.forms import ModelForm
from . import models
from .models import Traindelinfinies
from django import forms


#Ici on s'occupe de la création de trajets via la page HTML
#Je met en lien mon Model avec le formulaire de création
class TraindelinfiniesForm(ModelForm):
    class Meta:
        model = Traindelinfinies
        fields = ('city', 'hour', 'plan',)