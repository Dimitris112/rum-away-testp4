from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonials', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk and self.created_at != timezone.now():
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def was_edited(self):
        return self.updated_at and self.updated_at != self.created_at
