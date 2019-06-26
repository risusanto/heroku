from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('', include('food_ai.urls')),
]
