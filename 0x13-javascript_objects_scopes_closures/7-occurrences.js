#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  if (list.length === 0 || typeof searchElement === 'undefined') return 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) occurence++;
  }
  return occurence;
};
