from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_check, name='api_check'),
    path(r'recognize-food', views.recognize_food, name='recognize_food'),
]