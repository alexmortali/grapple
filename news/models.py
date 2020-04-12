from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

User = get_user_model()

# Create your models here.


class Post(models.Model):
    """ Model for news posts """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, default='News Post')
    sub_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='news', blank=True)
    preview_text = models.CharField(max_length=150)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('news:news_article', args=[self.slug])

    def __str__(self):
        return self.title
