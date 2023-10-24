#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    for (const movie of data.results) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
