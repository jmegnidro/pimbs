from rest_framework import serializers
from .models import Message, Notification
from utilisaturs.models import Utilisateur


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        expediteur_id = self.context['request'].data.get('expediteur')
        destinataire_id = self.context['request'].data.get('destinataire')
        expediteur = Utilisateur.objects.get(id=expediteur_id)
        destinataire = Utilisateur.objects.get(id=destinataire_id)

        message = Message.objects.create(
            expediteur=expediteur,
            destinataire=destinataire,
            contenu=validated_data.get('contenu'),
            statut=validated_data.get('statut')
        )
        return message


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    def create(self, validated_data):
        utilisateur_id = self.context['request'].data.get('utilisateur')
        utilisateur = Utilisateur.objects.get(id=utilisateur_id)

        notification = Notification.objects.create(
            utilisateur=utilisateur,
            contenu=validated_data.get('contenu'),
            statut=validated_data.get('statut')
        )
        return notification
