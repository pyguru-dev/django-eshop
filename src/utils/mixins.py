from django.http import Http404
from django.shortcuts import get_object_or_404
from apps.blog.models import Post


class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = []
        elif request.user.is_author:
            self.fields = []
        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if post.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)


class SuperUserAccessMixin():
    def dispatch(self, request,*args, **kwargs):        
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)


class HasAuthorMixin():
    pass