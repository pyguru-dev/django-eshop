from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
# from apps.accounts.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Gateway(BaseModel):
    title = models.CharField(max_length=50, verbose_name=_('عنوان'))
    # logo
    class Meta:
        verbose_name = _('درگاه پرداخت')
        verbose_name_plural = _('درگاه های پرداخت')


class Payment(BaseModel):
    payment_status = ()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('کاربر پرداخت کننده'))
    payment_code = models.CharField(unique=True, verbose_name=_('شناسه پرداخت'), max_length=100)
    # order = 'order_id'
    reference_id = models.CharField(unique=True, verbose_name=_('کد مرجع'), max_length=100)
    # payment_for = 'wallet_charge, online buy'
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE, verbose_name=_('درگاه پرداخت'))
    price = models.PositiveBigIntegerField(default=0, verbose_name=_('قیمت'))
    # payment_method = 'online-wallet'
    # status
    payment_success_at = models.DateTimeField(verbose_name=_('تاریخ موفقیت پرداخت'), null=True,blank=True)
    payment_failed_at = models.DateTimeField(verbose_name=_('تاریخ شکست پرداخت'), null=True,blank=True)    

    class Meta:
        verbose_name = _('پرداخت')
        verbose_name_plural = _('پرداخت ها')
        
class Factor(BaseModel):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name=_("پرداخت مرتبط"))
    file = models.FileField(verbose_name=_('فایل فاکتور'))    

class Bank(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('عنوان'), unique=True)
    loo = models.CharField(max_length=255, verbose_name=_('لوگو'), unique=True, blank=True,null=True)
    

class Payout(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("کاربر"))

    # user_id , bank_id, amount,description,approved_at


