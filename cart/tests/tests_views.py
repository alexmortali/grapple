from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class TestCartViews(TestCase):

    def test_cart_page(self):
        self.user = get_user_model().objects.create_user(
            'testuser', 'testemail@test.com', 'testpassword')
        page = self.client.get('/accounts/login/?next=/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')
