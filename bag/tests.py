from django.test import TestCase
from products.models import Product, Category
from profiles.models import User


class TestViews(TestCase):

    def test_get_bag_page(self):
        """
        Testing load homepage
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):

        user = User.objects.create_superuser(
            'myuser', 'myemail@test.com', 'password')
        self.client.force_login(user)

        category = Category.objects.create(
            name='lespaul', friendly_name='les paul')
        product = Product.objects.create(
            category=category,
            sku='12345',
            name='test',
            description='test',
            price=11.90,
            image_url='',
            image='',
        )
        product = Product.objects.get(pk=product.id)
        bag = {
            'product': product,
        }
        session = self.client.session
        session['bag'] = bag
        self.assertIn('bag', session.keys())
        self.assertIn('product', bag.keys())
