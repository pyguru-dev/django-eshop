from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, CreateView
from django.views.decorators.cache import cache_page
from .forms import ContactForm
from apps.blog.models import Post

# @cache_page(60 * 15)
class HomePageView(TemplateView):
    template_name = 'pages/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_posts"] = Post.objects.all()
        return context
    
    
class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = "pages/contact.html"
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class AboutView(TemplateView):
    template_name = "pages/about.html"