from django.urls import path
from .views import *
app_name = 'userapp'

urlpatterns = [
    #Registration Urls
    path('registration/utente/', UtenteRegistrationView.as_view(), name='register-utente'),
    path('registration/admin/', AdminRegistrationView.as_view(), name='register-admin'),
    path('utente/', UtenteListAPIView.as_view(), name='utente-details'),
    path('admin/', AdminListAPIView.as_view(), name='admin-details'),
    path('utente/<int:pk>/', UtenteDetailAPIView.as_view()),
    path('utente/<int:pk>/update/', UtenteUpdateAPIView.as_view()),
    path('utente/<int:pk>/delete/', UtenteDestroyAPIView.as_view()),
     
]
