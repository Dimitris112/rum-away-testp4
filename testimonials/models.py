from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name
