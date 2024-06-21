#!/usr/bin/node

// Get the first argument
const arg = process.argv[2];
// Attempt to convert the argument into an integer
const num = parseInt(arg);

if (!isNaN(num)) {
  // This block execute if num is a valid number
  console.log(`My number: ${num}`);
} else {
  // This block will execute if num is not a valid number
  console.log('Not a number');
}
