from django.db import models

class Deputado(models.Model):

    nome = models.CharField(max_length=512)
    partido = models.CharField(max_length=50)
    estado = models.CharField(max_length=10)
    regiao = models.CharField(max_length=127)
    cargo = models.CharField(max_length=500)
    curriculo = models.TextField(max_length=40000)
    carreira = models.TextField(max_length=40000)
    biografia = models.TextField(max_length=40000)
    papel = models.CharField(max_length=40000)

