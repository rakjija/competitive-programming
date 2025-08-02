const rl = require('node:readline').createInterface({
  input: process.stdin,
  output: process.output,
});

rl.on('line', (line) => {
  const [a, b, c, d] = line.trim().split(' ').map(Number);

  const diffs = [
    Math.abs(a + b - (c + d)),
    Math.abs(a + c - (b + d)),
    Math.abs(a + d - (b + c)),
  ];

  console.log(Math.min(...diffs));

  rl.close();
});
