from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = (
            'slug',
            'author',
        )
        # Replacing the text field with summernote editor widget for 'content'.
        widgets = {
            'content': SummernoteWidget()
        }

