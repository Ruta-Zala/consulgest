from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from django import forms

class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insert_Dossier
        fields = [
            'id',
            'Credit_Institute',
            'Position_Type',
            'Dossier_Name',
            'Field_1_test',
            'Field_2_test',
            'Field_3_test',
            'Field_4_test',
            'Dummy_Inference',
            'created_at'
        ]

class TestFileUploadSerializer(serializers.ModelSerializer):
        file = serializers.FileField()
        class Meta:
            model = Insert_File
            fields =  [ 
                    "id",
                    "name",
                    "file",
                    "created_at",
                    "updated_at",
                    "id_utente",
                    "id_template"
                    ]
         
        # def to_representation(self, instance):
        #     data = super().to_representation(instance)
        #     data['id_utente'] = self.context['request'].user.id
        #     return data

class MappaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mappa
        fields = [
            'Credit_Institute',
            'dict_institute'
        ]