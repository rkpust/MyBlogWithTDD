from django.test import TestCase
from .models import Post

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