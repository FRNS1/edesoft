from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', user_login, name='login'),
    path('index/', mostraUsers, name='index'),
    path('logout/', fazer_logout, name='fazer_logout'),
    path('newUser/', criaUsers, name='criaUsers'),
    path('editaUser/<int:id>', editaUser, name='editaUser'),
    path('deletaUser/<int:id>', deletaUser, name='deletaUser'),
]