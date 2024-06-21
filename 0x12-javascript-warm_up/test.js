#!/usr/bin/node

// Import the callMeMoby function
const callMeMoby = require('./callMeMoby');

// Define a function to be called
function printMessage() {
  console.log('Hello, world!');
}

// Call callMeMoby to execute printMessage 5 times
callMeMoby(5, printMessage);
