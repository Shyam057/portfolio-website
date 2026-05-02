from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from core.models import About

def blog_list(request):
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    about = About.objects.first()
    context = {
        'posts': posts,
        'categories': categories,
        'about': about,
    }
    return render(request, 'blog_app/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    about = About.objects.first()
    context = {
        'post': post,
        'about': about,
    }
    return render(request, 'blog_app/blog_detail.html', context)