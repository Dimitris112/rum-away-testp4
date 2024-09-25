from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.templatetags.static import static
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


def validate_image_format(value):
    """Validate that the uploaded image has an allowed format."""
    valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
    
    if hasattr(value, 'name'):
        file_name = value.name.lower()
        if not any(file_name.endswith(ext) for ext in valid_extensions):
            raise ValidationError('Unsupported file extension. Allowed extensions are: png, jpg, jpeg, gif, webp.')
    
    elif hasattr(value, 'url'):
        file_url = value.url.lower()
        if not any(file_url.endswith(ext) for ext in valid_extensions):
            raise ValidationError('Unsupported file extension. Allowed extensions are: png, jpg, jpeg, gif, webp.')
    
    else:
        raise ValidationError('Unsupported file type.')

class Reservation(models.Model):
    """Model representing a reservation made by a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    reservation_time = models.DateTimeField()
    special_requests = models.TextField(blank=True, null=True)
    num_guests = models.PositiveIntegerField(default=1)
    edited = models.BooleanField(default=False)
    hall = models.CharField(max_length=10, choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor')], default='indoor')

    def clean(self):
        """Validate that the number of guests does not exceed capacity based on the hall type."""
        super().clean()
        if self.hall == 'indoor' and self.num_guests > 70:
            raise ValidationError('Indoor capacity is limited to 70 guests.')
        elif self.hall == 'outdoor' and self.num_guests > 120:
            raise ValidationError('Outdoor capacity is limited to 120 guests.')

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.reservation_time} in the {self.hall} area"

class Comment(models.Model):
    """Model representing a comment made by a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Comment by {self.user.username} with rating {self.rating}"


class UserProfile(models.Model):
    """Model representing a user profile, including a bio and a featured image."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    featured_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_profile_picture_url(self):
        """Return the profile picture URL or a default image if none is available."""
        if self.featured_image and self.featured_image.url:
            return self.featured_image.url
        return static('images/nobody.jpg')

    def clean(self):
        """Validate the format of the featured image."""
        if self.featured_image:
            validate_image_format(self.featured_image)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a UserProfile when a User is created."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Automatically save the UserProfile when the User is saved."""
    instance.userprofile.save()

class Event(models.Model):
    """Model representing an event with a title, description and schedule."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    
    RECURRENCE_CHOICES = [
        ('daily', 'Daily'), 
        ('weekly', 'Weekly')
    ]
    
    recurrence = models.CharField(
        max_length=10, 
        choices=RECURRENCE_CHOICES,
        blank=True,
        null=True
    )
    
    recurrence_day = models.CharField(
        max_length=10,
        choices=[
            ('monday', 'Monday'), 
            ('tuesday', 'Tuesday'), 
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'), 
            ('friday', 'Friday'), 
            ('saturday', 'Saturday'),
            ('sunday', 'Sunday')
        ],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def get_next_occurrence(self):
        now = timezone.now()
        if self.recurrence == 'daily':
            return now.replace(hour=17, minute=0, second=0, microsecond=0)
        elif self.recurrence == 'weekly' and self.recurrence_day:
            day_index = {
                'monday': 0, 
                'tuesday': 1, 
                'wednesday': 2, 
                'thursday': 3, 
                'friday': 4, 
                'saturday': 5, 
                'sunday': 6
            }
            today_index = now.weekday()
            target_index = day_index[self.recurrence_day.lower()]
            days_until_target = (target_index - today_index + 7) % 7
            next_occurrence = now + timezone.timedelta(days=days_until_target)
            return next_occurrence.replace(hour=20, minute=0, second=0, microsecond=0)
        return None

class ContactMessage(models.Model):
    """Model representing a contact message submitted by a user."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email}) on {self.created_at}"

class Category(models.Model):
    """Model representing a menu category."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
