#!/usr/bin/node
const list = require('./100-data.js');

const newList = list.map((value, idx) => value * idx);

console.log(list);
console.log(newList);
