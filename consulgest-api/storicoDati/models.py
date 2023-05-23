from abc import ABC, abstractmethod
from django.db import models
from abstractDossier.models import AbstractDossier

class DatiStandard(AbstractDossier):
    id = models.AutoField(primary_key=True)
    data_affido_anno = models.CharField(max_length=255)
    scadenza_mandato_anno = models.CharField(max_length=255)
    scadenza_mandato_mese = models.CharField(max_length=255)
    data_nascita_anno = models.CharField(max_length=255)
    data_nascita_mese = models.CharField(max_length=255)
    data_affido_mese = models.CharField(max_length=255)




