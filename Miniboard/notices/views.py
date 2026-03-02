"""Views for the notices application."""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Notice
from .forms import NoticeForm


def home(request):
    """Display the homepage with list of all notices."""
    notices = Notice.objects.all()
    return render(request, 'notices/home.html', {'notices': notices})


def notice_detail(request, pk):
    """Display a single notice in detail."""
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'notices/notice_detail.html', {'notice': notice})


@require_http_methods(["GET", "POST"])
def create_notice(request):
    """View to create a new notice."""
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save()
            return redirect('notice_detail', pk=notice.pk)
    else:
        form = NoticeForm()
    
    return render(request, 'notices/create_notice.html', {'form': form})


@require_http_methods(["GET", "POST"])
def edit_notice(request, pk):
    """View to edit an existing notice."""
    notice = get_object_or_404(Notice, pk=pk)
    
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice_detail', pk=notice.pk)
    else:
        form = NoticeForm(instance=notice)
    
    return render(request, 'notices/edit_notice.html', {'form': form, 'notice': notice})


def delete_notice(request, pk):
    """View to delete a notice."""
    notice = get_object_or_404(Notice, pk=pk)
    
    if request.method == 'POST':
        notice.delete()
        return redirect('home')
    
    return render(request, 'notices/delete_confirm.html', {'notice': notice})


def about(request):
    """Display the about page (static page)."""
    return render(request, 'notices/about.html')
