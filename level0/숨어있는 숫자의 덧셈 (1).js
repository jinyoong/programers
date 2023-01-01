function solution(my_string) {
  let answer = 0;

  const numbers = my_string.split("").filter(element => !isNaN(element))
  answer = numbers.reduce((prev, cur) => parseInt(prev) + parseInt(cur))

  return answer;
}