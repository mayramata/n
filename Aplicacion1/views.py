
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def logins(request): #tiene que ir el nombre de la a´ñicacion aqui para pasarla como variable en url por medio de view.sewingcourse
    return render(request, 'pages/menu.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('menu')
    else:
        form = UserRegisterForm()

    return render(request, 'pages/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'pages/profile.html')

