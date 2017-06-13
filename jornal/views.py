from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):    
    return render(request, 'index.html', { 'active': 'index' })

def register(request):
    form = UserForm(request.POST or None)    
    if request.method == 'POST':
        if form.is_valid():                
            username = form.cleaned_data['username']                
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            horario = form.cleaned_data['horario']
            telephone = form.cleaned_data['telephone']
            
            user = Usuario.objects.create_user(username=username, email=email, password=password)
            user.horario = horario
            user.telephone = telephone
            user.save()
            user = authenticate(username=username, password=password)                
            if user is not None:
                if user.is_active:
                    return render(request, 'index.html', { 'active': 'index' })
            else:
                return render(request, 'index.html', { 'active': 'index', "form": form })
        else:
            return render(request, 'register.html', { 'active': 'register', 'form': form, 'error_message': 'Dados inválidos!' })
    else:
        return render(request, 'register.html', { 'active': 'register', "form": form })

    return render(request, 'register.html', { 'active': 'register', 'form': form })

def register_worktime(request):
    form = HorarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            horaInicio = form.cleaned_data['horaInicio']
            horaFim = form.cleaned_data['horaFim']

            horario = Horario()
            horario.horaInicio = horaInicio
            horario.horaFim = horaFim
            horario.save()

            if horario is not None:                
                return render(request, 'index.html', { 'active': 'index' })
            else:
                return render(request, 'register_worktime.html', { 'active': 'register_worktime', "form": form })    
    else:
        return render(request, 'register_worktime.html', { 'active': 'register_worktime', "form": form })

    return render(request, 'register_worktime.html', { 'active': 'register_worktime', 'form': form })

def user_list(request):
    users = Usuario.objects.all()
    return render(request, 'user_list.html', { 'active': 'user_list', 'users': users})