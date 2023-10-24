#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);

    const characters = data.characters;

    for (const character of characters) {
      request.get(character, (error, res, body) => {
        if (error) {
          console.error(error);
        } else {
          const data = JSON.parse(body);

          console.log(data.name);
        }
      });
    }
  }
});
