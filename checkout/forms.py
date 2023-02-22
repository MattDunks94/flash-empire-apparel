from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email', 
            'phone_number',
            'country',
            'street_address_1',
            'street_address_2',
            'town_or_city',
            'county',
            'postcode',
        )

    def __init__(self, *args, **kwargs):
        """
        Adding placeholders, classes and removing auto generated labels
        and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2 (Optional)',
            'town_or_city': 'Town/City',
            'county': 'County (Optional)',
            'postcode': 'Postcode',
        }

        # Set the cursor on 'full_name' when page loads.
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Iterate through each field and add '*' to them.
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            # Setting placeholder to the ones in the dictionary.
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # CSS class for stripe field.
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removing form labels.
            self.fields[field].label = False
