from rest_framework import serializers
from legislatura56 import models

# class PessoaSerializer(serializers.ModelSerializer):

#     class Meta:

#         db_table = ''
#         managed = True
#         verbose_name = 'ModelPessoa'
#         verbose_name_plural = 'ModelPessoas'
#         model = models.Pessoa
#         fields = '__all__'

class DeputadoSerializer(serializers.ModelSerializer):

    class Meta:

        db_table = ''
        managed = True
        verbose_name = 'ModelDeputado'
        verbose_name_plural = 'ModelDeputados'
        model = models.Deputado
        fields = '__all__'

        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# class StudentSerializer(serializers.ModelSerializer):

#     class Meta:

#         db_table = ''
#         managed = True
#         verbose_name = 'ModelStudent'
#         verbose_name_plural = 'ModelStudents'
#         model = models.Student
#         fields = '__all__'