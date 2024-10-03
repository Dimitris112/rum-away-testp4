from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.utils import timezone
from ..models import (
    Event,
    Reservation,
    Comment,
    UserProfile,
    ContactMessage,
    Category
)


class ViewsTestCase(TestCase):
    def setUp(self):
        """Set up the test case with a test user and an example event."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            date=timezone.now(),
            start_time=timezone.now().time(),
            end_time=timezone.now().time()
        )

        self.reservation = Reservation.objects.create(
            user=self.user,
            name='Test Reservation',
            reservation_time=timezone.now() + timezone.timedelta(days=1),
            special_requests='None',
            num_guests=2,
            hall='indoor'
        )

    def test_custom_signup_view(self):
        """Test that the custom signup view returns a 200 status code
        and contains 'Sign Up'."""
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')

    def test_custom_login_view(self):
        """Test that the custom login view redirects after a successful
        login."""
        response = self.client.post(
            reverse('login'),
            {
                'username': 'testuser',
                'password': 'testpassword'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_profile_view(self):
        """Test that the profile view returns a 200 status code
        and contains 'Profile'."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')

    def test_reservations_list_view(self):
        """Test that the reservations list view returns a 200 status code
        and contains 'Reservations'."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('reservations_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Reservations')

    def test_reservation_detail_view(self):
        """Test that the reservation detail view returns a 200 status code
        and shows reservation details."""
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(
            reverse('reservations_detail', args=[self.reservation.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Reservation Details')
        self.assertContains(response, 'indoor')
        self.assertContains(response, str(self.reservation.num_guests))

    def test_event_detail_view(self):
        """Test that the event detail view returns a 200 status code
        and contains event information."""
        response = self.client.get(
            reverse('event_detail', args=[self.event.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)
        self.assertContains(response, 'This is a test event.')

    def test_logout_view(self):
        """Test that the logout view redirects after a successful logout."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
