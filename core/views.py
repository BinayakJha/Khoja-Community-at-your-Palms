import email
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from requests import request
from .forms import *
from .models import *
from django.core.mail import EmailMessage, send_mail
# Create your views here.
class Tabs:
    def index(self):
        model = Eca.objects.all()
        # show the model by happening date and created_at
        model = model.order_by('-happening_date', '-created_at').reverse()
        context = {'model': model}
        return render(self, 'index.html', context)

    def add_eca(self):
        form = EcaForm()
        context = {'form': form}
        return render(self, 'forms.html', context)
    
    def eca_apply(self, name):
        model = Eca.objects.get(name=name)
        form = EcaForm()
        context = {'form': form,
                    'model': model}
        return render(self, 'apply_form.html', context)
    
    def login(self):
        return render(self, 'login.html')
    def signup(self):
        return render(self, 'signup.html')
    

class forms:
    def add_eca_submit(request):
        if request.method == 'POST':
            form = EcaForm(request.POST,  request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                print(form.errors)
                return render(request, 'forms.html', {'form': form})
        else:
            return render(request, 'forms.html', {'form': form})

class Authentication:
    def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password')
                return redirect('login')
        else:
            return render(request, 'login.html')
    
    def signup(self):
        if self.method != 'POST':
            return redirect('register')
        username = self.POST['email']
        email = self.POST['username']
        password = self.POST['pass']
        confirm_password = self.POST['new_pass']
        first_name = self.POST['name']
        user_type = self.POST['user_type']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(self, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(self, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=user_type)
                user.save()
                messages.info(self, 'User created')
                return redirect('login')
        else:
            messages.info(self, 'Password not matching')
            return redirect('signup')
    def logout(self):
        logout(self)
        return redirect('login')
    
    def eca_apply_submit(self):
        if self.method == 'POST':
            form = EcaApplyForm(self.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                print(form.errors)
                return render(self, 'apply_form.html', {'form': form})
        else:
            return render(self, 'apply_form.html', {'form': form})

class View:
    def view_eca(self, name):
        model = Eca.objects.get(name=name)
        context = {'model': model}
        return render(self, 'view_eca.html', context)
    
    def edit_eca(self, name):
        model = Eca.objects.get(name=name)
        form = EcaForm(instance=model)
        context = {'form': form,
                    'model': model}
        return render(self, 'edit_eca.html', context)
    def edit_eca_submit(self, name):
        model = Eca.objects.get(name=name)
        form = EcaForm(self.POST, self.FILES, instance=model)
       
        if form.is_valid():
            
            form.save()
            return redirect('index')
        else:
            print(form.errors)
            return render(self, 'edit_eca.html', {'form': form})
    