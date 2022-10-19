function solution(n) {
  let number = 0;

  for (let i = 0; i < n; i++) {
    number += 1
    while (number % 3 === 0 || String(number).indexOf(3) != -1) {
      number += 1
    }
  }

  return number;
}