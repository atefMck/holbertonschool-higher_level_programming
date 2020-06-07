#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  let j = 0;
  for (var i = list.length - 1; i >= 0; i--) {
    tsil[j] = list[i];
    j++;
  }
  return tsil;
};
