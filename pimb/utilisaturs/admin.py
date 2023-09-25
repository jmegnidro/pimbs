from django.contrib import admin

from .models import Utilisateur, ContactUtilisateur, DocumentUtilisateur, PlanificationUtilisateur


class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_inscription', 'role')
    search_fields = ['username', 'email']
    list_filter = ('role', 'date_inscription')


class ContactUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'nom', 'email', 'entreprise')
    search_fields = ['nom', 'email', 'entreprise']
    list_filter = ('entreprise',)


class DocumentUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'titre', 'type_document', 'date_upload')
    search_fields = ['titre', 'type_document']
    list_filter = ('type_document', 'date_upload')


class PlanificationUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'titre', 'date_planification', 'heure', 'duree', 'rappel')
    search_fields = ['titre']
    list_filter = ('date_planification', 'rappel')


# Inscription des modèles avec les classes Admin personnalisées
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(ContactUtilisateur, ContactUtilisateurAdmin)
admin.site.register(DocumentUtilisateur, DocumentUtilisateurAdmin)
admin.site.register(PlanificationUtilisateur, PlanificationUtilisateurAdmin)
