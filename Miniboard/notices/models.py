"""Models for the notices application."""

from django.db import models


class Notice(models.Model):
    """Model for storing notices/updates."""
    
    title = models.CharField(max_length=200, help_text="Title of the notice")
    content = models.TextField(help_text="Content of the notice")
    author = models.CharField(max_length=100, default="Anonymous", help_text="Author name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(default=False, help_text="Pin important notices to the top")
    
    class Meta:
        ordering = ['-is_pinned', '-created_at']  # Pinned notices first, then newest
        verbose_name_plural = "Notices"
    
    def __str__(self):
        return self.title
