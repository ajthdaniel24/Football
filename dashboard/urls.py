from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('', views.dashboard_view, name='dashboard'),
]
