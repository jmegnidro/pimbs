from rest_framework import generics
from .models import Entreprise, Fondateur, Innovation, Evenement
from .permissions import IsAdminAuthenticated
from .serializers import EntrepriseSerializer, FondateurSerializer, InnovationSerializer, EvenementSerializer


class EntrepriseListView(generics.ListCreateAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    permission_classes = [IsAdminAuthenticated]


class EntrepriseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    permission_classes = [IsAdminAuthenticated]


class FondateurListView(generics.ListCreateAPIView):
    queryset = Fondateur.objects.all()
    serializer_class = FondateurSerializer
    permission_classes = [IsAdminAuthenticated]


class FondateurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fondateur.objects.all()
    serializer_class = FondateurSerializer
    permission_classes = [IsAdminAuthenticated]


class InnovationListView(generics.ListCreateAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
    permission_classes = [IsAdminAuthenticated]


class InnovationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
    permission_classes = [IsAdminAuthenticated]


class EvenementListView(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAdminAuthenticated]


class EvenementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAdminAuthenticated]


class EntrepriseListViewCreate(generics.ListCreateAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    permission_classes = [IsAdminAuthenticated]


class EntrepriseDetailViewCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    permission_classes = [IsAdminAuthenticated]
