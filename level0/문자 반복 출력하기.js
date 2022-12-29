function solution(my_string, n) {
  var answer = '';
  for (let i = 0; i < my_string.length; i++) {
    answer += my_string[i].repeat(n)
  }
  const newAnswer = [...my_string].map(element => element.repeat(n)).join("")
  return answer;
}