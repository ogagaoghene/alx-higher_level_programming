#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const destiny = process.argv[3];

request(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = body;
    fs.writeFile(destiny, data, 'utf-8', (err) => {
      if (err) console.log(err || 'Success');
    });
  }
});
