from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='Index'),
    path('Actividades', views.actividades, name='Actividades'),
    path('Contacto', views.contacto, name='Contacto'),
    path('Horarios', views.horarios, name='Horarios'),
    path('Registro', views.registro_persona, name='Registro'),
    path('registroFormulario', views.registro, name='registroFormulario'),
    path('buscarpersona', views.buscarpersona, name='Busquedadni'),
    path('buscar/', views.buscar),
]


