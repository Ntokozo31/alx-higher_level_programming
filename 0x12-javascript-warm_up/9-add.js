#!/usr/bin/node

// Define the add function to sum the two integers
function add (a, b) {
  return a + b;
}
// Retrive and parse the command-line argument to integers
const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);
// Use add function to sum integers
const addition = add(a, b);
// Print the results of the addition
console.log(addition);
