#!/usr/bin/node
const length = process.argv.length - 2;
if (length < 2) {
  console.log(0);
} else {
  let j = 0;
  const argList = [];
  for (let i = 2; i < length + 2; i++) {
    argList[j] = Number(process.argv[i]);
    j++;
  }
  const maximum = Math.max(...argList);
  const newArgList = argList.filter(element => element < maximum);
  console.log(Math.max(...newArgList));
}
