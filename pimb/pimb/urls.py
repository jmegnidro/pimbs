"""pimb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from djoser.urls.base import router
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from entreprise.views import EntrepriseListView, EntrepriseDetailView, FondateurListView, FondateurDetailView, \
    InnovationDetailView, InnovationListView, EvenementListView, EvenementDetailView, EntrepriseListViewCreate, \
    EntrepriseDetailViewCreate

from soacial.views import MessageListView, MessageDetailView, NotificationListView, NotificationDetailView

schema_view = get_schema_view(
    openapi.Info(
        title="Programme d'innovation made in Benin",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.litslab.net",
        contact=openapi.Contact(email="dmegnidro@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('entreprise/', EntrepriseListView.as_view(), name='entreprise-list-detail'),
    path('entreprise/detail/<int:pk>/', EntrepriseDetailView.as_view(), name='entreprise-detail-detail'),

    path('entreprise/associe/fondation/event/', EntrepriseListView.as_view(), name='entreprise-associe'),
    path('entreprise/associe/fondation/event/<int:pk>/', EntrepriseDetailView.as_view(),
         name='entreprise-detail-asscoie'),

    path('fondateur/', FondateurListView.as_view(), name='fondateur-list'),
    path('fondateur/<int:pk>/', FondateurDetailView.as_view(), name='fondateur-detail'),

    path('innovation/', InnovationListView.as_view(), name='innovation-list'),
    path('innovation/<int:pk>/', InnovationDetailView.as_view(), name='innovation-detail'),

    path('evenement/', EvenementListView.as_view(), name='evenement-list'),
    path('evenement/<int:pk>/', EvenementDetailView.as_view(), name='evenement-detail'),
    # messagerie
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),

    # api connect
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),
    # path("auth/webauthn/", include('djoser.webauthn.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

]
