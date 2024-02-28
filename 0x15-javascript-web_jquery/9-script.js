const url = 'https://stefanbohacek.com/hellosalut/';
$('document').ready(function () {
  $.get(url, { lang: 'fr' }, function (data, status) {
    if (status === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
