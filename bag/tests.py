from django.test import TestCase


class TestViews(TestCase):

    def test_get_bag_page(self):
        """
        Testing load homepage
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
