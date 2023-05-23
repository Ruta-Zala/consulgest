from datetime import datetime
import json
from .models import *
from .serializers import *
from rest_framework import generics, permissions, authentication,viewsets, status
#from api.mixins import StaffEditorPermissionMixin
from rest_framework.response import Response
import pandas as pd
# from django.http import response,HttpResponse
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
import requests
from pratiche import parser
from django.http import JsonResponse
from rest_framework import views
from django.forms.models import model_to_dict
from pratiche.OperazioniCsv import test
from lotto.models import Lotto
from pratiche.script import *


fs = FileSystemStorage(location='uploads/')


@api_view(['GET'])
def Info1(request): #numero di dossier che possono diventare positivi, statistico  
    '''
    TO-DO:
    Impostare numero di dossier che possono diventare positivi come:
    Prendere la lista delle pratiche da Test_File o da Pratiche (Vedere come integrarli)
    Ammontare Affidato -> Ammontare Riscosso -> Numero di rate pagate -> Cash Balance


    Positivo - Negativo diventa Esito, da lista Pratiche
    Utilizzare Probability Calibration curves, Scikit Learn 


    '''
    pass

@api_view(['GET'])
def Info2(request): #numero di dossier negativi   
    '''
    TO-DO:
    Impostare numero di dossier che possono diventare negativi o quelli che sono già negativi come:
    Affidato vs. Riscosso vs. Numero di rate vs. Cash Balance 
    
    Positivo - diventa Esito, da lista Pratiche
    Utilizzare Probability Calibration curves, Scikit Learn 
    Considerare i file da CGManager Report

    '''        
    pass

@api_view(['GET'])
def Info3(request): #Valore Medio atteso di incasso per ogni posizione, su tutto il portafoglio
    '''
    TO-DO:
    Impostare Valore medio di incasso come:
    Affidato vs. Riscosso vs. Numero di Rate vs. Totale Affidato, crearne una colonna ed applicare una prediction
    Considerare i file da CGManager Report

    ''' 
    pass

@api_view(['GET'])
def Info4(request):
# INCIDENZA DELLE POSIZIONI FILTRATE SUL TOTALE PORTAFOGLIO
# (QUINDI CI VUOLE DI DEFAULT UN CALCOLO CHE INDICHI LA PERCENTUALE DI ESCUSSIONE
# RISPETTO AL NUMERO DI POSIZIONI AFFIDATE, ED UN FILTRO CHE INDICHI IL NUMERO DELLE POSIZIONI RISPETTO
# ALL’ANNO DI RICHIESTA ED IL PESO ATTESO SUL TOTALE)
    pass

@api_view(['GET'])
def Stat1(request): # PESO DEL VALORE ATTESO SUL VALORE AFFIDATO (Espresso in percentuale?)
    # Totale Valore Atteso dalla predizione sul Totale dell'affidato, come numero e come percentuale
    pass

@api_view(['GET'])
def Stat2(request): # PESO DEL NUMERO DI POSIZIONI POSITIVE SUL NUMERO DI DOSSIER AFFIDATI (Espresso in percentuale?)
    #Totale numero posizioni positive sul numero di dossier affidati, come numero e come percentuale
    pass

@api_view(['GET'])
def Dossiertotalnumber(request):
    count = Dossier.objects.all().count()
    return Response(count, status.HTTP_200_OK)

class DossierListCreateAPIView(permissions.IsAuthenticated,generics.ListCreateAPIView):
    queryset = Insert_Dossier.objects.all()
    serializer_class = DossierSerializer
    #authentication_classes = [authentication.SessionAuthentication,TokenAuthentication] # authentication.TokenAuthentication
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Position_Type'] #Filtering for
    
    def perform_create(self, serializer):
        serializer.is_valid()
        serializer.save()

