from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from headerTemplate.models import Template
from CGIBackend import settings

import jsonfield


# Create your models here.
#class Posizione_Test(models.Model):
#    Posizione_1_test = "Pos_1_test"
#    Posizione_2_test = "Pos_2_test"
#    Posizione_3_test = "Pos_3_test"
#    Posizione_4_test = "Pos_4_test"
#    OPZIONI_POSIZIONE_TEST = [
#        (Posizione_1_test, "Crediti in Phone Collection"),
#        (Posizione_2_test, "Crediti in pre-decadenza"),
#        (Posizione_3_test, "Crediti in post-decadenza"),
#        (Posizione_4_test, "NPL")
#    ]
#    id = models.AutoField(primary_key=True)
#    Tipo_Pratica = models.CharField(max_length=10,choices=OPZIONI_POSIZIONE_TEST)

# class CSV(models.Model):
#     file_name = models.FileField(upload_to='csvs')
#     activated = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#
#
#     def __str__(self):
#         return str(self.file_name)

# CAMPI DA AGGIUNGERE AI MODELLI DEI DOSSIER:
# DATA DI CREAZIONE
# NOME DOSSIER
# NUMERO DOSSIER E/O N.D.G.
# NOME DEBITORE,
# CAP/PAESE/PROVINCIA
# IMPORTO AFFIDATO
# PROBABILITA’ DI INCASSO
# IMPORTO ATTESO DI PAGAMENTO.

class Insert_Dossier(models.Model):
    id = models.AutoField(primary_key=True)
#   owner = models.ForeignKey(User)
    Position_1_test = "Pos_1_test"
    Position_2_test = "Pos_2_test"
    Position_3_test = "Pos_3_test"
    Position_4_test = "Pos_4_test"
    Position_Test = [
                (Position_1_test, "Phone Collection Credits"),
                (Position_2_test, "Pre-Falling Credits"),
                (Position_3_test, "Post-Decaying Credits"),
                (Position_4_test, "NPL")
    ]
    Credit_Institute = models.CharField(max_length=20,blank=False,null=False)
    Position_Type = models.CharField(choices=Position_Test, max_length=10, blank=True, null=True)
    Dossier_Name = models.CharField(max_length=120,blank=True)
    Field_1_test = models.CharField(max_length=120,blank=True)
    Field_2_test = models.DecimalField(max_digits=15,blank=True,decimal_places=4)
    Field_3_test = models.DecimalField(max_digits=15,blank=True,decimal_places=4)
    Field_4_test = models.DecimalField(max_digits=15,blank=True,decimal_places=4)
   # owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='Dossier_test', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def Dummy_Inference(self):
        #inf_dummy = ((self.campo_2_test+self.campo_3_test+self.campo_4_test)/3)
        return "%.3f" %(float(self.Field_2_test+self.Field_3_test+self.Field_4_test)/3)

class Insert_File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,blank=False,null=False)
    file = models.FileField(upload_to='uploads/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    id_utente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return self.Credit_Institute

# modello che memorizza le mappature fornite dall'utente
class Mappa(models.Model):
    id = models.AutoField(primary_key=True)
    Credit_Institute = models.CharField(max_length=20,blank=False,null=False, unique=True)
    dict_institute = jsonfield.JSONField()