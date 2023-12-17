from django.test import TestCase
from django.urls import reverse
from django.http.request import HttpRequest
from http import HTTPStatus
from model_bakery import baker
from django.contrib.auth import get_user_model
from .models import Post
from .forms import PostCreationForm

# Create your tests here.

User = get_user_model()

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts,0)

    def test_string_representation_of_objects(self):
        #Create post Manually
        # post = Post.objects.create(
        #     title = "Test Post Title",
        #     body = "Test Post Body"
        # )

        #Create post by model_bakery
        post = baker.make(Post)

        self.assertEqual(str(post),post.title)
        self.assertTrue(isinstance(post, Post))


class HomepageTest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(User)
        self.post1 = Post.objects.create(
            title = "Test Post Title 1",
            body = "Test Post Body 1",
            author = self.user
        )

        self.post2 = Post.objects.create(
            title = "Test Post Title 2",
            body = "Test Post Body 2",
            author = self.user
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get('/')

        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.body)


class DetailPageTest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(User)

        self.post = Post.objects.create(
            title = "Test Post Title 3",
            body = "Test Post Body 3",
            author = self.user
        )

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html')


    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response,self.post.title)
        self.assertContains(response,self.post.body)

    
class PostAuthorTest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(User)

        self.post = Post.objects.create(
            title = "Test Post Title 4",
            body = "Test Post Body 4",
            author = self.user
        )

    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))

    def test_post_belongs_to_user(self):
        self.assertTrue(hasattr(self.post, 'author'))
        self.assertEqual(self.post.author, self.user)

class PostCreationTest(TestCase):
    def setUp(self):
        self.url = reverse('create_post')
        self.template_name = 'posts/create-post.html'
        self.form_class = PostCreationForm
        self.title = "Sample title"
        self.body = "This is body of sample title"

        User.objects.create_user(
            username = 'testuser',
            email = 'testuser@myblog.com',
            password = 'test2Pas#us##'
        )

    def test_post_creation_page_exists(self):
        self.client.login(username = 'testuser', password = 'test2Pas#us##')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)

        form = response.context.get('form', None)

        self.assertIsInstance(form, self.form_class)


    def test_post_creation_form_creates_post(self):
        post_request = HttpRequest()

        post_request.user = baker.make(User)

        post_data = {
            'title': self.title,
            'body': self.body
        }

        post_request.POST = post_data
        form = self.form_class(post_request.POST)

        self.assertTrue(form.is_valid())

        post_obj = form.save(commit=False)
        
        self.assertIsInstance(post_obj, Post)

        post_obj.author = post_request.user
        post_obj.save()

        self.assertEqual(Post.objects.count(), 1)

    
    def test_post_creation_requires_login(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, expected_url='/accounts/login/?next=/create_post/')
        