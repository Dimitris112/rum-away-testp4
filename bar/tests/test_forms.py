from django.test import TestCase
from bar.forms import (
    UserProfileForm,
    ReservationForm,
    EventForm,
    CommentForm,
    UserForm,
)

from bar.models import User, Reservation, Event, Comment
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.core.exceptions import ValidationError
from bar.forms import validate_image_format
import datetime


class ValidateImageFormatTest(TestCase):
    """Test cases for the validate_image_format function."""

    def test_valid_image_format(self):
        """Test that valid image formats do not raise a ValidationError."""
        valid_files = [
            SimpleUploadedFile(
                name='test_image.png',
                content=b'file_content',
                content_type='image/png'
            ),
            SimpleUploadedFile(
                name='test_image.jpg',
                content=b'file_content',
                content_type='image/jpeg'
            ),
            SimpleUploadedFile(
                name='test_image.jpeg',
                content=b'file_content',
                content_type='image/jpeg'
            ),
            SimpleUploadedFile(
                name='test_image.gif',
                content=b'file_content',
                content_type='image/gif'
            ),
            SimpleUploadedFile(
                name='test_image.webp',
                content=b'file_content',
                content_type='image/webp'
            ),
        ]
        for file in valid_files:
            try:
                validate_image_format(file)
            except ValidationError:
                self.fail(
                    f"validate_image_format raised ValidationError for valid "
                    f"file: {file.name}"
                )

    def test_invalid_image_format(self):
        """Test that invalid image formats raise a ValidationError."""
        invalid_files = [
            SimpleUploadedFile(
                name='test_image.txt',
                content=b'file_content',
                content_type='text/plain'
            ),
            SimpleUploadedFile(
                name='test_image.pdf',
                content=b'file_content',
                content_type='application/pdf'
            ),
        ]
        for file in invalid_files:
            with self.assertRaises(ValidationError):
                validate_image_format(file)

    def test_no_file_attribute(self):
        """Test that a value without name or url raises a ValidationError."""
        with self.assertRaises(ValidationError):
            validate_image_format(None)


class UserProfileFormTest(TestCase):
    """Test cases for the UserProfileForm."""

    def test_user_profile_form_valid(self):
        """
        Test that the UserProfileForm is valid with proper data.

        This test creates a SimpleUploadedFile to simulate an image upload
        and checks if the form is valid with the provided bio and image.
        """
        image = SimpleUploadedFile(
            name='test_image.png',
            content=b'file_content',
            content_type='image/png'
        )
        form_data = {
            'bio': 'Test bio',
            'featured_image': image
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)


class UserFormTest(TestCase):
    """Test cases for the UserForm."""

    def test_valid_user_form(self):
        """
        Test that the UserForm is valid with proper data.

        This checks if the form is valid when provided with a first name,
        last name, and email.
        """
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        }
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_invalid_user_form_empty_fields(self):
        """
        Test that the UserForm is invalid with empty fields.

        This verifies that the form is invalid when no data is provided.
        """
        form_data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)

    def test_invalid_user_form_invalid_email(self):
        """
        Test that the UserForm is invalid with an improperly
        formatted email.

        This verifies that the form is invalid when an invalid email
        format is provided.
        """
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'invalid-email'
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class ReservationFormTest(TestCase):
    """Test cases for the ReservationForm."""

    def setUp(self):
        """
        Set up a user and hall for the reservation tests.

        Creates a test user and defines a hall type for use in
        reservation form tests.
        """
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )
        self.hall = 'indoor'

    def test_reservation_form_valid(self):
        """
        Test that the ReservationForm is valid with future date and
        proper data.

        This checks if the form is valid when provided with future
        reservation data, including the reservation date and time.
        """
        future_date = timezone.now() + datetime.timedelta(days=1)
        form_data = {
            'name': 'Dim D',
            'special_requests': 'None',
            'num_guests': 2,
            'hall': self.hall,
            'reservation_date': future_date.date(),
            'reservation_hour': '12',
            'reservation_minute': '30'
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_reservation_form_invalid_time(self):
        """
        Test that the ReservationForm is invalid with a past
        reservation date.

        This verifies that the form is invalid when the reservation
        date is set to a past date.
        """
        form_data = {
            'name': 'Dim D',
            'special_requests': 'None',
            'num_guests': 2,
            'hall': self.hall,
            'reservation_date': timezone.now().date() - datetime.timedelta(
                days=1),
            'reservation_hour': '12',
            'reservation_minute': '30'
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)


class EventFormTest(TestCase):
    """Test cases for the EventForm."""

    def test_valid_form(self):
        """
        Test that the EventForm is valid with proper data.
        """
        image = SimpleUploadedFile(
            name='test_event_image.png',
            content=b'file_content',
            content_type='image/png'
        )
        form_data = {
            'title': 'Test Event',
            'description': 'Test Description',
            'date': '2024-01-01T00:00:00Z',
            'start_time': '12:00',
            'end_time': '14:00',
            'recurrence': 'weekly',
            'recurrence_day': 'monday',
            'image': image
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)


class CommentFormTest(TestCase):
    """Test cases for the CommentForm."""

    def test_valid_comment_form(self):
        """
        Test that the CommentForm is valid with proper content.

        This checks if the form is valid when provided with valid comment
        content.
        """
        form_data = {'content': 'This is a comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_invalid_comment_form_empty_content(self):
        """
        Test that the CommentForm is invalid with empty content.

        This verifies that the form is invalid when no content is
        provided.
        """
        form_data = {'content': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
