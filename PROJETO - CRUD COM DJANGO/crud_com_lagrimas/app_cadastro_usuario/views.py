from django.shortcuts import render
from .models import Nota

# Create your views here.

def home(request):
    return render(request,'notas/index.html')

def criar_nota(request):
    nova_nota = Nota()
    nova_nota.titulo = request.POST.get( 'titulo' )
    nova_nota.conteudo = request.POST.get( 'conteudo' )
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