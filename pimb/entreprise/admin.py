from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Entreprise, Fondateur, Innovation, Evenement


class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'nom_entreprise', 'secteur_activite', 'site_web')
    search_fields = ['nom_entreprise', 'utilisateur__nom', 'utilisateur__prenom']
    list_filter = ('secteur_activite',)


class FondateurAdmin(admin.ModelAdmin):
    list_display = ('entreprise', 'nom', 'prenom', 'email')
    search_fields = ['nom', 'prenom', 'entreprise__nom_entreprise']


class InnovationAdmin(admin.ModelAdmin):
    list_display = ('entreprise', 'titre', 'date_publication', 'type_innovation')
    search_fields = ['titre', 'entreprise__nom_entreprise']
    list_filter = ('type_innovation',)


class EvenementAdmin(admin.ModelAdmin):
    list_display = ('entreprise', 'titre', 'date_evenement', 'lieu', 'date_creation')
    search_fields = ['titre', 'entreprise__nom_entreprise']
    list_filter = ('date_evenement', 'lieu')


# Enregistrement des modèles avec leurs classes d'administration personnalisées
admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(Fondateur, FondateurAdmin)
admin.site.register(Innovation, InnovationAdmin)
admin.site.register(Evenement, EvenementAdmin)
