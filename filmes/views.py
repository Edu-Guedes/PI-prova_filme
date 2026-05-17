from django.shortcuts import render

# Create your views here.
def lista_de_filmes(request):
    return render(request, 'filmes/lista_de_filmes.html')

def detalhes_do_filme(request):
    return render(request, 'filmes/detalhes_do_filme.html')