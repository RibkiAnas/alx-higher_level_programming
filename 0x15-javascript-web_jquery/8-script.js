// script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(document).ready(() => {
  $.getJSON(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    (data) => {
      const movies = data.results;
      for (let i = 0; i < movies.length; i++) {
        const title = movies[i].title;
        const li = $('<li>' + title + '</li>');
        $('#list_movies').append(li);
      }
    }
  );
});
