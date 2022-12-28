function solution(n) {
  var answer = 0;
  let x = parseInt(n / 7)
  let y = n % 7

  if (y === 0) {
    answer = x
  } else {
    answer = x + 1
  }

  return answer;
}

function solution2(n) {
    return Math.ceil(n / 7)
}