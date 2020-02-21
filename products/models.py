from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
    """ Model for Categories. Products can be placed in different 
    categories and features to show on home page """

    slug = models.SlugField(max_length=150, unique=True)
    title = models.CharField(max_length=150)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    """ Model for Products """
    
    slug = models.SlugField(max_length=150, unique=True)
    name = models.CharField(max_length=150, default='Product')
    image = models.ImageField(upload_to='products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField(max_length=200, verbose_name="Summary")
    description = models.TextField(max_length=1000, verbose_name="Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=9.99)

    def get_url(self):
        return reverse('poducts:product_detail', args=[self.slug])

    def __str__(self):
        return self.name