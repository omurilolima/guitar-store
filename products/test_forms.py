from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):

    def test_product_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_image_url_is_not_required(self):
        form = ProductForm({'image_url': ''})
        self.assertFalse(form.is_valid())

    def test_all_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, (
            '__all__'
        ))
