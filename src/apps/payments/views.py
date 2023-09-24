import logging
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException

from .models import Payment
from apps.shop.models import Order, OrderItem, Cart


def go_to_gateway_view(request):

    # get cart amount from cart table
    amount = 1000

    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        # bank = factory.auto_create()
        bank = factory.create(
            bank_models.BankType.ZARINPAL).set_request(request)
        bank.set_amount(amount)
        bank.set_client_callback_url(reverse('callback-gateway'))
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        context = bank.get_gateway()
        return render(request, 'redirect_to_bank.html', context=context)
    except AZBankGatewaysException as e:
        logging.critical(e)
        return render(request, 'redirect_to_bank.html')


def callback_gateway_view(request):
    user = request.user

    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    payment = Payment.objects.create(
        amount=bank_record.amount,
        user=user,
        tracking_code=bank_record.tracking_code,
    )

    if bank_record.is_success:
        order = Order.objects.create(
            user=user,
            payment=payment,
            total_amount=1000,
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
            )

        # clear cart items

        return HttpResponse("پرداخت با موفقیت انجام شد.")

    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")
