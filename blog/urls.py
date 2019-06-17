from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('single/<int:post_id>', views.blog_single, name='blog_single'),
]