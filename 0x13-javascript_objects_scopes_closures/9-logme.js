#!/usr/bin/node
var num = 0;
exports.logMe = function (item) {
  console.log('%d : %s', num, item);
  num++;
};
