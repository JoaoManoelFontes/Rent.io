from django.shortcuts import redirect, render
from ..models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# []home -> listagem de imóveis; acesso à página do usuário; filtragem de imóveis
# []customer -> página do usuário; listagem de imóveis do usuário; criação de imóveis


def sign_in(request):
    '''customer login view '''
    if request.method == 'GET':
        return render(request, 'core/login.html', {
            'title': 'Login',
        })

    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if not user:
        return render(request, 'core/login.html', {
            'title': 'Login',
            'error': 'Usuário ou senha inválidos'
        })

    login(request, user)
    return redirect('home')


def sign_out(request):
    '''customer logout view '''
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


def sign_up(request):
    '''customer sign up view '''
    if request.method == 'GET':
        return render(request, 'core/sign_up.html', {
            'title': 'Sign Up',
        })

    try:
        user = Customer.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            birth_date=request.POST['birth_date'],
            phone_number=request.POST['phone'],
            full_name=request.POST['full_name'],
        )
        user.save()

        login(request, user)
        return redirect('home')
    except Exception as e:
        return render(request, 'core/sign_up.html', {
            'title': 'Sign Up',
            'error': e
        })


@login_required(login_url='/login')
def edit_profile(request):
    '''customer edit profile view '''
    if request.method == 'GET':
        return render(request, 'core/edit_profile.html', {
            'title': 'Edit Profile',
        })

    try:
        user = request.user
        user.email = request.POST.get('email') if request.POST.get('email') else user.email
        user.birth_date = request.POST.get('birth_date') if request.POST.get('birth_date') else user.birth_date
        user.phone_number = request.POST.get('phone') if request.POST.get('phone') else user.phone_number
        user.full_name = request.POST.get('full_name') if request.POST.get('full_name') else user.full_name
        user.save()

        return redirect('home')
    except Exception as e:
        return render(request, 'core/edit_profile.html', {
            'title': 'Edit Profile',
            'error': e
        })
