from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('tracks/', views.tracks, name='tracks')
]
