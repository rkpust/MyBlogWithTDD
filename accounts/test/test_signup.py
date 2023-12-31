from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegistrationForm
from django.contrib.auth import get_user_model

# Create your tests here.

class AccountCreationTest(TestCase):

    def setUp(self) -> None:
        self.form_class = UserRegistrationForm
    

    def test_signup_page_exists(self):
        response = self.client.get(reverse('signup-page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, "Create Your Account Today")

    
    def test_signup_form_works_correctly(self):
        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        registration_data = {
            'username': 'testuser',
            'email': 'testuser@myblog.com',
            'password1': 'test2Pas#us##',
            'password2': 'test2Pas#us##'
        }

        form = self.form_class(registration_data )

        # To see error in form validation
        # print(form.errors)

        self.assertTrue(form.is_valid())

    
    def test_signup_form_creates_user_in_db(self):
        user_info = {
            'username': 'testuser1',
            'email': 'testuser1@myblog.com',
            'password1': 'test12Pas#us##',
            'password2': 'test12Pas#us##'
        }

        form = self.form_class(user_info)
        User = get_user_model()

        if form.is_valid():
            form.save()


        self.assertEqual(User.objects.count(), 1)
        