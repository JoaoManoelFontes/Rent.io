from django.urls import path

from .views.manager import home

urlpatterns = [
    path('', home, name='customer_home'),
]
