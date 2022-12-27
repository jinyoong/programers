function solution(array, n) {
  var answer = 0;

  array.forEach(element => {
    answer += element === n ? 1 : 0
  })

  return answer;
}