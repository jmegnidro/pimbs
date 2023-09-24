from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SessionVideo, Participant


class SessionVideoAdmin(admin.ModelAdmin):
    list_display = ('session_coaching', 'lien', 'heure_debut', 'heure_fin', 'statut')
    search_fields = ['session_coaching__utilisateur__nom', 'session_coaching__coach__utilisateur__nom']
    list_filter = ('statut',)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('session_video', 'utilisateur', 'statut')
    search_fields = ['session_video__session_coaching__utilisateur__nom', 'utilisateur__nom']
    list_filter = ('statut',)


# Enregistrement des modèles avec leurs classes d'administration personnalisées
admin.site.register(SessionVideo, SessionVideoAdmin)
admin.site.register(Participant, ParticipantAdmin)
