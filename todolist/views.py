from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from task.models import Task, User
from todolist.forms import UserForm
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks,
    }
    return render(request, 'home.html', context)

    
def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name= first_name, last_name= last_name, username= username, email= email, password= password)
            user.save()
            messages.success(request,'Your account has been registered successfully')

            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'registerUser.html', context)


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email=email)
            pwd_valid = check_password(password, user.password)

            context = {
                'name' : user.first_name,
            }
            return redirect(request, 'home', context)
        else:
            print(form.errors)
    else:
       form = UserForm()
    frm = {     
        'form': form,
        }
       
    return render(request, 'login.html', frm)
