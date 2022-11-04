from django.db import models

class Animal(models.Model):
    
    nome_animal = models.CharField(max_length=30)
    predador = models.CharField(max_length=5)
    venenoso = models.CharField(max_length=5)
    domestico = models.CharField(max_length=5)


