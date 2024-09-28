from django.test import TestCase
from django.contrib.auth.models import User
from bar.models import (
    Reservation,
    Comment,
    UserProfile,
    Event,
    ContactMessage,
    Category,
    validate_image_format,
)
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.staticfiles.storage import staticfiles_storage
from PIL import Image
from io import BytesIO


class ValidateImageFormatTests(TestCase):
    """Test cases for the validate_image_format function."""

    def test_valid_image_format(self):
        """Test that valid image formats do not raise ValidationError."""
        valid_files = [
            'image.png',
            'image.jpg',
            'image.jpeg',
            'image.gif',
            'image.webp',
        ]
        for file_name in valid_files:
            with self.subTest(file_name=file_name):
                validate_image_format(
                    type('File', (object,), {'name': file_name})()
                )

    def test_invalid_image_format(self):
        """Test that invalid image formats raise ValidationError."""
        invalid_files = [
            'image.bmp',
            'image.tiff',
            'image.pdf',
        ]
        for file_name in invalid_files:
            with self.subTest(file_name=file_name):
                with self.assertRaises(ValidationError):
                    validate_image_format(
                        type('File', (object,), {'name': file_name})()
                    )


class ReservationModelTests(TestCase):
    """Test cases for the Reservation model."""

    def setUp(self):
        """Set up a User instance for use in the tests."""
        self.user = User.objects.create(username='testuser')

    def test_reservation_creation(self):
        """Test creating a reservation and its string representation."""
        reservation = Reservation.objects.create(
            user=self.user,
            reservation_time=timezone.now(),
            num_guests=5,
            hall='indoor'
        )
        self.assertEqual(
            str(reservation),
            f"Reservation for {self.user.username} at "
            f"{reservation.reservation_time} in the {reservation.hall} area"
        )

    def test_clean_indoor_capacity_exceeded(self):
        """Test that exceeding indoor capacity raises ValidationError."""
        reservation = Reservation(user=self.user, num_guests=80, hall='indoor')
        with self.assertRaises(ValidationError):
            reservation.clean()

    def test_clean_outdoor_capacity_exceeded(self):
        """Test that exceeding outdoor capacity raises ValidationError."""
        reservation = Reservation(
            user=self.user,
            num_guests=130,
            hall='outdoor'
        )
        with self.assertRaises(ValidationError):
            reservation.clean()


class CommentModelTests(TestCase):
    """Test cases for the Comment model."""

    def setUp(self):
        """Set up a User instance for use in the tests."""
        self.user = User.objects.create(username='testuser')

    def test_comment_creation(self):
        """Test creating a comment and its string representation."""
        comment = Comment.objects.create(
            user=self.user,
            content='Great service!',
            rating=5
        )
        self.assertEqual(
            str(comment),
            f"Comment by {self.user.username} with rating {comment.rating}"
        )


class UserProfileModelTests(TestCase):
    """Test cases for the UserProfile model."""

    @classmethod
    def setUpTestData(cls):
        """Set up a User and UserProfile instance for use in the tests."""
        cls.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        cls.profile, created = UserProfile.objects.get_or_create(
            user=cls.user,
            defaults={'bio': 'Hello!', 'featured_image': None}
        )

    def test_user_profile_creation(self):
        """Test creating a user profile and ensure it is not None."""
        self.assertIsNotNone(self.profile)

    def test_get_profile_picture_url_with_image(self):
        """Test retrieving the profile picture URL when an image is present."""
        image = Image.new('RGB', (100, 100), color='red')
        image_file = BytesIO()
        image.save(image_file, format='JPEG')
        image_file.name = 'test_image.jpg'
        image_file.seek(0)

        # Create a SimpleUploadedFile using the in-memory image
        self.profile.featured_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_file.getvalue(),
            content_type='image/jpeg'
        )
        self.profile.save()

        url = self.profile.get_profile_picture_url()
        self.assertEqual(url, self.profile.featured_image.url)

    def test_get_profile_picture_url_without_image(self):
        """Test retrieving the default image URL when no image is present."""
        url = self.profile.get_profile_picture_url()
        expected_url = staticfiles_storage.url('images/nobody.jpg')
        self.assertEqual(url, expected_url)

    def test_clean_invalid_image_format(self):
        """Test that setting an invalid image format raises ValidationError."""
        self.profile.featured_image = type('File', (object,), {
            'name': 'image.bmp'
        })()
        with self.assertRaises(ValidationError):
            self.profile.clean()


class EventModelTests(TestCase):
    """Test cases for the Event model."""

    def setUp(self):
        """Set up an Event instance for use in the tests."""
        self.event = Event.objects.create(
            title='Live Music',
            description='Enjoy live music every weekend.',
            date=timezone.now(),
            start_time=timezone.now().time(),
            end_time=timezone.now().time(),
            recurrence='weekly',
            recurrence_day='saturday'
        )

    def test_event_creation(self):
        """Test creating an event and its string representation."""
        self.assertEqual(str(self.event), self.event.title)

    def test_get_next_occurrence_daily(self):
        """Test getting the next occurrence for a daily event."""
        self.event.recurrence = 'daily'
        next_occurrence = self.event.get_next_occurrence()
        self.assertIsNotNone(next_occurrence)

    def test_get_next_occurrence_weekly(self):
        """Test getting the next occurrence for a weekly event."""
        next_occurrence = self.event.get_next_occurrence()
        self.assertIsNotNone(next_occurrence)

    def test_get_next_occurrence_no_recurrence(self):
        """Test that no recurrence returns None for next occurrence."""
        self.event.recurrence = None
        next_occurrence = self.event.get_next_occurrence()
        self.assertIsNone(next_occurrence)


class ContactMessageModelTests(TestCase):
    """Test cases for the ContactMessage model."""

    def test_contact_message_creation(self):
        """Test creating a contact message and its string representation."""
        contact_message = ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            telephone='1234567890',
            message='Hello!'
        )
        self.assertEqual(
            str(contact_message),
            f"Message from {contact_message.name} "
            f"({contact_message.email}) on {contact_message.created_at}"
        )


class CategoryModelTests(TestCase):
    """Test cases for the Category model."""

    def test_category_creation(self):
        """Test creating a category and its string representation."""
        category = Category.objects.create(
            name='Drinks',
            description='All kinds of drinks.'
        )
        self.assertEqual(str(category), category.name)
