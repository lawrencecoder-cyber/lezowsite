from django.shortcuts import render


def home_view(request):
    return render(request, "templates/home.html")

from django.http import JsonResponse

def health_check(request):
    return JsonResponse({
        "status": "ok"
    })
