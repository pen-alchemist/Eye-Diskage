from django.urls import path

from backend import views

urlpatterns = [
    path('eye_diskage/django-ker-generate/', views.generator_view, name='eye-django-gen'),
    path('eye_diskage/caesar-cipher/', views.caesar_cipher_view, name='eye-caesar-text'),
]
