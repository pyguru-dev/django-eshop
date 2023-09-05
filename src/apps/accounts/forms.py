# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Address, User
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User
#         # fields = UserCreationForm.Meta.fields + ('mobile',)
#         fields = UserCreationForm.Meta.fields


# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = User
#         fields = UserChangeForm.Meta.fields

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AccountSettingForm():
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(AccountSettingForm, self).__init__(*args, **kwargs)
        self.fields['birthday'] = JalaliDateField(
            label=_('تاریخ تولد'), widget=AdminJalaliDateWidget)


# class AddressForm(forms.ModelForm):

#     class Meta:
#         model = Address
#         fields = ("",)
