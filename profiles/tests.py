from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_user_access_profile_page(self):
        """
        Test if an authenticated user can access profile
        """
        user = User.objects.create_superuser(
            'myuser', 'myemail@test.com', 'password')
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_logged_out(self):
        """
        Test if a non-authenticated user gets redirected
        when trying to access profile page
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
