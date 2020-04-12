from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def news_home(request):
    """ View to render news home page """
    # Order posts by latest posts
    posts = Post.objects.all().order_by('-created')

    template = 'news_home.html'
    context = {'posts': posts}
    return render(request, template, context)


def news_article(request, slug):
    """ View to render specific news  article page """
    # Get 5 of the latest posts
    other_posts = Post.objects.all().order_by('-created')[:5]

    # Get selected news article
    post = get_object_or_404(Post, slug=slug)
    template = 'news_article.html'
    context = {'post': post,
               'other_posts': other_posts}
    return render(request, template, context)
