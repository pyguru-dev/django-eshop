from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth, User
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import UserProfile

# User = get_user_model()


class AccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/dashboard.html"


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class LoginView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home_view')
    template_name = 'registration/login.html'


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exits():
                messages.info(request, 'email exists')
                return redirect('register_view')
            else:
                user = User.objects.create(email=email)
                user.save()

                login = auth.authenticate(email=email, password=password)
                auth.login(request, login)

                profile = UserProfile.objects.create(user=user)
                profile.save()

        else:
            messages.info(request, 'Password not match')
            return redirect('register_view')

    else:
        return render(request, 'registration/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home_view')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('login_view')
    else:
        return render(request, 'registration/login.html')


@login_required(login_url='login_view')
def logout(request):
    auth.logout(request)
    return redirect('home_view')
