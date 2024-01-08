#!/usr/bin/node

exports.add = function (a, b) {
  if (a === undefined || b === undefined) { return 'NaN'; }
  return Number(a) + Number(b);
};
