$(function () {
  var handler = StripeCheckout.configure({
    key: 'pk_live_KLzRFeS7szjMUC5JgGPT3LIV',
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
