from django.db import models
from asgiref.sync import sync_to_async
from django.core.mail import send_mail
import time
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import Http404
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from functools import wraps
# from six import text_type

from . import jalali


def jalali_converter(time):
    jmonths = []
    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    result = "{} {} {}، ساعت: {}:{}".format(
        time_to_tuple[2],
        time_to_tuple[1],
        time_to_tuple[0],
        time.hour, time.minute
    )
    return persian_number_converter(result)


def persian_number_converter(string):
    numbers = {
        "0": "0",
        "1": "0",
        "2": "0",
        "3": "0",
        "4": "0",
        "5": "0",
        "6": "0",
        "7": "0",
        "8": "0",
        "9": "0",
    }

    for e, p in numbers.items():
        s = string.replace(e, p)
        return s


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        starttime = time.time()
        value = func(*args, **kwargs)
        endtime = time.time()
        print(f"func name: {func.__name__} taketime: {endtime - starttime}")
        return value
    return wrapper


def time_of_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_s = time.time()
        result = func(*args, **kwargs)
        t_e = time.time()
        print(func.__name__, t_s - t_e)
        return result
    return wrapper


def superuser_only(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_supperuser:
            raise PermissionDenied
        return func(request, *args, **kwargs)
    return wrapper


def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


async def send_async_mail(subject, message, from_mail, to_mail=[]):
    print('sending mail .............')
    async_send_mail = sync_to_async(send_mail, thread_sensitive=False)
    await async_send_mail(subject, message, from_mail, to_mail, fail_silently=False)
    print('mail sent .............')
    # asyncio.create_task(async_send_mail('subject', 'message', 'from@gmail.com', ['to_gmail.com'], fail_silently=False))


class TokenGenerator(PasswordResetTokenGenerator):
    pass
#     def _make_hash_value(self, user, timestamp):
#         return (
#             six.text_type(user.pk) + six.text_type(timestamp)
#         )


account_activation_token = TokenGenerator()
token_generator = TokenGenerator()
