#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];
request.get(URL, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
