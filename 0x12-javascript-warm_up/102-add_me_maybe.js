#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  for (let index = 0; index < number; index++) {
    const incNumber = number++;
    theFunction(incNumber);
  }
};
