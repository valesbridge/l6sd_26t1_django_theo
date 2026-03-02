"""Admin configuration for the notices application."""

from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    """Admin interface for managing notices."""
    
    list_display = ('title', 'author', 'created_at', 'is_pinned')
    list_filter = ('created_at', 'is_pinned')
    search_fields = ('title', 'content', 'author')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'content')
        }),
        ('Details', {
            'fields': ('author', 'is_pinned')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
