from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import Utilisateur


class UtilisateurCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Utilisateur
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'role',
            'date_inscription',
            'date_derniere_connexion',
            'role')


class UtilisateurSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Utilisateur
        fields = '__all__'
