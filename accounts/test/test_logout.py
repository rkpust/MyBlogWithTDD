from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class LogoutTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@myblog.com'
        self.password = 'test2Pas#us##'

        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password
        )


    def test_logout_view_logs_out_user(self):
        self.client.login(username=self.username, password=self.password)

        self.assertTrue('_auth_user_id' in self.client.session)

        response = self.client.get(reverse('logout'))

        self.assertFalse('_auth_user_id' in self.client.session)