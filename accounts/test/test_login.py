from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@myblog.com'
        self.password = 'test2Pas#us##'

        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password
        )

    def test_login_page_exists(self):
        response = self.client.get(reverse('login-page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_page_has_login_form(self):
        response = self.client.get(reverse('login-page'))

        form = response.context.get('form')

        self.assertContains(response, 'Login Here')
        self.assertIsInstance(form, AuthenticationForm)


    def test_login_pages_logs_in_user(self):
        login_data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(reverse('login-page'), login_data)

        self.assertRedirects(response, reverse('homepage'))