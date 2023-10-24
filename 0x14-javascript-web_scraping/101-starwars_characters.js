#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const baseUrl = 'https://swapi-api.alx-tools.com/api';
const filmUrl = `${baseUrl}/films/${movieId}`;

request.get(filmUrl, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    let count = characters.length;
    const names = [];

    for (const character of characters) {
      request.get(character, (error, res, body) => {
        if (error) {
          console.error(error);
        } else {
          const data = JSON.parse(body);

          names.push(data.name);
          count--;

          // if count is zero, all character names are fetched
          if (count === 0) {
            names.sort(
              (a, b) => characters.indexOf(`${baseUrl}/people/${a}/`) - characters.indexOf(`${baseUrl}/people/${b}/`)
            );

            for (const name of names) {
              console.log(name);
            }
          }
          console.log(data.name);
        }
      });
    }
  }
});
