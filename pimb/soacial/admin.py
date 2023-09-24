from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Message, Notification


class MessageAdmin(admin.ModelAdmin):
    list_display = ('expediteur', 'destinataire', 'date_envoi', 'statut')
    search_fields = ['expediteur__username', 'destinataire__username', 'contenu']
    list_filter = ('statut', 'date_envoi')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'contenu', 'date_creation', 'statut')
    search_fields = ['utilisateur__username', 'contenu']
    list_filter = ('statut', 'date_creation')

    def short_contenu(self, obj):
        return f"{obj.contenu[:50]}..." if len(obj.contenu) > 50 else obj.contenu

    short_contenu.short_description = 'Contenu'


# Enregistrement des modèles avec leurs classes d'administration personnalisées
admin.site.register(Message, MessageAdmin)
admin.site.register(Notification, NotificationAdmin)
