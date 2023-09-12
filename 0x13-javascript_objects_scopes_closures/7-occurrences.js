#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occu = 0;
  list.forEach(element => {
    if (element === searchElement) { occu++; }
  });
  return occu;
};
