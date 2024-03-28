from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TraindelinfiniesForm
from django import forms
from django.urls import reverse
from .import models
import random


from letraindelinfinie.models import Traindelinfinies

# Create your views here.
def index(request) :
    listeTousTrains = Traindelinfinies.objects.all()
    return render (request, 'html/index.html',{
        "listeTrains" : listeTousTrains,

    })



#Ici on a créé une views pour ma barre de recherche avec un POST
def search_redirect(request):
    if request.method == 'POST':
        id = request.POST.get('search_id')
        if id:
            return redirect(reverse('show', kwargs={
                'train_id' : id,
            }))
        
    return redirect ('index')


def show(request, train_id) :
    #On récupère L'ID du train
    premierTrain = Traindelinfinies.objects.get(trainID = train_id)
    return render (request, 'html/show.html',{
        #je fais le lien entre les éléments de ma base de données et mon HTML
        "city" : premierTrain.city,
        "hour" : premierTrain.hour,
        "plan" : premierTrain.plan,
        "id" : int(train_id),
        "nextID" : int(train_id) +1,
        "previousID" : int(train_id) -1,
    })

def random(request) :
    #Ici on vient récupérer un ID au hasard et renvoyer ver la page show correspondante
    random_id = Traindelinfinies.objects.order_by('?').first()
    return redirect ('show', train_id = random_id.trainID)


def create(request):
    submitted = False
    if request.method == "POST":
        form = TraindelinfiniesForm(request.POST)
        #ici on sauvegarde dans la base de données les infos
        #et on s'assure d'être redirigé sur la page index
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/letraindelinfinie/index')
    else:
        form = TraindelinfiniesForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "html/create.html", {
        "form": form,
    })