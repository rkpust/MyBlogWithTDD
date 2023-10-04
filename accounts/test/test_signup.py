from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

# Create your tests here.

class AccountCreationTest(TestCase):
    def test_signup_page_exists(self):
        response = self.client.get(reverse('signup-page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, "Create Your Account Today")