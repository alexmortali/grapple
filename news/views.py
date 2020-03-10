from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def news_home(request):
    posts = Post.objects.all().order_by('-created')
    template = 'news_home.html'
    context = {'posts': posts}
    return render(request, template, context)

def news_article(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'news_article.html'
    context = {'post': post}
    return render(request, template, context)