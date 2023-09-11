#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const incrNumber = number + 1;
  theFunction(incrNumber);
};
