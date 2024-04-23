from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Nota

# Create your views here.

def home(request):
    notas = {
        'notas':Nota.objects.all()
    }
    return render(request,'notas/index.html', notas)

def criar_nota(request):
    nova_nota = Nota()
    #nova_nota.topico = request.POST.get('topico')
    nova_nota.titulo_db = request.POST.get( 'titulo_form' )
    nova_nota.conteudo_db = request.POST.get( 'conteudo_form' )
    nova_nota.save()
    #Exibir notas
    notas = {
        'notas': Nota.objects.all()
    }
    #Retornar notas
    return render(request,'notas/notas.html', notas)

def lista_notas(request):
    notas = {
        'notas':Nota.objects.all()
    }
    return render(request, 'notas/notas.html', notas)

def deletar_nota(request, id):
    nota = Nota.objects.filter(id_nota=id)
    nota.delete()
    return render(request,'notas/notas.html')