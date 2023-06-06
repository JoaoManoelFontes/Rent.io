from django.urls import path
from .views.home import home
from .views.auth import sign_in, sign_out

urlpatterns = [
    path('', home, name='home'),
    path('login/', sign_in, name='sign_in'),
    path('logout/', sign_out, name='sign_out'),
]
