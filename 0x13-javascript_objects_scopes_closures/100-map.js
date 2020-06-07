#!/usr/bin/node
const list = require('./100-data').list;
const map = list.map((x, idx) => x * idx);
console.log(list);
console.log(map);
