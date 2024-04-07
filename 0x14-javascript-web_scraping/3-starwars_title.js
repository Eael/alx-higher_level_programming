#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/'

request({ url: endpoint + id, method: 'GET' }, function (err, response, body) {
	console.log(err || body && JSON.parse(body).title);
});
