from django.urls import path

from backend import views

urlpatterns = [
    path('eye_diskage/django-ker-generate/', views.generator_view, name='eye-django-gen'),
    path('eye_diskage/caesar-cipher/', views.caesar_cipher_view, name='eye-caesar-text'),
    path('eye_diskage/vigenere-cipher/', views.vigenere_cipher_view, name='eye-vigenere-text'),
    path('eye_diskage/secure-random-numbers/', views.secure_random_numbers_view, name='eye-secure-numbers'),
]
