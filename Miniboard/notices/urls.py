"""URL configuration for the notices application."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('create/', views.create_notice, name='create_notice'),
    path('notice/<int:pk>/edit/', views.edit_notice, name='edit_notice'),
    path('notice/<int:pk>/delete/', views.delete_notice, name='delete_notice'),
    path('about/', views.about, name='about'),
]
