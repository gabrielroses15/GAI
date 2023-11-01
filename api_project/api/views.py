from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Pergunta
from .serializers import PerguntaSerializer

class PerguntaListView(generics.ListCreateAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PerguntaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer
from rest_framework import status
from rest_framework.response import Response

class PerguntaListView(generics.ListCreateAPIView):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

    def create(self, request, *args, **kwargs):
        pergunta = request.data.get('pergunta', None)

        if pergunta is not None and pergunta != "":
            import sys
            sys.path.append('C:\\Users\\gabriel.rosa\\Desktop\\GAI')
            import brain
            resposta = brain.APIrequest(pergunta)
            print("PERGUTA: {} RESPOSTA: {}".format(pergunta.lower(), resposta.lower()))
            if resposta.lower() == pergunta.lower().replace("?", "").replace(",", "").replace(".", "").replace("!", ""):
                resposta = "Desculpe, não posso te ajudar quanto a isto."

            # Cria um novo objeto Pergunta
            nova_pergunta = Pergunta(pergunta=pergunta, resposta=resposta)
            nova_pergunta.save()

            # Serializa e retorna a nova pergunta com a resposta gerada
            serializer = PerguntaSerializer(nova_pergunta)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'A pergunta não foi fornecida.'}, status=status.HTTP_400_BAD_REQUEST)
