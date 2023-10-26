from django.db import models

# Create your models here.
from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    completa = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
