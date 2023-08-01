from django.test import TestCase
from .forms import ProductForm, ReviewForm
from profiles.models import User


class TestProductForm(TestCase):

    def test_product_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_description_is_required(self):
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_product_price_is_required(self):
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')

    def test_image_url_is_not_required(self):
        form = ProductForm({'image_url': ''})
        self.assertFalse(form.is_valid())

    def test_all_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, (
            '__all__'
        ))


class TestReviewForm(TestCase):
    """
    Testing fields of the ReviewForm
    used for leaving a product review
    """
    def test_add_review(self):
        user = User.objects.create_superuser(
            'myuser', 'myemail@test.com', 'password')
        self.client.force_login(user)
        form = ReviewForm({'body': 'test_review'})
        self.assertTrue(form.is_valid())

    def test_body_is_required(self):
        form = ReviewForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_field_is_explicit_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ('body',))
