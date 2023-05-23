from django.urls import path
from . import views

urlpatterns = [
    path('dossier/', views.DossierView.as_view(), name='dossier-list'),
    path('dossier/<int:pk>/', views.DossierViewQ.as_view(), name='dossier-id_rud'),
    #path('dossier/<int:pk>/', views.DossierView.as_view(), name='dossier-id_lc'),
    path('dossier_create/', views.DossierCreate.as_view(), name='dossier-create'),
    #path('dossier/<int:idUser>/', views.DossierViewQ.as_view(), name='dossier-by-id'),
   ]
