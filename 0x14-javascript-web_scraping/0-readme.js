#!/usr/bin/node

const filepath = process.argv[2];
const fs = require('fs');
fs.readFile(filepath, 'utf-8', function (error, content) {
  console.log(error || content);
});
