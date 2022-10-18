#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    for (const characters of data) {
      request(characters, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    }
  }
});
