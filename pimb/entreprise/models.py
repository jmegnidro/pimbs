from django.db import models

from utilisaturs.models import Utilisateur


# Create your models here.


class Entreprise(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    nom_entreprise = models.CharField(max_length=255)
    description = models.TextField()
    site_web = models.URLField(max_length=200, null=True, blank=True)
    secteur_activite = models.CharField(max_length=200)


class Fondateur(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.URLField(null=True, blank=True)


class Innovation(models.Model):
    TYPE_CHOICES = [('Produit', 'Produit'), ('Service', 'Service'), ('Processus', 'Processus')]
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_publication = models.DateField()
    type_innovation = models.CharField(max_length=20, choices=TYPE_CHOICES)


class Evenement(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_evenement = models.DateField()
    lieu = models.CharField(max_length=200)
    image = models.ImageField(upload_to='evenements/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
