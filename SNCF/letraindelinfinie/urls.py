
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

#Création des urls pour les différentes pages

urlpatterns = [
    path('index/', views.index, name="index"),
    path('show/<int:train_id>/', views.show, name='show'),
    path('show/', views.search_redirect, name = 'search_redirect'),
    path('random/', views.random, name="random"),
    path('create/', views.create, name='create'),
]
