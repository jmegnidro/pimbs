from django.db import models

from utilisaturs.models import Utilisateur

from coachs.models import SessionCoaching


# Create your models here.

class SessionVideo(models.Model):
    STATUT_CHOICES = [('Planifiée', 'Planifiée'), ('En Cours', 'En Cours'), ('Terminée', 'Terminée')]
    session_coaching = models.OneToOneField(SessionCoaching, on_delete=models.CASCADE)
    lien = models.URLField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)


class Participant(models.Model):
    STATUT_CHOICES = [('En attente', 'En attente'), ('Connecté', 'Connecté'), ('Déconnecté', 'Déconnecté')]
    session_video = models.ForeignKey(SessionVideo, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
