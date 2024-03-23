
from django.urls import path
from app_cadastro_usuario import views

urlpatterns = [
    #rota, view responsável, nome de referência
    
    #rota principal - homepage
    path('',views.home,name='home'), 
    
    #blocodenotas.com/notas
    path('notas/', views.criar_nota,  name="listagem_notas"),
    
    path('lista_notas/', views.lista_notas,  name='lista_notas'),
    
]