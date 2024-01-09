#!/usr/bin/node

const dict = require('./101-data').dict;
const sort = {};
for (const [k, v] of Object.entries(dict)) {
  if (sort[v] === undefined) {
    sort[v] = [k];
  } else {
    sort[v].push(k);
  }
}
console.log(sort);
