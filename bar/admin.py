from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin
from .models import Reservation, Comment, UserProfile, Event, ContactMessage

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('user', 'created_at', 'rating')
    search_fields = ('user__username', 'content')
    list_filter = ('created_at', 'rating')
    ordering = ('-created_at',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'start_time', 'end_time', 'recurrence', 'recurrence_day')
    fields = ('title', 'description', 'date', 'start_time', 'end_time', 'image', 'recurrence', 'recurrence_day')
    search_fields = ('title', 'description')
    list_filter = ('recurrence', 'recurrence_day')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'telephone', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reservation_time', 'hall', 'num_guests')
    search_fields = ('user__username', 'reservation_time', 'hall')
    
    def save_model(self, request, obj, form, change):
        if obj.hall == 'indoor' and obj.num_guests > 70:
            raise ValidationError(_('Indoor reservations can accept a maximum of 70 guests.'))
        elif obj.hall == 'outdoor' and obj.num_guests > 120:
            raise ValidationError(_('Outdoor reservations can accept a maximum of 120 guests.'))
        super().save_model(request, obj, form, change)


admin.site.register(UserProfile)
