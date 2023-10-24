#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      if (response.statusCode !== 200) {
        reject(new Error('Invalid status code <' + response.statusCode + '>'));
      }
      resolve(JSON.parse(body).name);
    });
  });
}

async function printCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  request(url, async (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const data = JSON.parse(body);
    const characters = data.characters;
    for (let i = 0; i < characters.length; i++) {
      try {
        const name = await getCharacterName(characters[i]);
        console.log(name);
      } catch (error) {
        console.error('Error: ', error);
      }
    }
  });
}

printCharacters(movieId);
