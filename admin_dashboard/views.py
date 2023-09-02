from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_admin:
        # Only admin users can access this view
        return render(request, 'admin_dashboard/dashboard.html')
    else:
        # Redirect other users to a different page or show a message
        return render(request, 'admin_dashboard/access_denied.html')
