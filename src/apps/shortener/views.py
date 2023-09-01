from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Url
from .serializers import UrlSerializer


def create_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        slug = request.POST.get('slug')

        new_url = Url(url=url, slug=slug)
        new_url.save()
        return


def url_redirect(request, slug):
    url = get_object_or_404(Url, slug=slug)
    url.visit_count += 1
    url.save()

    return redirect(url.url)


class UrlViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Url.objects.all()
        url = get_object_or_404(queryset, pk=pk)
        url.visit_count += 1
        url.save()
