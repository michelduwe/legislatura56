"""restdjango URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from legislatura56.api.viewsets import DeputadoViewset
from legislatura56.views import ImportarDados, display, Home, ProcuraDeputado, ListaDeputados

rota = routers.DefaultRouter()
# rota.register(r'pessoa', PessoaViewset, basename='pessoa')
rota.register(r'deputado', DeputadoViewset, basename='deputado')
# rota.register(r'student', StudentViewset, basename='Estudante')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apidocs/', include(rota.urls)),
    path('importar/', ImportarDados.as_view(), name="importar"),
    path('dep/', display, name='display'),
    path('', Home.as_view(), name="home"),
    path('resultados/', ProcuraDeputado.as_view(), name="resultados"),
    path('lista_deputados/', ListaDeputados.as_view(), name="lista_deputados"),
    path('deputado', ListaDeputados.as_view(), name="deputado")
]
