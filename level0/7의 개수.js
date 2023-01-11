function solution(array) {
  var answer = 0;
  const number = array.join("");
  
  answer = number.split("7").length - 1

  return answer;
}