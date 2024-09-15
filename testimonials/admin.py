from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'rating', 'created_at', 'updated_at')
    search_fields = ('name', 'content')

admin.site.register(Testimonial, TestimonialAdmin)
