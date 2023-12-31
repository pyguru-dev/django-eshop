from django.urls import path
from .views import (UserRegisterView, UserLoginView, AccountView, AccountSettingView, AccountPaymentView,
                    AccountOrderView, AccountAddressView,
                    PasswordChangeView, PasswordChangeDoneView, user_logout)


# app_name='apps.accounts'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register_view'),
    path('login/', UserLoginView.as_view(), name='login_view'),
    path('logout/', user_logout, name='logout'),


    path('', AccountView.as_view(), name='account_index'),
    path('setting/', AccountSettingView.as_view(), name='account_setting'),
    path('payments/', AccountPaymentView.as_view(), name='account_payments'),
    path('orders/', AccountOrderView.as_view(), name='account_orders'),
    path('addresses/', AccountAddressView.as_view(), name='account_addresses'),
    
    path('password_change/', PasswordChangeView.as_view(),
         name='password_change_view'),
    path('password_change/done', PasswordChangeDoneView.as_view(),
         name='password_change_done_view'),



]
