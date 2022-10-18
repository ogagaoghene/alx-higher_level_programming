#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const result = {};

request(URL, (err, res, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed) {
        if (task.userId in result) {
          result[task.userId] += 1;
        } else {
          result[task.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
