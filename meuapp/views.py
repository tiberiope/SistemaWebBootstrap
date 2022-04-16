from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.

def index(request):
    features = Feature.objects.all()

    return render(request, 'index.html', {'features': features})

def registro(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if senha == senha2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail já cadastrado!')
                return redirect('registro')
            elif User.objects.filter(username=usuario).exists():
                messages.info(request, 'Usuário já cadastrado!')
                return redirect('registro')
            else:
                user = User.objects.create_user(username=usuario, email=email, password=senha)
                user.save();
                
                return redirect('login')
        else:
            messages.info(request, 'Senhas não são igual!')
            return redirect('registro')
    else:
        return render(request, 'registro.html')

def counter(request):
    posts = [1, 2, 3, 4, 5, 'ta', 'te', 'ti']
    return render(request, 'counter.html', {'posts': posts})

def login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        user = auth.authenticate(username=usuario, password=senha)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credenciais inválidas!')
            return redirect('login')
        
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
