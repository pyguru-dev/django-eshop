from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ['title', 'body', 'author']


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ['title', 'body', 'author']


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")
    
    
