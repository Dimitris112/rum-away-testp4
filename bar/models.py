from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.templatetags.static import static

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.reservation_time} on Table {self.table.number}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_time = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.TextField()

    def __str__(self):
        return f"Order by {self.user.username} on Table {self.table.number} for ${self.total_amount}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=1)  # Rating from 1 to 5

    def __str__(self):
        return f"Comment by {self.user.username} with rating {self.rating}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        default='images/nobody.jpg'
    )

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_profile_picture_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        return static('images/nobody.jpg')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    recurrence = models.CharField(
        max_length=10, 
        choices=[('daily', 'Daily'), ('weekly', 'Weekly')],
        blank=True,
        null=True
    )
    recurrence_day = models.CharField(
        max_length=10,
        choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),
                 ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'),
                 ('sunday', 'Sunday')],
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
            day_index = dict(monday=0, tuesday=1, wednesday=2, thursday=3, friday=4, saturday=5, sunday=6)
            today_index = now.weekday()
            target_index = day_index[self.recurrence_day.lower()]
            days_until_target = (target_index - today_index + 7) % 7
            next_occurrence = now + timezone.timedelta(days=days_until_target)
            return next_occurrence.replace(hour=20, minute=0, second=0, microsecond=0)
        return None
