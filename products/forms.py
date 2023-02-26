from django import forms
from django.forms.widgets import Select
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview

# Rating choices for form field rating
RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # Collecting categories friendly names.
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        # Displays friendly name.
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-5'


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = (
            'body',
            'rating',
        )
    # Changing field to choice field, limits the rating value.
    rating = forms.ChoiceField(choices=RATING_CHOICES)
