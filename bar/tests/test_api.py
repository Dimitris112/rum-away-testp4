from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from bar.models import UserProfile
from cloudinary.models import CloudinaryField


class UserProfileApiTest(TestCase):

    def setUp(self):
        """Set up a user and their profile for testing purposes."""
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        self.featured_image_url = "http://example.com/test_image.jpg"

        self.profile, created = UserProfile.objects.get_or_create(
            user=self.user,
            defaults={
                "bio": "Test bio",
                "featured_image": self.featured_image_url
            }
        )

        if not created:
            self.profile.bio = "Test bio"
            self.profile.featured_image = self.featured_image_url
            self.profile.save()

    def tearDown(self):
        """Clean up the user profile and user after each test."""
        if hasattr(self, 'profile'):
            self.profile.delete()
        if hasattr(self, 'user'):
            self.user.delete()

    def test_profile_exists(self):
        """Test that a valid request to the user_profile_api returns the
        correct user profile data."""
        self.client.login(username='testuser', password='testpass')

        # Request to the user_profile_api
        response = self.client.get(
            reverse('user_profile_api', kwargs={'user_id': self.user.id})
        )

        self.assertEqual(response.status_code, 200)  # OK

        json_response = response.json()

        self.assertEqual(json_response['username'], 'testuser')
        self.assertEqual(json_response['bio'], 'Test bio')
        self.assertIn('profile_picture', json_response)
        self.assertEqual(
            json_response['member_since'],
            self.user.date_joined.strftime("%Y-%m-%d")
        )

    def test_profile_not_found(self):
        """Test that a request for a non-existent user profile returns a
        404 status with the appropriate error message."""
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(
            # Non-existent user ID
            reverse('user_profile_api', kwargs={'user_id': 9999})
        )

        self.assertEqual(response.status_code, 404)  # Not Found
        json_response = response.json()
        self.assertEqual(json_response['error'], 'User profile not found')

    def test_unauthenticated_access(self):
        """Test that an unauthenticated request redirects to the login page."""
        response = self.client.get(
            reverse('user_profile_api', kwargs={'user_id': self.user.id})
        )

        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertIn('/accounts/login/', response.url)
