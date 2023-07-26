from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',accueil,name="accueil"),
    path('inscription_proprietaire',Proprietaire_reregister,name="inscription_proprietaire"),
    path('ajouter_appartement',ajouter_appartement_,name="ajouter_appartement"),
    path('appartement/<int:appartement_id>/', detail_appartement, name='detail_appartement'),
    path('profil/<int:props_id>/', visit_profil, name='visit_profil'),
    path('Proprietaire_login/', Proprietaire_login, name='Proprietaire_login'),
    path('profil/', profil, name='profil'),
    path('logout/', LogoutView.as_view(next_page='accueil'), name='logout'),
    path('signe_log/',view_signe_log,name="signe_log"),
]