from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from testimonials.models import Testimonial, Comment


class TestimonialViewsTestCase(TestCase):
    def setUp(self):
        """Create a test user and a testimonial."""
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

        self.testimonial = Testimonial.objects.create(
            name='Test User',
            content='This is a test testimonial.',
            rating=5,
            user=self.user
        )

    def test_add_comment_view(self):
        """Test adding a comment successfully."""
        response = self.client.post(
            reverse('add_comment', args=[self.testimonial.id]),
            {'content': 'This is a test comment.'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(
            content='This is a test comment.'
        ).exists())

    def test_add_comment_view_invalid(self):
        """Test adding a comment with invalid data."""
        response = self.client.post(
            reverse('add_comment', args=[self.testimonial.id]),
            {'content': ''},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Comment.objects.count(), 0)

    def test_edit_comment_view(self):
        """Test editing a comment successfully."""
        comment = Comment.objects.create(
            content='Initial comment.',
            user=self.user,
            testimonial=self.testimonial
        )
        response = self.client.post(
            reverse('edit_comment', args=[comment.id]),
            {'content': 'Updated comment.'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        comment.refresh_from_db()
        self.assertEqual(comment.content, 'Updated comment.')

    def test_edit_comment_view_invalid(self):
        """Test editing a comment with invalid data."""
        comment = Comment.objects.create(
            content='Another comment.',
            user=self.user,
            testimonial=self.testimonial
        )
        response = self.client.post(
            reverse('edit_comment', args=[comment.id]),
            {'content': 'A' * 51},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        comment.refresh_from_db()
        self.assertEqual(comment.content, 'Another comment.')

    def test_delete_comment(self):
        """Test deleting a comment successfully."""
        comment = Comment.objects.create(
            content='Comment to be deleted.',
            user=self.user,
            testimonial=self.testimonial
        )
        response = self.client.post(
            reverse('delete_comment', args=[comment.id]),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())

    def test_unauthenticated_add_comment(self):
        """Test adding a comment when unauthenticated."""
        self.client.logout()
        response = self.client.post(
            reverse('add_comment', args=[self.testimonial.id]),
            {'content': 'Should not be added.'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 302)

    def test_unauthenticated_edit_comment(self):
        """Test editing a comment when unauthenticated."""
        comment = Comment.objects.create(
            content='Comment by user.',
            user=self.user,
            testimonial=self.testimonial
        )
        self.client.logout()
        response = self.client.post(
            reverse('edit_comment', args=[comment.id]),
            {'content': 'Should not be updated.'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 302)

    def test_unauthenticated_delete_comment(self):
        """Test deleting a comment when unauthenticated."""
        comment = Comment.objects.create(
            content='Comment by user.',
            user=self.user,
            testimonial=self.testimonial
        )
        self.client.logout()
        response = self.client.post(
            reverse('delete_comment', args=[comment.id]),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        """Log out the client after tests."""
        self.client.logout()
