from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse

from crud.forms.user_form import RegForm, LoginForm


def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            pwd = request.POST.get('pwd')
            r_pwd = request.POST.get('r_pwd')
            email = request.POST.get('email')

            User.objects.create_user(
                username=name,
                password=pwd,
                email=email,
            )

            return redirect('/')
        errors = form.errors.get('__all__')

        context = {
            'form': form,
            'errors': errors
        }

        return render(request, 'reg.html', context=context)
    form = RegForm()
    context = {
        'form': form
    }

    return render(request, 'reg.html', context=context)


def login(request):
    if request.user.is_authenticated:  # 如果已经登录，则直接返回首页
        return redirect(reverse('crud:book'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = request.POST.get('name')
        pwd = request.POST.get('pwd')

        user = auth.authenticate(username=user, password=pwd)

        if user:
            auth.login(request, user)
            return redirect('/')

        errors = form.errors.get('__all__')

        context = {
            'form': form,
            'errors': errors
        }
        return render(request, 'login.html', context=context)

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context=context)


def logout(request):
    auth.logout(request)

    return redirect(reverse('crud:login'))
