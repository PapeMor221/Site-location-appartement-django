from django.shortcuts import render
from django.shortcuts import render, redirect
#from .forms import AppartementForm
from .forms import ProprietaireForm, ReservationForm
from .models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def accueil(request):
    appartements = Appartement.objects.all()
    props = Proprietaire.objects.all()
    return render(request, 'accueil.html', {'appartements': appartements, "proprietaires":props})


def Proprietaire_reregister(request):
    
    if request.method == 'POST':
        # Créer l'utilisateur et le connecter
        user = Proprietaire.objects.create_user(
            nom = request.POST['Nom'],
            username=request.POST['username'],
            email=request.POST['email'],
            telephone = request.POST['telephone'],
            password=request.POST['password1'],
            profil_photo = request.FILES.get('profil_photo')
        )
        
        user.save()
        #login(request, user)
        return redirect('Proprietaire_login')
    
    return render(request, "inscription_Proprietaire.html")

def view_signe_log(request):
    #print(request)
    context : dict = {}
    return render(request, "signe_log.html", context)

""""
@login_required(login_url='/signe_log/')
def ajouter_appartement(request):
    if request.method == 'POST':
        form = AppartementForm(request.POST, request.FILES)
        if form.is_valid():
            appartement = form.save()  # Enregistre l'appartement
            images = request.FILES.getlist('images')  # Récupère la liste des images
            for image in images:
                ImageAppartement.objects.create(appartement=appartement, image=image)  # Crée un objet ImageAppartement pour chaque image
            return redirect('accueil')  # Redirige vers la page d'accueil après l'ajout de l'appartement
    else:
        form = AppartementForm()
    return render(request, 'ajouter_appartement.html', {'form': form})"""

@login_required(login_url='/signe_log/')
def ajouter_appartement_(request):
    
    if request.method == 'POST':
        
        nom = request.POST['nom']
        ville = request.POST['ville']
        adresse = request.POST['adresse']
        profil_photo = request.FILES.get('profil_photo')
        taille = request.POST['taille']
        nombre_chambres = request.POST['nombre_chambres']
        salle_de_bain = request.POST['salle_de_bain']
        garrage = request.POST['garrage']
        prix = request.POST['prix']
        description = request.POST['description']
        #profil_photo = request.POST['profil_photo'],
        
        appartement = Appartement(
            nom = nom,
            ville=ville,
            adresse = adresse,
            profil_photo = profil_photo,
            taille = taille,
            nombre_chambres = nombre_chambres,
            salle_de_bain = salle_de_bain,
            garrage = salle_de_bain,
            prix=prix,
            description=description,
            proprietaire = request.user.proprietaire
            )

        appartement.save()

        images = request.FILES.getlist('images')  # Récupère la liste des images
        for image in images:
            ImageAppartement.objects.create(appartement=appartement, image=image)  # Crée un objet ImageAppartement pour chaque image
        return redirect('accueil')  # Redirige vers la page d'accueil après l'ajout de l'appartement

    return render(request, 'ajouter_appartement.html')




def detail_appartement(request, appartement_id):
    appartement = Appartement.objects.get(id=appartement_id)
    images = appartement.imageappartement_set.all()
    
    if request.method == 'POST':
        # Enregistrer le message
        message = Message(
            expediteur_name = request.POST['Nom'],
            expediteur_email= request.POST['email'],
            expediteur_phone = request.POST['telephone'],
            contenu = request.POST['contenu'],
            destinataire= appartement.proprietaire,
            appartement = appartement,
            
        )
        message.save()
        #messages.success(request, "Réservation effectuée avec succès.")
        return redirect('detail_appartement', appartement_id=appartement.id)
        

    context = {
        'appartement': appartement,
        'images': images
    }

    return render(request, 'detail_appartement.html', context)


def Proprietaire_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        print(user is not None)
        if user is not None:
            #login(request, user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profil')
    
    return render(request, 'login.html')


@login_required(login_url='/signe_log/')
def profil(request):
    user = request.user
    #context = {'user': user}
    
    proprietaire = request.user.proprietaire  # Supposons que vous ayez un modèle de propriétaire avec une relation OneToOne avec User
    messages = Message.objects.filter(appartement__proprietaire=proprietaire)
    appartements = Appartement.objects.filter(proprietaire=proprietaire)
    
    context = {
        'user': user,
        'messages': messages,
        'appartements':appartements
    }
    
    return render(request, 'profil_Proprietaire.html', context)


def visit_profil(request, props_id):
    proprietaire = Proprietaire.objects.get(id=props_id)
    appartements = Appartement.objects.filter(proprietaire=proprietaire)

    context = {
        'proprietaire': proprietaire,
        'appartements':appartements
    }

    return render(request, 'visit_profil.html', context)


def messages_proprietaire(request):
    proprietaire = request.user.proprietaire  # Supposons que vous ayez un modèle de propriétaire avec une relation OneToOne avec User
    messages = Message.objects.filter(appartement__proprietaire=proprietaire)
    
    context = {
        'messages': messages
    }
    
    return render(request, 'messages_proprietaire.html', context)

