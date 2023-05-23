from django.urls import path
from . import views

urlpatterns = [
    path('batch/', views.LottoDetailsView.as_view(), name='lotto-list'),
    path('batchByID/<int:pk>/', views.LottoByIDView.as_view(), name='lotto-id'),
    path('batchUser/', views.LottoByIDUserView.as_view(), name='lotto-by-id'),
   ]
