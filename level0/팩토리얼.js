function solution(n) {
  let answer = 0;
  let number = 1;

  for (let i = 1; i <= 11; i++) {
    number *= i

    if (number > n) {
      answer = i - 1
      break
    }
  }

  return answer;
}

console.log(solution(1))
console.log(solution(24))