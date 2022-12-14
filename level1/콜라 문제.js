function solution(a, b, n) {
  var answer = 0;

  let empty = n
  let coke = parseInt(empty / a) * b

  while (coke > 0 && empty >= a) {
    answer += coke

    empty = empty - parseInt(coke / b) * a + coke
    coke = parseInt(empty / a) * b
  }

  return answer;
}

console.log(solution(3, 2, 20))