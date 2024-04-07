#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  console.log(err || `code: ${response.statusCode}`);
});
