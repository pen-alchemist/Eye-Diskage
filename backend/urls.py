from django.urls import path

from backend import views

urlpatterns = [
    path('api/blog/all/', views.blog_collection_view, name='blog-all'),
    path('api/blog/read/<str:slug>/', views.blog_reading_view, name='blog-reading'),
]