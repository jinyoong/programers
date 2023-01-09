function solution(n) {
  var answer = 0;

  for (let i = 1; i <= n; i++) {
    answer += countYaksu >= 3 ? 1 : 0
  }

  return answer;
}

function countYaksu(n) {
  let result = 0;

  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      result += 2
    }

    if (i * i === n) {
      result -= 1
    }
  }

  return result
}