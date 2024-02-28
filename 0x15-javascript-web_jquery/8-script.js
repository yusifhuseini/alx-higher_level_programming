const url = 'https://swapi-api.hbtn.io/api/films/';
$.get(url, { format: 'json' }, function (data, status) {
  if (status === 'success') {
    const results = data.results;
    for (const film of results) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    }
  }
});
