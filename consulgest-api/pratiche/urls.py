from django.urls import path
from . import views
from .views import HeaderStandardView, MappaCreateView, UploadFileView, MappaGetByIdView, ParseHeadersView, TestView
#from .viewsets import DossierViewSet
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register("upload", UploadFileView)
# urlpatterns = router.urls

urlpatterns = [
    path('pratiche/',views.DossierListCreateAPIView.as_view()),
    path('dettagliopratiche/<int:pk>/', views.DossierDetailAPIView.as_view()),
    path('updatepratiche/<int:pk>/update/', views.DossierUpdateAPIView.as_view()),
    path('cancellapratiche/<int:pk>/delete/', views.DossierDeleteAPIView.as_view()),
    path('uploadfilepratiche/', UploadFileView.as_view()),
    path('dettagliofilepratiche/<int:pk>',views.UploadedFileDetailView.as_view()),
    path('totaldossiernumber/', views.Dossiertotalnumber),
    path('getlistheaders/', HeaderStandardView.as_view()),
    path('mappa/', MappaCreateView.as_view()),
    path('mappa/<int:pk>/', MappaGetByIdView.as_view()),
    path('parseheaders/', ParseHeadersView.as_view()),
    path('test/', TestView.as_view()),
]
