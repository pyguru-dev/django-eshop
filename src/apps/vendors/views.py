from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Vendor

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'
    context_object_name = 'vendors'
        

class VendorDetailView(TemplateView):
    pass