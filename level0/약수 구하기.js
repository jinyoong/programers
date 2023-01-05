function solution(n) {
  let answer = [];

  for (let number = 1; number <= Math.sqrt(n); number++) {
    if (n % number !== 0) continue;

    answer.push(number)

    if (number !== Math.sqrt(n)) {
      answer.push(parseInt(n / number))
    }
  }

  return answer.sort((a, b) => a - b);
}