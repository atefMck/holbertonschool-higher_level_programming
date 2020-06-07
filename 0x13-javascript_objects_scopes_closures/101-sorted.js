#!/usr/bin/node
const dict = require('./101-data').dict;
const tcid = {};
for (const [key, value] of Object.entries(dict)) {
  if (tcid[value]) {
    tcid[value].push(key);
  } else {
    tcid[value] = [key];
  }
}
console.log(tcid);
