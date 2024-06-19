#!/usr/bin/node

// check if atleast two arguments are passed
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  // Print the two arguments in a specified format
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else {
  // Print an error massege less then two arguments is passed
  console.log('please provide at least two arguments');
}
