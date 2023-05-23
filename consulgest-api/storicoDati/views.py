from django.shortcuts import render
from rest_framework import generics, permissions, authentication,viewsets, status
from .models import DatiStandard
from .serializers import DatiStandardSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DatiStandardView(permissions.IsAuthenticated,generics.ListAPIView):
    queryset = DatiStandard.objects.all()
    serializer_class = DatiStandardSerializer
    # filterset_fields = ['id_dossier']


# class DatiStandardCreateView(permissions.IsAuthenticated,generics.ListCreateAPIView):
#     queryset = DatiStandard.objects.all()
#     serializer_class = DatiStandardSerializer
#     filter_backends = [DjangoFilterBackend]

