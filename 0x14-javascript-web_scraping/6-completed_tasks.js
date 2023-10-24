#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};
  for (const task of body) {
    if (task.completed) {
      tasksCompleted[task.userId] = tasksCompleted[task.userId] || 0;
      tasksCompleted[task.userId]++;
    }
  }
  console.log(tasksCompleted);
});
