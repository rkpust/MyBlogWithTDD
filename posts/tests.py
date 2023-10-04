from django.test import TestCase
from .models import Post
from http import HTTPStatus
from model_bakery import baker
from django.contrib.auth import get_user_model

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