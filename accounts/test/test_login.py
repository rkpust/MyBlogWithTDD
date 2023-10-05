from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm


class LoginTest(TestCase):
    def test_login_page_exists(self):
        response = self.client.get(reverse('login-page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_page_has_login_form(self):
        response = self.client.get(reverse('login-page'))

        form = response.context.get('form')

        self.assertContains(response, 'Login Here')
        self.assertIsInstance(form, AuthenticationForm)