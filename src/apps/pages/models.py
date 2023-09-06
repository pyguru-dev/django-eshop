from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class ContactSubject(BaseModel):
    title = models.CharField(max_length=250)


class ContactModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('نام'))
    mobile = models.CharField(max_length=12, verbose_name=_(
        'موبایل'), null=True, blank=True)
    email = models.CharField(max_length=250, verbose_name=_(
        'ایمیل'), null=True, blank=True)
    message = models.TextField(verbose_name=_('پیام'))

    def __str__(self) -> str:
        return self.name + ' : ' + self.mobile


class FaqGroup(BaseModel):
    title = models.CharField(max_length=100, unique=True)


class Faq(BaseModel):
    question = models.CharField(max_length=255, unique=True)
    answer = models.CharField(max_length=255, unique=True)
