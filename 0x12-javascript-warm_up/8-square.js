#!/usr/bin/node

let x, y;
const size = process.argv[2];
if (size === undefined || isNaN(size)) {
  console.log('Missing size');
}
for (x = 0; x < parseInt(size); x++) {
  let output = '';
  for (y = 0; y < size; y++) {
    output += 'X';
  }
  console.log(output);
}
