from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('single/<int:post_id>', views.blog_single, name='blog_single'),
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('post_list',  views.post_list, name='post_list'),
]