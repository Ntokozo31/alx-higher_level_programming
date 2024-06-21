#!/usr/bin/node

// first user provided argument
const arg1 = process.argv[2];
// Second user provided argument
const arg2 = process.argv[3];

if (!arg1 && !arg2) {
  // If both arguments are false (i.e undefined)
  console.log('undefined is undefined');
} else if (!arg2) {
  // If argument 1 is true but argument 2 is false
  console.log(`${arg1} is undefined`);
} else {
  // If both arguments are true
  console.log(`${arg1} is ${arg2}`);
}
