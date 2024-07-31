#!/usr/bin/node


// Import the request module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.log('Please provide a Movie ID');
  process.exit(1);
}

// URL for the Star Wars API for the given movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API to get the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status Code:', response.statusCode);
    return;
  }
  
  // Parse the JSON response
  const filmData = JSON.parse(body);
  
  // Get the list of character URLs from the response
  const characters = filmData.characters;
  
  // Iterate over each character URL and make a request to get the character details
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      
      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status Code:', response.statusCode);
        return;
      }
      
      // Parse the JSON response for the character details
      const characterData = JSON.parse(body);
      
      // Print the character name
      console.log(characterData.name);
    });
  });
});
