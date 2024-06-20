#!/usr/bin/node

// Retrive and parse the command line argument to integer,exclude the first two elements
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));
// If there are fewer arguments, print 0
if (args.length < 2) {
  console.log(0);
} else {
  // Sort the array in decending order and get the second element
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
