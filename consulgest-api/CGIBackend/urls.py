"""CGIBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pratiche.urls')),
    path('api/', include('userapp.urls', namespace='api')),
    path('api/', include('headerTemplate.urls')),
    path('api/', include('dossier.urls')),
    path('api/', include('lotto.urls')),
    path('api/', include('storicoDati.urls')),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('login/', LoginView.as_view(),name='account_login'),
    path('logout/', LogoutView.as_view(),name='account_logout'),
    path('verify-email/',VerifyEmailView.as_view(), name='rest_verify_email'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),name='account_confirm_email'),
]
