function solution(age) {
  const ageString = "abcdefghij";
  var answer = '';

  while (age > 0) {
    answer = ageString[age % 10] + answer;
    age = parseInt(age / 10)
  }

  return answer;
}