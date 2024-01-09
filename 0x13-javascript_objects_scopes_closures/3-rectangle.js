#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      let shape = '';
      for (let w = 0; w < this.width; w++) {
        shape += 'X';
      }
      console.log(shape);
    }
  }
}

module.exports = Rectangle;
