from django.test import TestCase
from .models import Product, Category
from profiles.models import User


class TestProductViews(TestCase):
    def test_all_products_load(self):
        """
        Test if product page is loaded
        """
        all_products_page = self.client.get('/products/')
        self.assertEqual(all_products_page.status_code, 200)
        self.assertTemplateUsed(all_products_page, 'products/products.html')

    def test_load_product_detail_page(self):
        """
        Test if the product detail page is loaded
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

        product_detail = self.client.get('/products/1/')
        self.assertTemplateUsed(product_detail, 'products/product_detail.html')

    def test_nonadmin_redirect_creating_product(self):
        """
        Test if testuser gets redirected to homepage when
        trying to add a product as non admin
        """
        self.client.login(username="test", password="test")
        add_product = self.client.get('/products/add')
        self.assertEqual(add_product.status_code, 301)

    def test_edit_product(self):
        """
        Test update product info in the store
        """
        user = User.objects.create_superuser('myuser', 'myemail@test.com', 'password')
        self.client.force_login(user)

        category = Category.objects.create(name='lespaul', friendly_name='les paul')
        product = Product.objects.create(
            category=category,
            sku='12345',
            name='test',
            description='test',
            price=11.90,
            image_url='',
            image='',
        )

        # check if product was created
        self.assertEqual(
            product.name,
            'test')

        response = self.client.post(f'/products/edit/{product.id}/', {
            'category': '',
            'sku': '12345',
            'name': 'product_updated',
            'description': 'test',
            'price': 11.90,
            'image_url': '',
            'image': '',
        })

        edited_product = Product.objects.filter(name="product_updated")
        self.assertEqual(len(edited_product), 1)

    def test_delete_product(self):
        """
        Test delete a product
        """
        user = User.objects.create_superuser('myuser', 'myemail@test.com', 'password')
        self.client.force_login(user)

        category = Category.objects.create(name='lespaul', friendly_name='les paul')
        product = Product.objects.create(
            category=category,
            sku='12345',
            name='test',
            description='test',
            price=11.90,
            image_url='',
            image='',
        )
        product_page = self.client.get(f'/products/{product.id}/')
        self.assertTemplateUsed(product_page, 'products/product_detail.html')

        self.client.get(f'/products/delete/{product.id}/')

        existing_products = Product.objects.filter(pk=product.id)
        self.assertEqual(len(existing_products), 0)
