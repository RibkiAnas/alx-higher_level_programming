#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((value, idx) => value * idx);

console.log(list);
console.log(newList);
