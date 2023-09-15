from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import connection
from django.db import reset_queries


def unauthenticated_user(view_func):
    @wraps
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticate:
            return redirect('home_view')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @wraps
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you dont have permission')
        return wrapper
    return decorator


def database_debug(func):
    @wraps
    def wrapper(*args, **kwargs):
        reset_queries()
        results = func()
        query_info = connection.queries
        print('function_name: {}'.format(func.__name__))
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return results
    return wrapper
