from django.shortcuts import render
rom django.http import JsonResponse

def home_view(request):
    return render(request, "home.html")


def health_check(request):
    return JsonResponse({
        "status": "ok"
    })
