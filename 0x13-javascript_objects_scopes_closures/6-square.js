#!/usr/bin/node
const SquareOld = require('./5-square');

module.exports = class Square extends SquareOld {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      let line = '';
      if (typeof c === 'undefined') c = 'X';
      for (let j = 0; j < this.width; j++) line += `${c}`;
      console.log(line);
    }
  }
};
