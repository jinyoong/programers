function solution(my_string, num1, num2) {
  const change = [my_string[num1], my_string[num2]];

  const answerArray = my_string.split("");
  answerArray[num1] = change[1];
  answerArray[num2] = change[0]; 

  return answerArray.join("");
}