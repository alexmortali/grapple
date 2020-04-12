from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

# Create your models here.


class Review(models.Model):
    """ Model for reviews """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=35, default="Review Title")
    review = models.TextField(max_length=400)
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
