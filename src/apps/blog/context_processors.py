from .models import BlogCategory


def blog_categories(request):
    return {
        'blog_categories': BlogCategory.objects.all()
    }
