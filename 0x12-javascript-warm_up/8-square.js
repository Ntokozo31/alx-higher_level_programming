#!/usr/bin/node

// Retrive the argument from the user
const arg = process.argv[2];
// Convert our argument to integer
const size = parseInt(arg, 10);
// Check if our argument has been converted
if (isNaN(size)) {
  // Print the massege if our argument has not been converted
  console.log('Missing size');
} else {
  // Loop to print each raw of the square
  for (let i = 0; i < size; i++) {
    // Print a raw of 'X' charachetrs
    console.log('X'.repeat(size));
  }
}
