from django.test import TestCase
from .models import Post
from profiles.models import User


class TestBlogViews(TestCase):
    """
    Testing creating and displaying a post
    """
    def test_load_blog_page(self):
        """
        Test creating the post detail page
        """
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/index.html')
        self.assertEqual(response.status_code, 200)
