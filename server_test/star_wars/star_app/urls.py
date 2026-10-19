from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('facciones/', views.listadoDeFacciones, name='listadoDeFacciones'),
    path('facciones/<int:faccion_id>/', views.detalleFaccion, name='detalleFaccion')
]