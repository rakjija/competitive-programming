const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [A, B, C, D, E, F] = input;

const group1 = [A, B, C, D].map(Number);
const group2 = [E, F].map(Number);

const group1Sum = group1
  .map(Number)
  .sort((a, b) => b - a)
  .slice(0, 3)
  .reduce((acc, cur) => acc + cur, 0);

const group2Sum = group2
  .map(Number)
  .sort((a, b) => b - a)
  .slice(0, 1)
  .reduce((acc, cur) => acc + cur, 0);

console.log(group1Sum + group2Sum);
