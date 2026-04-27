def api_root(request):
    return JsonResponse({
        "activities": f"{base_url}/api/activities/",
        # Dodaj tu kolejne endpointy w przyszłości
    })

"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
import os

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
if CODESPACE_NAME:
    base_url = f"https://{CODESPACE_NAME}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

def activities_view(request):
    return JsonResponse({"message": f"Activities endpoint. Base URL: {base_url}/api/activities/"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/activities/', activities_view, name='activities'),
]
