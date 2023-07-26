from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(Utilisateur)
admin.site.register(Proprietaire)
admin.site.register(Appartement)
admin.site.register(ImageAppartement)
admin.site.register(Reservation)
admin.site.register(Message)

