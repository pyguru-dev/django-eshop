# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from .models import User

User = get_user_model()

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User
#         # fields = UserCreationForm.Meta.fields + ('mobile',)        
#         fields = UserCreationForm.Meta.fields        


# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = User
#         fields = UserChangeForm.Meta.fields


class AccountSettingForm():
    class Meta:
        model = User
        
    def __init__(self, *args, **kwargs):
        super(AccountSettingForm, self).__init__(*args, **kwargs)
        self.fields['birthday']=JalaliDateField(label=_('تاریخ تولد'), widget=AdminJalaliDateWidget)