from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from CGIBackend import settings

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_utente = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)

  @property
  def utente(self):
    pk = self.pk
    if self.is_utente:
            utente = Utente.objects.filter(utente_id = pk)[0]
            utente = utente.__serialize__()

    return utente

class Admin(models.Model):
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    margine = models.FloatField(default=0.10)

class Utente(models.Model):
    utente = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.utente.username

    def __serialize__(self):
        dict = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
        return dict