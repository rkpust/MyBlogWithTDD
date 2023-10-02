from django.test import TestCase
from .models import Post
from http import HTTPStatus

# Create your tests here.

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts,0)

    def test_string_representation_of_objects(self):
        post = Post.objects.create(
            title = "Test Post Title",
            body = "Test Post Body"
        )

        self.assertEqual(str(post),post.title)


class HomepageTest(TestCase):
    def setUp(self) -> None:
        post1 = Post.objects.create(
            title = "Test Post Title 1",
            body = "Test Post Body 1"
        )

        post2 = Post.objects.create(
            title = "Test Post Title 2",
            body = "Test Post Body 2"
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get('/')

        self.assertContains(response, 'Test Post Title 1')
        self.assertContains(response, 'Test Post Title 2')
