from django.test import TestCase
from products.models import Product, Category
# Create your tests here.


class TestProductModels(TestCase):

    def test_can_create_a_product(self):
        category = Category.objects.create(title='category',
                                           slug='catslug',
                                           featured=False,
                                           image='test.png',
                                           )
        product = Product(name='testproduct',
                          slug="testslug",
                          category=category,
                          image='image.png',
                          summary="summary",
                          description="description",
                          price=19.99,
                          )
        product.save()
        self.assertEqual(product.name, 'testproduct')
        self.assertEqual(product.slug, 'testslug')
        self.assertEqual(product.category, category)
        self.assertEqual(product.image, 'image.png')
        self.assertEqual(product.summary, 'summary')
        self.assertEqual(product.description, 'description')
        self.assertEqual(product.price, 19.99)

    def test_can_create_a_category(self):
        category = Category(title='category',
                            slug='catslug',
                            featured=False,
                            image='test.png',
                            )
        category.save()
        self.assertEqual(category.title, 'category')
        self.assertEqual(category.slug, 'catslug')
        self.assertEqual(category.featured, False)
        self.assertEqual(category.image, 'test.png')
