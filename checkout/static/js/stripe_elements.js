var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#8A868F'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times text-danger"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit + loading overlay
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    // Prevents form from submitting. Disables card element.
    // Triggers loading overlay.
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    }
    var url = 'checkout/cache_checkout_data/';
    // Posting the url and postData.
    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    first_name: $.trim(form.first_name.value),
                    last_name: $.trim(form.last_name.value),
                    email: $.trim(form.email.value),
                    address: {
                        line_1: $.trim(form.street_address_1.value),
                        line_2: $.trim(form.street_address_2.value),
                        town_city: $.trim(form.town_or_city.value),
                        county: $.trim(form.county.value),
                        country: $.trim(form.country.value),

                    }

                }
            },
            shipping_details: {
                first_name: $.trim(form.first_name.value),
                last_name: $.trim(form.last_name.value),
                address: {
                    line_1: $.trim(form.street_address_1.value),
                    line_2: $.trim(form.street_address_2.value),
                    town_city: $.trim(form.town_or_city.value),
                    county: $.trim(form.county.value),
                    postcode: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            }
        }).then(function (result) {
            // If an error occurs, loading overlay hidden, card element enabled.
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times text-danger"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    // If failing to post data to the view, reload the page, without charging user.
    }).fail(function() {
        location.reload
    })
});