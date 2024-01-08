#!/usr/bin/node

const [a, b] = process.argv.slice(2);

function add (a, b) {
  if (a === undefined || b === undefined) { return 'NaN'; }
  return Number(a) + Number(b);
}

console.log(add(a, b));
