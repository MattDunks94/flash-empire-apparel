// Public Key
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
// Client Secret Key
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
// Card element style
var style = {
    base: {
      iconColor: '#6D6B6B',
      color: '#000',
      fontWeight: '500',
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',
      ':-webkit-autofill': {
        color: '#fce883',
      },
      '::placeholder': {
        color: '#6D6B6B',
      },
    },
    invalid: {
      iconColor: '#dc3545',
      color: '#dc3545',
    },
  };

// Card Element
var card = elements.create('card', {style: style});
// Mount card element to element with ID.
card.mount('#card-element');