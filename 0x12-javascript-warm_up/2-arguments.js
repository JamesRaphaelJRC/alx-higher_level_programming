#!/usr/bin/node
const argCount = process.argv.length;
if (argCount > 3) {
  console.log('Arguments found');
} else if (argCount === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
