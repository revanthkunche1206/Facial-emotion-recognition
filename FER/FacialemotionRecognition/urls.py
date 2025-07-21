from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detect_emotion/', views.detect_emotion, name='detect_emotion'),
]
