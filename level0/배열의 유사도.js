function solution(s1, s2) {
  var answer = 0;

  s2.forEach(element => {
    answer += s1.includes(element) ? 1 : 0
  })

  return answer;
}