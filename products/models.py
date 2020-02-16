from django.db import models

# Create your models here.

class Category(models.Model):
    """ Model for Categories. Products can be placed in different 
    categories and features to show on home page """

    slug = models.SlugField()
    title = models.CharField(max_length=250)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Product(models.Model):
    """ Model for Products """
    
    slug = models.SlugField(editable=False)
    name = models.CharField(max_length=250, default='Product')
    image = models.ImageField(upload_to='products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField(max_length=200, verbose_name="Summary")
    description = models.TextField(max_length=1000, verbose_name="Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=9.99)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name