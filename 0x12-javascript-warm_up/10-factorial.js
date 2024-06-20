#!/usr/bin/node

// Define the recurcive to compute the factorial
function factorial (n) {
  // If n is 0 or 1 return 1
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
// Retrive and parse the command line argument to integer
const arg = parseInt(process.argv[2], 10);
// Compute the factorial
const result = isNaN(arg) ? 1 : factorial(arg);
// Print the results of the factorial computation
console.log(result);
