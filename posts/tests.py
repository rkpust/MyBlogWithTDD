from django.test import TestCase
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts,0)