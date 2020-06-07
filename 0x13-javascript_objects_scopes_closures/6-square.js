#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
