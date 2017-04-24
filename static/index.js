$(function () {
  var handler = StripeCheckout.configure({
    key: 'pk_test_wxQMpcEtVnRcl9jfz8GKfPk8',
    image: 'https://stripe.com/img/documentation/checkout/marketplace.png',
    locale: 'auto',
    zipCode: true,
    shippingAddress: true,
    billingAddress: true,
    token: function (token, extra_info) {
      // You can access the token ID with `token.id`.
      // Get the token ID to your server-side code for use.
      $.post({
        contentType: 'application/json',
        data: JSON.stringify({
          token: token,
          extra_info: extra_info,
        }),
        type: 'POST',
        dataType: 'json',
        url: '/buy',
        cache: false,
      })
    }
  });

  document.getElementById('order-button').addEventListener('click', function (e) {
    // TODO: get size of shirt from select

    handler.open({
      name: 'opolis.design',
      description: '1 Shirt',
      amount: 3000
    });
    e.preventDefault();
  });
});

a = {
  'id': 'tok_1ABzVnEIlOex05FHfe1Ej0EV',
  'object': 'token',
  'card': {
    'id': 'card_1ABzVnEIlOex05FHjhCgoooi',
    'object': 'card',
    'address_city': 'sf',
    'address_country': 'United States',
    'address_line1': '405 webster st',
    'address_line1_check': 'pass',
    'address_line2': None,
    'address_state': 'MA',
    'address_zip': '02131',
    'address_zip_check': 'pass',
    'brand': 'Visa',
    'country': 'US',
    'cvc_check': 'pass',
    'dynamic_last4': None,
    'exp_month': 2,
    'exp_year': 2019,
    'funding': 'credit',
    'last4': '4242',
    'metadata': {},
    'name': 'vp',
    'tokenization_method': None
  },
  'client_ip': '76.126.175.23',
  'created': 1493010803,
  'email': 'saldf@lksdj.co',
  'livemode': False,
  'type': 'card',
  'used': False
}

b = {
  'billing_name': 'kj',
  'billing_address_country': 'Kazakhstan',
  'billing_address_country_code': 'KZ',
  'billing_address_zip': 'kj',
  'billing_address_line1': 'k',
  'billing_address_city': 'j',
  'shipping_name': 'kj',
  'shipping_address_country': 'Kazakhstan',
  'shipping_address_country_code': 'KZ',
  'shipping_address_zip': 'kj',
  'shipping_address_line1': 'k',
  'shipping_address_city': 'j'
}
