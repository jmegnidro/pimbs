from rest_framework import serializers
from .models import Entreprise, Fondateur, Innovation, Evenement


class EntrepriseSerialize(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'


class FondateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fondateur
        fields = '__all__'


class InnovationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Innovation
        fields = '__all__'


class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'


class EntrepriseSerializer(serializers.ModelSerializer):
    fondateurs = FondateurSerializer(many=True, read_only=True, source='fondateur_set')
    innovations = InnovationSerializer(many=True, read_only=True, source='innovation_set')
    evenements = EvenementSerializer(many=True, read_only=True, source='evenement_set')

    class Meta:
        model = Entreprise
        fields = ('id', 'utilisateur', 'nom_entreprise', 'description', 'site_web',
                  'secteur_activite', 'fondateurs', 'innovations', 'evenements')
