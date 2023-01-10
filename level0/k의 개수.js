function solution(i, j, k) {
  let answer = 0;

  for (let number = i; number <= j; number++) {
    answer += String(number).split("").filter(element => Number(element) === k).length
  }

  return answer;
}

function solution2(i, j, k) {
  let answer = 0;

  for (let number = i; number <= j; number++) {
    answer += String(number).split(String(k)).length - 1
  }

  return answer;
}