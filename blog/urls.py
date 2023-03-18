from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_post_list, name='view_post_list'),
]
