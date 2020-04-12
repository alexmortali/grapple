from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    """ Model for Categories. Products can be placed in different
    categories and featured to show on home page """

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products:list_of_products_by_category',
                       args=[self.slug]
                       )

    def __str__(self):
        return self.title


class Product(models.Model):
    """ Model for Products """

    name = models.CharField(max_length=150, default='Product')
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images', blank=True)
    summary = models.TextField(max_length=200, verbose_name="Summary")
    description = models.TextField(max_length=1000, verbose_name="Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=9.99)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])

    def __str__(self):
        return self.name
