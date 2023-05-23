from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from requests import Response
#from MyCare_BackEnd.userapp import serializers
from userapp.serializers import *
from rest_framework import generics
from .models import Utente
from django_filters.rest_framework import DjangoFilterBackend

class UtenteRegistrationView(RegisterView): 
    serializer_class = UtenteCustomRegistrationSerializer  

class AdminRegistrationView(RegisterView):
    serializer_class = AdminCustomRegistrationSerializer

class AdminListAPIView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminDetailSerializer

class UtenteListAPIView(generics.ListAPIView): 
    queryset = Utente.objects.all()
    serializer_class = UtenteDetailSerializer
    
class UtenteDetailAPIView(generics.RetrieveAPIView): 
    queryset = Utente.objects.all()
    serializer_class = UtenteDetailSerializer
    lookup_field = 'pk'

class UtenteUpdateAPIView(generics.UpdateAPIView): 
    queryset = Utente.objects.all()
    serializer_class = UtenteDetailSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

class UtenteDestroyAPIView(generics.DestroyAPIView):
    queryset = Utente.objects.all()
    serializer_class = UtenteDetailSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)