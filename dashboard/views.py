from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.role == 'admin':
        return render(request, 'dashboard/admin_dashboard.html')
    return redirect('login')

@login_required
def manager_dashboard(request):
    if request.user.role == 'manager':
        return render(request, 'dashboard/manager_dashboard.html')
    return redirect('login')

@login_required
def dashboard_view(request):
    if request.user.role == 'admin':
        return render(request, 'dashboard/admin_dashboard.html')
    elif request.user.role == 'manager':
        return render(request, 'dashboard/manager_dashboard.html')
    return render(request, 'dashboard/player_dashboard.html') 



