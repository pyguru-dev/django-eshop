from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'