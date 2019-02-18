from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import Registrationform, editUser
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'accounts/home.html')

def getlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print(name, password)
        auth=authenticate(request, username=name, password=password)
        if auth is not None:
            login(request, auth)
            return redirect(reverse('accounts:index'))
        else:
            return redirect(reverse('accounts:login'))
    return render(request, 'accounts/login.html')

def getlogout(request):
    logout(request)
    return redirect(reverse('accounts:index'))


def getregistration(request):
    if request.method == 'POST':
        form=Registrationform(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            form.save()
            print('registration done!')
            return redirect(reverse('accounts:login'))
    form = Registrationform()
    return render(request, 'accounts/registration.html', {'form':form})


def getprofile(request, p_id=None):
    if request.user.is_authenticated:
        if p_id:
            user = get_object_or_404(User, pk=p_id)
        else:
            user = request.user

        return render(request, 'accounts/profile.html', {'user': user})
    return redirect(reverse('accounts:login'))

def geteditprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = editUser(request.POST or None, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:profile'))
        return render(request, 'accounts/edit_profile.html', {'form': editUser(instance=request.user)})
    return redirect(reverse('accounts:login'))


def getchangepassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(data=request.POST or None, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect(reverse('accounts:profile'))
            return redirect(reverse('accounts:change_password'))
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/change_password.html', {'form': form})
