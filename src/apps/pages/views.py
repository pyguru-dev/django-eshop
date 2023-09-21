from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.views.decorators.cache import cache_page
from django.contrib import messages
from .forms import ContactForm
from .models import ContactSubject, Faq, FaqGroup
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
    success_url = reverse_lazy('contact_view')  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = ContactSubject.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)
    
# def ContactUsCreate(request):
#     if  request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact = Contact.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 mobile=form.cleaned_data['mobile'],
#                 subject=form.cleaned_data['subject'],
#                 message=form.cleaned_data['message'],
#             )
#             contact.save()
            # messages.success(request, 'contact us stored ')
            #   message_to_admin = "name:{0}\nmobile:{1}\nemail:{2}\nsubject:{3}\nmessage:{4}".format(name,mobile,email,subject,message)  
            #   send_mail(subject, message, 'sender@gmail.com', ['admin@gmail.com'], fail_silently=False)
               
#             return redirect('contact_view')
#         else:
#             context = {'form' : form}
#             return render(request, 'pages/contact.html', context)
        
        
class AboutView(TemplateView):
    template_name = "pages/about.html"
    
    
class FaqsView(ListView):
    model = FaqGroup
    template_name = 'pages/faqs.html'
    context_object_name = 'faqGroups'
    
    