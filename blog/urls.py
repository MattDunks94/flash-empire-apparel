from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_post_list, name='view_post_list'),
    path('<slug:slug>/', views.view_post_detail, name='post_detail'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
]
