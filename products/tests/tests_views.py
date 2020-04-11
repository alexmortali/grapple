from django.test import TestCase
from products.models import Product, Category
# Create your tests here.


class TestProductsViews(TestCase):

    def test_all_products_page(self):
        page = self.client.get('/products/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'list_of_products.html')

    def test_products_by_category_page(self):
        category = Category.objects.create(title='category',
                                           slug='catslug',
                                           featured=False,
                                           image='test.png',
                                           )
        page = self.client.get('/products/category/'+category.slug+'/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'list_of_products_by_category.html')

    def test_product_detail_page(self):
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
                                         price=19.99,)
        page = self.client.get('/products/'+product.slug+'/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'product_detail.html')
