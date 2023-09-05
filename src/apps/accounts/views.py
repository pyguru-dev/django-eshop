import csv
import datetime
from typing import Any, Optional
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth, User
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model

from apps.payments.models import Payment
from .models import UserProfile

# User = get_user_model()


class AccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/dashboard.html"

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'accounts/profile_update.html'
    # success_url = reverse_lazy('accounts')
    fields = []

    def get_object(self, queryset):
        return User.objects.get(pk = self.request.user.pk)

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


def export_payments_to_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['content-Disposition'] = 'attachment;filename=payments' + \
        str(datetime.datetime.now)+'.csv'
    csvWriter = csv.writer(response)
    csvWriter.writerow(['id', 'price'])
    payments = Payment.objects.all()
    for payment in payments:
        csvWriter.writerow([payment.id, payment.price])

    return response


def export_payments_to_excel(request):
    response = HttpResponse(content_type="application/mx-excel")
    response['content-Disposition'] = 'attachment;filename=payments' + \
        str(datetime.datetime.now)+'.xls'

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('payments')
    columns = ['id', 'price']
    rownumbers = 0

    for col in range(len(columns)):
        worksheet.write(rownumbers, col, columns[col])

    payments = Payment.objects.all().values_list("id", "price")
    for payment in payments:
        rownumbers += 1
        for col in range(len(payment)):
            worksheet.write(rownumbers, col, payment[col])

    workbook.save(response)
    return response


def export_payments_to_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response['content-Disposition'] = 'attachment;filename=payments' + \
        str(datetime.datetime.now)+'.pdf'
        
    template_path = 'accounts/templates/payment_pdf.html'
    template = get_template(template_path)

    payments = Payment.objects.all()
    context={'payments':payments}
    
    html = template.render(context)
    pisa.CreatePDF(html, dest=response)
    
    return response
    