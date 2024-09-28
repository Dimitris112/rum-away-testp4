from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from testimonials.models import Testimonial, Comment


class TestimonialModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )

    def test_create_testimonial(self):
        """Test that a testimonial can be created."""
        testimonial = Testimonial.objects.create(
            name='John Doe',
            content='This is a great product!',
            rating=5,
            user=self.user
        )
        self.assertEqual(testimonial.name, 'John Doe')
        self.assertEqual(testimonial.content,
                         'This is a great product!')
        self.assertEqual(testimonial.rating, 5)
        self.assertEqual(testimonial.user, self.user)

    def test_string_representation(self):
        """Test the string representation of a testimonial."""
        testimonial = Testimonial(
            name='Jane Doe', content='Amazing service!'
        )
        self.assertEqual(str(testimonial),
                         'Jane Doe: Amazing service!...')


class CommentModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.testimonial = Testimonial.objects.create(
            name='John Doe',
            content='This is a great product!',
            rating=5,
            user=self.user
        )

    def test_create_comment(self):
        """Test that a comment can be created."""
        comment = Comment.objects.create(
            content='Great testimonial!',
            user=self.user,
            testimonial=self.testimonial
        )
        self.assertEqual(comment.content, 'Great testimonial!')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.testimonial, self.testimonial)

    def test_string_representation(self):
        """Test the string representation of a comment."""
        comment = Comment(
            content='Nice testimonial!',
            user=self.user,
            testimonial=self.testimonial
        )
        self.assertEqual(
            str(comment),
            f'testuser: Nice testimonial!... on {self.testimonial.id}'
        )

    def test_comment_clean(self):
        """Test that a comment with empty content raises a ValidationError."""
        comment = Comment(user=self.user, testimonial=self.testimonial)
        with self.assertRaises(ValidationError):
            comment.clean()

    def test_comment_content_limit(self):
        """Test that a comment content exceeds maximum length."""
        long_content = 'x' * 51  # Content longer than 50 characters
        comment = Comment(
            content=long_content,
            user=self.user,
            testimonial=self.testimonial
        )
        with self.assertRaises(ValidationError):
            comment.clean()
