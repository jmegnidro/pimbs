from django.db import models

from utilisaturs.models import Utilisateur


# Create your models here.


class Coach(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    biographie = models.TextField()
    tarif_horaire = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilite = models.BooleanField(default=True)


class DomaineExpertise(models.Model):
    nom_domaine = models.CharField(max_length=100)
    description = models.TextField()


class CoachDomaine(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    domaine = models.ForeignKey(DomaineExpertise, on_delete=models.CASCADE)


class DemandeCoaching(models.Model):
    STATUT_CHOICES = [('En Attente', 'En Attente'), ('Acceptée', 'Acceptée'), ('Refusée', 'Refusée')]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    domaine = models.ForeignKey(DomaineExpertise, on_delete=models.CASCADE)
    date_soumission = models.DateField(auto_now_add=True)
    date_souhaitee = models.DateField()
    heure_souhaitee = models.TimeField()
    message = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    date_reponse = models.DateField(null=True, blank=True)
    commentaire_coach = models.TextField(null=True, blank=True)


class SessionCoaching(models.Model):
    STATUT_CHOICES = [('Planifiée', 'Planifiée'), ('Terminée', 'Terminée'), ('Annulée', 'Annulée')]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='sessions_utilisateur')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='sessions_coach')
    date_session = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    note_utilisateur = models.PositiveIntegerField(null=True, blank=True)
    commentaire_utilisateur = models.TextField(null=True, blank=True)
