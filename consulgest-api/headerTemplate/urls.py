from django.urls import path
from . import views

urlpatterns = [
    path('template/', views.TemplateView.as_view(), name='template-list'),
    path('template/<int:pk>/', views.TemplateImportDetail.as_view(), name='template-detail'),
    path('template/<int:idUser>/', views.TemplateView.as_view(), name='template-list'),
    path('defaultcolumns/', views.TemplateImportList.as_view(), name='default-columns'),
]
