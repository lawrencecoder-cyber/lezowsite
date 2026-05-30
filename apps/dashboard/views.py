from django.shortcuts import render
from .services import DashboardService


def dashboard_view(request):
    context = DashboardService.build_dashboard_context()
    return render(request, "dashboard/index.html", context)
