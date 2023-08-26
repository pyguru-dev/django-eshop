from django.views.generic import TemplateView, CreateView
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'pages/index.html'
    
    
class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = "pages/contact.html"
    
    
class AboutView(TemplateView):
    template_name = "pages/about.html"