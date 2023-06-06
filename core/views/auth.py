from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# []home -> listagem de imóveis; acesso à página do usuário; filtragem de imóveis
# []customer -> página do usuário; listagem de imóveis do usuário; criação de imóveis


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'core/login.html')

    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if not user:
        return render(request, 'core/login.html', {'error': 'Usuário ou senha inválidos'})

    login(request, user)
    return redirect('home')


def sign_out(request):
    logout(request)
    return redirect('home')


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'core/sign_up.html')
