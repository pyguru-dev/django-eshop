import time

from django.http import Http404
from . import jalali
from django.utils import timezone
from django.core.exceptions import PermissionDenied

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
    def wrapper(*args, **kwargs):
        starttime = time.time()
        value=func(*args, **kwargs)
        endtime=time.time()
        print(f"func name: {func.__name__} taketime: {endtime - starttime}")
        return value
    return wrapper


def superuser_only(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_supperuser:
            raise PermissionDenied
        return func(request, *args, **kwargs)
    return wrapper

