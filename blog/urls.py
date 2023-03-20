from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_post_list, name='view_post_list'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path(
        'edit_blog_post/<slug:slug>', views.edit_blog_post, name='edit_blog_post'
        ),
    path(
        'remove_blog_post/<slug:slug>', views.remove_blog_post, name='remove_blog_post'
        ),
    path('<slug:slug>/', views.view_post_detail, name='post_detail'),
]
