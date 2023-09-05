from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
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
    fields = "__all__"
    template_name = "pages/contact.html"
    # success_url = reverse_lazy('contact_view')
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
# def ContactUsCreate(request):
#     if  request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact = Contact.objects.create(
#                 name=form.cleaned_data['name']
#             )
#             contact.save()
#             return redirect('contact_view')
#         else:
#             context = {'form' : form}
#             return render(request, 'pages/contact.html', context)
        
        
class AboutView(TemplateView):
    template_name = "pages/about.html"