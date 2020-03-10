from django.conf.urls import url
from . import views
app_name = 'news'

urlpatterns = [
    url(r'^$', views.news_home, name='news_home'),
    url(r'^(?P<slug>[-\w]+)/$', views.news_article, name='news_article')
]