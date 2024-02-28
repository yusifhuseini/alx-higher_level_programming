const url = 'https://stefanbohacek.com/hellosalut/';
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    lang = $('INPUT#language_code').val();
    $.get(url, { lang: lang }, function (data, status) {
      if (status === 'success') {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
