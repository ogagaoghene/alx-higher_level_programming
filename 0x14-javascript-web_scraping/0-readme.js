#!/usr/bin/node

const fs = require('fs');

const readAFile = path => {
  fs.readFile(path, 'utf8', (err, data) => {
    console.log(err || data);
  });
};
readAFile(process.argv[2]);
