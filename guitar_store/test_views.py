from django.test import TestCase


class TestGuitarStoreViews(TestCase):
    """
    Testing creating and displaying a post
    """
    def test_load_homepage(self):
        """
        Test creating the post detail page
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertEqual(response.status_code, 200)

    def test_load_error_404(self):
        """
        Test redirect to error 404 page
        """
        response = self.client.get('/broken-link')
        self.assertEqual(response.status_code, 404)
