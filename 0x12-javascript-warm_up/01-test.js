#!/usr/bin/node

// Import the addMeMaybe function
const addMeMaybe = require('./addMeMaybe');

// Define a function to be called with the incremented number
function printIncrementedNumber(number) {
  console.log(`Incremented number: ${number}`);
}

// Call addMeMaybe with an initial number and the print function
addMeMaybe(5, printIncrementedNumber);
