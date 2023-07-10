/**
 * JS 배열에서 shift() 메소드는 선형시간(O(n))이 소요된다
 *
 */

const queue = [1, 2, 3];
queue.push(4);
const value = queue.shift(); // ❌: O(n)
console.log(value);
