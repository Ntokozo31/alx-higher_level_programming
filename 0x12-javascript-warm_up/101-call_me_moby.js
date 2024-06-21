#!/usr/bin/node

// Define the function that will execute another function x times
function callMeMoby(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the function to make it visible from outside
module.exports = callMeMoby;
