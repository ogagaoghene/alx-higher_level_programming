#!/usr/bin/node
// Gather information for STARWARS API 🔥

const request = require('request');
const ID = process.argv[2];
const URL = `https://swapi-api.hbtn.io/api/films/${ID}`;

request(URL, (req, res, body) => {
  if (res.statusCode === 404) {
    console.log('Movie doesnt exist');
  } else {
    console.log(JSON.parse(body).title);
  }
});
