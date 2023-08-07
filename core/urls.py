from django.urls import path
from .views.home import home
from .views.auth import sign_in, sign_out, sign_up

urlpatterns = [
    path('', home, name='home'),
    path('login/', sign_in, name='sign_in'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', sign_out, name='sign_out'),
]
