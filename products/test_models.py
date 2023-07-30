from django.test import TestCase
from .models import Product, Category
from profiles.models import User


class TestProductModel(TestCase):
    def test_creating_a_product(self):
        """
        Creating a product
        """
        category = Category.objects.create(name='test')
        product = Product.objects.create(
            category=category,
            sku='12345',
            name='test',
            description='test',
            price=11.90,
            image_url='',
            image='',
        )
        # cheking the __str__() method
        # called by str()
        self.assertEqual(
            product.name,
            'test')
