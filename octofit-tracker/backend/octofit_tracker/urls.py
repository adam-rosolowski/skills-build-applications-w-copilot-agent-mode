

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
from pymongo import MongoClient

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
if CODESPACE_NAME:
    base_url = f"https://{CODESPACE_NAME}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

def api_root(request):
    return JsonResponse({
        "activities": f"{base_url}/api/activities/",
        # Dodaj tu kolejne endpointy w przyszłości
    })

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
if CODESPACE_NAME:
    base_url = f"https://{CODESPACE_NAME}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

def activities_view(request):
    return JsonResponse({"message": f"Activities endpoint. Base URL: {base_url}/api/activities/"})

def get_collection_json(collection_name):
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    data = list(db[collection_name].find({}, {'_id': False}))
    return data

def users_view(request):
    return JsonResponse(get_collection_json('users'), safe=False)

def teams_view(request):
    return JsonResponse(get_collection_json('teams'), safe=False)

def leaderboard_view(request):
    return JsonResponse(get_collection_json('leaderboard'), safe=False)

def workouts_view(request):
    return JsonResponse(get_collection_json('workouts'), safe=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/activities/', activities_view, name='activities'),
    path('api/users/', users_view, name='users'),
    path('api/teams/', teams_view, name='teams'),
    path('api/leaderboard/', leaderboard_view, name='leaderboard'),
    path('api/workouts/', workouts_view, name='workouts'),
]
