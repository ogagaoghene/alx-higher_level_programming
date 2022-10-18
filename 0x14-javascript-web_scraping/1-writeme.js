#!/usr/bin/node

const fs = require('fs');
const textToWrite = process.argv[3];
const path = process.argv[2];

const writeAFile = (path, textToWrite) => {
  fs.writeFile(path, textToWrite, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
};
writeAFile(path, textToWrite);
