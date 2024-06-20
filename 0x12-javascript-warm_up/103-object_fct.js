#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr () {
    this.value++;
  }
};
console.log(myObject);

// Increment the value and print the object
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
