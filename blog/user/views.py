from django.shortcuts import render, redirect
from .forms import ResgisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.


def UserRegister(request):
    form = ResgisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        login(request, new_user)
        messages.success(request, 'alindi')
        return redirect('index')
    context = {'form': form}
    return render(request, 'register.html', context=context)

    '''
    if request.method == 'POST':
        form = ResgisterForm(request.POST)
        if form.is_valid():
            new_user = User(username=form.cleaned_data.get('username'))
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            login(request, new_user)
            messages.success(request, 'alindi')
            return redirect('index')
        context = {'form': form}
        return render(request, 'register.html', context=context)
    else:
        form = ResgisterForm()
        context = {'form': form}
        return render(request, 'register.html', context=context)
    '''

def UserLogin(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', context=context)
    return render(request, 'login.html', context=context)

# No backend authenticated the credentials


def UserLogout(request):
    logout(request)
    return redirect("index")