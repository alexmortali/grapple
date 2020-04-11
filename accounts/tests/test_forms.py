from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm


class TestForms(TestCase):
    def test_sign_up_is_valid(self):
        form = UserRegistrationForm({"username": "testuser",
                                     "email": "test@test.com",
                                     "password1": "testpassword",
                                     "password2": "testpassword",
                                     })
        self.assertTrue(form.is_valid())

    def test_login_is_valid(self):
        form = UserLoginForm({"username": "testuser",
                              "password": "testpassword",
                              })
        self.assertTrue(form.is_valid())

    def test_username_is_missing(self):
        form = UserRegistrationForm({"username": "",
                                     "email": "test@test.com",
                                     "password1": "testpassword",
                                     "password2": "testpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"This field is required."])

    def test_password1_is_missing(self):
        form = UserRegistrationForm({"username": "testuser",
                                     "email": "test@test.com",
                                     "password1": "",
                                     "password2": "testpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password1"], [u"This field is required."])

    def test_password2_is_missing(self):
        form = UserRegistrationForm({"username": "testuser",
                                     "email": "test@test.com",
                                     "password1": "testpassword",
                                     "password2": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"This field is required."])

    def test_passwords_dont_match(self):
        form = UserRegistrationForm({"username": "testuser",
                                     "email": "test@test.com",
                                     "password1": "testpassword",
                                     "password2": "wrongpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"Passwords must match"])

    def test_username_already_exists(self):
        self.user = User.objects.create_user(
            username='test_existing_user', password='testpass')
        form = UserRegistrationForm({"username": "test_existing_user",
                                     "email": "test@test.com",
                                     "password1": "testpassword",
                                     "password2": "testpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"A user with that username already exists."])
