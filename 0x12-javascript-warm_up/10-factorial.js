#!/usr/bin/node
const firstArg = Number(process.argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(firstArg));
