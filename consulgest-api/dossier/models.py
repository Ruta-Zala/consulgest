from django.db import models
from CGIBackend import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_migrate
from django.core.management import call_command
from abstractDossier.models import AbstractDossier
from storicoDati.models import DatiStandard
from lotto.models import Lotto

class Dossier(AbstractDossier):
    id = models.AutoField(primary_key=True)
    id_lotto = models.ForeignKey(Lotto, on_delete=models.CASCADE)
    id_dati_standard = models.OneToOneField(DatiStandard, on_delete=models.CASCADE, null=True)
    data_affido = models.CharField(max_length=255)
    scadenza_mandato = models.CharField(max_length=255)
    data_nascita = models.CharField(max_length=255)

