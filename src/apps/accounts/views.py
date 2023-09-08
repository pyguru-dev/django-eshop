import csv
import datetime
from django.forms.models import BaseModelForm

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView, LoginView as BaseLoginView
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from apps.accounts.forms import ChangePasswordForm, RegisterForm, LoginForm
from apps.payments.models import Payment
from utils.utils import account_activation_token
from .models import UserProfile, User


class AccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/dashboard.html"


class AccountSettingView(LoginRequiredMixin, generic.TemplateView):
    # model = User
    template_name = 'accounts/settings.html'
    # success_url = reverse_lazy('accounts')
    # fields = []

    # def get_object(self, queryset):
    #     return User.objects.get(pk=self.request.user.pk)

class AccountPaymentView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/payments.html'

class AccountOrderView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/shop_orders.html'


class AccountAddressView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/shop_addresses.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        current_site = get_current_site(self.request)
        mail_message = render_to_string('accounts/account_verification_mail.html', {
            'user': user,
            'domail': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })

        to_mail = form.cleaned_data.get('email')
        email = EmailMessage('subject', mail_message, to=to_mail)
        email.send()
        return HttpResponse('email sent')


class LoginView(BaseLoginView):
    # form_class = LoginForm
    # success_url = reverse_lazy('home_view')
    pass

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home_view')
                else:
                    return HttpResponse('account is not active')
            else: 
                return HttpResponse('credential is wrong')
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form':form})

def activate_account_mail(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_encode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('ok')
    else:
        return HttpResponse('link invalid')


class PasswordChangeView(BasePasswordChangeView):
    success_url = reverse_lazy('')


class PasswordChangeDoneView(generic.TemplateView):
    pass


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

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_view')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('login_view')
    else:
        return render(request, 'registration/login.html')


@login_required(login_url='login_view')
def user_logout(request):
    logout(request)
    return redirect('home_view')

@login_required(login_url='login_view')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        user = request.user
        if form.is_valid():
            cd = form.cleaned_data
            old_password= cd['old_password']
            password= cd['password']
            password_confirmation= cd['password_confirmation']
            if not user.check_password(old_password):
                return HttpResponse('رمز عبور فعلی شما درست نیست')
            elif password != password_confirmation:
                return HttpResponse('رمز عبور ها یکی نیستند')
            else:
                user.set_password(password)
                user.save()
                return HttpResponse('password changed')
        else: 
            form = ChangePasswordForm()
        return render(request, '', {'form':form})
                
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
    context = {'payments': payments}

    html = template.render(context)
    pisa.CreatePDF(html, dest=response)

    return response
