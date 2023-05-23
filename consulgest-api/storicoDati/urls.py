from django.urls import path
from .views import DatiStandardView

urlpatterns = [
    path('storicoDati/', DatiStandardView.as_view(), name='dati-standard'),
]
