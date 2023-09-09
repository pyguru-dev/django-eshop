# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import Address, User
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = User
#         fields = UserChangeForm.Meta.fields

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        # fields = UserCreationForm.Meta.fields + ('mobile',) 
        fields = ['username', 'email', 'password1', 'password2']

# class LoginForm(forms.Form): 
       
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.TextInput()
    password = forms.TextInput()

class ChangePasswordForm(forms.Form):
    old_password = forms.PasswordInput()
    password = forms.PasswordInput()
    password_confirmation = forms.PasswordInput()

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('رمز عبور باید بیشتر از 8 کاراکتر باشد')
        else:
            return password
        
    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data['password_confirmation']
        
        if password != password_confirmation:
            raise forms.ValidationError('رمز عبور ها یکی نیستند')
        return password_confirmation
    


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
