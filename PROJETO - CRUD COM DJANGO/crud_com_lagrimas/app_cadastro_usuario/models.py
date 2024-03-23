from django.db import models

# Create your models here.


class Nota(models.Model):
    id_nota = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=200)
    conteudo = models.TextField(max_length=5000)