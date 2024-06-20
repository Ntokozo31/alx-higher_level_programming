#!/usr/bin/node

// Define the function that increments the number and calls another function
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

// Export the function to make it visible from outside
module.exports = addMeMaybe;
