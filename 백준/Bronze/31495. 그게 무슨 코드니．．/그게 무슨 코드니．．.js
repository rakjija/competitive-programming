const input = () => {
  return require('node:fs')
    .readFileSync('/dev/stdin')
    .toString()
    .trim()
    .split('\n');
};

const S = input()[0];
if (S.startsWith('"') && S.endsWith('"') && S.length > 2) {
  console.log(S.slice(1, -1));
} else {
  console.log('CE');
}
