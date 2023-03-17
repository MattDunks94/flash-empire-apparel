from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = (
        'status',
        'created_on'
        )
    list_display = (
        'title',
        'author',
        'slug',
        'created_on',
        'status'
    )
    search_fields = [
        'title'
    ]
    summernote_fields = (
        'content'
    )
