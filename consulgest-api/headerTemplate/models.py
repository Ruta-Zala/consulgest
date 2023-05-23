from django.db import models
from CGIBackend import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_migrate
from django.core.management import call_command
import jsonfield


class Template(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # colonne = ArrayField(models.CharField(max_length=255))
    colonne_mappate = jsonfield.JSONField()
    id_utente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class DefaultColumns(models.Model):
    name = models.CharField(max_length=255)


# sistema per caricare i dati di default su db
def load_fixtures(sender, **kwargs):
    call_command('loaddata', 'default_columns')


post_migrate.connect(load_fixtures)
