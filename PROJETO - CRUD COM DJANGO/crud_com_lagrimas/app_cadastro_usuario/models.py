from django.db import models
from django import forms


# Create your models here.


class Nota(models.Model):
    
    #TOPICO_CHOICE =( ('outros', 'Outros'),('trabalho' , 'Trabalho'),('estudos', 'Estudos'),('lembretes', 'Lembretes'), )
    
    id_nota = models.AutoField(primary_key=True)
    #topico = models.TextField(max_length=1, choices= TOPICO_CHOICE, default=1)
    titulo_db = models.TextField(max_length=200)
    conteudo_db = models.TextField(max_length=5000)
