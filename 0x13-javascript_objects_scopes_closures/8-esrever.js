#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  if (typeof list === 'undefined') return 0;
  let listLength = list.length - 1;
  for (let i = 0; i < list.length; i++, listLength--) {
    revList[i] = list[listLength];
  }
  return revList;
};
