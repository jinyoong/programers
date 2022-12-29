function solution(my_string, letter) {
  var answer = '';

  answer = my_string.replaceAll(letter, "");
  // my_string.split(letter).join("");
  return answer;
}