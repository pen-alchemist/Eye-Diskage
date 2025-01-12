from django.urls import path

from backend import views

urlpatterns = [
    path('blog/main/', views.main_page_view, name='blog-all'),
    path('blog/read/<str:slug>/', views.post_read_view, name='blog-reading'),
]