from django.db import models

from utilisaturs.models import Utilisateur


# Create your models here.

class Message(models.Model):
    STATUT_CHOICES = [('Lu', 'Lu'), ('Non-lu', 'Non-lu')]
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus')
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)


class Notification(models.Model):
    STATUT_CHOICES = [('Vue', 'Vue'), ('Non-vue', 'Non-vue')]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
