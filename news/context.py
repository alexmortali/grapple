from news.models import Post


def featured_news_posts_list(request):
    """ Returns featured Posts for home page """
    
    featured_posts = Post.objects.filter(featured=True).order_by('created')
    return {'featured_posts': featured_posts}