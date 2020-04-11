from django.test import TestCase
from reviews.models import Review
from products.models import Product, Category
from django.contrib.auth import get_user_model
# Create your tests here.


class TestPostModel(TestCase):

    def test_can_create_a_review(self):
        user = get_user_model().objects.create(username='testuser')

        category = Category.objects.create(title='category',
                                           slug='catslug',
                                           featured=False,
                                           image='test.png',
                                           )

        product = Product.objects.create(name='testproduct',
                                         slug="testslug",
                                         category=category,
                                         image='image.png',
                                         summary="summary",
                                         description="description",
                                         price=19.99,
                                         )
        review = Review(user=user,
                        product=product,
                        title='test',
                        review='review',
                        rating=4.0,
                        )
        review.save()
        self.assertEqual(review.user, user)
        self.assertEqual(review.product, product)
        self.assertEqual(review.title, 'test')
        self.assertEqual(review.review, 'review')
        self.assertEqual(review.rating, 4.0)
