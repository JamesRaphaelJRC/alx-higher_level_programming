#!/usr/bin/node
function factorial (num) {
  if (num === 0) return 1;
  if (num < 0) return 0;
  return num * factorial(num - 1);
}
let num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) num = 0;
console.log(factorial(num));
