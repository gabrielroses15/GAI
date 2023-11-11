from django.db import models

# Create your models here.
from django.db import models

class Pergunta(models.Model):
    pergunta = models.CharField(max_length=255)
    resposta = models.CharField(max_length=255)

    def __str__(self):
        return self.pergunta
