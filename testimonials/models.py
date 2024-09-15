from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonials', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def was_edited(self):
        return self.created_at != self.updated_at