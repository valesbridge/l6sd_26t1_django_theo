"""App configuration for the notices application."""

from django.apps import AppConfig


class NoticesConfig(AppConfig):
    """Configuration class for the notices app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notices'
    verbose_name = 'Notices'
