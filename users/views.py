from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active == True:
            login(request, user)
            return redirect('users:index')
    return render(request, 'login.html')

def fazer_logout(request):
    
    logout(request)

    return redirect('../')

@login_required(login_url='/')
def mostraUsers(request):
    usuariosQuerySet = User.objects.all()
    context = {'usuariosQuerySet': usuariosQuerySet}
    return render(request, 'index.html', context)

@login_required(login_url='/')
def criaUsers(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = User.objects.create_user(username=f'{username}', password=f'{password}', last_name=f'{last_name}', first_name=f'{first_name}', email=f'{email}')
        user.save()
        return redirect('users:index')
    return render(request, 'createUser.html')

@login_required
def editaUser(request, id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user.username = username
        user.password = password
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('users:index')
    context = {'user': user}
    return render(request, 'editUser.html', context)

@login_required
def deletaUser(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('users:index')
