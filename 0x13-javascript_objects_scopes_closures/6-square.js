#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c = undefined) {
    const shape = c || 'X';
    for (let h = 0; h < this.height; h++) {
      let line = '';
      for (let w = 0; w < this.width; w++) {
        line += shape;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
