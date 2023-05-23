from django.db import models

# Create your models here.
class AbstractDossier(models.Model):
    committente_codice = models.CharField(max_length=255)
    id_profilo_esattore = models.CharField(max_length=255)
    esattore_codice = models.CharField(max_length=255)
    committente_desc = models.CharField(max_length=255)
    profilo_desc = models.CharField(max_length=255)
    p_iva = models.CharField(max_length=255)
    luogo_nascita = models.CharField(max_length=255)
    cap = models.CharField(max_length=255)
    citta = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    tipo_telefono1 = models.CharField(max_length=255)
    tipo_telefono2 = models.CharField(max_length=255)
    filiale = models.CharField(max_length=255)
    minimo_dovuto = models.CharField(max_length=255)
    rate_arretrate = models.CharField(max_length=255)
    importo_capitale = models.CharField(max_length=255)
    importo_interessi = models.CharField(max_length=255)
    importo_spese = models.CharField(max_length=255)
    importo_spese_recupero = models.CharField(max_length=255)
    importo_differenza = models.CharField(max_length=255)
    debitoresiduo = models.CharField(max_length=255)
    importo_rata = models.CharField(max_length=255)


    class Meta:
        abstract = True