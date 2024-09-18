# admin.py
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Table, Reservation, Order, Comment, UserProfile, Event, ContactMessage

class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

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

admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
