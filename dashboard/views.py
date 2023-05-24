from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    """Display user dashboard."""
    return render(request, 'dashboard/dashboard.html')