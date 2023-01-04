function solution(box, n) {
  var answer = 1;

  box.map(element => {
    answer *= parseInt(element / n)
  })

  return answer;
}