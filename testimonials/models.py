from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError


class Testimonial(models.Model):
    """
    User-submitted testimonial with a rating and optional user reference.
    """
    name = models.CharField(max_length=80)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='testimonials', null=True, blank=True
    )
    was_edited = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Returns name and first 20 characters of the content."""
        return f"{self.name}: {self.content[:20]}..."


class Comment(models.Model):
    """
    Comment on a testimonial, linked to a user and testimonial.
    """
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='testimonial_comments'
    )
    testimonial = models.ForeignKey(
        Testimonial,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    was_edited = models.BooleanField(default=False)

    class Meta:
        """Orders comments by creation date, newest first."""
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Returns username and first 20 characters of the comment."""
        return (f"{self.user.username}: {self.content[:20]}... "
                f"on {self.testimonial.id}")

    def clean(self):
        """Validates comment content length."""
        if not self.content:
            raise ValidationError('Comment cannot be empty.')
        if len(self.content) > 50:
            raise ValidationError('Comment cannot exceed 50 characters.')
