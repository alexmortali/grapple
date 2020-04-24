from django.test import TestCase, Client


class AccountPostTest(TestCase):

    def test_create_an_account(self):
        c = Client()
        response = c.post('/', {'username': 'name', 'password': 'pass'})
        self.assertEqual(response.status_code, 200)
