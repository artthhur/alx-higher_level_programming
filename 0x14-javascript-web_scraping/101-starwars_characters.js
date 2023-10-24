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

    const fetchCharacters = (characterUrls, index = 0) => {
      if (index < characterUrls.length) {
        const characterUrl = characterUrls[index];
        request.get(characterUrl, (error, response, characterBody) => {
          if (error) {
            console.error(error);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
            fetchCharacters(characterUrls, index + 1);
          }
        });
      }
    };

    fetchCharacters(charactersUrls);
  }
});
