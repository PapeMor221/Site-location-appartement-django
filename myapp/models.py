from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
# Create your models here.


class Utilisateur(User):
    nom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = "Utilisateur"
        verbose_name = 'Utilisateur'
        verbose_name_plural = "Utilisateurs"
        
        
class Proprietaire(User):
    nom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    profil_photo = models.ImageField(upload_to='Profil_Proprietaire/', default = "")
    licence = models.CharField(max_length=30, default = "")
    Taxe_Number = models.CharField(max_length=30, default = "")
    Specialite = models.CharField(max_length=30, default = "")
    # Autres champs spécifiques au propriétaire

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = "Proprietaire" 
        verbose_name = 'Proprietaire'
        verbose_name_plural = "Proprietaires"
        

class Appartement(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, default="")
    ville = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    profil_photo = models.ImageField(upload_to='Profil_Appartement/', default="")
    taille = models.CharField(max_length=100)
    nombre_chambres = models.CharField(max_length=100)
    salle_de_bain = models.CharField(max_length=100 ,default="")
    garrage = models.CharField(max_length=100,default="")
    prix = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.adresse
        


class ImageAppartement(models.Model):
    appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='appartements/')
    # Autres champs spécifiques à l'image

    def __str__(self):
        return self.image.name


class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    # Autres champs spécifiques à la réservation

    def __str__(self):
        return f"{self.utilisateur.username} - {self.appartement.adresse}"
    
    

class Message(models.Model):
    expediteur_name = models.CharField(max_length=100 , default="")
    expediteur_email = models.EmailField(default="")
    expediteur_phone = models.CharField(max_length=100, default="")
    destinataire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, related_name='messages_recus')
    appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE, default="")
    #reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De: {self.expediteur_name} à: {self.destinataire}"
