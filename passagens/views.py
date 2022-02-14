from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    # É possível passar conteúdo à view por um 'contexto', segue um exemplo abaixo.
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        contexto = {'form':form}
        return render(request, 'resultado.html', contexto)