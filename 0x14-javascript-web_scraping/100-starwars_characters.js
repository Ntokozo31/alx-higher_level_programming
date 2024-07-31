#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/filims/${id}';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.perse(body);
    const characters = content.characters;
    //console.log(charecters);
    for (const character of characters) {
      request.get(character, (error, response, body) => {
	if (error) {
	  console.log(error);
	} else {
	  const names = JSON.parse(body);
	  console.log(names.name);

	}
      });
    }
  } 
});
