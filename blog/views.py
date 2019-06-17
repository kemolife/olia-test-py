from django.shortcuts import render
from .models import Post, Settings
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_popular = Post.objects.all()[:3]
    setting = Settings.objects.get(pk=1)
    return render(request, 'blog/post_list.html', {'posts': posts, 'posts_popular': posts_popular, 'setting': setting})

def blog_single(request,post_id):
    post = Post.objects.get(pk=post_id)
    print(post)
    return render(request, 'blog/blog-single.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def category(request):
    return render(request, 'blog/category.html')

def contact(request):
    return render(request, 'blog/contact.html')

def index(request):
    return render(request, 'blog/index.html')


