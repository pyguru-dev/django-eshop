# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

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
