from django.test import TestCase
from bar.forms import UserProfileForm, UserForm, ReservationForm, EventForm
from bar.models import UserProfile, User, Reservation, Event
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
import datetime


class UserProfileFormTest(TestCase):
    def test_user_profile_form_valid(self):
        """Test that the UserProfileForm is valid with correct data."""
        form_data = {'featured_image': None, 'bio': 'This is my bio.'}
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_profile_form_invalid_image_format(self):
        """Test that the UserProfileForm is invalid with an unsupported image format."""
        invalid_image = SimpleUploadedFile("invalid_file.txt", b"file_content")
        form_data = {'featured_image': invalid_image, 'bio': 'This is my bio.'}
        form = UserProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('featured_image', form.errors)


class UserFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_user_form_valid(self):
        """Test that the UserForm is valid with proper data."""
        form_data = {'first_name': 'Dim', 'last_name': 'D', 'email': 'dim.d@example.com'}
        form = UserForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_user_form_invalid_email(self):
        """Test that the UserForm is invalid with a wrong formatted email."""
        form_data = {'first_name': 'Dim', 'last_name': 'D', 'email': 'invalid_email'}
        form = UserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class ReservationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.hall = 'indoor'

    def test_reservation_form_valid(self):
        """Test that the ReservationForm is valid with future date and proper data."""
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
        """Test that the ReservationForm is invalid with a past reservation date."""
        form_data = {
            'name': 'Dim D',
            'special_requests': 'None',
            'num_guests': 2,
            'hall': self.hall,
            'reservation_date': timezone.now().date() - datetime.timedelta(days=1),
            'reservation_hour': '12',
            'reservation_minute': '30'
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('reservation_date', form.errors)


class EventFormTest(TestCase):
    def test_event_form_valid(self):
        """Test that the EventForm is valid with proper data."""
        form_data = {
            'title': 'Test Event',
            'description': 'This is a test event.',
            'date': '2024-09-30',
            'start_time': '12:00',
            'end_time': '13:00',
            'image': None,
            'recurrence': 'never',
            'recurrence_day': 'monday'
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_event_form_invalid_time(self):
        """Test that the EventForm is invalid when end time is before start time."""
        form_data = {
            'title': 'Sample Event',
            'description': 'This is a sample event.',
            'date': '2024-09-30',
            'start_time': '14:00',
            'end_time': '12:00',
            'image': None,
            'recurrence': 'never',
            'recurrence_day': 'monday'
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('end_time', form.errors)
