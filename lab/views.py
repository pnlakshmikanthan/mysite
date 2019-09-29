from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .models import Person,Doctor,Test


def index(request):
        tests=Test.objects.all
        context={'tests':tests}
        return render(request,'index.html',context)  

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})



        