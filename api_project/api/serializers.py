from rest_framework import serializers
from .models import Pergunta

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ['pergunta', 'resposta']
