from email import message
from posixpath import split
from unicodedata import name
from urllib import request
from wsgiref.validate import validator
from django.core.exceptions import ValidationError
from rest_framework import serializers, fields
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import *
# from servizi.models import SingoloServizio
from django.core.validators import *
from rest_framework.validators import UniqueValidator

class AdminCustomRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def get_cleaned_data(self):
        data = super(AdminCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'first_name' : self.validated_data.get('first_name', ''),
            'last_name' : self.validated_data.get('last_name', ''),
            'email' : self.validated_data.get('email', '')
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(AdminCustomRegistrationSerializer, self).save(request)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        admin = Admin(admin=user,first_name=self.cleaned_data.get('first_name'),last_name=self.cleaned_data.get('last_name'),email=self.cleaned_data.get('email')
        )
        admin.save()
        return user

class UtenteCustomRegistrationSerializer(RegisterSerializer):
    id = fields.ReadOnlyField()
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def get_cleaned_data(self):
        data = super(UtenteCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'first_name' : self.validated_data.get('first_name', ''),
            'last_name' : self.validated_data.get('last_name', ''),
            'email' : self.validated_data.get('email', '')
        }
        data.update(extra_data)
        return data
      

    def save(self, request,*args,**kwargs):
        user = super(UtenteCustomRegistrationSerializer, self).save(request)
        user.is_utente = True
        user.is_active = True
        user.save()
        utente = Utente(
            utente=user,
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
        )

        return user



class UtenteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = [
        'id',
        'first_name',
        'last_name',
        'email'
        ]

class AdminDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"
  
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'is_utente',
        ]


# SERIALIZER BADANTE FILTRATO PER CITTA'
class FilterUtenteSerialize(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = [
        'id',
        'first_name',
        'last_name'
        ]