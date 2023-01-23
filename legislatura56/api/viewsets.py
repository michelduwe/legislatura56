from rest_framework import viewsets
from legislatura56.api import serializers
from legislatura56 import models

# class PessoaViewset(viewsets.ModelViewSet):

#     serializer_class = serializers.PessoaSerializer
#     queryset = models.Pessoa.objects.all()

class DeputadoViewset(viewsets.ModelViewSet):

    serializer_class = serializers.DeputadoSerializer
    queryset = models.Deputado.objects.all()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# class StudentViewset(viewsets.ModelViewSet):

#     serializer_class = serializers.StudentSerializer
#     queryset = models.Student.objects.all()