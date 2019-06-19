from django.shortcuts import render
from .models import Post, Settings, Category, Tag, Comment
from django.utils import timezone


# Create your views here.
def _get_setting():
    return Settings.objects.get(pk=1)


def index(request):
    latest_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'latest_posts': latest_posts, 'setting': _get_setting()})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_popular = Post.objects.all()[:3]
    return render(request, 'blog/post_list.html', {'posts': posts, 'posts_popular': posts_popular, 'setting': _get_setting()})


def blog_single(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post__lte=post_id)
    print(post)
    return render(request, 'blog/blog-single.html', {'post': post, 'setting': _get_setting(), 'comments': comments})


def about(request):
    return render(request, 'blog/about.html', {'setting': _get_setting()})


def category(request):
    return render(request, 'blog/category.html', {'setting': _get_setting()})


def contact(request):
    return render(request, 'blog/contact.html', {'setting': _get_setting()})
