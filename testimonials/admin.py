from django.contrib import admin
from .models import Testimonial, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('user', 'created_at')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'rating', 'created_at', 'updated_at', 'user')
    search_fields = ('name', 'content', 'user__username')
    list_filter = ('rating', 'created_at', 'updated_at')
    inlines = [CommentInline]
    readonly_fields = ('created_at', 'updated_at', 'user')
    ordering = ('-created_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Testimonial, TestimonialAdmin)
