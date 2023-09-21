from django.shortcuts import render


def error404_handler(request, *args, **argv):
    return render(request, "errors/404.html", {})
