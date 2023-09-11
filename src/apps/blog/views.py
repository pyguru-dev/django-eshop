from django.views import generic
from django.views.generic.edit import FormMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .models import Post
from .forms import CommentCreateForm


class PostListView(generic.ListView):
    model = Post
    # queryset = Post.objects.all().select_related('category')
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    paginate_by = 12
    

class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    # slug_field = 'post_id'
    # slug_url_kwarg = 'id'

    # def get_object(self, queryset):
    #     slug = self.kwargs.get('post_id')
    #     return get_object_or_404(Post.objects.published(), slug=slug)

    # form_class = CommentCreateForm

    # def get_success_url(self) -> str:
    #     return reverse('post_detail', kwargs={'pk': self.object.id})

    # def get_context_data(self, **kwargs):
    #     context = super(PostDeleteView, self).get_context_data(**kwargs)
    #     context['form'] = CommentCreateForm(
    #         initial={'article': self.object, 'user': self.request.user})
    #     return context

    # def post(self, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         self.form_valid(self)
    #     else:
    #         pass

    # def form_valid(self, form):
    #     form.save()
    #     return super(PostDeleteView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin,
                     CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


def post_by_tag(request, slug):
    posts = Post.objects.filter(tags__slug=slug)
    context = {
        'posts': posts
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
        'comments': post.comments.filter(approved=True)
    }
    return render(request, "blog/post_detail.html", context)


class AuthorListView(generic.ListView):
    model = User
    # queryset = Post.objects.all().select_related('posts')
    # queryset = User.authors.all()
    context_object_name = 'authors'
    template_name = 'blog/author_list.html'
    paginate_by = 24


class AuthorDetailView(generic.DetailView):
    template_name = "blog/author_detail.html"
    context_object_name = 'author'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(author=self.request.user)


class SearchListView(generic.ListView):
    pass
