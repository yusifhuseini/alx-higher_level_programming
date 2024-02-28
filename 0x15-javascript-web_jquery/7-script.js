const url = 'https://swapi-api.hbtn.io/api/people/5/';
$.get(url, { format: 'json' }, function (data, status) {
  if (status === 'success') {
    const name = data.name;
    $('DIV#character').text(name);
  }
});
