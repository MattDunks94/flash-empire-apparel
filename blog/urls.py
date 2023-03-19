from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_post_list, name='view_post_list'),
    path('<slug:slug>/', views.view_post_detail, name='post_detail'),
]
