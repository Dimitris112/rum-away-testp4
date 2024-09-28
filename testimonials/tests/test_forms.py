from django.test import TestCase
from django.contrib.auth.models import User
from testimonials.forms import TestimonialForm, CommentForm
from testimonials.models import Testimonial, Comment


class TestimonialFormTests(TestCase):
    def setUp(self):
        """Create a user for testing."""
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_valid_testimonial_form(self):
        """Test valid testimonial form submission."""
        form_data = {
            'content': 'This is a valid testimonial.',
            'rating': 5
        }
        form = TestimonialForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())
        testimonial = form.save()
        self.assertEqual(testimonial.content,
                         'This is a valid testimonial.')
        self.assertEqual(testimonial.rating, 5)
        self.assertEqual(testimonial.name, 'testuser')
        self.assertEqual(testimonial.user, self.user)

    def test_invalid_testimonial_form(self):
        """Test invalid testimonial form submission."""
        form_data = {
            'content': '',  # Invalid because content is empty
            'rating': 5
        }
        form = TestimonialForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)

    def test_save_without_user(self):
        """Test saving testimonial form without user."""
        form_data = {
            'content': 'This is a valid testimonial.',
            'rating': 5
        }
        form = TestimonialForm(data=form_data)
        self.assertTrue(form.is_valid())
        testimonial = form.save()
        self.assertEqual(testimonial.name, '')
        self.assertIsNone(testimonial.user)


class CommentFormTests(TestCase):
    def setUp(self):
        """Create a user and a testimonial for testing."""
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.testimonial = Testimonial.objects.create(
            name='Test User',
            content='This is a test testimonial.',
            rating=5,
            user=self.user
        )

    def test_valid_comment_form(self):
        """Test valid comment form submission."""
        form_data = {
            'content': 'This is a valid comment.'
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        comment.user = self.user
        comment.testimonial = self.testimonial
        comment.save()
        self.assertEqual(comment.content, 'This is a valid comment.')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.testimonial, self.testimonial)

    def test_invalid_comment_form(self):
        """Test invalid comment form submission."""
        form_data = {
            'content': ''
        }
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)

    def test_comment_form_widget(self):
        """Test that the comment form uses the correct widget."""
        form = CommentForm()
        self.assertIn('form-control',
                      form.fields['content'].widget.attrs['class'])
        self.assertEqual(form.fields['content'].widget.attrs['rows'], 3)
