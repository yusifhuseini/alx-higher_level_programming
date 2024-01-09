#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  list.forEach(e => reverse.unshift(e));
  return reverse;
};
