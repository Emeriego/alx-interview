#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(`${apiUrl}${movieId}`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.error('Error fetching movie:', error);
  }
});

function printCharacters(characters, index) {
  if (index < characters.length) {
    request(characters[index], function (error, response, body) {
      if (!error && response.statusCode === 200) {
        console.log(JSON.parse(body).name);
        printCharacters(characters, index + 1);
      } else {
        console.error('Error fetching character:', error);
      }
    });
  }
}
