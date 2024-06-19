#!/usr/bin/node

// check if the first argument exist and print it
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
