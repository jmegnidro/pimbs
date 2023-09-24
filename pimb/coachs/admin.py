from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Coach, DomaineExpertise, CoachDomaine, DemandeCoaching, SessionCoaching


class CoachAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'tarif_horaire', 'disponibilite')
    search_fields = ['utilisateur__nom', 'utilisateur__prenom', 'biographie']
    list_filter = ('disponibilite',)


class DomaineExpertiseAdmin(admin.ModelAdmin):
    list_display = ('nom_domaine',)
    search_fields = ['nom_domaine', 'description']


class CoachDomaineAdmin(admin.ModelAdmin):
    list_display = ('coach', 'domaine')
    search_fields = ['coach__utilisateur__nom', 'domaine__nom_domaine']
    list_filter = ('domaine',)


class DemandeCoachingAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'coach', 'domaine', 'date_soumission', 'statut')
    search_fields = ['utilisateur__nom', 'coach__utilisateur__nom', 'domaine__nom_domaine', 'message']
    list_filter = ('statut', 'domaine')


class SessionCoachingAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'coach', 'date_session', 'statut')
    search_fields = ['utilisateur__nom', 'coach__utilisateur__nom']
    list_filter = ('statut',)


# Enregistrement des modèles avec leurs classes d'administration personnalisées
admin.site.register(Coach, CoachAdmin)
admin.site.register(DomaineExpertise, DomaineExpertiseAdmin)
admin.site.register(CoachDomaine, CoachDomaineAdmin)
admin.site.register(DemandeCoaching, DemandeCoachingAdmin)
admin.site.register(SessionCoaching, SessionCoachingAdmin)
