from django.urls import path
from . import views

urlpatterns = [
    path('bolna/', views.bolna_webhook, name='bolna_webhook'),
]