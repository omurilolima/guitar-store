from django.test import TestCase
from blog.forms import CommentForm


class TestCommentForm(TestCase):
    """
    Testing fields of the CommentForm
    used for leaving a comment in a blog post
    """
    def test_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_field_is_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
