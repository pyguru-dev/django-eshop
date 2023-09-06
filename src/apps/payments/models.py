from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Gateway(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('عنوان'))
    # logo
    class Meta:
        verbose_name = _('درگاه پرداخت')
        verbose_name_plural = _('درگاه های پرداخت')


class Payment(models.Model):
    payment_status = ()

    user = models.ForeignKey(
        User, related_name='payments', on_delete=models.CASCADE, verbose_name=_('کاربر پرداخت کننده'))
    payment_code = ''
    order = 'order_id'
    reference_id = ''
    payment_for = 'wallet_charge, online buy'
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE, verbose_name=_('درگاه پرداخت'))
    price = models.PositiveBigIntegerField(default=0, verbose_name=_('قیمت'))
    payment_method = 'online-wallet'
    payment_verified_at = ''
    payment_failed_at = ''
    

    class Meta:
        verbose_name = _('پرداخت')
        verbose_name_plural = _('پرداخت ها')
        
class Factor(models.Model):
    pass
    # payment_id, file

class Bank(models.Model):
    pass
    # title , logo

class Payout(models.Model):
    pass
    # user_id , bank_id, amount,description,approved_at


