from django.views import generic
from .forms import ContactForm

class ContactCreateView(generic.CreateView):
    form_class = ContactForm
    template_name = "pages/contact.html"
    