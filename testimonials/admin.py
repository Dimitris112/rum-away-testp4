from django.contrib import admin
from django.db.models import Count
from .models import Testimonial, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('user', 'created_at')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'rating', 'created_at', 'updated_at', 'user', 'total_comments_count')
    search_fields = ('name', 'content', 'user__username')
    list_filter = ('rating', 'created_at', 'updated_at')
    inlines = [CommentInline]
    readonly_fields = ('created_at', 'updated_at', 'user')

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def total_comments_count(self, obj):
        return obj.comments.count()
    total_comments_count.short_description = 'Amount of Comments'
    total_comments_count.admin_order_field = 'comments_count'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(total_comments_count=Count('comments'))
        return queryset

admin.site.register(Testimonial, TestimonialAdmin)
