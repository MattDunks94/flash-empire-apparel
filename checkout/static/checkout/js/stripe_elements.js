// Public Key
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
// Client Secret Key
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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

// Handle realtime validation errors.
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times text-danger"></i>
        </span>
        <span>${event.error.message}</span>`
        // Assign errorDiv with the html.
        $(errorDiv).html(html)
    }

    else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times text-red"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});