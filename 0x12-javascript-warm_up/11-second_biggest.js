#!/usr/bin/node

function search (arr) {
  if (arr.length < 2) { return (0); }
  return arr.map(Number).sort((x, y) => x - y)[arr.length - 2];
}

console.log(search(process.argv.slice(2)));
