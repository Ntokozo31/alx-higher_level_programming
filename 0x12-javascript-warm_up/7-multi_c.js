#!/usr/bin/node

// Retrive the argument passes by the user
const arg = process.argv[2];
// Convert our first argument into integer
const x = parseInt(arg, 10);
// Check if our first argument was converted
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // If x was converted we loop x times
  for (let i = 0; i < x; i++) {
    // Print out a massege each iteration of a loop
    console.log('C is fun');
  }
}
