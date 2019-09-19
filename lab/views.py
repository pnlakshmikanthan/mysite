from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm
from django.contrib import messages
from .models import Person,Doctor,Test


def index(request):
    if request.method == 'POST':
        test=request.POST.get('test')
        tests1=Test.objects.filter(test_name=test)
        context={'tests1':tests1}
        return render(request,'index.html',context)   
    else:
        print("Some output")
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



        