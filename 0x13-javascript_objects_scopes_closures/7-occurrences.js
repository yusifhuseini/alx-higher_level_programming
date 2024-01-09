#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const e of list) {
    count = (e === searchElement) ? count + 1 : count;
  }
  return count;
};
