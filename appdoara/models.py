from django.db import models

class Melhores(models.Model):
  personagem = models.CharField(max_length = 50)
  ator = models.TextField()
  temporada = models.DateField()

class Mortes(models.Model):
  nome = models.CharField(max_length = 50)
  personagem = models.TextField()
  motivoMorte = models.TextField()
  data = models.DateField()
  