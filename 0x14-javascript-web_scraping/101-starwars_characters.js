#!/usr/bin/node
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(link, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body).characters;
  printChars(data, 0);
});

function printChars (chars, idx) {
  request(chars[idx], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    if (idx + 1 < chars.length) {
      printChars(chars, idx + 1);
    }
  });
}
