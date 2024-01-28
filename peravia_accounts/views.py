from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import RegisterForm, LoginForm
from django.contrib import messages


# ----------------------------------------------------------
def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            if not login_form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password')
                return redirect(reverse('accounts:login_user'))
    form = LoginForm()
    return render(
        request=request,
        template_name='accounts/LoginPage.html',
        context={'login_form': form,
                 'page_name': 'Login',
                 'page_title': 'Account - Login',
                 'title': 'Peravia | Login'})


# ----------------------------------------------------------
def RegisterUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            phone_number = register_form.cleaned_data.get('phone_number')
            CustomUser.objects.create_user(email=email, phone_number=phone_number, password=password)
            messages.success(request, 'Registration successful.')
            return redirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(
        request=request,
        template_name='accounts/RegisterPage.html',
        context={'register_form': form,
                 'page_name': 'Register',
                 'page_title': 'Account - Register',
                 'title': 'Peravia | Register'})


# ----------------------------------------------------------
@login_required(login_url=reverse_lazy('accounts:login_user'))
def LogoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('/')
