from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Table, Reservation, Order, Comment, UserProfile

class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
