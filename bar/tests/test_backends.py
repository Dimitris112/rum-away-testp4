from django.test import TestCase
from django.contrib.auth import get_user_model
from bar.backends import CaseInsensitiveUsernameBackend

UserModel = get_user_model()

class CaseInsensitiveUsernameBackendTest(TestCase):
    """Test case for the CaseInsensitiveUsernameBackend authentication backend."""

    def setUp(self):
        """Set up a test user for authentication tests."""
        self.username = 'TestUser'
        self.password = 'securepassword'
        self.user = UserModel.objects.create_user(username=self.username, password=self.password)

    def test_authenticate_case_insensitive_username(self):
        """Test authentication with usernames of different cases."""
        backend = CaseInsensitiveUsernameBackend()

        for test_username in ['testuser', 'TESTUSER', 'TeStUsEr']:
            user = backend.authenticate(None, username=test_username, password=self.password)
            self.assertEqual(user, self.user, f"Expected user to be authenticated for username '{test_username}'")

    def test_authenticate_incorrect_password(self):
        """Test authentication with the correct username but incorrect password."""
        backend = CaseInsensitiveUsernameBackend()

        user = backend.authenticate(None, username='TestUser', password='wrongpassword')
        self.assertIsNone(user, "User should not be authenticated with an incorrect password.")

    def test_authenticate_nonexistent_user(self):
        """Test authentication with a username that does not exist."""
        backend = CaseInsensitiveUsernameBackend()

        user = backend.authenticate(None, username='nonexistentuser', password='password')
        self.assertIsNone(user, "User should not be authenticated because the username does not exist.")

    def test_authenticate_without_username(self):
        """Test authentication without providing a username."""
        backend = CaseInsensitiveUsernameBackend()

        user = backend.authenticate(None, username=None, password=self.password)
        self.assertIsNone(user, "User should not be authenticated without a username.")
