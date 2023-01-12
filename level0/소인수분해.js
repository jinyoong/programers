function solution(n) {
  var answer = [];

  for (let number = 2; number <= n; number++) {
    if (!isPrime(number)) continue;

    if (n % number !== 0) continue;

    answer.push(number)

    while (n % number !== 0) {
      n = parseInt(n / number)
    }

    if (n === 1) break
  }

  return answer;
}

function isPrime(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}