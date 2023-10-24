#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;

    charactersUrls.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