class DossierDetailAPIView(permissions.IsAuthenticated,generics.RetrieveAPIView):
    queryset = Insert_Dossier.objects.all()
    serializer_class = DossierSerializer
    #authentication_classes = [authentication.SessionAuthentication,TokenAuthentication]
#    permission_classes = [permissions.DjangoModelPermissions]

class DossierUpdateAPIView(permissions.IsAuthenticated,generics.UpdateAPIView):
    queryset = Insert_Dossier.objects.all()
    serializer_class = DossierSerializer
    lookup_field = 'pk'
    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
#   permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        serializer.save()

class DossierDeleteAPIView(permissions.IsAuthenticated,generics.DestroyAPIView):
    queryset = Insert_Dossier.objects.all()
    serializer_class = DossierSerializer
    lookup_field = 'pk'
    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
#   permission_classes = [permissions.DjangoModelPermissions]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

#class DossierOperation(generics.GenericAPIView):
#    queryset = Dossier_test.object.all()
#    serializer_class = DossierSerializer
#    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

class UploadFileView(permissions.IsAuthenticated,generics.ListCreateAPIView):
        serializer_class = TestFileUploadSerializer
        queryset = Insert_File.objects.all()

        @action(detail=True, methods=['POST'])
        def create(self, request, *args, **kwargs):

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
   
            lotto = Lotto()
            lotto.name = serializer.validated_data['name']
            lotto.created_at = datetime.now()
            lotto.updated_at = datetime.now()
            lotto.utente = request.user
            lotto.template = serializer.validated_data['id_template']
            lotto.save()
            
            template = serializer.validated_data['id_template']
            
            # ricarica l'oggetto lotto per assicurarti che il suo id sia aggiornato
            lotto.refresh_from_db()
            print(f"questo è liddddd --> {lotto.id}")
            
            serializer.save()    
            
            read_dossier(serializer.validated_data['file'], lotto, template)
            
            return Response("Success")

class UploadedFileDetailView(permissions.IsAuthenticated,generics.RetrieveAPIView):
        serializer_class = TestFileUploadSerializer
        queryset = Insert_File.objects.all()
        #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['id']

        def detail(self):
            File_Detail = Insert_File.objects.all()
            return Response(File_Detail, status.HTTP_200_OK)

class HeaderStandardView(permissions.AllowAny,views.APIView):
    def get(self, request, *args, **kwargs):
        res = parser.Parser.getStandardHeader(self)
        return Response(res)
       
class MappaCreateView(permissions.AllowAny,generics.CreateAPIView):
    serializer_class = MappaSerializer
    queryset = Mappa.objects.all()
    
    def post(self, request, **args):
        try:
            mappa = Mappa()
            mappa.Credit_Institute = request.data['Credit_Institute']
            mappa.dict_institute = request.data['dict_institute']
            mappa.save()
            return Response("Success")
        except Exception as e:
             return Response((e),status=status.HTTP_406_NOT_ACCEPTABLE)
         
class MappaGetByIdView(permissions.AllowAny,generics.RetrieveAPIView):
    serializer_class = MappaSerializer
    
    def get(self, request, *args, **kwargs):
        id_mappa = kwargs['pk']
        queryset = Mappa.objects.filter(id = id_mappa)[0]
        return Response(model_to_dict(queryset))
        
    lookup_field = ['pk']
    
class ParseHeadersView(permissions.AllowAny,views.APIView):
    
    
    def post(self, request, *args, **kwargs):
        # data_json = kwargs['data']
        # file = kwargs['file']
        
        
        # DATA_JSON E FILE ORA SONO STATICI PER TEST
        file = "testt.csv" 
        data_json = json.dumps({
            "valore1": {
                "type": 'str',
            },
            "valore2":{
                "type": 'str',
            }
        })
        
        
        parser.Parser.replacementHeaders(None, data_json, file)
        return Response("success")
    
class TestView(permissions.AllowAny, views.APIView):
    def post(self, request, *args, **kwargs):
        test()
        return Response("success")
    
    



    
    