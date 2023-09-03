from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Gateway(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('عنوان'))
    
    class Meta:
        verbose_name = _('درگاه پرداخت')
        verbose_name_plural = _('درگاه های پرداخت')


class Payment(models.Model):
    payment_status = ()

    user = models.ForeignKey(
        User, related_name='payments', on_delete=models.CASCADE, verbose_name=_('کاربر پرداخت کننده'))
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE, verbose_name=_('درگاه پرداخت'))
    price = models.PositiveBigIntegerField(default=0, verbose_name=_('قیمت'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('تاریخ بروزرسانی'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))

    class Meta:
        verbose_name = _('پرداخت')
        verbose_name_plural = _('پرداخت ها')