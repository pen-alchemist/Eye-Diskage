from django.urls import path

from backend import views

urlpatterns = [
    path('eye_diskage/generate/', views.generator_view, name='eye_diskage-gen'),
]
