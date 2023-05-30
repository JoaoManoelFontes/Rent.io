from django.shortcuts import render

# Create your views here.

# []home -> listagem de imóveis; acesso à página do usuário; filtragem de imóveis
# []customer -> página do usuário; listagem de imóveis do usuário; criação de imóveis


def home(request):
    return render(request, 'core/index.html')
