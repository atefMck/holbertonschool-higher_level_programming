#!/usr/bin/node
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(link, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body).characters;
  for (let i = 0; i < data.length; i++) {
    const charLink = data[i];
    request(charLink, function (error, response, body) {
      if (error) throw error;
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
