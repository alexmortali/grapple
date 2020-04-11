from django.test import TestCase
from django.contrib.auth import get_user_model


class TestCheckoutViews(TestCase):

    def test_checkout_page(self):
        self.user = get_user_model().objects.create_user(
            'testuser', 'testemail@test.com', 'testpassword')
        page = self.client.get('/accounts/login/?next=/checkout/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')

    def test_payment_page(self):
        self.user = get_user_model().objects.create_user(
            'testuser', 'testemail@test.com', 'testpassword')
        page = self.client.get('/accounts/login/?next=/checkout/payment')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')
